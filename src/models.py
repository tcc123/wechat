#coding:utf-8
import inspect

import web

db = web.database(dbn='sqlite', db="wechat.db")


class DBManage(object):
    # TODO: 改成objects吧
    @classmethod
    def table(cls):
        return cls.__name__.lower()

    @classmethod
    def get_by_id(cls, id):
        itertodo = db.select(cls.table(), where="id=$id", vars=locals())
        # 参考：https://groups.google.com/forum/#!msg/webpy/PP81l8C5kbQ/90Hgx3HUqG0J
        return next(iter(itertodo), None)

    @classmethod
    def get_all(cls):
        # inspect.ismethod(cls.get_all)
        return db.select(cls.table())

    @classmethod
    def create(cls, **kwargs):
        return db.insert(cls.table(), **kwargs)

    @classmethod
    def update(cls, **kwargs):
        db.update(cls.table(), where="id=$id", vars={"id": kwargs.pop('id')}, **kwargs)

    @classmethod
    def delete(cls, id):
        db.delete(cls.table(), where="id=$id", vars=locals())


class User(DBManage):
    id = None
    username = None
    password = None
    registed_time = None


class Topic(DBManage):
    id = None
    name = None
    created_time = None
    owner = None


class Message(DBManage):
    id = None
    content = None
    top_id = None
    user_id = None
    reply_to = None
