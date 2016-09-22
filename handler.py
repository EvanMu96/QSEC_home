'url handlers'

import re, time, json, logging, hashlib, base64, asyncio

from MyPy import get, post

from model import User, Comment, Article


@get('/')
async def index(request):
    summary = 'test string'
    articles = [
        Article(id='1', name='Test Blog', summary=summary, create_at=time.time()-120),
        Article(id='1', name='Test Blog', summary=summary, create_at=time.time() - 120),
        Article(id='1', name='Test Blog', summary=summary, create_at=time.time() - 120),
    ]
    return {
        '__template__': 'blog.html',
        'aricles': articles
    }


@get('/api/users')
def api_get_users():
    users = yield from User.findAll(orderBy='create_at desc')
    for u in users:
        u.password = '******'
    return dict(users)

