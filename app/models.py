from . import db

class QuranSearch(db.Model):
    __table__ = db.Model.metadata.tables['quran_search']

class Words(db.Model):
    __table__ = db.Model.metadata.tables['Words']

class Ayas(db.Model):
    __table__ = db.Model.metadata.tables['Ayas']
