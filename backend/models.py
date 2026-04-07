from config import db

class Contact(db.Model):
    #represent the db as a class

    #db fields
    id = db.Column(db.Integer, primary_key=True) #key used to index must be unique
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    #pass json object (use dictionary)
    def to_json(self):
        return {
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email,
        }