from flask import Flask, jsonify, request, session, redirect
from flask_jwt_extended import create_access_token, JWTManager, jwt_required, get_jwt_identity
from passlib.hash import pbkdf2_sha256
import uuid
from hello import db
import datetime

class User:

    def start_session(self, user):
        # del user['password']
        session['logged_in'] = True
        db.users.update_one({"username": request.form.get('username1')},{"$set":{"last_login_at":datetime.datetime.now().strftime("%c") }})
        session['user'] = user
        return jsonify(user), 200

    def signup(self):
        print(request.form)

        user = {
            "_id": uuid.uuid4().hex,
            "username": request.form.get('username'),
            "email": request.form.get('email'),
            "password": request.form.get('password'),
            "last_login_at": datetime.datetime.now().strftime("%c"),
            "created_at": datetime.datetime.now().strftime("%c")
            # "confirm-password": request.form.get('confirm-password')

        }
        # user_token = {
        #     "id": user['_id'],
        #     "username":request.form.get('username'),
            
        # }

        

        #check username
        if db.users.find_one({"username": user['username']}):
            return jsonify({"error": "Username Already exists! Try again with uniq Username!"}), 400


        #check password
        if user['password'] != request.form.get('confirm-password'):
            return jsonify({"error": "Password doesn't Match !"}), 400
            
        # // encrypt password
        user['password'] = pbkdf2_sha256.encrypt(user['password'])


        #check if email exists 
        if db.users.find_one({"email": user['email']}):
            return jsonify({"error": "Email ID is already Registered !"}), 400

        if db.users.insert_one(user):
            return self.start_session(user)
            # access_token = create_access_token(identity=user['username'])
            # return jsonify(access_token=access_token)
        return jsonify({"error": "SignUp Failed !"}), 400

    def logout(self):
        session.clear()
        return redirect('/')

    def login(self):
        
        user = db.users.find_one({
           "username" : request.form.get('username1')
        })
        if user and pbkdf2_sha256.verify(request.form.get('password1'), user['password']):
            # token = create_access_token(identity=user['username'])
            # access_token=token
            return self.start_session(user)

        return jsonify({"error": "Invalid Login Credentials !"}), 401

      
