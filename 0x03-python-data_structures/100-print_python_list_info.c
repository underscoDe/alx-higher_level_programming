#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - Prints basic info about Python lists
 * @p: A PyObject list.
 *
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
    int list_size, allocated, i;
    PyObject *list_object;

    list_size = Py_SIZE(p);
    allocated = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python List = %d\n", list_size);
    printf("[*] Allocated = %d\n", allocated);

    for (i = 0; i < list_size; i++)
    {
        printf("Element %d: ", i);

        list_object = PyList_GetItem(p, i);
        printf("%s\n", Py_TYPE(list_object)->tp_name);
    }
}
