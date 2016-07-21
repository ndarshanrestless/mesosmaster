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
    DEBUG=False,  # True,
    SECRET_KEY='bar007',
    USERNAME='postgres',
    PASSWORD='bar',
))
app.config.from_object(__name__)


@app.route('/')
def index():
    return Response("This is Meso cluster master, What are you looking at?", 200)


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


@app.route('/registermaster', methods=['POST'])
@status_400_on_exception
def register_master():
    ipdb.set_trace()
    
    jd = request.args
    print jd

    # Assert all the rating fields exsits in request
    assert jd is not None, "Need to send the ip of mesos master"

    #todo save in Postgres the state
    
    return Response("Successfully registered the master with ip:{}".
                    format(jd['mesos_server_ip']), 200)

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
