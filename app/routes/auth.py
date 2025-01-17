from flask import Blueprint


bp = Blueprint('auth', __name__)


@bp.route('/signup', methods=['POST'])
def signup():
    pass


@bp.route('/verify-email/<token>', methods=['GET'])
def verify(token):
    pass


@bp.route('/login', methods=['POST'])
def login():
    pass
