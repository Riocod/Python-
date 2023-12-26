import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description='根据正则表达式模式重命名文件。')
    parser.add_argument("-p", dest="path", help="包含文件的目录路径。")
    parser.add_argument("-r", dest="pattern", help="用于重命名的正则表达式模式。")
    return parser.parse_args()