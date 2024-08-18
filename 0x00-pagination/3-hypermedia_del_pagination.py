#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """ get page from data_set by index """
        idx_dast = self.__indexed_dataset
        dast = self.__dataset
        if index:
            idx = index
        else:
            idx = 0
        assert idx < len(dast) and idx >= 0
        data = [[None] for _ in range(page_size)]
        j = 0
        count = page_size
        while count:
            item = idx_dast.get(idx)
            if item:
                data[j] = item
                j += 1
                idx += 1
                count -= 1
            else:
                idx += 1
        hypermedia = {"index": index, "next_index": idx,
                      "page_size": page_size, "data": data}
        return hypermedia
