var Hamming = require('../hamming');
var expect = require('chai').expect;

describe('Hamming', function () {
  var hamming = new Hamming();

  it('no difference between identical strands', function () {
    expect(Hamming.compute('A', 'A')).to.equal(0);
  });

  it('complete hamming distance for single nucleotide strand', function () {
    expect(Hamming.compute('A','G')).to.equal(1);
  });

  it('complete hamming distance for small strand', function () {
    expect(Hamming.compute('AG','CT')).to.equal(2);
  });

  it('small hamming distance', function () {
    expect(Hamming.compute('AT','CT')).to.equal(1);
  });

  it('small hamming distance in longer strand', function () {
    expect(Hamming.compute('GGACG', 'GGTCG')).to.equal(1);
  });

  it('large hamming distance', function () {
    expect(Hamming.compute('GATACA', 'GCATAA')).to.equal(4);
  });

  it('hamming distance in very long strand', function () {
    expect(Hamming.compute('GGACGGATTCTG', 'AGGACGGATTCT')).to.equal(9);
  });

  it('throws error when strands are not equal length', function() {
    expect(function() { Hamming.compute('GGACGGATTCTG', 'AGGAC'); }).to.throw('DNA strands must be of equal length.');
  });
});
