from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine, desc
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
    # Items with greater ids are the items added most lately
    latest = session.query(Item).order_by(desc(Item.id)).limit(8).all()
    return render_template('catalog.html', categories=categories, latest=latest)


@app.route('/catalog/<string:category_name>/')
def categoryItems(category_name):
    categories = session.query(Category).all()
    items = session.query(Item).filter_by(category_name=category_name).all()
    return render_template('categoryitem.html', categories=categories, category_name=category_name, items=items)


@app.route('/catalog/<int:item_id>/')
def itemInfo(item_id):
    item = session.query(Item).filter_by(id=item_id).one()
    return render_template('iteminfo.html', item=item)


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
    if request.method == 'POST':
        return "edit item " + str(item_id)
    else:
        item = session.query(Item).filter_by(id=item_id).one()
        return "edit item " + str(item_id)


@app.route('/item/<int:item_id>/delete/', methods=['GET', 'POST'])
def deleteItem(item_id):
    item = session.query(Item).filter_by(id=item_id).one()
    if request.method == 'POST':
        session.delete(item)
        session.commit()
        return redirect(url_for('latestItems'))
    else:
        return render_template('deleteitem.html', item=item)


@app.route('/catalog.json/')
def catalogJSON():
    categories = session.query(Category).all()
    return jsonify(Categories=[c.serialize for c in categories])


if __name__ == '__main__':

    app.debug = True
    app.run(host='0.0.0.0', port=5000)
