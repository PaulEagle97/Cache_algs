"""
Simplified implementation of the LFU Cache. Can handle only integers.
"""
import numpy as np

class LFU:
    def __init__(self, size):
        # initialize cache values with 0s
        self._body = np.zeros((size, 2), dtype=int)
        self._misses = 0

    def get_idx(self, elem):
        # search for an idx of the element
        idx = np.where(self._body[:, 0] == elem)[0]
        return idx

    def access(self, elem):
        # search for the element in the cache
        page_idx = self.get_idx(elem)
        # check for cache miss
        if len(page_idx) == 0:
            self._misses += 1
            # compute the lowest freq among pages
            min_freq = np.min(self._body[:, 1])
            # get all pages with this freq
            least_used_block = self._body[self._body[:, 1] == min_freq]
            # FIFO page removal
            page_to_be_removed = least_used_block[0]
            # get idx of this page in cache
            page_idx = self.get_idx(page_to_be_removed[0])[0]
            elem_freq = 1
        else:
            # get the freq of the elem
            elem_freq = self._body[page_idx[0]][1]
            # incr it by 1
            elem_freq += 1
        # create a mask for removal
        mask = np.ones(len(self._body), dtype=bool)
        mask[page_idx] = False
        # apply the mask
        self._body = self._body[mask]
        # add the element to the top of the cache
        self._body = np.vstack((self._body, np.array([elem, elem_freq])))

    def load_str_seq(self, seq):
        # split the sequence by whitespaces
        for a_str in seq.split():
            # run the cache access procedure
            self.access(int(a_str))

    @property
    def state(self):
        # get a copy of cache values
        return (self._body.copy(), self._misses)