#!/usr/bin/python3
"""Script that prints all City objects from the database"""
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(State, City).filter(
        State.id == City.state_id).order_by(City.id)
    for state, city in cities:
        print(f"{state.name}: ({city.id}) {city.name}")
    session.close()
