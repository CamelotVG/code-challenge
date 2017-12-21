// Define your Hamming class here.
// `npm test` to ensure the unit tests pass and
// your code meets all of the conditions.
// You may use ES6 or ES5 to solve.



// Class representing the Hamming Distance between two DNA strands.
class Hamming {

    // Computes the Hamming Distance.
    // @param {string, string} strandOne - DNA strand. strandTwo - DNA strand.
    // @returns {number} Number of differences
    compute(strandOne, strandTwo) {
        let hammingDistance = 0;
        if (strandOne.length !== strandTwo.length) {
            throw 'DNA strands must be of equal length.'
        } else {
            for(let i = 0; i < strandOne.length; i++) {
                strandOne[i] !== strandTwo[i] ? hammingDistance++ : null;
            }
                return hammingDistance
        }
    }
}

module.exports = Hamming;
