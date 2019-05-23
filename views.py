from app import app
from flask import Flask, render_template,request
from models import *
from flask_restful import Resource, Api
from flask_jsonpify import jsonify
from json import dumps
import json
import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

api = Api(app)

@app.route("/")
def insertQuestions():
    # engine = create_engine('mysql://root:@localhost/first_schema')
    # #Base.metadata.create_all(engine) # here we create all tables
    # Session = sessionmaker(bind=engine)
    # session = Session()
    # csvfile = open('question.csv', 'r')
    #
    # fieldnames = ("question", "answer", "opt1", "opt2", "opt3", "opt4")
    # reader = csv.DictReader( csvfile, fieldnames)
    # #reader = csv.DictReader( csvfile, fieldnames)
    # buffer = []
    # for row in reader:
    #     buffer.append({
    #         'question':row['question'],
    #         'answer':row['answer'],
    #         'opt1':row['opt1'],
    #         'opt2':row['opt2'],
    #         'opt3':row['opt3'],
    #         'opt4':row['opt4']
    #     })
    #     if len(buffer) % 10000 == 0:
    #         session.bulk_insert_mappings(buffer)
    #         buffer = []
    #
    # session.bulk_insert_mappings(questions,buffer)
    # session.commit()
    return jsonify({'text':'Hello World!'})


class InsertItems(Resource):
    def post(datas):
        #data = jsonify(request.get_json(datas))
        print(request.get_json(datas))
        #cur=mysql.connection.cursor()
        for ans in request.get_json(datas):
            anss = userans(ans['qid'],ans['sanswer'])
            db.session.add(anss)
            db.session.commit()
        return 'success'

    def get(self):
        useranswers = userans.query.all()
        userans_schema=useransSchema(many=True)
        output=userans_schema.dump(useranswers).data
        return jsonify({'user':output})

class listQuestions(Resource):
    def get(self):
        questionss = questions.query.all()
        questions_schema=questionsSchema(many=True)
        output=questions_schema.dump(questionss).data
        return output

api.add_resource(listQuestions, '/listquest') # Route_1
api.add_resource(InsertItems, '/insertItems') # Route_1
