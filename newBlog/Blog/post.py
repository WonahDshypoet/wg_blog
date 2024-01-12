'''
Post module that saves posts to Database,
Gets posts from database,

'''

import uuid
from .database import Database
import datetime


class Post(object):

    def __init__(self, blog_id, title, author, content, created_date=datetime.datetime.utcnow(), id=None):
        self.blog_id = blog_id
        self.title = title
        self.author = author
        self.content = content
        self.id = uuid.uuid4().hex if id is None else id
        self.created_date = created_date

    def save_to_mongo(self):
        Database.initialize()
        Database.insert(collection='posts', data=self.json())

    def json(self):
        return{
            'id': self.id,
            'blog_id': self.blog_id,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'created_date': self.created_date
        }

    @classmethod
    def from_mongo(cls, id):
        Database.initialize()
        post_data = Database.find_one(collection='posts', query={'id': id})
        return cls(blog_id=post_data['blog_id'],
                   title=post_data['title'],
                   author=post_data['author'],
                   content=post_data['content'],
                   created_date=post_data['created_date'],
                   id=post_data['id'])

    @staticmethod
    def from_blog(id):
        Database.initialize()
        return [post for post in Database.find(collection='posts', query={'blog_id': id})]
