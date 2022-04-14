from data.headhunter import HeadHunter
from data.seeker import Seeker


def get_user_by_tg_id(session, tg_id: int):
    headhunter = session.query(HeadHunter).filter(
        HeadHunter.tg_user_id == tg_id).first()
    if headhunter:
        return headhunter
    seeker = session.query(Seeker).filter(Seeker.tg_user_id == tg_id).first()
    if not seeker:
        return False
    return seeker
