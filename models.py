from app import db
from app import ma

class userans(db.Model):
    uid = db.Column('uid', db.Integer, primary_key = True)
    qid = db.Column(db.Integer)
    ans = db.Column(db.String(100))

    def __init__(self, qid, ans):
        #self.uid = uid
        self.qid = qid
        self.ans = ans

class useransSchema(ma.ModelSchema):
    class Meta:
        model=userans


class questions(db.Model):
    idquestions = db.Column('idquestions', db.Integer, primary_key = True)
    question = db.Column(db.String(1000))
    answer = db.Column(db.String(100))
    opt1 = db.Column(db.String(100))
    opt2 = db.Column(db.String(100))
    opt3 = db.Column(db.String(100))
    opt4 = db.Column(db.String(100))


    def __init__(self,idquestions,question, answer, opt1, opt2, opt3, opt4):
        self.idquestions = idquestions
        self.question = question
        self.answer = answer
        self.opt1 = opt1
        self.opt2 = opt2
        self.opt3 = opt3
        self.opt4 = opt4

class questionsSchema(ma.ModelSchema):
    class Meta:
        model=questions
