from flask import Flask, request, session, g, Response
from flask.json import jsonify
import sys
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import random
import ipdb
from functools import wraps

# create our little application :)
app = Flask(__name__)
app.config.update(dict(
    DATABASE='postgres',
    HOST='localhost',
    DEBUG=True,
    SECRET_KEY='bar007',
    USERNAME='postgres',
    #PASSWORD='bar',
))
app.config.from_object(__name__)

@app.route('/')
def index():
    return Response("This is Meso cluster master, What are you looking at?", 200)


def connect_db():
    try:
        conn = psycopg2.connect(
            "dbname='postgres' user='postgres'")
            #"host='localhost'")
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


def query_db(db, query, args=(), one=False):
    cur = db.cursor()
    cur.execute(query, args)
    r = [dict((cur.description[i][0], value)
              for i, value in enumerate(row)) for row in cur.fetchall()]
    #cur.connection.close()
    return (r[0] if r else None) if one else r

def status_400_on_exception(f):
    """Decorator for generating a 400 bad request response."""
    @wraps(f)
    def _f(*args, **kwargs):
        try:
            retval = f(*args, **kwargs)
        except Exception as e:
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


@app.route('/registermaster', methods=['POST'])
#@status_400_on_exception
def register_master():
    ipdb.set_trace()
    
    jd = request.args
    
    # Assert all the rating fields exsits in request
    assert jd is not None, "Need to send the ip of mesos master"
    
    try:
        db = get_db()
        db.cursor().execute("INSERT INTO registered_mesos VALUES "
                            "(%s, %s)", (jd['ip'], 
                                        jd['id_name']))
    except Exception as err:
        return Response("{}".format(err),400) 
    
    return Response("Successfully registered the master with ip:{}".
                    format(jd['mesos_server_ip']), 200)

@app.route('/dockercontainer', methods=['POST'])
@status_400_on_exception
def docker_container_info():
    ipdb.set_trace()
    
    jd = request.args
    
    assert jd is not None, "Need the information of the docker container"
    
    try:
        db = get_db()
        db.cursor().execute(
            """INSERT INTO docker_container_data VALUES (%s, %s, %s)""" 
            (str(jd['docker_id']), str(jd['mesos_master_id']), 
             str(jd['mesos_slave_id'])))

        db.save
    except IntegrityError as err:
        return Response("Already exists so skipping DB insert", 200)
    except IntegrityError as err:
        return Response("{}".format(err), 400)
 
        
    
    return Response("Thank you for the details. The Docker_id is - {}."
                    "The Master id is - {}. The slave id is - {}.".
                    format (jd['docker_id'], jd['mesos_master_id'], 
                            jd['mesos_slave_id']), 200) 

    
@app.route('/dockerdeath', methods=['POST'])
@status_400_on_exception
def docker_death():
    ipdb.set_trace()
    jd = request.args

    # Assert all the rating fields exsits in request
    assert jd is not None, "Need to send the ip of mesos master"

    return Response("Successfully got ot knwo the dockerid:{} died ".
                    format(jd['docker_id']), 200)

    
def get_next_mesos_to_spin_docker():
    pass
    
if __name__ == '__main__':
    if len(sys.argv) >= 2:
        port = int(sys.argv[1])
    else:
        port = 4000
    app.run(host='0.0.0.0', port=port)
