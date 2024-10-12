from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response200_o_kish import ErrorResponse200OKish
from openapi_server.models.error_response400_bad_admin_or_value import ErrorResponse400BadAdminOrValue
from openapi_server.models.error_response401_bad_key_for_basic_auth import ErrorResponse401BadKeyForBasicAuth
from openapi_server.models.error_response404_not_found import ErrorResponse404NotFound
from openapi_server.models.float_value_object import FloatValueObject
from openapi_server.models.int32_value_object import Int32ValueObject
from openapi_server.models.int64_string_value_object import Int64StringValueObject
from openapi_server.models.int64_value_object import Int64ValueObject
from openapi_server.models.string_value_object import StringValueObject
from openapi_server.models.table_def import TableDef
from openapi_server import util


async def read_float_table_0(request: web.Request, table_name, start_index=None, num_elements=None) -> web.Response:
    """read_float_table_0

    Read table elements #### Examples #### * Read all elements in a table named ftable: https://1.2.3.4/api/v1/device/strategy/tables/floats/ftable * Read elements 5 and up in a table named ftable starting with index 5: https://1.2.3.4/api/v1/device/strategy/tables/floats/ftable?startIndex&#x3D;5 * Read 3 consecutive elements in a table named ftable starting with the element at index 10: https://1.2.3.4/api/v1/device/strategy/tables/floats/ftable?startIndex&#x3D;10&amp;numElements&#x3D;3 

    :param table_name: Name of float table to read; starting index and number of elements may be specified (defaults to all elements)
    :type table_name: str
    :param start_index: Index of first element to read (default is 0)
    :type start_index: int
    :param num_elements: Number of elements to read (default is number of elements in the table minus startIndex)
    :type num_elements: int

    """
    return web.Response(status=200)


async def read_float_table_element_0(request: web.Request, table_name, index) -> web.Response:
    """read_float_table_element_0

    Read specified table element

    :param table_name: Name of float table to read
    :type table_name: str
    :param index: Index of element to read
    :type index: int

    """
    return web.Response(status=200)


async def read_float_tables_0(request: web.Request, ) -> web.Response:
    """read_float_tables_0

    Returns an array of the name and length of all the float tables in the strategy


    """
    return web.Response(status=200)


async def read_int32_table_0(request: web.Request, table_name, start_index=None, num_elements=None) -> web.Response:
    """read_int32_table_0

    \&quot;Read a range of table elements from the specified integer32 table\&quot;  #### Examples ####  * Read all elements in a table named itable: https://1.2.3.4/api/v1/device/strategy/tables/int32s/itable  * Read elements 5 and up in a table named itable starting with index 5: https://1.2.3.4/api/v1/device/strategy/tables/int32s/itable?startIndex&#x3D;5  * Read 3 consecutive elements in a table named itable starting with the element at index 10: https://1.2.3.4/api/v1/device/strategy/tables/int32s/itable?startIndex&#x3D;10&amp;numElements&#x3D;3 

    :param table_name: Name of integer32 table to read; starting index and number of elements may be specified (defaults to all elements)
    :type table_name: str
    :param start_index: Index of first element to read (default is 0)
    :type start_index: int
    :param num_elements: Number of elements to read (default is number of elements in the table minus startIndex)
    :type num_elements: int

    """
    return web.Response(status=200)


async def read_int32_table_element_0(request: web.Request, table_name, index) -> web.Response:
    """read_int32_table_element_0

    Read specified integer32 table element

    :param table_name: Name of the integer32 table to read
    :type table_name: str
    :param index: Index of element to read
    :type index: int

    """
    return web.Response(status=200)


async def read_int32_tables_0(request: web.Request, ) -> web.Response:
    """read_int32_tables_0

    Returns an array of the name and length of all the integer32 tables in the strategy


    """
    return web.Response(status=200)


async def read_int64_table_0(request: web.Request, table_name, start_index=None, num_elements=None) -> web.Response:
    """read_int64_table_0

    \&quot;Read a range of table elements from the specified integer64 table\&quot;  #### Examples ####  * Read all elements in a table named i64table: https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table  * Read elements 5 and up in a table named i64table starting with index 5: https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table?startIndex&#x3D;5  * Read 3 consecutive elements in a table named i64table starting with the element at index 10: https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table?startIndex&#x3D;10&amp;numElements&#x3D;3 

    :param table_name: Name of the integer64 table to read; starting index and number of elements may be specified (defaults to all elements)
    :type table_name: str
    :param start_index: Index of first element to read (default is 0)
    :type start_index: int
    :param num_elements: Number of elements to read (default is number of elements in the table minus startIndex)
    :type num_elements: int

    """
    return web.Response(status=200)


async def read_int64_table_as_string_0(request: web.Request, table_name, start_index=None, num_elements=None) -> web.Response:
    """read_int64_table_as_string_0

    \&quot;Read a range of table elements from the specified integer64 table\&quot;  #### Examples ####  * Read all elements in a table named i64table: https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table/_string  * Read elements 5 and up in a table named i64table starting with index 5: https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table/_string?startIndex&#x3D;5  * Read 3 consecutive elements in a table named i64table starting with the element at index 10: https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table/_string?startIndex&#x3D;10&amp;numElements&#x3D;3 

    :param table_name: Name of the integer64 table to read; starting index and number of elements may be specified (defaults to all elements)
    :type table_name: str
    :param start_index: Index of first element to read (default is 0)
    :type start_index: int
    :param num_elements: Number of elements to read (default is number of elements in the table minus startIndex)
    :type num_elements: int

    """
    return web.Response(status=200)


async def read_int64_table_element_0(request: web.Request, table_name, index) -> web.Response:
    """read_int64_table_element_0

    Read specified integer64 table element

    :param table_name: Name of integer64 table to read
    :type table_name: str
    :param index: Index of element to read
    :type index: int

    """
    return web.Response(status=200)


async def read_int64_table_element_as_string_0(request: web.Request, table_name, index) -> web.Response:
    """read_int64_table_element_as_string_0

    Read specified integer64 table element as string

    :param table_name: Name of integer64 table to read
    :type table_name: str
    :param index: Index of element to read
    :type index: int

    """
    return web.Response(status=200)


async def read_int64_tables_0(request: web.Request, ) -> web.Response:
    """read_int64_tables_0

    Returns an array of the name and length of all the integer64 tables in the strategy


    """
    return web.Response(status=200)


async def read_string_table_0(request: web.Request, table_name, start_index=None, num_elements=None) -> web.Response:
    """read_string_table_0

    \&quot;Read a range of table elements from the specified string table\&quot;  #### Examples ####  * Read all elements in a table named strTable: https://1.2.3.4/api/v1/device/strategy/tables/strings/strTable  * Read elements 5 and up in a table named i64table starting with index 5: https://1.2.3.4/api/v1/device/strategy/tables/strings/strTable?startIndex&#x3D;5  * Read 3 consecutive elements in a table named i64table starting with the element at index 10: https://1.2.3.4/api/v1/device/strategy/tables/strings/strTable?startIndex&#x3D;10&amp;numElements&#x3D;3 

    :param table_name: Name of string table to read; starting index and number of elements may be specified (defaults to all elements)
    :type table_name: str
    :param start_index: Index of first element to read (default is 0)
    :type start_index: int
    :param num_elements: Number of elements to read (default is number of elements in the table minus startIndex)
    :type num_elements: int

    """
    return web.Response(status=200)


async def read_string_table_element_0(request: web.Request, table_name, index) -> web.Response:
    """read_string_table_element_0

    Read specified table element

    :param table_name: Name of string table to read
    :type table_name: str
    :param index: Index of element to read
    :type index: int

    """
    return web.Response(status=200)


async def read_string_tables_0(request: web.Request, ) -> web.Response:
    """read_string_tables_0

    Returns an array of the name and length of all the string tables in the strategy


    """
    return web.Response(status=200)


async def write_float_table_0(request: web.Request, table_name, float_array, start_index=None) -> web.Response:
    """write_float_table_0

    Write table elements #### Examples #### * Write the values (1.5, 2.4, 3.5) to 3 consecutive elements in a table named ftable starting with the element at index 10:POST to https://1.2.3.4/api/v1/device/strategy/tables/floats/ftable?startIndex&#x3D;10  with body of the POST request set to [ 1.5, 2.4, 3.5 ] 

    :param table_name: Name of float table to write; starting index may be specified
    :type table_name: str
    :param float_array: Array of element values to write starting at startIndex
    :type float_array: List[float]
    :param start_index: Index of first element to write (default is 0)
    :type start_index: int

    """
    return web.Response(status=200)


async def write_float_table_element_0(request: web.Request, table_name, index, float_element_object) -> web.Response:
    """write_float_table_element_0

    Write specified table element

    :param table_name: Name of float table to write
    :type table_name: str
    :param index: Index of element to write
    :type index: int
    :param float_element_object: Element to write starting at index
    :type float_element_object: dict | bytes

    """
    float_element_object = FloatValueObject.from_dict(float_element_object)
    return web.Response(status=200)


async def write_int32_table_0(request: web.Request, table_name, int32_array, start_index=None) -> web.Response:
    """write_int32_table_0

    \&quot;Write a range of table elements\&quot; #### Examples #### * Write the values (1, 2, 3) to 3 consecutive elements in a table named itable starting with the element at index 10:POST to https://1.2.3.4/api/v1/device/strategy/tables/int32s/itable?startIndex&#x3D;10  with body of the POST request set to [ 1, 2, 3 ]       

    :param table_name: Name of integer32 table to write; starting index may be specified
    :type table_name: str
    :param int32_array: Array of element values to write starting at startIndex; if the list of elements is too long to fit in the specified table, extra elements will be ignored
    :type int32_array: List[int]
    :param start_index: Index of first element to write (default is 0)
    :type start_index: int

    """
    return web.Response(status=200)


async def write_int32_table_element_0(request: web.Request, table_name, index, int32_element_object) -> web.Response:
    """write_int32_table_element_0

    Write specified integer32 table element

    :param table_name: Name of the integer32 table to write
    :type table_name: str
    :param index: Index of element to write
    :type index: int
    :param int32_element_object: Element to write at index specified
    :type int32_element_object: dict | bytes

    """
    int32_element_object = Int32ValueObject.from_dict(int32_element_object)
    return web.Response(status=200)


async def write_int64_table_0(request: web.Request, table_name, int64_array, start_index=None) -> web.Response:
    """write_int64_table_0

    \&quot;Write a range of table elements\&quot; #### Examples #### * Write the values (1, 2, 3) to 3 consecutive elements in a table named i64table starting with the element at index 10:POST to https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table?startIndex&#x3D;10  with body of the POST request set to [ 1, 2, 3 ] 

    :param table_name: Name of integer64 table to write; starting index may be specified
    :type table_name: str
    :param int64_array: Array of element values to write starting at startIndex; if the array of elements is too long  to fit in the specified table, extra elements will be ignored
    :type int64_array: List[int]
    :param start_index: Index of first element to write; default is 0
    :type start_index: int

    """
    return web.Response(status=200)


async def write_int64_table_as_string_0(request: web.Request, table_name, int64_as_string_array, start_index=None) -> web.Response:
    """write_int64_table_as_string_0

    \&quot;Write a range of table elements\&quot; #### Examples #### * Write the values (1, 2, 3) to 3 consecutive elements in a table named i64table starting with the element at index 10:POST to https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table/_string?startIndex&#x3D;10  with body of the POST request set to [ \&quot;1\&quot;, \&quot;2\&quot;, \&quot;3\&quot; ] 

    :param table_name: Name of integer64 table to write; starting index may be specified
    :type table_name: str
    :param int64_as_string_array: Array of element values to write starting at startIndex; if the array of elements is too long  to fit in the specified table, extra elements will be ignored
    :type int64_as_string_array: List[str]
    :param start_index: Index of first element to write; default is 0.
    :type start_index: int

    """
    return web.Response(status=200)


async def write_int64_table_element_0(request: web.Request, table_name, index, int64_element_object) -> web.Response:
    """write_int64_table_element_0

    Write specified integer64 table element

    :param table_name: Name of the integer64 table to write
    :type table_name: str
    :param index: Index of element to write
    :type index: int
    :param int64_element_object: Element to write starting at index specified
    :type int64_element_object: dict | bytes

    """
    int64_element_object = Int64ValueObject.from_dict(int64_element_object)
    return web.Response(status=200)


async def write_int64_table_element_as_string_0(request: web.Request, table_name, index, int64_element_object) -> web.Response:
    """write_int64_table_element_as_string_0

    Write specified integer64 table element as string

    :param table_name: Name of the integer64 table to write
    :type table_name: str
    :param index: Index of element to write
    :type index: int
    :param int64_element_object: Element to write starting at index specified
    :type int64_element_object: dict | bytes

    """
    int64_element_object = Int64StringValueObject.from_dict(int64_element_object)
    return web.Response(status=200)


async def write_string_table_0(request: web.Request, table_name, string_array, start_index=None) -> web.Response:
    """write_string_table_0

    \&quot;Write a range of table elements\&quot; #### Examples #### * Write the values (\&quot;first\&quot;, \&quot;second\&quot;, \&quot;third\&quot;) to 3 consecutive elements in a table named strTable starting with the element at index 10:POST to https://1.2.3.4/api/v1/device/strategy/tables/strings/strtable?startIndex&#x3D;10  with body of the POST request set to [ \&quot;first\&quot;, \&quot;second\&quot;, \&quot;third\&quot; ] 

    :param table_name: Name of string table to write; starting index may be specified
    :type table_name: str
    :param string_array: Array of element values to write starting at startIndex; if an element value is longer than the string width, the string will be truncated to fit
    :type string_array: List[str]
    :param start_index: Index of first element to write (default is 0)
    :type start_index: int

    """
    return web.Response(status=200)


async def write_string_table_element_0(request: web.Request, table_name, index, string_element_object) -> web.Response:
    """write_string_table_element_0

    Write specified table element

    :param table_name: Name of string table to write
    :type table_name: str
    :param index: Index of element to write
    :type index: int
    :param string_element_object: Element to write starting at index
    :type string_element_object: dict | bytes

    """
    string_element_object = StringValueObject.from_dict(string_element_object)
    return web.Response(status=200)
