from clock import Clock
from lfu import LFU
from lru import LRU
import matplotlib.pyplot as plt
import numpy as np

num_tests = 100
cache_len = 5
seq_len = 1000
# define probabilities of a number distribution
probs = np.array([0.13, 0.02, 0.01, 0.11, 0.34, 0.2, 0.05, 0.07, 0.06, 0.01])
# print(np.sum(probs))
acc_lst = []
for cache_len in range(1,11):
    accuracy = 0
    for _ in range(num_tests):
        # bin_seq = np.random.binomial(n=10, p=0.5, size=seq_len)
        biased_seq = np.random.choice(range(len(probs)), size=seq_len, p=probs)
        # create a cache with <cache_len> pages
        cache = Clock(cache_len)
        cache.load_str_seq(str(biased_seq)[1:-1])
        num_misses = cache.state[1]
        accuracy += (1 - num_misses/seq_len)/num_tests
    acc_lst.append(accuracy)

x_vals = [x for x in range(1,11)]
plt.plot([x for x in range(1,11)], acc_lst)
# Add labels to the axes
plt.xlabel('Size')
plt.ylabel('Efficiency')

print(f"Number of tests: {num_tests}\nAccuracy: {accuracy}")

# Add a title to the plot
plt.title('Cache efficiency vs Cache size')
plt.show()