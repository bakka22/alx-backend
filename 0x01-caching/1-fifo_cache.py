#!/usr/bin/env python3
""" FIFO Replacment policy """
BasicCache = __import__('0-basic_cache').BasicCache
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BasicCache):
    """ Caching system that implements FIFO Replacment policy """

    def __init__(self):
        """ initialize an instance of the class """
        super().__init__()
        self.key_q = []

    def put(self, key, item):
        """ assign a value to a key in self.cache_data"""
        #if not key or not item:
            #return
        self.cache_data[key] = item
        if key not in self.key_q:
            self.key_q.append(key)
            if len(self.key_q) > BaseCaching.MAX_ITEMS:
                dis = self.key_q.pop(0)
                print(f"DISCARD: {dis}")
                del self.cache_data[dis]
        else:
            self.key_q.append(key)
            self.key_q.remove(key)

    def get(self, key):
        """ retrieve a value of a key from self.cache_data """
        if not key:
            return None
        return self.cahce_data.get(key, None)
