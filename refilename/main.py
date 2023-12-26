from argparse_setup import parse_arguments
from refilename import RenameFiles

def main():
    args = parse_arguments()

    # 使用提供的路径实例化 RenameFiles 类
    renamer = RenameFiles(args.path)

    # 编译正则表达式模式
    renamer.compile_regex_pattern(args.pattern)

    # 使用更新后的模式调用 replacestring 方法
    renamer.replacestring()

    # 打印更新后的文件名
    for file_name in renamer.finefile:
        print(file_name)


if __name__ == "__main__":
    main()