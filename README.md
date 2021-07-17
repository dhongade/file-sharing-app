# File Sharing App
## Full-Stack Web Development 
### Tools: 
#### Framework: Python-Flask
#### Database: MongoDB

### Specifications: 
1. It is an website model for file storing and sharing purpose.
2. You can upload your files here and download them or share them with your friends via given link in.
3. Admin keeps track of which user downloaded which file.
4. Firstly user have to login or signup, then only user get the access to traverse throughout the website. 
5. User can upload, delete or share their files.
6. Maximum allowed size of a uploaded file is 20MB.
7. The allowed file types are: JPG, GIF, PNG, DOC, DOCX, XLS, XLSX, PPT, PPTX, PDF, CSV - only.

### Start the server using following steps:
#### Set port to 5000 
* All commands given below are for Linux.
* step 1: Install vertual environment inside your project folder and activate it. <br>
          $ python3 -m venv venv <br>
          $ . venv/bin/activate

* step 2: Install all other required dependencies given in requirements.txt.  <br>
* step 3: Create a folder inside a project folder named 'uploads' to store all files uploaded by user.
* step 4: Set FLASK_APP environment variable using <br>
          $ export FLASK_APP=hello.py <br>
          $ export FLASK_ENV=development   //debug mode 'on' <br>
          $ flask run    //to run the server 

* To login or create account go to the link below: <br>
 http://127.0.0.1:5000
 
 * To see all your uploaded files go to: <br>
 http://127.0.0.1:5000/table
 
 * Logout to go back to the homepage.

  
  
    
    
