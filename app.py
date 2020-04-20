"""Flask app for Cupcakes"""
from flask import Flask, render_template, redirect, flash, session, request, jsonify, url_for
from models import Cupcake, db, connect_db
import json


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQALCHEMY_ECHO']= True
app.config['SECRET_KEY'] = 'secret'

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)
db.create_all()

@app.route('/')
def home_page():

    return render_template('homepage.html')

@app.route('/api/cupcakes')
def list_all_cupcakes():
     """Return JSON for all cupcakes"""
     
     cupcakes = Cupcake.query.all()
     serialized = [c.serialize_cupcake() for c in cupcakes]

     return jsonify(cupcakes = serialized)

@app.route('/api/cupcakes/<int:id>')
def list_one_cupcake(id):
    """Return JSON for a single cupcake"""

    cupcake = Cupcake.query.get_or_404(id)
    serialize = cupcake.serialize_cupcake()
    return jsonify(cupcake=serialize)

@app.route('/api/cupcakes/search')
def search_cupcake(search):
    res = Cupcake.query.filter(Cupcake.flavor.ilike('%'+search+'%')).all()
    serialize=res.serialize_cupcake()
    return jsonify(cupcake=serialize)

@app.route('/api/cupcakes', methods=["POST"])
def post_cupcake():
    """Post cupcake"""
    new_cupcake = Cupcake(flavor=request.json["flavor"], size=request.json['size'], rating=request.json['rating'],image=request.json['image'])
    db.session.add(new_cupcake)
    db.session.commit()
    response_json = jsonify(cupcake=new_cupcake.serialize_cupcake())
    return (response_json,201)

@app.route('/api/cupcakes/<int:id>', methods=['PATCH'])
def patch_cupcake(id):
    """Return JSON patch"""
    cupcake = Cupcake.query.get_or_404(id)
    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)
    db.session.commit()
    return jsonify(cupcake=cupcake.serialize_cupcake())

@app.route('/api/cupcakes/<int:id>', methods=["DELETE"])
def delete_cupcake(id):
    """Delete cupcake"""
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message="deleted")






    
