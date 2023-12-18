pub mod ex_1 {
    use regex::Regex;
    use std::fs::read_to_string;
    use once_cell::sync::Lazy;
    use std::cmp::{max, min};

    static SYMBOLS: Lazy<Regex> = Lazy::new(|| Regex::new(r#"\d+"#).unwrap());

    pub fn execute(file: &str) {
        let file_data = read_to_string(file).expect("File not found.");
        let input: Vec<Vec<char>> = file_data.lines()
            .map(|l| l.chars().collect::<Vec<char>>())
            .collect();

        let total = 0;

        let width = input[0].len();
        let height = input.len();

        for row in 0..height {
            let mut left = 0;
            let mut right = 0;

            while left < width {
                if input[row][left].is_numeric() {
                    right = left;
                    while right < width && input[row][right].is_numeric() {
                        right += 1;
                    }

                    let num_str: usize = input[row][left..right]
                        .iter()
                        .map(|c| c.to_string())
                        .collect::<Vec<String>>()
                        .join("")
                        .parse()
                        .unwrap();

                    let left_peek = if left > 0 {left - 1} else {left};
                    let right_peek = if right < width {right + 1} else {right};

                    // Peek top if applicable
                    if row > 0 {
                        let mut added = false;
                        for peek in left_peek..right_peek {
                            let ch = input[row - 1][peek];
                            if ch != '.' && !ch.is_numeric() {

                            }
                        }
                    }
                    // Peek bottom
                }
                left += 1;
            }
        }

        println!("{:?}", input);
    }
}
