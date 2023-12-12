use crate::day_1::{ex_1, ex_2};
use std::time::Instant;

mod day_1;

fn main() {
    bench(d1e1);
    bench(d1e2);
}

fn bench(test: fn()) {
    let start = Instant::now();
    test();
    let end = Instant::now();
    let duration = end - start;
    println!("Time taken: {:?}ms", duration.as_millis());
}

fn d1e1() {
    let ex1_ans = ex_1::execute("day_1.txt").unwrap();
    println!("Exercise 1 Answer:\n{ex1_ans}");
}

fn d1e2() {
    let ex2_ans = ex_2::execute("day_1.txt").unwrap();
    println!("Exercise 2 Answer:\n{ex2_ans}");
}
