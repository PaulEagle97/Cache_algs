"""
Simplified implementation of the LRU Cache. Can handle only integers.
"""
import numpy as np

class LRU:
    def __init__ (self, size):
        # initialize cache values with 0s
        self._body = np.zeros(size, dtype=int)

    def get_idx(self, elem):
        # search for an idx of the element
        idx = np.where(self._body == elem)[0]
        return idx

    def access(self, elem):
        # search for the element in the cache
        elem_idx = self.get_idx(elem)
        # check for cache miss
        if len(elem_idx) == 0:
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
            # run the LRU cache access procedure
            self.access(int(a_str))

    @property
    def state(self):
        # get a copy of cache values
        return self._body.copy()

def main():
    seq = "1 3 5 4 2 4 3 2 1 0 5 3 5 0 4 3 5 4 3 2 1 3 4 5"
    # create a cache with 4 cells
    cache_1 = LRU(4)
    cache_1.load_str_seq(seq)
    print(cache_1.state)
    
    # create a cache with 5 cells
    cache_2 = LRU(5)
    cache_2.load_str_seq(seq)
    print(cache_2.state)

if __name__ == "__main__":
    main()