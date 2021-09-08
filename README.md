# Learning SQLModel
A simple app that I am using to become more familiar with FastAPI and more particularly, SQLModel.

(This code was essentially built from the documentation available for SQLModel [here](https://sqlmodel.tiangolo.com/))

## Getting Started
1. Clone this repository and navigate into it.
```bash
git clone git@github.com:joemudryk/learning-sqlmodel.git
cd learning-sqlmodel
```
2. Then run with either docker or a python virtual environment

#### ...with Docker
To run the app using just docker, you can call the script
```bash
# docker will need to be installed
./scripts/run_with_docker.sh
```

#### ...with a python virtual environment
```bash
# python3.9 is recommended
python -m venv venv
source venv/bin/activate
pip install -r requirements
python main.py
```

## Challenge
I have been looking into a few ORMs to use with FastAPI such as [ormar](https://github.com/collerek/ormar/) 
and [tortoise-orm](https://github.com/tortoise/tortoise-orm). Then to my delight, 
Sebastián Ramírez released [SQLModel](https://github.com/tiangolo/sqlmodel), 
which looks like it has everything I was after (along with his great coding style and documentation).

Unfortunately I wasn't able to get database migrations working with my limited experience in that area.  
I tried using [Alembic](https://alembic.sqlalchemy.org/en/latest/), but with no success. Any feedback or instructions 
on how database migrations can be done with SQLModel, would be greatly appreciated.

Databases I am intending to use are
- SQLite
- postgreSQL
- CockroachDB