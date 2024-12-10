from pathlib import Path
from .metrolojfile import MetrolojFile, Channel
from .getfiles import getfiles
import statistics


def combine_channels(channels: list[Channel]) -> list[list[float]]:
    res = []
    for ich in range(len(channels[0].correlation)):
        c0 = [x.correlation for x in channels if x.index == ich]
        ch_mean = [0.0] * len(c0)
        for i in range(len(c0)):
            ch_mean[i] = statistics.fmean([x[i] for x in c0])
        res.append(ch_mean)
    return res


def combine(root: Path, outfile: Path) -> None:
    files = getfiles(root)
    mjfiles = [MetrolojFile(x) for x in files]
    headers = []
    datas = []
    channels = []
    for mjfile in mjfiles:
        headers.append(mjfile.header)
        datas += mjfile.data
        channels += mjfile.channels
    # check if headers are equal
    for h in headers:
        if not h == headers[0]:
            print("WARNING: Headers not equal")
    writethis = [headers[0]] + datas
    with open(outfile, "wt") as fp:
        fp.write("\n".join(["\t".join(x) for x in writethis]))

    with open(Path(outfile.parent, outfile.stem + ".txt"), "wt") as fp:
        fp.write(
            "\n".join(
                ["\t".join([str(y) for y in x]) for x in combine_channels(channels)]
            )
        )
