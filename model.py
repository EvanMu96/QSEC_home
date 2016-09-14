import time, uuid
from orm import Model, StringField, BooleanField, FloatField, TextField

# We use float type to store time in order to ignore timezone


def next_id():
    return '%015d%s000' % (int(time.time()*1000, uuid.uuid4().hex))


class User(Model):
    __table__ = 'users'

    id = StringField(primary_key=True, default=next_id(), ddl='varchar(50)')
    email = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    admin = BooleanField()
    create_at = FloatField(default=time.time())


class Article(Model):
    __table__ = 'Article'

    id = StringField(primary_key=True, default=next_id(), ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    user_name = StringField(ddl='varchar(50)')
    summary = StringField(ddl='varchar(50)')
    content = TextField()
    create_at = FloatField(default=time.time())


class Comment(Model):
    __table__ = 'Comment'

    id = StringField(primary_key=True, default=next_id(), ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    blog_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    content = TextField()
    create_at = FloatField(default=time.time())




