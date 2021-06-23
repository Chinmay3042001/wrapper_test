import ctypes

_x = ctypes.CDLL("./underlyingC.so")
def py_wrapper(a,b):
    return (_x.add(ctypes.c_int(a),ctypes.c_int(b)))

py_wrapper(2,3)