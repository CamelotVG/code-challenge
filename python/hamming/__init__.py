# Define your compute function here.
# run python -m unittest test.hamming_test to ensure the
# unit tests pass and your code meets all of the conditions.
#

# If the maximum number of base pairs is relatively small, using
# izip instead of zip will not have much effect. However, if the
# number of base pairs is very large, the performance gains could
# be considerable.
#
# In Py 3.X `izip` has replaced `zip` in builtins. Since the target
# python version is unspecified, we account for both
try:
    # As the saying goes, in Python it is better to ask for
    # forgiveness than to ask for permission...
    from itertools import izip as zip
except ImportError as e:
    # Sanity check for 2.X / 3.X compat., 
    import sys
    PY_VERSION = sys.version_info[0]
    assert PY_VERSION >= 3

# Maximum number of allowed base pairs (1 Kbp pair = 1000 bp)
MAX_BP = 1000

def compute(s, t, exceed_max_kbp=False):
    """
    Return the Hamming distance between equal length DNA sequences.

    In addition to checking sequence length, Rosalind problem specification
    states that strings must be shorter than 1 kilobase pair

    NOTE: Additional kwarg `exceed_max_kbp` specified to handle case where
          larger than 1 kilobase pair is desired
    """
    # get the number of base pairs from each sequence of DNA
    bp_s, bp_t = map(len, (s, t))

    # sequences must be of equal length and less than MAX_BP
    if (bp_s != bp_t):
        raise ValueError("Undefined for sequences of unequal length")
    elif (bp_s > MAX_BP or bp_t > MAX_BP) and not exceed_max_kbp:
        raise ValueError("Sequences exceed maxium specified length")

    # return the number of mutations
    return sum(x != y for x, y in zip(s, t))