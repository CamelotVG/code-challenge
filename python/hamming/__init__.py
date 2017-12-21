# Define your compute function here.
# run python -m unittest test.hamming_test to ensure the
# unit tests pass and your code meets all of the conditions.

# Resources:
# https://stackoverflow.com/questions/35328953/how-to-compare-individual-characters-in-two-strings-in-python-3
# https://docs.python.org/3/library/functions.html#zip
# https://stackoverflow.com/questions/41821112/how-can-i-sum-the-product-of-two-list-items-using-for-loop-in-python




def compute(strand_one, strand_two):
    """
    Returns the hamming distance between two DNA strands.

    Args:
        strand_one (str): The first DNA strand.
        strand_two (str): The second DNA strand.

    Returns:
        int: The hamming distance.

    """
    if len(strand_one) != len(strand_two):
        raise ValueError
    else:
        return sum(nucleotides_one != nucleotides_two for nucleotides_one, nucleotides_two in zip(strand_one, strand_two))
