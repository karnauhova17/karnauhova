import datetime
from flask import Flask

from models import db, TrainingType, Visit, Client, Mentor
from routes import api, index

app = Flask(__name__)
app.register_blueprint(api)
app.register_blueprint(index)
db.init_app(app)

with app.app_context():
    db.create_all()

    # Типы тренировок:
    groupTraining = TrainingType(name='Group training')
    singleTraining = TrainingType(name='Single training')
    aerobicsTraining = TrainingType(name='Aerobics training')
    db.session.add(groupTraining)
    db.session.add(singleTraining)
    db.session.add(aerobicsTraining)

    # Клиенты:
    clientKatya = Client(firstname='Ekaterina', lastname='Petrova', patronymic='Alexandrovna')
    db.session.add(clientKatya)
    clientAnna2 = Client(firstname='Anna', lastname='Ivanova', patronymic='Andreevna')
    db.session.add(clientAnna2)


    # Тренеры:
    mentorVasya = Mentor(firstname='Vasiliy', lastname='Pavlov', patronymic='Petrovich')
    db.session.add(mentorVasya)
    mentorAndrey2 = Mentor(firstname='Andrey', lastname='Istomin', patronymic='Ivanov')
    db.session.add( mentorAndrey2)

    # Сохраним типы тренировок, клиентов и тренеров:
    db.session.commit()

    # Посещения:
    visit = Visit(client_id =  clientKatya.id, mentor_id = mentorVasya.id, trainingtype_id=singleTraining.id, visit_date=datetime.datetime.now())
    visit2 = Visit(client_id =  clientAnna2.id, mentor_id = mentorAndrey2.id, trainingtype_id=singleTraining.id, visit_date=datetime.datetime.now())
    db.session.add(visit)
    db.session.add(visit2)
    db.session.commit()

if __name__ == '__main__':
  app.run()

