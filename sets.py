# A Venn diagram is an easy way to see the relationship between sets graphically.
# It tells us how many elements are common between the two sets,
# how many elements are only in one set, and how many elements are in neither set.

from matplotlib_venn import venn2
import matplotlib.pyplot as plt
from sympy import FiniteSet
from pylab import savefig


def draw_venn(sets):
    venn2(subsets=sets)
    savefig('venn.png')
    plt.show()


if __name__ == '__main__':
    s1 = FiniteSet(1, 3, 5, 7, 9, 11, 13, 15, 17, 19)
    s2 = FiniteSet(2, 3, 5, 7, 11, 13, 17, 19)
    draw_venn([s1,s2])