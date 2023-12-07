pub mod ex_1 {
    use std::fs;

    pub fn get_digits(input: &str) -> u32 {
        let chars: Vec<char> = input.chars().collect();
        let len = chars.len();

        if len == 0 {
            return 0;
        }

        let mut left: usize = 0;
        let mut right: usize = chars.len() - 1;

        while left < right {
            if chars[left].is_digit(10) {
                break;
            }
            left += 1;
        }
        while right > left {
            if chars[right].is_digit(10) {
                break;
            }
            right -= 1;
        }

        if left == right {
            chars[left].to_digit(10).unwrap() * 11
        } else {
            chars[left].to_digit(10).unwrap() * 10
            + chars[right].to_digit(10).unwrap()
        }
    }

    pub fn execute(path: &str) -> Result<u32, ()> {
        let contents = fs::read_to_string(path)
            .expect("File {path} not found.");

        let mut sum: u32 = 0;

        for line in contents.split("\n") {
            sum += get_digits(line);
        }

        Ok(sum)
    }
}

pub mod ex_2 {
    use std::{fs, fmt::Display};
    use aho_corasick::AhoCorasick;

    const nums: &[&str; 18] = &["1", "2", "3", "4", "5", "6", "7", "8", "9",
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];

    pub fn text_to_digit(input: &str) -> u32 {
        match input {
            "1" | "one" => 1,
            "2" | "two" => 2,
            "3" | "three" => 3,
            "4" | "four" => 4,
            "5" | "five" => 5,
            "6" | "six" => 6,
            "7" | "seven" => 7,
            "8" | "eight" => 8,
            "9" | "nine" => 9,
            _ => 0
        }
    }

    pub fn get_digits(input: &str) -> u32 {
        let matches = find_overlapping_matches(input);
        if matches.len() == 1 {
            let first_slice = matches[0];
            let digit = text_to_digit(&input[first_slice.0..first_slice.1]);
            return 11 * digit;
        } else if matches.len() > 1 {
            let first_slice = matches[0];
            let last_slice = matches.last().unwrap();

            let first_digit = text_to_digit(&input[first_slice.0 .. first_slice.1]);
            let last_digit = text_to_digit(&input[last_slice.0 .. last_slice.1]);

            return first_digit * 10 + last_digit;
        }
        0
    }


    pub fn find_overlapping_matches(input: &str) -> Vec<(usize, usize)> {
        let ac = AhoCorasick::builder()
            .ascii_case_insensitive(true)
            .build(nums)
            .unwrap();

        let mut matches = vec![];

        for mat in ac.find_overlapping_iter(input) {
            matches.push((mat.start(), mat.end()));
        }
        matches
    }


    pub fn execute(path: &str) -> Result<u32, ()> {
        let contents = fs::read_to_string(path)
            .expect("File {path} not found.");

        let mut sum: u32 = 0;
        for line in contents.split("\n") {
            sum += get_digits(line);
        }
        Ok(sum)
    }
}
