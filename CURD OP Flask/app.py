from flask import Flask,request,render_template,redirect

app=Flask(__name__)


@app.route("/")
def hello():
    return render_template("create.html")




@app.route('/insert')
def show():
    return render_template('sign.html')


@app.route("/insertdata",methods=['GET',"POST"])
def create():
   if request.method=='POST':
       email=request.form.get("email")
       password=request.form.get("password")       
       stre=email+" "+password
       with open('data.txt','a') as file:
        file.write(stre+"\n")
       return redirect('/insert')
  

    
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
               email=request.form.get('email')
               password=request.form.get('password')
            
               with open('data.txt','r') as file:
                for i in file.readlines():
                    er, pwd = i.strip().split(' ')
                    if er == email and pwd == password:
                        return render_template('welcome.html',user=email)
               
    else:   
        
        return render_template('welcome.html',er)     
               
            

                    








if __name__=='__main__':    

    app.run(debug=True)