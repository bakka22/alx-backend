#!/usr/bin/env python3
""" LFU Replacment policy """
from collections import deque
BasicCache = __import__('0-basic_cache').BasicCache
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BasicCache):
    """ Caching system that implements LFU Replacment policy """

    def __init__(self):
        """ initialize an instance of the class """
        super().__init__()
        self.key_q = []

    def put(self, key, item):
        """ assign a value to a key in self.cache_data"""
        if not key or not item:
            return
        cand = {}
        if key not in self.cache_data:
            if len(self.cache_data.keys()) == BaseCaching.MAX_ITEMS:
                for k, value in self.cache_data.items():
                    if not cand.get(value["uses"]):
                        cand[value["uses"]] = []
                    cand[value["uses"]].append(k)
                cands = cand[sorted(cand.keys())[0]]
                if len(cands) == 1:
                    print(f"DISCARD: {cands[0]}")
                    del self.cache_data[cands[0]]
                    self.key_q.remove(cands[0])
                else:
                    for k in self.key_q:
                        if k in cands:
                            print(f"DISCARD: {k}")
                            del self.cache_data[k]
                            self.key_q.remove(k)
                            break
            self.cache_data[key] = {"item": item, "uses": 1}
            self.key_q.append(key)
        else:
            self.cache_data[key]["item"] = item
            self.cache_data[key]["uses"] += 1
            self.key_q.append(key)
            self.key_q.remove(key)

    def get(self, key):
        """ retrieve a value of a key from self.cache_data """
        if not key or key not in self.cache_data:
            return None
        self.key_q.append(key)
        self.key_q.remove(key)
        self.cache_data[key]["uses"] += 1
        return self.cache_data.get(key).get("item")

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key).get("item")))
