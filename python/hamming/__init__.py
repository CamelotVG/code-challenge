# Define your compute function here.
# run python -m unittest test.hamming_test to ensure the
# unit tests pass and your code meets all of the conditions.
#


def compute(strand_x, strand_y):
    x_len = len(strand_x)
    y_len = len(strand_y)
    dist = 0

    if x_len != y_len:
        raise ValueError("DNA strands must be of equal length.")
    elif strand_x != strand_y:
        for i in range(x_len):
            if strand_x[i] != strand_y[i]:
                dist += 1

    return dist
