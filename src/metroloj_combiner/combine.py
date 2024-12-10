from pathlib import Path
from .metrolojfile import MetrolojFile
from .getfiles import getfiles


def combine(root: Path, outfile: Path) -> None:
    files = getfiles(root)
    headers = []
    datas = []
    for file in files:
        mf = MetrolojFile(file)
        headers.append(mf.header)
        datas += mf.data
    # check if headers are equal
    for h in headers:
        if not h == headers[0]:
            print("WARNING: Headers not equal")
    writethis = [headers[0]] + datas
    with open(outfile, "wt") as fp:
        fp.write("\n".join(["\t".join(x) for x in writethis]))
