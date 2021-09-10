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

After running the app, then navigate to http://0.0.0.0:8080 to interact with the API. 

---

## Update a model and run a database migration 
An example of using alembic to update the database keeping up to date with the models

### Update the model
Example of updating a SQLModel
```python
class HeroBase(SQLModel):
    name: str
    secret_name: str
    age: Optional[int] = None
    power: Optional[str] = None                # New


class Hero(HeroBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
```
**Note:** Be sure that the new class variable is either Optional or has a default value. This is so alembic can back 
populate entries in the database if needed.

#### Also make sure the models you are using are imported in [migrations/env.py](migrations/env.py)

### Autogenerate a new migration
```bash
python -m alembic revision --autogenerate -m "Add power to Hero model"
```
Or use the [autogenerate_migration.sh](scripts/autogenerate_migration.sh) script in the scripts directory, saves a bit of typing.
### Apply the migration 
```python
python -m alembic upgrade head
```

## All done
And Bob's your Aunty. A fairly simplistic way of using SQLModel with alembic :) 