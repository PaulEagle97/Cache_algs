"""
Simplified implementation of the LFU Cache. Can handle only integers.
"""
import numpy as np

class LFU:
    def __init__(self, size):
        # initialize cache values with 0s
        self._body = np.zeros((size, 2), dtype=int)

    def get_idx(self, elem):
        # search for an idx of the element
        idx = np.where(self._body[:, 0] == elem)[0]
        return idx

    def access(self, elem):
        # search for the element in the cache
        page_idx = self.get_idx(elem)
        # check for cache miss
        if len(page_idx) == 0:
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
            # run the LRU cache access procedure
            self.access(int(a_str))

    @property
    def state(self):
        # get a copy of cache values
        return self._body.copy()


def main():
    seq = "1 3 5 4 2 4 3 2 1 0 5 3 5"
    # seq += " 0 "
    # seq += "4 3 5 4 3 2 1 3 4 5"
    # create a cache with 4 cells
    cache_1 = LFU(4)
    cache_1.load_str_seq(seq)
    # print(f"Cache 1:\n{cache_1.state}")
    
    # create a cache with 5 cells
    cache_2 = LFU(5)
    cache_2.load_str_seq(seq)
    print(f"Cache 2:\n{cache_2.state}")



if __name__ == "__main__":
    main()