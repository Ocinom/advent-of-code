use std::time::Instant;

mod day_1;
mod day_2;
mod day_3;

fn main() {
    // bench(d1e1);
    // bench(d1e2);

    // println!("Day 2 benches: ");
    // bench(d2e1);
    // bench(d2e2);
    day_3::ex_1::execute("inputs/day_3.txt");
    // day_3::ex_1::execute("inputs/test.txt");
}

fn bench(test: fn()) {
    let start = Instant::now();
    test();
    let end = Instant::now();
    let duration = end - start;
    println!("Time taken: {:?}ms", duration.as_millis());
}

fn d1e1() {
    let ex1_ans = day_1::ex_1::execute("inputs/day_1.txt").unwrap();
    println!("Exercise 1 Answer:\n{ex1_ans}");
}

fn d1e2() {
    let ex2_ans = day_1::ex_2::execute("inputs/day_1.txt").unwrap();
    println!("Exercise 2 Answer:\n{ex2_ans}");
}

fn d2e1() {
    let ex1_ans = day_2::ex_1::execute("inputs/day_2.txt");
    println!("Exercise 1 Answer:\n{ex1_ans}");
}

fn d2e2() {
    let ex2_ans = day_2::ex_2::execute("inputs/day_2.txt");
    println!("Exercise 2 Answer:\n{ex2_ans}");
}
