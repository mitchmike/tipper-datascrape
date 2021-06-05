from sqlalchemy import Column, Integer, String, Date, DateTime, Boolean, Sequence, UniqueConstraint
from sqlalchemy.orm import relationship

from base import Base

class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer, Sequence('player_id_seq'), primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    number = Column(Integer)
    team = Column(String)
    games = Column(Integer)
    age = Column(String)
    DOB = Column(Date)
    height = Column(Integer)
    weight = Column(Integer)
    position = Column(String)
    updated_at = Column(DateTime)
    injuries = relationship("Injury", back_populates="player")
    __table_args__ = (UniqueConstraint('first_name', 'last_name', 'DOB', 'team', name='uix_1'), )
    def __repr__(self):
        return "<Player(id='%s', number='%s', team='%s', \
first_name='%s', last_name='%s', games='%s', \
age='%s', DOB='%s', height='%s', weight='%s', \
position='%s', updated_at='%s')>" % (self.id, self.number, self.team, self.first_name, 
            self.last_name, self.games, self.age, self.DOB, self.height,
        self.weight, self.position, self.updated_at)

