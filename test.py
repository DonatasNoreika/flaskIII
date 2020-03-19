from app import db, Query

# jonas = Query('Jonas', 'jonas@mail.com', 'Kažkoks labai rimtas atsiliepimas.')
# antanas = Query('Antanas', 'antanas@mail.lt', 'Antano nuomonė labai svarbi.')
# juozas = Query('Juozas', 'juozukas@friends.lt', 'Aš labai piktas, nes blogai.')
# bronius = Query('Bronius', 'bronka@yahoo.com', 'Aš tai linksmas esu, man patinka.')


# db.session.add_all([jonas, antanas, juozas, bronius])
# db.session.add(antanas)
# db.session.add(juozas)
# db.session.add(bronius)
# db.session.commit()


antanas = Query.query.get(2)
db.session.delete(antanas)
db.session.commit()
