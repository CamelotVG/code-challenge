import unittest

import hamming


class HammingTest(unittest.TestCase):

    def test_identical_strands(self):
        self.assertEqual(0, hamming.compute('A', 'A'))

    def test_long_identical_strands(self):
        self.assertEqual(0, hamming.compute('GGACTGA', 'GGACTGA'))

    def test_complete_compute_in_single_nucleotide_strands(self):
        self.assertEqual(1, hamming.compute('A', 'G'))

    def test_complete_compute_in_small_strands(self):
        self.assertEqual(2, hamming.compute('AG', 'CT'))

    def test_small_compute_in_small_strands(self):
        self.assertEqual(1, hamming.compute('AT', 'CT'))

    def test_small_compute(self):
        self.assertEqual(1, hamming.compute('GGACG', 'GGTCG'))

    def test_small_compute_in_long_strands(self):
        self.assertEqual(2, hamming.compute('ACCAGGG', 'ACTATGG'))

    def test_non_unique_character_in_first_strand(self):
        self.assertEqual(1, hamming.compute('AGA', 'AGG'))

    def test_non_unique_character_in_second_strand(self):
        self.assertEqual(1, hamming.compute('AGG', 'AGA'))

    def test_same_nucleotides_in_different_positions(self):
        self.assertEqual(2, hamming.compute('TAG', 'GAT'))

    def test_large_compute(self):
        self.assertEqual(4, hamming.compute('GATACA', 'GCATAA'))

    def test_large_compute_in_off_by_one_strand(self):
        self.assertEqual(9, hamming.compute('GGACGGATTCTG', 'AGGACGGATTCT'))

    def test_very_large_compute(self):
        self.assertEqual(0, hamming.compute('CAT' * 5000, 'CAT' * 5000))

    def test_empty_strands(self):
        self.assertEqual(0, hamming.compute('', ''))

    def test_disallow_first_strand_longer(self):
        with self.assertRaises(ValueError):
            hamming.compute('AATG', 'AAA')

    def test_disallow_second_strand_longer(self):
        with self.assertRaises(ValueError):
            hamming.compute('ATA', 'AGTG')


if __name__ == '__main__':
    unittest.main()
