from flask import Flask,request,render_template,redirect
import pymysql

app=Flask(__name__)

# con=pymysql.connect(
#     host='localhost',
#     passwd='root',
#     user='root',
   
# )

# app.config['SQLAlCHEMY_DATABSE_URI']= 'sqlite:///students.db'
# app.configx['SQLALCHEMY_TRACK_MODIFICATION']=False
# db.int_app(app)

# @app.before_first_request
# def create_Table():
#     db.creat_all()

data={}
@app.route("/insertdata",methods=['GET',"POST"])
def create():
   if request.method=='POST':
       email=request.form.get("email")
       password=request.form.get("password")
       data['email']=email
       data['passwod']=password
       file =open("templates/data.txt",'r')
       stre=email+" "+password
       with open('templates/data.txt','a') as file:
        file.write(stre+"\n")
       return redirect('/insert')
   
   return render_template("sign.html")
    
       
   
@app.route('/insert')
def show():

    return render_template('sign.html',ali=data)

      
        
        

@app.route("/")
def hello():
    return render_template("create.html")


if __name__=='__main__':    

    app.run(debug=True)