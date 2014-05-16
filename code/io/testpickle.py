__author__ = 'sancheng'

import datetime
from datetime import timedelta as dlt
import shelve

import pickle
import cPickle

import StringIO
import cStringIO



#print 'format1:%s, format2:%d' % ('string',11)
#test mail notification
class Car:
    def __init__(self):
        self.brand = 'ford'
        self.oilconsume = 11
        self.producedate = datetime.date.today() - dlt(days=365)
        self.trademark = 'focus'

    def __repr__(self):
        return self.brand + " " + self.trademark + " " + str(self.oilconsume)


import pickle

f = open('serializedobj.bin', 'wb+')

pickle.dump(Car(), f)

f.close()

loadedobj = pickle.load(open('serializedobj.bin', 'rb'))

import pprint

pprint.pprint(loadedobj)

