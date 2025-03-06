import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = "asdf324fdhgfbbdfg"
    MONGO_URI = 'mongodb+srv://diablo:OH4WLGrCZOlG6FH6@cluster0.qokt3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER')
    ALLOWED_EXTENSIONS = {'pptx', 'docx', 'xlsx'}
    ROOT_DIR = os.path.abspath(os.curdir)
    BASE_URL = 'http://35.226.169.72:80/'
    SMTP2GO_API_KEY = os.getenv('SMTP2GO_API_KEY')
    SMTP2GO_SENDER = os.getenv('SMTP2GO_SENDER')
