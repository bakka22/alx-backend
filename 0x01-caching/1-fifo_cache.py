#!/usr/bin/env python3
""" FIFO Replacment policy """
from collections import OrderedDict
BasicCache = __import__('0-basic_cache').BasicCache
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BasicCache):
    """ Caching system that implements FIFO Replacment policy """

    def __init__(self):
        """ initialize an instance of the class """
        super().__init__()
        # self.key_q = []
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ assign a value to a key in self.cache_data
        if not key or not item:
            return
        if key not in self.key_q:
            self.key_q.append(key)
        self.cache_data[key] = item
        if len(self.key_q) > BaseCaching.MAX_ITEMS:
            dis = self.key_q.pop(0)
            print(f"DISCARD: {dis}")
            del self.cache_data[dis]"""
        if key is None or item is None:
            return

        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {first_key}")


    def get(self, key):
        """ retrieve a value of a key from self.cache_data """
        if not key:
            return None
        return self.cahce_data.get(key)
