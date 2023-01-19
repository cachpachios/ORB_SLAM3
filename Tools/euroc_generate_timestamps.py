import os
from pathlib import Path


def generate_timestamps():
    for folder in os.listdir("."):
        if not os.path.isdir(folder):
            continue

        cam0_timestamps = [x.name.split(".")[0] for x in (Path(folder) / "mav0" / "cam0" / "data").glob("*.png")]
        cam1_timestamps = [x.name.split(".")[0] for x in (Path(folder) / "mav0" / "cam1" / "data").glob("*.png")]

        common = set(cam0_timestamps).intersection(set(cam1_timestamps))
        
        d = Path("timestamps") / (folder+".txt")
        d.parent.mkdir(parents=True, exist_ok=True)
        with open(d, "w") as f:
            for timestamp in sorted(common):
                f.write(timestamp+"\n")

if __name__ == "__main__":
    generate_timestamps()