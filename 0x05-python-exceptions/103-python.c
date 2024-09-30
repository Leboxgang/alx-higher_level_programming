#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints basic information about Python lists.
 * @p: A PyObject representing a list.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	const char *type;
	
	fflush(stdout);
	
	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	
	size = PyList_Size(p);
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);
	
	for (i = 0; i < size; i++)
	{
		type = Py_TYPE(PyList_GetItem(p, i))->tp_name;
		printf("Element %zd: %s\n", i, type);
		
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(PyList_GetItem(p, i));
		else if (strcmp(type, "float") == 0)
			print_python_float(PyList_GetItem(p, i));
	}
}

/**
 * print_python_bytes - Prints basic information about Python bytes objects.
 * @p: A PyObject representing a bytes object.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *string;
	
	fflush(stdout);
	
	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	
	size = PyBytes_Size(p);
	string = PyBytes_AsString(p);
	
	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", string);
	
	printf("  first %zd bytes:", size < 10 ? size + 1 : 10);
	for (i = 0; i < size && i < 10; i++)
		printf(" %02x", (unsigned char)string[i]);
	printf("\n");
}

/**
 * print_python_float - Prints basic information about Python float objects.
 * @p: A PyObject representing a float object.
 */
void print_python_float(PyObject *p)
{
	double value;

	fflush(stdout);
	
	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	value = PyFloat_AsDouble(p);
	printf("  value: %g\n", value);
}
