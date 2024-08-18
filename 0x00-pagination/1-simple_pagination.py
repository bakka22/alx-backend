#!/usr/bin/env python3
""" simple pagination """
from typing import Tuple, List
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ eturn a tuple of size two containing a start index and an end index"""
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ return a page from the data_set """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        ds = self.dataset()
        ln = len(ds)
        start, end = index_range(page, page_size)
        if start >= ln or end >= ln:
            return []
        r_l = [[None] for _ in range(page_size)]
        j = 0
        for i in range(start, end):
            r_l[j] = ds[i]
            j += 1
        return r_l
