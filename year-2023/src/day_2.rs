pub mod ex_1 {
    use regex::Regex;
    use once_cell::sync::Lazy;
    use std::fs::read_to_string;
    
    const MAX_RED: usize = 12;
    const MAX_GREEN: usize  = 13;
    const MAX_BLUE: usize = 14;

    const GAME_NO_RE: &str = r"Game (?<n>\d+):";
    const ITEMS_TALLY_RE: &str = r"(?:(\d+) (red|green|blue))";

    static GAME_NO: Lazy<Regex> = Lazy::new(|| Regex::new(GAME_NO_RE).unwrap());
    static ITEMS_TALLY: Lazy<Regex> = Lazy::new(|| Regex::new(ITEMS_TALLY_RE).unwrap());

    pub fn check_line_possible(input: &str) -> Option<usize> {
        // Game 123: 1 red, 2 blue, 3 green; 4 blue, 5 green; (...)
        let game_caps = GAME_NO.captures(input);
        if game_caps.is_none() { return None };

        let game = game_caps.unwrap().name("n").unwrap().as_str();

        for (_, [number, color]) in ITEMS_TALLY.captures_iter(input).map(|c| c.extract()) {
            let max = match color {
                "red" => MAX_RED,
                "green" => MAX_GREEN,
                "blue" => MAX_BLUE,
                _ => todo!(),
            };

            if number.parse::<usize>().unwrap() > max {
                return None;
            }
        }

        if let Ok(num) = game.parse::<usize>() {
            return Some(num);
        } else {
            println!("{:?}", game);
            return None;
        }
    }

    pub fn execute(file: &str) {
        let mut total: usize = 0;

        for line in read_to_string(file).expect("File not found.").lines() {
            total += match check_line_possible(line) {
                Some(num) => num,
                None => 0,
            };
        }

        println!("{:?}", total);
    }
}
