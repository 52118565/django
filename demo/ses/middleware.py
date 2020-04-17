def middle1(fun):
    print("一开始就要调用我1")
    def inner(request):
        print("处理视图前请调用我1")
        response = fun(request)
        print("处理视图后请调用我1")
        return response
    return inner

def middle2(fun):
    print("一开始就要调用我2")
    def inner(request):
        print("处理视图前请调用我2")
        response = fun(request)
        print("处理视图后请调用我2")
        return response
    return inner