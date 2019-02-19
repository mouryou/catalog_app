# Catalog App

## Requirements

- [Python 2.7](https://www.python.org/download/releases/2.7/)
- [Flask](http://flask.pocoo.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [oauth2client](https://github.com/googleapis/oauth2client)
  
Please follow these pages to install them before running the project.  
This project is tested in Ubuntu 16.04.5 LTS.  

## Instructions

1. Run `python --version` to make sure you are using python2.7
2. Run `python database_setup.py` to setup the database
3. Run `python application.py` to start the project
4. Open `localhost:5000` to use the catalog application. If you use the address `127.0.0.1:5000`, login may fail.  

## Notes

- API Endpoints are `/catalog.json/`, `/item/<int:item_id>/json` and `/catalog/<string:category_name>/json`
- Read: `/catalog/`, `/catalog/<string:category_name>/` and `/catalog/<int:item_id>/`
- Create: `/item/add/`
- Update: `/item/<int:item_id>/edit/`
- Delete: `/item/<int:item_id>/delete/`
- User can only create new items after login, and only who creates the item can edit or delete it. Who tries to visit these protected pages by url will be redirected to the login page.