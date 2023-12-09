"""
Simplified implementation of the LRU Cache. Can handle only integers.
"""
import numpy as np

class LRU:
    def __init__ (self, size):
        # initialize cache values with 0s
        self._body = np.zeros(size, dtype=int)
        self._misses = 0

    def get_idx(self, elem):
        # search for an idx of the element
        idx = np.where(self._body == elem)[0]
        return idx

    def access(self, elem):
        # search for the element in the cache
        elem_idx = self.get_idx(elem)
        # check for cache miss
        if len(elem_idx) == 0:
            self._misses += 1
            # FIFO removal
            elem_idx = np.array([0])
        # create a mask for removal
        mask = np.ones(len(self._body), dtype=bool)
        mask[elem_idx] = False
        # apply the mask
        self._body = self._body[mask]
        # add the element to the top of the cache
        self._body = np.append(self._body, elem)

    def load_str_seq(self, seq):
        # split the sequence by whitespaces
        for a_str in seq.split():
            # run the cache access procedure
            self.access(int(a_str))

    @property
    def state(self):
        # get a copy of cache values
        return (self._body.copy(), self._misses)