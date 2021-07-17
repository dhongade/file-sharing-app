# File Sharing App
## Full-Stack Web Development 
### Tools: 
#### Framework: Python-Flask
#### Database: MongoDB

### Specifications: 
1. It is an website model for file sharing purpose.
2. You can upload your files here and download them or share them with your friends via given link in.
3. Firstly user have to login or signup if new user, then only user get the access to travel trough out the website. 
4. User can upload, delete or share their files.
5. Maximum allowed size of a uploaded file is 20MB.
6. The allowed file types are: JPG, GIF, PNG, DOC, DOCX, XLS, XLSX, PPT, PPTX, PDF, CSV - only.

### Start the server using following steps:
#### Set port to 5000 
* cmd for ubantu
* step 1: Install vertual environment inside your projct folder and activate it. <br>
          cmd: python3 -m venv venv <br>
          cmd: . venv/bin/activate

* step 2: Install all other required dependencies given in requirements.txt.  <br>
* step 3: Create a folder inside a project folder named 'uploads' to store all files uploaded by user.
* step 4: Set FLASK_APP environment variable using <br>
          cmd: export FLASK_APP=hello.py <br>
          cmd: export FLASK_ENV=development   //debug mode 'on' <br>
          cmd: flask run    //to run the server 

* To login or create account go to the link below: <br>
 http://127.0.0.1:5000
 
 * To see all your uploaded files go to: <br>
 http://127.0.0.1:5000/table
 
 * Logout to go back to the homepage.

  
  
    
    
