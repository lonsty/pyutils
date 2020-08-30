def convert_to_safe_filename(filename):
    """去掉文件名中的非法字符。
    :param str filename: 文件名
    :return str: 合法文件名
    """
    return "".join([c for c in filename if c not in r'\/:*?"<>|']).strip()
