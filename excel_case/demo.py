def fun(foo):
    def add():
        print('日志打印')
        foo()
        print('日志上传成功')

    return add


@fun
def test01():
    print('这是自动化用例01')


@fun
def test02():
    print('这是自动化用例02')


test01()
test02()
