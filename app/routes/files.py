from flask import Blueprint

bp = Blueprint('files', __name__)


@bp.route('/upload', methods=['POST'])
def upload():
    pass


@bp.route('/files', methods=['GET'])
def list_all_files():
    pass


@bp.route('/download/<file_id>', methods=['GET'])
def download():
    pass


@bp.route('/secure-download/<token>', methods=['GET'])
def secure_download():
    pass
