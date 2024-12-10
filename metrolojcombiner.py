from metroloj_combiner import combine
from pathlib import Path

if __name__ == "__main__":
    root = Path.cwd()
    outfile = Path(root, "combined.tsv")
    combine(root, outfile)
