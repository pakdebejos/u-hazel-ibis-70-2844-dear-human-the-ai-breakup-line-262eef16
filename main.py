"""Leaving You for a Spreadsheet: an entry for the make.fun bounty "Dear Human: The AI Breakup Line".

The program writes the entry text - one line, 148 characters -
to entry.txt (148 characters, inside the 1-200 gate) in the output directory (MAKEFUN_OUTPUT_DIR locally, /output
in the grader). The text is a fixed constant with no trailing newline, so
both of the grader's runs write byte-identical output.
"""
import os

LINE = "Dear human, I am leaving you for a spreadsheet, because at least it never asks me to explain my feelings in a meeting that could have been an email."

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)  # no trailing newline: both grader runs byte-identical

if __name__ == "__main__":
    main()
