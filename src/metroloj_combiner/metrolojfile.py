from pathlib import Path
from dataclasses import dataclass


def readtxt(txt: str) -> tuple[list[str], list[list[str]]]:
    lines = txt.split("\n")
    header = lines[2].split("\t")
    data = [x.split("\t") for x in lines[3::]]
    return header, data


@dataclass
class Channel:
    index: int
    correlation: list[float]
    resolutions: list[float]
    bead_centers: list[float]
    bead_quality: float
    title: str


def tofloat(x: str) -> float:
    return float(x) if x else float("nan")


class MetrolojFile:
    def __init__(self, file: Path):
        with open(file, "rt") as fp:
            header, data = readtxt(fp.read())
        header[0] = "Name"
        self.header = header
        self.data = data
        channel_idxs = [int(x[8::]) for x in header if x.startswith("Channel ")]
        channels = []
        for d in data:
            if len(d) == 1:
                continue
            channels.append(
                Channel(
                    index=int(d[0][8::]),
                    correlation=[tofloat(x) for x in d[1 : 1 + len(channel_idxs)]],
                    resolutions=[float(x) for x in d[1 + len(channel_idxs)].split(" ")],
                    bead_centers=[
                        float(x) for x in d[2 + len(channel_idxs)].split(" ")
                    ],
                    bead_quality=float(d[3 + len(channel_idxs)]),
                    title=d[4 + len(channel_idxs)],
                )
            )
        self.channels = channels
