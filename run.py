from flask import Flask
from flask_uploads import UploadSet, configure_uploads, ALL

app = Flask(__name__)

app.config.from_object('config.Config')

# Create an upload set for videos
# Configure the app to use this upload set
videos = UploadSet('videos', ALL)
configure_uploads(app, videos)