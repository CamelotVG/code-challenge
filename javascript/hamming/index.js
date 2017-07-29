// Define your Hamming class here.
// `npm test` to ensure the unit tests pass and
// your code meets all of the conditions.
// You may use ES6 or ES5 to solve.


class Hamming {

    static compute(strand_x, strand_y){
       const x_len = strand_x.length;
       const y_len = strand_y.length;
       let dist = 0;

        if (x_len !== y_len){
            throw new Error('DNA strands must be of equal length.');
        } else if (strand_x !== strand_y){

                for (let i = 0; i < x_len; i++) {
                    let x_char  =  strand_x.charAt(i);
                    let y_char  =  strand_y.charAt(i);
                    if (x_char !== y_char) {
                        dist++;
                    }
                }

        }

        return dist;
    }
}


module.exports = Hamming;
