import argparse
import os


def get_args() -> argparse.Namespace:
    """
    Return arguments
    :return: argparse.Namespace
    """
    parser = argparse.ArgumentParser(
        description="A command line utility that downloads pages from "
                    "the Internet and stores them on your computer"
    )
    parser.add_argument("page_url")
    parser.add_argument(
        "--output",
        help="set output folder",
        default=os.getcwd(),
        type=str
    )
    return parser.parse_args()