from flask import request, jsonify
from config import app, db
from models import Contact

#decorator - endpoint, request type
@app.route("/contacts", methods =["GET"])
def get_contacts():
    contacts = Contact.query.all()
    #get Python objects and want to turn into JSON data
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    return jsonify({"contacts": json_contacts})

@app.route("/create_contact", methods =["POST"])
def create_contacts():
    first_name = request.json.get("firstName")
    last_name = request.json.get("firstName")
    email = request.json.get("firstName")
    #if did not get all fields from request
    if not first_name or not last_name or not email:
        return jsonify({"message":"You must include all provided fields"}), 400
    
    new_contact = Contact(first_name, last_name, email)
    try:
        #write to db
        db.session.add(new_contact)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    
    return jsonify({"message": "User Created"}), 201

#path parameter for which id to update
@app.route("/update_contact/<int:user_id>", methods=["PATCH"])
def update_contact(user_id):
    #get specific contact for the user
    contact = Contact.query.get(user_id)

    if not contact:
        return jsonify({"message": "User not found"}), 404

    data = request.json
    
    #get works by finding key value first else use second param
    contact.first_name = data.get("firstName", contact.first_name)
    contact.last_name = data.get("lastName", contact.last_name)
    contact.email = data.get("email", contact.email)
    #already in session
    db.session.commit()

    return jsonify({"message": "User updated."}), 200

@app.route("/delete_contact/<int:user_id>", methods=["DELETE"])
def delete_contact(user_id):
    contact = Contact.query.get(user_id)

    if not contact:
        return jsonify({"message": "User not found"}), 404

    db.session.delete(contact)
    db.session.commit()

    return jsonify({"message": "User deleted!"}), 200

#only when running file directly
if __name__ == "__main__":
    #create db if it doesn't exist
    with app.app_context():
        db.create_all()
    
    app.run(debug=True)