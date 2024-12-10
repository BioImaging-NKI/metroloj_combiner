from pathlib import Path


def readtxt(txt: str) -> tuple[list[str], list[list[str]]]:
    lines = txt.split("\n")
    header = lines[2].split("\t")
    data = [x.split("\t") for x in lines[3::]]
    return header, data


class MetrolojFile:
    def __init__(self, file: Path):
        self.data = [[""]]
        self.header = [""]
        with open(file, "rt") as fp:
            (self.header, self.data) = readtxt(fp.read())
