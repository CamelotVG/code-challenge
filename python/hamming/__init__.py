# Define your compute function here.
# run python -m unittest test.hamming_test to ensure the
# unit tests pass and your code meets all of the conditions.

# Resources:
# https://stackoverflow.com/questions/35328953/how-to-compare-individual-characters-in-two-strings-in-python-3
# https://docs.python.org/3/library/functions.html#zip




def compute(strand_one, strand_two):
    if len(strand_one) != len(strand_two):
        raise ValueError
    else:
        for nucleotides_one, nucleotides_two in zip(strand_one, strand_two):
            return sum(nucleotides_one != nucleotides_two)