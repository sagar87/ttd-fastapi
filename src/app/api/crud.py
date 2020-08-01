from app.api.models import NoteSchema
from app.db import notes, database


async def post(payload: NoteSchema):
    query = notes.insert().values(title=payload.title, description=payload.description)
    return await database.execute(query=query)

async def get(id: int):
    # query = notes.select().where(id == notes.c.id)
    q = "SELECT * FROM notes WHERE id = :id"
    return await database.fetch_one(query=q, values={"id": id})

async def get_all():
    q = "SELECT * FROM notes"
    return await database.fetch_all(query=q)

async def put(id: int, payload: NoteSchema):
    query = (
        notes
        .update()
        .where(id == notes.c.id)
        .values(title=payload.title, description=payload.description)
        .returning(notes.c.id)
    )
    return await database.execute(query=query)


async def delete(id: int):
    query = notes.delete().where(id == notes.c.id)
    return await database.execute(query=query)