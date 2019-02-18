from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item

app = Flask(__name__)

engine = create_engine('sqlite:///catalog.db',
                       connect_args={'check_same_thread': False})
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
    categories = session.query(Category).all()
    items = session.query(Item).filter_by(category_name=category_name).all()
    return render_template('categoryitem.html', categories=categories, category_name=category_name, items=items)


@app.route('/catalog/<string:category_name>/<int:item_id>/')
def itemInfo(category_name, item_id):
    return "page of information of " + item_id + " in category " + category_name


@app.route('/catalog/<string:category_name>/<int:item_id>/json')
def itemJSON(category_name, item_id):
    return "json of " + item_id + " in category " + category_name


@app.route('/item/add/', methods=['GET', 'POST'])
def addItem():
    if request.method == 'POST':
        categories = session.query(Category).all()
        newItem = Item(
            name=request.form['name'], description=request.form['description'], category_name=request.form['category'])
        session.add(newItem)
        session.commit()
        return redirect(url_for('categoryItems', category_name=request.form['category']))
    else:
        categories = session.query(Category).all()
        return render_template('additem.html', categories=categories)


@app.route('/item/<int:item_id>/edit/', methods=['GET', 'POST'])
def editItem(item_id):
    return "edit item " + item_id


@app.route('/item/<int:item_id>/delete/', methods=['GET', 'POST'])
def deleteItem(item_id):
    return "delete item " + item_id


@app.route('/catalog.json/')
def catalogJSON():
    categories = session.query(Category).all()
    return jsonify(Categories=[c.serialize for c in categories])


if __name__ == '__main__':

    app.debug = True
    app.run(host='0.0.0.0', port=5000)
