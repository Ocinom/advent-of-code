pub mod ex_1 {
    use std::fs;
    use std::env;

    pub fn read_file() -> String {
        let ex1_path = "1_1.txt";

        let contents = fs::read_to_string(ex1_path)
            .expect("Should have been able to read the file");

        contents
    }

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
        let contents = fs::read_to_string(&path)
            .expect("File {path} not found.");

        let mut sum: u32 = 0;

        for line in contents.split("\n") {
            sum += get_digits(line);
        }

        Ok(sum)
    }
}
