import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    rollnumber = Column(Integer, primary_key = True, autoincrement = False)
    uname      = Column(String(30), nullable = False)
    email      = Column(String(30), nullable = False)
    password   = Column(String(20), nullable = False)
    inclass    = Column(Integer, nullable = True)
    yearin     = Column(Integer, nullable = True)
    dob        = Column(String(11), nullable = False)
    profilepic = Column(String(500), nullable = True)
    rank       = Column(Integer, nullable = False, default = 0)

class Clubs(Base):
    __tablename__ = 'clubs'

    clubid     = Column(Integer, primary_key = True, autoincrement = True)
    clubdesc   = Column(String(500), nullable = False)

class Posts(Base):
    __tablename__ = 'posts'

    postid     = Column(Integer, primary_key = True, autoincrement = True)
    postedby   = Column(Integer, ForeignKey(User.rollnumber), nullable = False)
    moderatedby= Column(Integer, ForeignKey(User.rollnumber), nullable = True, default = 0)
    club       = Column(Integer, ForeignKey(Clubs.clubid), nullable = True)
    title      = Column(String(40), nullable = False)
    shortdesc  = Column(String(300), nullable = False)
    longdesc   = Column(String(1500), nullable = True)
    startdate  = Column(String(11), nullable = False)
    enddate    = Column(String(11), nullable = False)
    postpic    = Column(String(500), nullable = True)
    contact    = Column(Integer, nullable = True)
    modstatus  = Column(Integer, unique = False, default = 0)

engine = create_engine('sqlite:///campusdiaries.db')
Base.metadata.create_all(engine)
