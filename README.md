# flask_SqlAlchemy_MySQL

In this example, we are trying to create MySQL tables using SQLAlchemy and Flask 

### Extension:
- Restful: [Flask](http://flask-restplus.readthedocs.io/en/stable/)

- SQL ORM: [Flask-SQLalchemy](http://flask-sqlalchemy.pocoo.org/2.1/)

- Testing: [Flask-Testing](http://flask.pocoo.org/docs/0.12/testing/)


## Installation

Install with pip3:

```
$ pip3 install -r requirements.txt
```

## Flask Application Structure 
```
Note that if we decide to continue this project, this is how our folder structure will be!
.
|──────app/
| |────__init__.py
| |────api/
| | |────__init__.py
| | |────cve/
| | |────user/
| | |────oauth/
| |──────config.Development.cfg
| |──────config.Production.cfg
| |──────config.Testing.cfg
| |────dao/
| |────model/
| |────oauth/
| |────util/
|──────run.py
|──────tests/

```


## Flask Configuration

#### Example

```
app = Flask(__name__)
app.config['DEBUG'] = True
```
### Configuring From Files

#### Example Usage

```
app = Flask(__name__ )
app.config.from_pyfile('config.Development.cfg')
```

#### cfg example

```

##Flask settings
DEBUG = True  # True/False
TESTING = False

##SWAGGER settings
SWAGGER_DOC_URL = '/api'

....


```

#### Builtin Configuration Values

SERVER_NAME: the name and port number of the server. 

JSON_SORT_KEYS : By default Flask will serialize JSON objects in a way that the keys are ordered.

- [reference¶](http://flask.pocoo.org/docs/0.12/config/)


### OAuth Setup
add your `client_id` and `client_secret` into config file.

### ESDAO Setup
add your `ES host` and `ES port` into config file 



 
## Run Flask
### Run flask for develop
```
$ python webapp/run.py
```
In flask, Default port is `5000`

### Run flask for production

** Run with gunicorn **

In  webapp/

```
$ gunicorn -w 4 -b 127.0.0.1:5000 run:app

```

* -w : number of worker
* -b : Socket to bind


### Run with Docker

```
$ docker build -t  .

$ docker run -p 5000:5000 --name  
 
```

In image building, the webapp folder will also add into the image


## Unittest
```
$ nosetests webapp/ --with-cov --cover-html --cover-package=app
```
- --with-cov : test with coverage
- --cover-html: coverage report in html format
