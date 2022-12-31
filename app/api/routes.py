from flask import Flask
app = Flask(__name__)


from urllib import response
from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, User, Contact, contact_schema, contacts_schema

api = Blueprint('api',__name__, url_prefix='/api')


@api.route('/contacts', methods = ['POST'])
@token_required
def create_contact(current_user_token):
    print("comin here")
    name = request.json['name']
    email = request.json['email']
    beer = request.json['beer']
    user_token = current_user_token.token
    print(name)
    print(f'BIG TESTER: {current_user_token.token}')
    
    contact = Contact(email,name, beer,user_token)
    
    db.session.add(contact)
    db.session.commit()
    
    response = contact_schema.dump(contact)
    return jsonify(response)


@api.route('/contacts', methods = ['GET'])
@token_required
def get_contact(current_user_token):
    a_user = current_user_token.token
    contacts = Contact.query.filter_by(user_token=a_user).all()
    response = contacts_schema.dump(contacts)
    return jsonify(response)


@api.route('/contacts/<id>', methods = ['GET'])
@token_required
def get_single_contact(id):
    contact = Contact.query.get(id)
    response = contact_schema.dump(contact)
    return jsonify(response)

@api.route('/contacts/<id>', methods = ['POST','PUT'])
@token_required
def update_contact(current_user_token,id):
    contact = Contact.query.get(id)
    contact.name = request.json['name']
    contact.email = request.json['email']
    contact.beer = request.json['beer']
    contact.user_token = current_user_token.token

    db.session.commit()
    response = contact_schema.dump(contact)
    return jsonify(response)

@api.route('/contacts/<id>', methods = ['DELETE'])
@token_required
def delete_contact(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()
    response = contact_schema.dump(contact)
    return jsonify(response)