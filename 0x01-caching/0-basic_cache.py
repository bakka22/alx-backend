#!/usr/bin/env python3
""" Basic Caching """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Caching system """
    def __init__(self):
        """ initiate an instance of the class """
        super().__init__()

    def put(self, key, item):
        """ assign a value for the key in self.cache_data """
        if not key or not item:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ retrieve the value of the key from self.cache_data """
        if not key:
            return None
        return self.cache_data.get(key)
