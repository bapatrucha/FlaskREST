from db import db

class ItemModel(db.Model):

    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'id': self.id, 'name': self.name, 'price': self.price}

    @classmethod
    def findByName(cls, name):
        return cls.query.filter_by(name=name).first()  # using sqlAlchemy

    def save(self):
        db.session.add(self)
        db.session.commit()
        # without sqlAlchemy
        # conn = sqlite3.connect('data.db')
        # cursor = conn.cursor()
        # query = "INSERT INTO items values (?,?)"
        # print("creating a new item {}".format(self.name))
        # cursor.execute(query, (self.name,self.price,))
        # conn.commit()
        # conn.close()


    def delete(self):
        db.session.delete(self)
        db.session.commit()
        # without sqlAlchemy
        # conn = sqlite3.connect('data.db')
        # cursor = conn.cursor()
        # updateQuery = "UPDATE items set price = ? where name = ?"
        # cursor.execute(updateQuery, (self.price, self.name,))
        # conn.commit()
        # conn.close()
