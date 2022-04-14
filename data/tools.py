from data.task import *
from data.headhunter import *
from data.headhunter import *
from data.seeker import *
from data.job import *
from data.replies import *

def get_user_by_tg_id(session, tg_id: int):
    headhunter = session.query(HeadHunter).filter(
        HeadHunter.tg_user_id == tg_id).first()
    if headhunter:
        return headhunter
    seeker = session.query(Seeker).filter(Seeker.tg_user_id == tg_id).first()
    if not seeker:
        return False
    return seeker

def get_relative_job(session, tg_id, tags: list):
    return session.query(Job).first()
