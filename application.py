from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item

app = Flask(__name__)

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/catalog/')
def latestItems():
    categories = session.query(Category).all()
    return render_template('catalog.html', categories=categories)


@app.route('/catalog/<string:category_name>/')
def categoryItems(category_name):
    return "page of the list of items of " + category_name


@app.route('/catalog/<string:category_name>/<string:item_name>/')
def itemInfo(category_name, item_name):
    return "page of information of " + item_name + " in category " + category_name


@app.route('/catalog/<string:category_name>/<string:item_name>/json')
def itemJSON(category_name, item_name):
    return "json of " + item_name + " in category " + category_name


@app.route('/item/add/', methods=['GET', 'POST'])
def addItem():
    return "page to add an item"


@app.route('/item/<string:item_name>/edit/', methods=['GET', 'POST'])
def editItem(item_name):
    return "edit item " + item_name


@app.route('/item/<string:item_name>/delete/', methods=['GET', 'POST'])
def deleteItem(item_name):
    return "delete item " + item_name


@app.route('/catalog.json/')
def catalogJSON():
    categories = session.query(Category).all()
    return jsonify(Categories=[c.serialize for c in categories])


if __name__ == '__main__':

    app.debug = True
    app.run(host='0.0.0.0', port=5000)
