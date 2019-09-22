import argparse
from config import config as cfg


def get_args():
    """Преобразование аргументов командной строки в объект"""
    parser = argparse.ArgumentParser(description=cfg.DESCRIPTION)
    parser.add_argument('urls', nargs='+', help='List of extractor url')
    parser.add_argument('--here', action='store_true', help='Show result in console')
    parser.add_argument('-u', '--urlstore', action='store_true', help='Store articles in url name based directories')
    parser.add_argument('-f', '--filename', nargs='?', help='Name of file which will be fill text from url')
    parser.add_argument('-t', '--ticker', action='store_true', help='Display text in console with pause on each row')
    parser.add_argument('-w', '--width', nargs='?', const=cfg.DEFAULT_TEXT_WIDTH, help='Max width of text')
    parser.add_argument('-a', '--adaptive', action='store_true', help='Adapt width of text in console')
    return parser.parse_args()
