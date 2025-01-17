def upload_file(file, current_user):
    return {"message": "must be nice"}, 200


def list_files():
    return {"message": "ooga"}, 200


def generate_download_link(file_id, current_user):
    return {"message": "booga"}, 200


def download_file(token, current_user):
    return {"message": "you didnt see anything"}, 200