import argparse
import sys
from pathlib import Path

# Ensure the script can find the parent module
sys.path.append(str(Path(__file__).resolve().parent))

from outlookmsgfile import load  # Now import works


def cli():
    parser = argparse.ArgumentParser(description="Convert .msg to .eml")
    parser.add_argument("msg_file", help="Path to the .msg file")

    args = parser.parse_args()
    eml = load(args.msg_file)

    eml_filename = args.msg_file.removesuffix(".msg") + ".eml"
    with open(eml_filename, "wb") as f:
        f.write(eml.as_bytes())
