import datetime

import sqlalchemy as sa
import sqlalchemy.ext.declarative

Base = sqlalchemy.ext.declarative.declarative_base()


class Users(Base):
    __tablename__ = "users"

    user_id: int = sa.Column(sa.BigInteger, primary_key=True)
    first_name: str = sa.Column(sa.Text)
    last_name: str = sa.Column(sa.Text)
    created_at: datetime = sa.Column(sa.DateTime, default=datetime.datetime.utcnow)
    updated_at: datetime = sa.Column(
        sa.DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow
    )

    def __init__(self, user_id: int, first_name: str, last_name: str):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return "<User(user_id='%s', first_name='%s', last_name='%s')>" % (
            self.user_id, self.first_name, self.last_name)
