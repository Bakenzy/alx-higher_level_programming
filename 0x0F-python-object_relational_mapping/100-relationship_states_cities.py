#!/usr/bin/python3
"""This script deletes all State objects with a name
containing the letter a from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City, Base
from relationship_state import State
if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    california = State(name="California")
    san_francisco = City(name="San Francisco")
    san_francisco.state = california
    session.add(california)
    session.add(san_francisco)
    session.commit()
