from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()

class StudentModel(db.Model):
    __tablename__="student"
    id=db.Column(db.Interger,primerykey=True)
    name=db.Column(db.String())
    password=db.Column(db.String())
    
    
    def __init__(self,id,name,password):
        
        self.id=id
        self.name=name
        self.password=password
                                        