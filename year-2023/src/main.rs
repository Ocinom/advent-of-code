use crate::day_1::{ex_1};

mod day_1;

fn main() {
    let contents = ex_1::execute("1_1.txt").unwrap();

    println!("With text:\n{contents}");
}
