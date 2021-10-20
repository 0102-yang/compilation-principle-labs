def check_valid_identifier(identifier):
    """ 判断一个标识符是否有效。 """
    return (identifier[0].isalpha() or identifier[0] == '_') and identifier[1:].isalnum()


def check_valid_identifier_test():
    string = input('请输入待检查的标识符：')
    print('是标识符' if check_valid_identifier(string) else '不是标识符')


if __name__ == '__main__':
    with open('identifiers.txt', 'r') as file:
        identifiers = file.readline().split()
        for item in identifiers:
            print('字符串\'' + item + '\'是标识符' if check_valid_identifier(item) else '字符串\'' + item + '\'不是标识符')
