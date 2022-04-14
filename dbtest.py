from venv import create

from data.db_session import global_init
from data.task import *
from data.headhunter import *
from data.headhunter import *
from data.seeker import *
from data.job import *
from data.replies import *

from datetime import date
from data.db_session import create_session

import json 

global_init('sqlite.sqlite')

sess = create_session()


seeker = add_seeker(sess, 123, 'sdfdfd', 'full name', json.dumps(['asfd']))

hh = add_headhunter(sess, 1234, 'SasyCo', 'Sfogfbok')

tsk = add_task(sess, 'Sasd', 'dfggfgfg', 1000, date(2021, 12, 13), json.dumps(['prog']), hh)

add_task_reply(sess, tsk, 'Rep', seeker)


def get_user(session, tg_id:int):
    headhunter = session.query(HeadHunter).filter(HeadHunter.tg_user_id == tg_id).first()
    if headhunter: return headhunter
    seeker = session.query(Seeker).filter(Seeker.tg_user_id == tg_id).first()
    if not seeker: return False
    return seeker

print(get_user(sess, 1456))

