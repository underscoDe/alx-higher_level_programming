#!/usr/bin/python3
"""Deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa.
Usage: ./13-model_state_delete_a.py <mysql username> /
                                    <mysql password> /
                                    <database name>
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)

    my_session = Session()

    for row in my_session.query(State).filter(State.name.like('%a%')).all():
        my_session.delete(row)
    my_session.commit()
    my_session.close()
