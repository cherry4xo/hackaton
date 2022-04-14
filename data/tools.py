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


def get_relative_job(session, tg_id, tags):
    tg_id = int(tg_id)

    user = session.query(Seeker).filter(Seeker.tg_user_id == tg_id).first()
    viewed_ids = list(json.loads(user.viewed_job_ids))

    jobs = session.query(Job).all()
    tags = set([str(x).lower for x in list(tags)])

    found = {}
    for job in jobs:
        if job.id in viewed_ids:
            continue

        job_tags = set(json.loads(job.skills))

        job_tags = set([str(x).lower for x in job_tags])

        intersection = job_tags & tags

        match_count = len(intersection)

        found[job] = match_count

    ready = {k: v for k, v in sorted(found.items(), key=lambda item: item[1])}

    if len(ready) == 0:
        return None

    job_to_display = next(iter(ready))

    viewed_ids.append(job_to_display.id)
    user.viewed_job_ids = str(viewed_ids)
    session.commit()

    return job_to_display


def get_relative_task(session, tg_id: int, tags):
    tg_id = int(tg_id)
    user = session.query(Seeker).filter(Seeker.tg_user_id == tg_id).first()
    viewed_ids = list(json.loads(user.viewed_task_ids))

    jobs = session.query(Task).all()
    tags = set([str(x).lower for x in list(tags)])

    found = {}
    for job in jobs:
        if job.id in viewed_ids:
            continue

        job_tags = set(json.loads(job.skills))

        job_tags = set([str(x).lower for x in job_tags])

        intersection = job_tags & tags

        match_count = len(intersection)

        found[job] = match_count

    ready = {k: v for k, v in sorted(found.items(), key=lambda item: item[1])}

    if len(ready) == 0:
        return None

    job_to_display = next(iter(ready))

    viewed_ids.append(job_to_display.id)
    user.viewed_task_ids = str(viewed_ids)
    session.commit()

    return job_to_display
