#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - Prints basic information about a Python list
 * @p: PyObject pointer to the list
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, allocated, i;
	PyObject *item;

	if (!PyList_Check(p))
	{
		printf("Invalid List Object\n");
		return;
	}
	
	size = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;
	
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
