import os
import shutil
import tempfile
from pathlib import Path
from flask import Flask, request, render_template_string, send_file, redirect, url_for, flash
from werkzeug.utils import secure_filename
from .core import HTTrackToTemplate

app = Flask(__name__)
app.secret_key = "supersecretkey"

UPLOAD_FOLDER = tempfile.gettempdir()
ALLOWED_EXTENSIONS = {'zip'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'httrack_zip' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['httrack_zip']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            upload_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(upload_path)
            extract_dir = os.path.join(UPLOAD_FOLDER, filename + "_extracted")
            shutil.unpack_archive(upload_path, extract_dir)
            output_dir = os.path.join(UPLOAD_FOLDER, filename + "_template")
            template_name = request.form.get("template_name", "website_template")
            converter = HTTrackToTemplate()
            converter.convert(extract_dir, output_dir, template_name)
            # Zip the output for download
            zip_path = shutil.make_archive(output_dir, 'zip', output_dir)
            return redirect(url_for('download', zipfile=os.path.basename(zip_path)))
        else:
            flash('Invalid file type. Please upload a .zip file.')
            return redirect(request.url)
    return render_template_string("""
    <!doctype html>
    <title>HTTrack to Template Web</title>
    <h1>Upload HTTrack Website (.zip)</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=httrack_zip>
      <input type=text name=template_name placeholder="Template Name (optional)">
      <input type=submit value=Convert>
    </form>
    {% with messages = get_flashed_messages() %}
      {% if messages %}
        <ul>
        {% for message in messages %}
          <li>{{ message }}</li>
        {% endfor %}
        </ul>
      {% endif %}
    {% endwith %}
    """)

@app.route('/download/<zipfile>')
def download(zipfile):
    zip_path = os.path.join(UPLOAD_FOLDER, zipfile)
    return send_file(zip_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)