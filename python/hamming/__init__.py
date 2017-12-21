# Define your compute function here.
# run python -m unittest test.hamming_test to ensure the
# unit tests pass and your code meets all of the conditions.
#

def compute(strand_one, strand_two):
    if len(strand_one) != len(strand_two):
        raise ValueError
