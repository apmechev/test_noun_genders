from sqlalchemy import Boolean, DateTime, Column, Integer, String, ForeignKey, Float

class Tag(Model):
    __tablename__ = 'tag'
    id = Column(Integer(), primary_key=True)
    tagname = Column('tagname', String())

class UserTag(Model):
    __tablename__ = 'usertag'
    id = Column(Integer(), primary_key=True)
    user = Column('word_id', Integer(), ForeignKey('word.id'))
    tag = Column('tag_id', Integer(),  ForeignKey('tag.id'))

class Word(Model)
    __tablename__ = 'word'
    id = Column(Integer(), primary_key=True)
    word = Column('word', String())
    gender = Column('gender', Integer() ForeignKey('gender.id'))

class Genders(Model):
    __tablename__ = 'gender'
    id = Column(Integer(), primary_key=True)
    gender = Column('gender', String())

