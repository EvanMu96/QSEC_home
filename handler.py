'url handlers'

import re, time, json, logging, hashlib, base64, asyncio

from MyPy import get, post

from model import User, Comment, Article


@get('/')
async def index(request):
    users = await User.findAll()
    return {
        '__template__': 'test.html',
        'user': users
    }
