#! python3.9
from fastapi import FastAPI
from starlette.routing import RedirectResponse

from database import create_db_and_tables
from api import heroes


app = FastAPI(
    title='Learning SQLModel',
    description='Loving the clean coding styles coming from Sebastián Ramírez, keep up the great work :)',
)

# Include FastAPI api routers
app.include_router(heroes.router)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get('/', tags=['Admin'])
def redirect_root_to_docs():
    return RedirectResponse('/docs/')


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app="main:app", host='0.0.0.0', port=8080, reload=True)
