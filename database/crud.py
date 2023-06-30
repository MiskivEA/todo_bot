from sqlalchemy import select
from sqlalchemy.orm import Session

from database.database import engine
from database.models import Task


def create_task(task_text, telegram_id):
    with Session(engine) as db:
        task = Task(
            telegram_id=telegram_id,
            title=task_text[:10],
            description=task_text,
            status=False,
        )
        db.add(task)
        db.commit()


def get_tasks():
    session = Session(engine)
    stmt = select(Task)
    tasks = session.scalars(stmt)
    return tasks
