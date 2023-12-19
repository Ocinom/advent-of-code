pub mod ex_1 {
    use regex::Regex;
    use std::fs::read_to_string;
    use once_cell::sync::Lazy;
    use std::cmp::{max, min};

    static SYMBOLS: Lazy<Regex> = Lazy::new(|| Regex::new(r#"\d+"#).unwrap());

    pub fn is_symbol(ch: char) -> bool{
        return ch != '.' && !ch.is_numeric();
    }

    pub fn execute(file: &str) {
        let file_data = read_to_string(file).expect("File not found.");
        let input: Vec<Vec<char>> = file_data.lines()
            .map(|l| l.chars().collect::<Vec<char>>())
            .collect();

        let mut total = 0;

        let width = input[0].len();
        let height = input.len();

        for row in 0..height {
            let mut left = 0;
            let mut right = 0;

            if input[row].len() == 0 {
                continue;
            }

            // Scan the line from left to right
            while left < width {

                // First encountering a number while scanning the line
                if input[row][left].is_numeric() {

                    // Both indices are at the start of the number
                    right = left;

                    // The right index moves until no number is found or it is at the end
                    while right < width - 1 && input[row][right + 1].is_numeric() {
                        right += 1;
                    }

                    // left_peek left  right right_peek
                    //         | |         | |      
                    //         v v         v v
                    //   . . . . . . . . . . . . . . .      
                    //   . . . . 1 2 3 4 5 6 . . . . .
                    //   . . . . . . . . . . . . . . .

                    // Why
                    // Also, collecting contiguous numerical strings to form its
                    // respective number
                    let mut num_parsed: usize;
                    if let Ok(num) = input[row][left..right+1]
                        .iter()
                        .map(|c| c.to_string())
                        .collect::<Vec<String>>()
                        .join("")
                        .parse() {
                            num_parsed = num;
                    } else {
                        left += 1;
                        continue;
                    }

                    println!("{}", num_parsed);

                    // Annoying boundary checks
                    let left_peek = if left > 0 {left - 1} else {left};
                    let right_peek = if right < width - 1 {right + 1} else {right};

                    // Check left and right
                    if is_symbol(input[row][left_peek]) || is_symbol(input[row][right_peek]) {
                        left = right + 1;
                        total += num_parsed;
                        continue;
                    }

                    // Peek top if applicable
                    // TRIGGER WARNING: BOILER PLATE
                    if row > 0 {
                        let mut added = false;
                        for peek in left_peek..(right_peek + 1) {
                            if added {break;}
                            // We got those stupid symbols
                            let ch = input[row - 1][peek];
                            if is_symbol(ch) {
                                // We don't want to add the same number again.
                                left = right + 1;
                                total += num_parsed;
                                added = true;
                                break;
                            }
                        }

                        // Sure I can label the loops later at some point. Whatever
                        if added {continue;}
                    }
                    
                    // Peek bottom
                    // TRIGGER WARNING: BOILER PLATE
                    if row < height - 1 {
                        let mut added = false;
                        for peek in left_peek..(right_peek + 1) {
                            if added {break;}

                            let ch = input[row + 1][peek];
                            if is_symbol(ch) {
                                left = right + 1;
                                total += num_parsed;
                                added = true;
                                break;
                            }
                        }
                        if added {continue;}
                    }
                }

                left += 1;
            }
        }

        println!("{:?}", total);
    }
}
