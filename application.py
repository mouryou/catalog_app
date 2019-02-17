from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/catalog/')
def latestItems():
    return "page of latest added items"

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
    return "json of catalog"

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
