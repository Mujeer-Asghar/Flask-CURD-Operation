from flask import Flask,request,render_template,redirect

# from models import db,StudentModel


app=Flask(__name__)

# app.config['SQLAlCHEMY_DATABSE_URI']= 'sqlite:///students.db'
# app.configx['SQLALCHEMY_TRACK_MODIFICATION']=False
# db.int_app(app)

# @app.before_first_request
# def create_Table():
#     db.creat_all()


@app.route("/insertdata",methods=['GET',"POST"])
def create():
   
        return render_template("create.html")
        
        

@app.route("/")
def hello():
    return render_template("create.html")


if __name__=='__main__':    

    app.run(debug=True)