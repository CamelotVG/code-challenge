class Hamming {

  /**
   * Determines the Hamming distance between two DNA strands.
   *
   * @param {string} dna1 A string representation of a DNA strand
   * @param {string} dna2 A string representation of a DNA strand
   * @return {number} This returns the Hamming distance of two DNA strands
   */

  compute(dna1, dna2) {
    // Added a test to ensure both inputs are provided
    if (!dna1 || !dna2) {
      throw 'Two DNA strands are required.';
    }

    // Used the spread operator (...) to convert string to array
    // Could have also used the standard String.split() function.
    var dna1 = [...dna1];
    var dna2 = [...dna2];

    // Enforces the requirement that DNA must be the same length
    if (dna1.length !== dna2.length) {
      throw 'DNA strands must be of equal length.'
    }

    // Summer initialized outside the scope of the forEach()
    var distance = 0;

    // Uses Array.prototype.forEach() to iterate through strands
    // Could have also used the standard for... loop.
    dna1.forEach(function(atom1, ind) {
      var atom2 = dna2[ind];

      if (atom1 !== atom2) {
        distance += 1;
      }
    });

    return distance;
  }
}

module.exports = Hamming;
