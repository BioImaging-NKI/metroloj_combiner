from pathlib import Path


def getfiles(root: Path) -> list[Path]:
    beads = [x for x in root.glob("*") if x.is_dir() and x.name.startswith("bead")]
    result = []
    for bead in beads:
        files = [x for x in bead.glob("**/*.xls")]
        if len(files) > 1:
            print(f"WARNING: Found more than one .xls file for this bead. {bead}")
        result.append(files[0])
    return result
