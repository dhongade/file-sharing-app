from flask import Flask, render_template, session, redirect, jsonify, request, flash, abort, send_file
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from werkzeug.utils import secure_filename
from functools import wraps
import pymongo, datetime, uuid
from bson import ObjectId
import os


app = Flask(__name__)
app.config['UPLOAD_PATH'] = '/home/mona/Desktop/my_flask_app/uploads'
app.config['ALLOWED_EXTENSIONS'] = ['.jpg', '.gif', '.png', '.doc', '.docs', '.xls', '.xlsx', '.ppt', '.pptx', '.pdf', '.csv']
    

# jwt = JWTManager(app)

# # JWT Config
# app.config["JWT_SECRET_KEY"] = "this-is-secret-key" #change it
app.secret_key = os.urandom(16)

# database 
client = pymongo.MongoClient('localhost', 27017)
db = client.MY_FLASK_APP


# decorators

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/')
    return wrap

from user import routes

@app.route('/')
@app.route('/', methods=['POST'])
def logIn():
    return render_template('login_page.html')

@app.route('/table')
# @app.route('/table', methods = ['POST'])
@login_required
# @jwt_required
def table():
    uploaded_files = db.files.find({
        "userId": session['user']['_id'],
        "isActive":True
    })
    return render_template('table.html', uploaded_files=uploaded_files)

@app.route('/handle_file_upload', methods=['POST'])
@login_required
def handle_file_upload():
    f = request.files['uploadedFile']

    # size = len(f.read())
    extension = os.path.splitext(f.filename)[1]
    filename = secure_filename(f.filename)
    # f.save(os.path.join(app.config['UPLOAD_PATH'], filename))
    filepath = os.path.join(app.config['UPLOAD_PATH'], filename)
    f.save(filepath)
    size = os.stat(filepath).st_size
    
    
    if db.files.find_one({"originalFilename": f.filename, "userId": session['user']['_id'], "isActive": True}):
        flash("File with this name is Already Available !")
        return redirect('/table')
   
    if f.filename == '':
        flash("No selected File")
        return redirect('/table')

    if extension not in app.config['ALLOWED_EXTENSIONS']:
        flash("File type not allowed")
        return redirect('/table')

    # chec file size
    if size > 20*1024*1024:
        flash("file limit excceded")
        return redirect('/table')
    
    if size < 1024:
        size = str(size) + " bytes"
    elif size < 1024*1024:
        size = str(size/1024) + " kB"
    else:
        size = str(size/(1024*1024)) + " MB"
    
    
    db.files.insert_one({
        # "_id": uuid.uuid4().hex,
        "userId": session['user']['_id'],
        "originalFilename": f.filename,
        "fileType": extension,
        "fileSize": size,
        "filePath":filepath, 
        "createAt": datetime.datetime.now().strftime("%c"),
        "isActive":True,
    })

    return redirect('/table')

@app.route('/download/<fileId>/<fileNameSlugified>', methods=['GET'])
@login_required
def showDownloadPage(fileId, fileNameSlugified):
    print("file id is:" + fileId)

    file_object = None
    try:
        file_object = db.files.find_one({
            '_id': ObjectId(fileId),
            'isActive': True
        })
    except:
        pass

    if file_object is None:
        return abort(404)

    return render_template('download.html', file=file_object)
    # return "Your downloads will come here"+fileNameSlugified

@app.route('/download/<fileId>', methods=['GET'])
@login_required
def download(fileId):
    file_object = db.files.find_one({
        "_id": ObjectId(fileId),
        "isActive": True
    })
    if file_object is None:
        abort(404)
    
    db.file_downloads.insert_one({
        "UserId": session['user']['_id'],
        "FileId": file_object['_id'],
        "DownloadedAt": datetime.datetime.now().strftime("%c")
    })
    
    filePath = file_object['filePath']
    return send_file(filePath, as_attachment=True)
    return redirect('/table')


@app.route('/table/<fileId>', methods=['GET'])
@login_required
def delete(fileId):
    db.files.update_one({"_id": ObjectId(fileId)},{"$set":{"isActive":False}})
    return redirect('/table')

# if __name__ == '__main__':
#     app.run(host="localhost", debug=True)


