from flask import render_template, request, redirect, url_for, flash
from run import app, videos
import os

@app.route('/')
def index():

    return render_template('upload.html')

# Handles the upload button press
@app.route('/upload', methods=['POST'])
def upload():

    if 'video' not in request.files:
        flash('No file part')
        return redirect(request.url)
    
    uploaded_file = request.files['video']
    
    if uploaded_file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    
    if uploaded_file and videos.file_allowed(uploaded_file, uploaded_file.filename):
        filename = videos.save(uploaded_file)
        #process_video(os.path.join(app.config['UPLOADED_VIDEOS_DEST'], filename))
        return redirect(url_for('results'))

    # Redirects if above conditions fail
    return redirect(request.url)

# Listen at port '5000'
if __name__ == '__main__':
    app.run(debug=True, port=5000)