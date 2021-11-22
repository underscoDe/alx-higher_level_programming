#include "Python.h"

/**
 * print_python_list_info - Prints some basic info about Python lists
 *
 * @p: A PyObject list
 *
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
    int list_size, allocated, i = 0;
    PyObject *list_object;

    /* get the list object size */
    list_size = Py_SIZE(p);
    /* cast the PyObject into PyListObject */
    allocated = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python List = %d\n", size);
    printf("[*] Allocated = %d\n", alloc);

    /* loop over the list */
    for (; i < list_size; i++)
    {
        printf("Element %d: ", i);
        list_object = PyList_GetItem(p, i);
        printf("%s\n", Py_TYPE(obj)->tp_name);
    }
}
