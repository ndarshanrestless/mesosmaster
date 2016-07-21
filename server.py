
from flask import Flask, request, session, g, Response
from flask.json import jsonify
import sys
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import random
import ipdb

# create our little application :)
app = Flask(__name__)
app.config.update(dict(
    DATABASE='postgres',
    HOST='localhost',
    DEBUG=False,  # True,
    SECRET_KEY='bar007',
    USERNAME='postgres',
    PASSWORD='bar',
))
app.config.from_object(__name__)


@app.route('/')
def index():
    return Response("This is Meso cluster master, What are you looking at?", 200)


'''
import jwt
import logging
import logging.handlers
from functools import wraps


# Setup logging for better debugging
MAX_LOG_FILE_SIZE = 512*1024*1024
LOG_FILENAME = '/home/admin/work/barlogs/server-%s.log' % (sys.argv[1])
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
handler = logging.handlers.RotatingFileHandler(
    LOG_FILENAME, maxBytes=MAX_LOG_FILE_SIZE, backupCount=5)
log.addHandler(handler)


# salt = uuid.uuid4().hex
secret = 'barhopper$$007$$'



def status_400_on_exception(f):
    """Decorator for generating a 400 bad request response."""
    @wraps(f)
    def _f(*args, **kwargs):
        try:
            retval = f(*args, **kwargs)
        except Exception as e:
            log.exception('exception in {}'.format(f.__name__))
            if app.debug:
                with closing(StringIO()) as s:
                    traceback.print_exception(*sys.exc_info(), file=s)
                    response = s.getvalue()
            else:
                response = repr(e)
            resp = jsonify(response=response, status={'success': False})
            resp.status_code = 400
            return resp
        else:
            return retval
    return _f


def connect_db():
    try:
        conn = psycopg2.connect(
            "dbname='postgres' user='postgres'"
            "host='localhost' password='bar'")
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    except:
        print "Unable to connect to PG database"
    return conn


def get_db():
    """
    Opens a new database connection
    if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'postgres_db'):
        g.postgres_db = connect_db()

    return g.postgres_db


@app.before_request
def before_request():
    g.postgres_db = connect_db()


@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'postgres_db', None)
    if db is not None:
        db.close()


def tokenCreate(username, deviceid):
    token = jwt.encode({'username': username, 'deviceid': deviceid},
                       secret, algorithm='HS256')
    return token


def tokenGetPayload(token):
    jret = jwt.decode(token, secret, algorithms=['HS256'])
    return jret


@app.route('/scrape', methods=['POST'])
@status_400_on_exception
def scrape_bar():
    jd = request.get_json()
    location = jd.pop('location')
    radius = int(jd.get('radius')) * 1610  # to meters
    type = jd.get('type', 'bar')
    totalrows, total_google_requests \
        = db_insert_google_bar(location, radius, get_db(), type=type)
    return jsonify(result=(totalrows, total_google_requests))

    
# eg: POST ratebar?device_id=007&
# bar_id=554ca521944c028e4da1b7e75623c9acaf9297a1
@app.route('/ratebar', methods=['POST'])
@status_400_on_exception
def rate_bar():
    jd = request.get_json()

    # Assert all the rating fields exsits in request
    assert jd is not None, "body cannot be empty & needs mandatory fields"
    assert 'bar_id' in jd, "bar_id needs to be provided"
    assert 'delta_time' in jd, "delta_time mandatory parameter"

    # todo: remove the fake random insert when naren start sendig device_id
    # assert 'device_id' in jd, "device_id needs to be provided"
    jd['device_id'] = random.randint(1, 2)

    bar_id = jd['bar_id']
    jd.pop('bar_id')

    delta_time = int(jd.pop('delta_time'))
    
    rating_fields = ('ambience_rating', 'women_quality_rating',
                     'men_quality_rating', 'drink_rating',
                     'hospitality_rating', 'average_age')
    
    assert all(keys in jd for keys in rating_fields),\
        "missing one of field {}".format(rating_fields)

    jd = {k: int(v) for k, v in jd.iteritems()}

    jd['bar_id'] = bar_id
    device_id = jd['device_id']

    db = get_db()
    insert_user(device_id, db)  # ??? what is this for todo
    # do the real calculation on post and insert into DB
    inserted_rowid = insert_rating_into_bar(jd, device_id,
                                                bar_id, delta_time, db)
    return jsonify(result=inserted_rowid)
    
@app.route('/feedback', methods=['POST'])
@status_400_on_exception
def feedback():
    jd = request.get_json()
    
    # Assert all the rating fields exsits in request
    assert jd is not None, "body cannot be empty & needs mandatory fields"
    assert 'feedback_text' in jd,\
        "feedback_text manatatory and cannot be empty"
    assert 'device_id' in jd, "device_id is mandatory field"

    device_id = jd.get('device_id', '')
    feedback_text = jd.get('feedback_text', '')
    user_name = jd.get('user_name', 'anonmyous')
    
    insert_feedback(get_db(), device_id,
                        feedback_text, user_name)
    resp = jsonify(dict({'success': True}))
    resp.status_code = 200
    return resp


@app.route('/logout', methods=['POST'])
def logout():
    # remove the username from the session if it's there
    session_value = session.pop('username', None)
    if session_value:
        return Response("Successfully logged out user username:{}".
                        format(session_value), 200)
    else:
        return Response("Hey, you had never logged in actually! :{}".
                        format(session_value), 200)


@app.route('/getnearbybars/', methods=['GET'])
@status_400_on_exception
def get_nearby_bars():
    dic = request.args.to_dict()

    location = dic.get('location')
    radius = int(dic.get('radius')) * 1610  # to meters

    db = get_db()
    dic = request.args.to_dict()
    assert 'open_now' in dic, "open_now mandatory parameter"
    assert 'delta_time' in dic, "delta_time mandatory parameter"
    open_now_filter = bool(int(dic.pop('open_now')))
    result = db_get_nearby_bars(location, radius, db, open_now_filter,
                                    args=dic)
    return jsonify(result=result)


@app.route('/getonebar/', methods=['GET'])
@status_400_on_exception
def get_one_bar():
    assert 'bar_id' in request.args, 'bar_id mandatory parameter'
    assert 'delta_time' in request.args, 'delta_time mandatory parameter'
    bar_id = request.args.get('bar_id')
    delta_time = int(request.args.get('delta_time'))
    db = get_db()
    rj = db_get_one_bar_information(bar_id, delta_time, db)
    return jsonify(result=rj)
'''
    
if __name__ == '__main__':
    if len(sys.argv) >= 2:
        port = int(sys.argv[1])
    else:
        port = 4000
    app.run(host='0.0.0.0', port=port)
