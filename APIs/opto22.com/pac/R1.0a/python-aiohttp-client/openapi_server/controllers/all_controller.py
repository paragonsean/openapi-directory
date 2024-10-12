from typing import List, Dict
from aiohttp import web

from openapi_server.models.controller_response import ControllerResponse
from openapi_server.models.digital_point_state_object import DigitalPointStateObject
from openapi_server.models.digital_point_state_var import DigitalPointStateVar
from openapi_server.models.error_response200_o_kish import ErrorResponse200OKish
from openapi_server.models.error_response400_bad_admin_or_value import ErrorResponse400BadAdminOrValue
from openapi_server.models.error_response401_bad_key_for_basic_auth import ErrorResponse401BadKeyForBasicAuth
from openapi_server.models.error_response404_not_found import ErrorResponse404NotFound
from openapi_server.models.float_value_object import FloatValueObject
from openapi_server.models.float_var import FloatVar
from openapi_server.models.int32_value_object import Int32ValueObject
from openapi_server.models.int32_var import Int32Var
from openapi_server.models.int64_string_value_object import Int64StringValueObject
from openapi_server.models.int64_value_object import Int64ValueObject
from openapi_server.models.int64_var import Int64Var
from openapi_server.models.int64_var_as_string import Int64VarAsString
from openapi_server.models.strategy_response import StrategyResponse
from openapi_server.models.string_value_object import StringValueObject
from openapi_server.models.string_var import StringVar
from openapi_server.models.table_def import TableDef
from openapi_server import util


async def read_analog_input_eu(request: web.Request, io_name) -> web.Response:
    """read_analog_input_eu

    Reads the value in engineering units (EU) of the specified analog input

    :param io_name: Name of the analog input point to read
    :type io_name: str

    """
    return web.Response(status=200)


async def read_analog_inputs(request: web.Request, ) -> web.Response:
    """read_analog_inputs

    Returns the name and engineering units (EU) for all analog input points in the strategy


    """
    return web.Response(status=200)


async def read_analog_output_eu(request: web.Request, io_name) -> web.Response:
    """read_analog_output_eu

    Reads the value in engineering units (EU) of the specified analog output

    :param io_name: Name of analog output point to read
    :type io_name: str

    """
    return web.Response(status=200)


async def read_analog_outputs(request: web.Request, ) -> web.Response:
    """read_analog_outputs

    Returns the name and engineering units (EU) for all analog output points in the strategy


    """
    return web.Response(status=200)


async def read_device_details(request: web.Request, ) -> web.Response:
    """read_device_details

    Returns controller&#39;s type; firmware version; both mac addresses; and uptime in seconds


    """
    return web.Response(status=200)


async def read_digital_input_state(request: web.Request, io_name) -> web.Response:
    """read_digital_input_state

    Returns the specified digital input point&#39;s state (true &#x3D; on, false &#x3D; off)

    :param io_name: Name of the digital input point to read
    :type io_name: str

    """
    return web.Response(status=200)


async def read_digital_inputs(request: web.Request, ) -> web.Response:
    """read_digital_inputs

    Returns the name and state (true &#x3D; on, false &#x3D; off) of all digital input points in the strategy. If there is no strategy in the controller, or the strategy includes no digital inputs, the returned array will be empty.


    """
    return web.Response(status=200)


async def read_digital_output_state(request: web.Request, io_name) -> web.Response:
    """read_digital_output_state

    Returns the specified digital output point&#39;s state (true &#x3D; on, false &#x3D; off)

    :param io_name: Name of the digit output point to read
    :type io_name: str

    """
    return web.Response(status=200)


async def read_digital_outputs(request: web.Request, ) -> web.Response:
    """read_digital_outputs

    Returns the name and state (true &#x3D; on, false &#x3D; off) of all digital output points in the strategy


    """
    return web.Response(status=200)


async def read_down_timer_value(request: web.Request, down_timer_name) -> web.Response:
    """read_down_timer_value

    Returns current value of the specified down timer

    :param down_timer_name: Name of the down timer variable to read
    :type down_timer_name: str

    """
    return web.Response(status=200)


async def read_down_timer_vars(request: web.Request, ) -> web.Response:
    """read_down_timer_vars

    Returns the name and current value of all down timers in the strategy


    """
    return web.Response(status=200)


async def read_float_table(request: web.Request, table_name, start_index=None, num_elements=None) -> web.Response:
    """read_float_table

    Read table elements #### Examples #### * Read all elements in a table named ftable: https://1.2.3.4/api/v1/device/strategy/tables/floats/ftable * Read elements 5 and up in a table named ftable starting with index 5: https://1.2.3.4/api/v1/device/strategy/tables/floats/ftable?startIndex&#x3D;5 * Read 3 consecutive elements in a table named ftable starting with the element at index 10: https://1.2.3.4/api/v1/device/strategy/tables/floats/ftable?startIndex&#x3D;10&amp;numElements&#x3D;3 

    :param table_name: Name of float table to read; starting index and number of elements may be specified (defaults to all elements)
    :type table_name: str
    :param start_index: Index of first element to read (default is 0)
    :type start_index: int
    :param num_elements: Number of elements to read (default is number of elements in the table minus startIndex)
    :type num_elements: int

    """
    return web.Response(status=200)


async def read_float_table_element(request: web.Request, table_name, index) -> web.Response:
    """read_float_table_element

    Read specified table element

    :param table_name: Name of float table to read
    :type table_name: str
    :param index: Index of element to read
    :type index: int

    """
    return web.Response(status=200)


async def read_float_tables(request: web.Request, ) -> web.Response:
    """read_float_tables

    Returns an array of the name and length of all the float tables in the strategy


    """
    return web.Response(status=200)


async def read_float_var(request: web.Request, float_name) -> web.Response:
    """read_float_var

    Returns value of the specified float variable

    :param float_name: Name of float variable to read
    :type float_name: str

    """
    return web.Response(status=200)


async def read_float_vars(request: web.Request, ) -> web.Response:
    """read_float_vars

    Returns the name and value of all (single-precision) float variables in the strategy


    """
    return web.Response(status=200)


async def read_int32_table(request: web.Request, table_name, start_index=None, num_elements=None) -> web.Response:
    """read_int32_table

    \&quot;Read a range of table elements from the specified integer32 table\&quot;  #### Examples ####  * Read all elements in a table named itable: https://1.2.3.4/api/v1/device/strategy/tables/int32s/itable  * Read elements 5 and up in a table named itable starting with index 5: https://1.2.3.4/api/v1/device/strategy/tables/int32s/itable?startIndex&#x3D;5  * Read 3 consecutive elements in a table named itable starting with the element at index 10: https://1.2.3.4/api/v1/device/strategy/tables/int32s/itable?startIndex&#x3D;10&amp;numElements&#x3D;3 

    :param table_name: Name of integer32 table to read; starting index and number of elements may be specified (defaults to all elements)
    :type table_name: str
    :param start_index: Index of first element to read (default is 0)
    :type start_index: int
    :param num_elements: Number of elements to read (default is number of elements in the table minus startIndex)
    :type num_elements: int

    """
    return web.Response(status=200)


async def read_int32_table_element(request: web.Request, table_name, index) -> web.Response:
    """read_int32_table_element

    Read specified integer32 table element

    :param table_name: Name of the integer32 table to read
    :type table_name: str
    :param index: Index of element to read
    :type index: int

    """
    return web.Response(status=200)


async def read_int32_tables(request: web.Request, ) -> web.Response:
    """read_int32_tables

    Returns an array of the name and length of all the integer32 tables in the strategy


    """
    return web.Response(status=200)


async def read_int32_var(request: web.Request, int32_name) -> web.Response:
    """read_int32_var

    Returns value of the specified integer32 variable

    :param int32_name: Name of integer32 variable to read
    :type int32_name: str

    """
    return web.Response(status=200)


async def read_int32_vars(request: web.Request, ) -> web.Response:
    """read_int32_vars

    Returns the name and value of all integer32 variables in the strategy


    """
    return web.Response(status=200)


async def read_int64_table(request: web.Request, table_name, start_index=None, num_elements=None) -> web.Response:
    """read_int64_table

    \&quot;Read a range of table elements from the specified integer64 table\&quot;  #### Examples ####  * Read all elements in a table named i64table: https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table  * Read elements 5 and up in a table named i64table starting with index 5: https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table?startIndex&#x3D;5  * Read 3 consecutive elements in a table named i64table starting with the element at index 10: https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table?startIndex&#x3D;10&amp;numElements&#x3D;3 

    :param table_name: Name of the integer64 table to read; starting index and number of elements may be specified (defaults to all elements)
    :type table_name: str
    :param start_index: Index of first element to read (default is 0)
    :type start_index: int
    :param num_elements: Number of elements to read (default is number of elements in the table minus startIndex)
    :type num_elements: int

    """
    return web.Response(status=200)


async def read_int64_table_as_string(request: web.Request, table_name, start_index=None, num_elements=None) -> web.Response:
    """read_int64_table_as_string

    \&quot;Read a range of table elements from the specified integer64 table\&quot;  #### Examples ####  * Read all elements in a table named i64table: https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table/_string  * Read elements 5 and up in a table named i64table starting with index 5: https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table/_string?startIndex&#x3D;5  * Read 3 consecutive elements in a table named i64table starting with the element at index 10: https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table/_string?startIndex&#x3D;10&amp;numElements&#x3D;3 

    :param table_name: Name of the integer64 table to read; starting index and number of elements may be specified (defaults to all elements)
    :type table_name: str
    :param start_index: Index of first element to read (default is 0)
    :type start_index: int
    :param num_elements: Number of elements to read (default is number of elements in the table minus startIndex)
    :type num_elements: int

    """
    return web.Response(status=200)


async def read_int64_table_element(request: web.Request, table_name, index) -> web.Response:
    """read_int64_table_element

    Read specified integer64 table element

    :param table_name: Name of integer64 table to read
    :type table_name: str
    :param index: Index of element to read
    :type index: int

    """
    return web.Response(status=200)


async def read_int64_table_element_as_string(request: web.Request, table_name, index) -> web.Response:
    """read_int64_table_element_as_string

    Read specified integer64 table element as string

    :param table_name: Name of integer64 table to read
    :type table_name: str
    :param index: Index of element to read
    :type index: int

    """
    return web.Response(status=200)


async def read_int64_tables(request: web.Request, ) -> web.Response:
    """read_int64_tables

    Returns an array of the name and length of all the integer64 tables in the strategy


    """
    return web.Response(status=200)


async def read_int64_var(request: web.Request, int64_name) -> web.Response:
    """read_int64_var

    Returns value of the specified integer64 variable

    :param int64_name: Name of integer64 variable to read
    :type int64_name: str

    """
    return web.Response(status=200)


async def read_int64_var_as_string(request: web.Request, int64_name) -> web.Response:
    """read_int64_var_as_string

    Returns value of the specified integer64 variable as a string

    :param int64_name: Name of integer64 variable to read
    :type int64_name: str

    """
    return web.Response(status=200)


async def read_int64_vars(request: web.Request, ) -> web.Response:
    """read_int64_vars

    Returns the name and value of all integer64 variables in the strategy


    """
    return web.Response(status=200)


async def read_int64_vars_as_strings(request: web.Request, ) -> web.Response:
    """read_int64_vars_as_strings

    Returns the name and value as a string of all integer64 variables in the strategy


    """
    return web.Response(status=200)


async def read_strategy_details(request: web.Request, ) -> web.Response:
    """read_strategy_details

    Returns the name, date, time, and CRC of the strategy currently in the controller, and the number of charts currently running. Empty strings and a 0 will be returned when there is no strategy.


    """
    return web.Response(status=200)


async def read_string_table(request: web.Request, table_name, start_index=None, num_elements=None) -> web.Response:
    """read_string_table

    \&quot;Read a range of table elements from the specified string table\&quot;  #### Examples ####  * Read all elements in a table named strTable: https://1.2.3.4/api/v1/device/strategy/tables/strings/strTable  * Read elements 5 and up in a table named i64table starting with index 5: https://1.2.3.4/api/v1/device/strategy/tables/strings/strTable?startIndex&#x3D;5  * Read 3 consecutive elements in a table named i64table starting with the element at index 10: https://1.2.3.4/api/v1/device/strategy/tables/strings/strTable?startIndex&#x3D;10&amp;numElements&#x3D;3 

    :param table_name: Name of string table to read; starting index and number of elements may be specified (defaults to all elements)
    :type table_name: str
    :param start_index: Index of first element to read (default is 0)
    :type start_index: int
    :param num_elements: Number of elements to read (default is number of elements in the table minus startIndex)
    :type num_elements: int

    """
    return web.Response(status=200)


async def read_string_table_element(request: web.Request, table_name, index) -> web.Response:
    """read_string_table_element

    Read specified table element

    :param table_name: Name of string table to read
    :type table_name: str
    :param index: Index of element to read
    :type index: int

    """
    return web.Response(status=200)


async def read_string_tables(request: web.Request, ) -> web.Response:
    """read_string_tables

    Returns an array of the name and length of all the string tables in the strategy


    """
    return web.Response(status=200)


async def read_string_var(request: web.Request, string_name) -> web.Response:
    """read_string_var

    Returns value of the specified string

    :param string_name: Name of string variable to read
    :type string_name: str

    """
    return web.Response(status=200)


async def read_string_vars(request: web.Request, ) -> web.Response:
    """read_string_vars

    Returns the name and value of all string variables in the strategy


    """
    return web.Response(status=200)


async def read_up_timer_value(request: web.Request, up_timer_name) -> web.Response:
    """read_up_timer_value

    Returns current value of the specified up timer

    :param up_timer_name: Name of the up timer variable to read
    :type up_timer_name: str

    """
    return web.Response(status=200)


async def read_up_timer_vars(request: web.Request, ) -> web.Response:
    """read_up_timer_vars

    Returns the name and current value of all up timers in the strategy


    """
    return web.Response(status=200)


async def write_analog_output_eu(request: web.Request, io_name, body) -> web.Response:
    """write_analog_output_eu

    Sets the value of the specified analog output point

    :param io_name: Name of the analog output point to write
    :type io_name: str
    :param body: Value to write
    :type body: dict | bytes

    """
    body = FloatValueObject.from_dict(body)
    return web.Response(status=200)


async def write_digital_output_state(request: web.Request, io_name, body) -> web.Response:
    """write_digital_output_state

    Sets the value of the specified digital output point

    :param io_name: Name of the digital output point to write
    :type io_name: str
    :param body: Value to write
    :type body: dict | bytes

    """
    body = DigitalPointStateObject.from_dict(body)
    return web.Response(status=200)


async def write_float_table(request: web.Request, table_name, float_array, start_index=None) -> web.Response:
    """write_float_table

    Write table elements #### Examples #### * Write the values (1.5, 2.4, 3.5) to 3 consecutive elements in a table named ftable starting with the element at index 10:POST to https://1.2.3.4/api/v1/device/strategy/tables/floats/ftable?startIndex&#x3D;10  with body of the POST request set to [ 1.5, 2.4, 3.5 ] 

    :param table_name: Name of float table to write; starting index may be specified
    :type table_name: str
    :param float_array: Array of element values to write starting at startIndex
    :type float_array: List[float]
    :param start_index: Index of first element to write (default is 0)
    :type start_index: int

    """
    return web.Response(status=200)


async def write_float_table_element(request: web.Request, table_name, index, float_element_object) -> web.Response:
    """write_float_table_element

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


async def write_float_var(request: web.Request, float_name, body) -> web.Response:
    """write_float_var

    Sets the value of a float variable

    :param float_name: Name of the float variable to write
    :type float_name: str
    :param body: Value to write to the float variable
    :type body: dict | bytes

    """
    body = FloatValueObject.from_dict(body)
    return web.Response(status=200)


async def write_int32_table(request: web.Request, table_name, int32_array, start_index=None) -> web.Response:
    """write_int32_table

    \&quot;Write a range of table elements\&quot; #### Examples #### * Write the values (1, 2, 3) to 3 consecutive elements in a table named itable starting with the element at index 10:POST to https://1.2.3.4/api/v1/device/strategy/tables/int32s/itable?startIndex&#x3D;10  with body of the POST request set to [ 1, 2, 3 ]       

    :param table_name: Name of integer32 table to write; starting index may be specified
    :type table_name: str
    :param int32_array: Array of element values to write starting at startIndex; if the list of elements is too long to fit in the specified table, extra elements will be ignored
    :type int32_array: List[int]
    :param start_index: Index of first element to write (default is 0)
    :type start_index: int

    """
    return web.Response(status=200)


async def write_int32_table_element(request: web.Request, table_name, index, int32_element_object) -> web.Response:
    """write_int32_table_element

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


async def write_int32_var(request: web.Request, int32_name, body) -> web.Response:
    """write_int32_var

    Sets the value of an integer32 variable

    :param int32_name: Name of integer32 variable to write
    :type int32_name: str
    :param body: Value to write to the integer32 variable
    :type body: dict | bytes

    """
    body = Int32ValueObject.from_dict(body)
    return web.Response(status=200)


async def write_int64_table(request: web.Request, table_name, int64_array, start_index=None) -> web.Response:
    """write_int64_table

    \&quot;Write a range of table elements\&quot; #### Examples #### * Write the values (1, 2, 3) to 3 consecutive elements in a table named i64table starting with the element at index 10:POST to https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table?startIndex&#x3D;10  with body of the POST request set to [ 1, 2, 3 ] 

    :param table_name: Name of integer64 table to write; starting index may be specified
    :type table_name: str
    :param int64_array: Array of element values to write starting at startIndex; if the array of elements is too long  to fit in the specified table, extra elements will be ignored
    :type int64_array: List[int]
    :param start_index: Index of first element to write; default is 0
    :type start_index: int

    """
    return web.Response(status=200)


async def write_int64_table_as_string(request: web.Request, table_name, int64_as_string_array, start_index=None) -> web.Response:
    """write_int64_table_as_string

    \&quot;Write a range of table elements\&quot; #### Examples #### * Write the values (1, 2, 3) to 3 consecutive elements in a table named i64table starting with the element at index 10:POST to https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table/_string?startIndex&#x3D;10  with body of the POST request set to [ \&quot;1\&quot;, \&quot;2\&quot;, \&quot;3\&quot; ] 

    :param table_name: Name of integer64 table to write; starting index may be specified
    :type table_name: str
    :param int64_as_string_array: Array of element values to write starting at startIndex; if the array of elements is too long  to fit in the specified table, extra elements will be ignored
    :type int64_as_string_array: List[str]
    :param start_index: Index of first element to write; default is 0.
    :type start_index: int

    """
    return web.Response(status=200)


async def write_int64_table_element(request: web.Request, table_name, index, int64_element_object) -> web.Response:
    """write_int64_table_element

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


async def write_int64_table_element_as_string(request: web.Request, table_name, index, int64_element_object) -> web.Response:
    """write_int64_table_element_as_string

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


async def write_int64_var(request: web.Request, int64_name, body) -> web.Response:
    """write_int64_var

    Sets the value of an integer64 variable

    :param int64_name: Name of integer64 variable to write
    :type int64_name: str
    :param body: Value to write to the integer64 variable
    :type body: dict | bytes

    """
    body = Int64ValueObject.from_dict(body)
    return web.Response(status=200)


async def write_int64_var_as_string(request: web.Request, int64_name, body) -> web.Response:
    """write_int64_var_as_string

    Sets the value of an integer64 variable as a string

    :param int64_name: Name of integer64 variable to write
    :type int64_name: str
    :param body: Value to write to the integer64 variable
    :type body: dict | bytes

    """
    body = Int64StringValueObject.from_dict(body)
    return web.Response(status=200)


async def write_string_table(request: web.Request, table_name, string_array, start_index=None) -> web.Response:
    """write_string_table

    \&quot;Write a range of table elements\&quot; #### Examples #### * Write the values (\&quot;first\&quot;, \&quot;second\&quot;, \&quot;third\&quot;) to 3 consecutive elements in a table named strTable starting with the element at index 10:POST to https://1.2.3.4/api/v1/device/strategy/tables/strings/strtable?startIndex&#x3D;10  with body of the POST request set to [ \&quot;first\&quot;, \&quot;second\&quot;, \&quot;third\&quot; ] 

    :param table_name: Name of string table to write; starting index may be specified
    :type table_name: str
    :param string_array: Array of element values to write starting at startIndex; if an element value is longer than the string width, the string will be truncated to fit
    :type string_array: List[str]
    :param start_index: Index of first element to write (default is 0)
    :type start_index: int

    """
    return web.Response(status=200)


async def write_string_table_element(request: web.Request, table_name, index, string_element_object) -> web.Response:
    """write_string_table_element

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


async def write_string_var(request: web.Request, string_name, body) -> web.Response:
    """write_string_var

    Sets the value of a string variable

    :param string_name: Name of string variable to write
    :type string_name: str
    :param body: String to write. If the value is longer than the string width, the string will be truncated to fit.
    :type body: dict | bytes

    """
    body = StringValueObject.from_dict(body)
    return web.Response(status=200)
