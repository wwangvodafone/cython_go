package main

// #cgo CFLAGS: -I/usr/include/python3.8
// #cgo LDFLAGS: -lpython3.8
// #include <Python.h>
import "C"

import (
    "fmt"
    "unsafe"
)

func main() {
    // Initialize Python interpreter
    C.Py_Initialize()

    // Import the module containing the function
    module := C.PyImport_ImportModule(C.CString("copy_files"))

    // Get the function object
    function := C.PyObject_GetAttrString(module, C.CString("start_process"))

    // Create the arguments tuple
    var args *C.PyObject = C.PyTuple_New(1)
    var str2 string = "/home/wwang/cython/cython/log/"
    var pystr2 *C.PyObject = C.PyUnicode_FromString((*C.char)(unsafe.Pointer(&[]byte(str2)[0])))
    C.PyTuple_SetItem(args, 0, pystr2)

    C.PyObject_CallObject(function, args)
    // Print the result
    fmt.Printf("OK")

    // Clean up
    C.Py_Finalize()
}
