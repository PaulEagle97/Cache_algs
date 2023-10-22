"""
Simplified implementation of the Clock(Second Chance) Cache. Can handle only integers.
"""
import numpy as np

class Clock:
    def __init__(self, size):
        # initialize cache values with 0s
        self._body = np.zeros((size, 2), dtype=int)
        self._pg_ptr = 0

    def get_idx(self, elem):
        # search for an idx of the element
        idx = np.where(self._body[:, 0] == elem)[0]
        return idx
    def _move_ptr(self):
        self._pg_ptr = (self._pg_ptr + 1) % len(self._body)

    def access(self, elem):
        # search for the element in the cache
        page_idx = self.get_idx(elem)
        # check for cache miss
        if len(page_idx) == 0:
            # move the pointer to next page with 0 chance
            while self._body[self._pg_ptr][1] != 0:
                # nullify chance of page with 1 chance
                self._body[self._pg_ptr][1] = 0
                # move the pointer to next page
                self._move_ptr()
            # get idx of the page with 0 chance
            page_idx = np.array([self._pg_ptr])
            # move the pointer to next page
            self._move_ptr()
            # create a mask for removal
            mask = np.ones(len(self._body), dtype=bool)
            mask[page_idx] = False
            # apply the mask
            self._body = self._body[mask]
            # substitute the removed page with the new element
            self._body = np.insert(self._body, page_idx, np.array([elem, 0]), axis=0)
        else:
            # give the page a 2nd chance
            self._body[page_idx[0]][1] = 1

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
    seq = "1 2 3 1 3 4 2 4 1 5 6"
    # create a cache with 4 pages
    cache_1 = Clock(4)
    cache_1.load_str_seq(seq)
    print(f"Cache 1:\n{cache_1.state}")


if __name__ == "__main__":
    main()