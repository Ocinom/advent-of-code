use crate::day_1::{ex_1, ex_2};

mod day_1;

fn main() {
    let ex1_ans = ex_1::execute("day_1.txt").unwrap();
    let ex2_ans = ex_2::execute("day_1.txt").unwrap();

    println!("Exercise 1 Answer:\n{ex1_ans}");
    println!("Exercise 2 Answer:\n{ex2_ans}");
}
