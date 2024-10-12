from typing import List, Dict
from aiohttp import web

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
from openapi_server.models.string_value_object import StringValueObject
from openapi_server.models.string_var import StringVar
from openapi_server import util


async def read_down_timer_value_0(request: web.Request, down_timer_name) -> web.Response:
    """read_down_timer_value_0

    Returns current value of the specified down timer

    :param down_timer_name: Name of the down timer variable to read
    :type down_timer_name: str

    """
    return web.Response(status=200)


async def read_down_timer_vars_0(request: web.Request, ) -> web.Response:
    """read_down_timer_vars_0

    Returns the name and current value of all down timers in the strategy


    """
    return web.Response(status=200)


async def read_float_var_0(request: web.Request, float_name) -> web.Response:
    """read_float_var_0

    Returns value of the specified float variable

    :param float_name: Name of float variable to read
    :type float_name: str

    """
    return web.Response(status=200)


async def read_float_vars_0(request: web.Request, ) -> web.Response:
    """read_float_vars_0

    Returns the name and value of all (single-precision) float variables in the strategy


    """
    return web.Response(status=200)


async def read_int32_var_0(request: web.Request, int32_name) -> web.Response:
    """read_int32_var_0

    Returns value of the specified integer32 variable

    :param int32_name: Name of integer32 variable to read
    :type int32_name: str

    """
    return web.Response(status=200)


async def read_int32_vars_0(request: web.Request, ) -> web.Response:
    """read_int32_vars_0

    Returns the name and value of all integer32 variables in the strategy


    """
    return web.Response(status=200)


async def read_int64_var_0(request: web.Request, int64_name) -> web.Response:
    """read_int64_var_0

    Returns value of the specified integer64 variable

    :param int64_name: Name of integer64 variable to read
    :type int64_name: str

    """
    return web.Response(status=200)


async def read_int64_var_as_string_0(request: web.Request, int64_name) -> web.Response:
    """read_int64_var_as_string_0

    Returns value of the specified integer64 variable as a string

    :param int64_name: Name of integer64 variable to read
    :type int64_name: str

    """
    return web.Response(status=200)


async def read_int64_vars_0(request: web.Request, ) -> web.Response:
    """read_int64_vars_0

    Returns the name and value of all integer64 variables in the strategy


    """
    return web.Response(status=200)


async def read_int64_vars_as_strings_0(request: web.Request, ) -> web.Response:
    """read_int64_vars_as_strings_0

    Returns the name and value as a string of all integer64 variables in the strategy


    """
    return web.Response(status=200)


async def read_string_var_0(request: web.Request, string_name) -> web.Response:
    """read_string_var_0

    Returns value of the specified string

    :param string_name: Name of string variable to read
    :type string_name: str

    """
    return web.Response(status=200)


async def read_string_vars_0(request: web.Request, ) -> web.Response:
    """read_string_vars_0

    Returns the name and value of all string variables in the strategy


    """
    return web.Response(status=200)


async def read_up_timer_value_0(request: web.Request, up_timer_name) -> web.Response:
    """read_up_timer_value_0

    Returns current value of the specified up timer

    :param up_timer_name: Name of the up timer variable to read
    :type up_timer_name: str

    """
    return web.Response(status=200)


async def read_up_timer_vars_0(request: web.Request, ) -> web.Response:
    """read_up_timer_vars_0

    Returns the name and current value of all up timers in the strategy


    """
    return web.Response(status=200)


async def write_float_var_0(request: web.Request, float_name, body) -> web.Response:
    """write_float_var_0

    Sets the value of a float variable

    :param float_name: Name of the float variable to write
    :type float_name: str
    :param body: Value to write to the float variable
    :type body: dict | bytes

    """
    body = FloatValueObject.from_dict(body)
    return web.Response(status=200)


async def write_int32_var_0(request: web.Request, int32_name, body) -> web.Response:
    """write_int32_var_0

    Sets the value of an integer32 variable

    :param int32_name: Name of integer32 variable to write
    :type int32_name: str
    :param body: Value to write to the integer32 variable
    :type body: dict | bytes

    """
    body = Int32ValueObject.from_dict(body)
    return web.Response(status=200)


async def write_int64_var_0(request: web.Request, int64_name, body) -> web.Response:
    """write_int64_var_0

    Sets the value of an integer64 variable

    :param int64_name: Name of integer64 variable to write
    :type int64_name: str
    :param body: Value to write to the integer64 variable
    :type body: dict | bytes

    """
    body = Int64ValueObject.from_dict(body)
    return web.Response(status=200)


async def write_int64_var_as_string_0(request: web.Request, int64_name, body) -> web.Response:
    """write_int64_var_as_string_0

    Sets the value of an integer64 variable as a string

    :param int64_name: Name of integer64 variable to write
    :type int64_name: str
    :param body: Value to write to the integer64 variable
    :type body: dict | bytes

    """
    body = Int64StringValueObject.from_dict(body)
    return web.Response(status=200)


async def write_string_var_0(request: web.Request, string_name, body) -> web.Response:
    """write_string_var_0

    Sets the value of a string variable

    :param string_name: Name of string variable to write
    :type string_name: str
    :param body: String to write. If the value is longer than the string width, the string will be truncated to fit.
    :type body: dict | bytes

    """
    body = StringValueObject.from_dict(body)
    return web.Response(status=200)
