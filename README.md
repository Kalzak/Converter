# Converter
Sick of having to open up the browser and use the internet to do conversions?
Well I was, so I made this.
It's simple.
It's fast.
What more do you need?
(A lot actually, check my _goals_ section)

## Desc
- Converts values easily and quickly
- Supports:
  - Binary
  - Hex
  - Ascii string
  - Decimal

- To use:
  - I recommend setting the file as executable and placing in /usr/bin for easy access
    - I have as simple bash script to do this for convenience, it does the following
      - Creates a copy of `conv.py` named `conv`
      - Add the executable permission bit to `conv`
      - Moves `conv` to `usr/bin`
    - Run `sudo bash add_to_user_binaries.sh` (sudo needed to add permission bit and place in `/usr/bin`
    - Once this is run you can simple run `conv` at any time in your terminal
  - `conv <inputFormat><outputFormat> <inputData>`
  - `<inputFormat>` and `<outputFormat>` should be one of the following letters
    - __b__ -> Binary
    - __x__ -> Hexadecimal
    - __s__ -> Ascii string
    - __d__ -> Decimal
  - Example commands
    - Convert hexadecimal value `0x1337` to decimal
      - `conv xd 0x1337`
      - `conv xd 1337`
    - Convert ascii string "foo bar" to binary
      - `conv sb "foo bar"`

## Goal
- I want this program to be able to do all computing related conversions in [here](https://www.rapidtables.com/convert/number/index.html)
- Extremely efficient to use with the least number of keystrokes
- We want to save time so convenience features are desired
  - EG: A flag to automatically remove `0x` from the beginning of a hex string to save time manually removing it if not needed
- Support for strings other than ASCII (UTF-8, UTF-16)
- I'd prefer to have this written in C just for the sake of minimalism but Python was used to a working program quickly
