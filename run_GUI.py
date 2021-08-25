from dai_post_processor import post_processor as pp
import argparse


def main():
    args = _parse_args()
    doc_ai2 = pp.open_doc_ai(args.path)

    # Start configuration GUI
    mywin = pp.configGUI(doc_ai2)
    mywin.start()


def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", required=True)

    return parser.parse_args()


if __name__ == '__main__':
    main()