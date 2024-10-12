from typing import List, Dict
from aiohttp import web

from openapi_server.models.digital_point_state_object import DigitalPointStateObject
from openapi_server.models.digital_point_state_var import DigitalPointStateVar
from openapi_server.models.error_response400_bad_admin_or_value import ErrorResponse400BadAdminOrValue
from openapi_server.models.error_response401_bad_key_for_basic_auth import ErrorResponse401BadKeyForBasicAuth
from openapi_server.models.error_response404_not_found import ErrorResponse404NotFound
from openapi_server.models.float_value_object import FloatValueObject
from openapi_server.models.float_var import FloatVar
from openapi_server import util


async def read_analog_input_eu_0(request: web.Request, io_name) -> web.Response:
    """read_analog_input_eu_0

    Reads the value in engineering units (EU) of the specified analog input

    :param io_name: Name of the analog input point to read
    :type io_name: str

    """
    return web.Response(status=200)


async def read_analog_inputs_0(request: web.Request, ) -> web.Response:
    """read_analog_inputs_0

    Returns the name and engineering units (EU) for all analog input points in the strategy


    """
    return web.Response(status=200)


async def read_analog_output_eu_0(request: web.Request, io_name) -> web.Response:
    """read_analog_output_eu_0

    Reads the value in engineering units (EU) of the specified analog output

    :param io_name: Name of analog output point to read
    :type io_name: str

    """
    return web.Response(status=200)


async def read_analog_outputs_0(request: web.Request, ) -> web.Response:
    """read_analog_outputs_0

    Returns the name and engineering units (EU) for all analog output points in the strategy


    """
    return web.Response(status=200)


async def read_digital_input_state_0(request: web.Request, io_name) -> web.Response:
    """read_digital_input_state_0

    Returns the specified digital input point&#39;s state (true &#x3D; on, false &#x3D; off)

    :param io_name: Name of the digital input point to read
    :type io_name: str

    """
    return web.Response(status=200)


async def read_digital_inputs_0(request: web.Request, ) -> web.Response:
    """read_digital_inputs_0

    Returns the name and state (true &#x3D; on, false &#x3D; off) of all digital input points in the strategy. If there is no strategy in the controller, or the strategy includes no digital inputs, the returned array will be empty.


    """
    return web.Response(status=200)


async def read_digital_output_state_0(request: web.Request, io_name) -> web.Response:
    """read_digital_output_state_0

    Returns the specified digital output point&#39;s state (true &#x3D; on, false &#x3D; off)

    :param io_name: Name of the digit output point to read
    :type io_name: str

    """
    return web.Response(status=200)


async def read_digital_outputs_0(request: web.Request, ) -> web.Response:
    """read_digital_outputs_0

    Returns the name and state (true &#x3D; on, false &#x3D; off) of all digital output points in the strategy


    """
    return web.Response(status=200)


async def write_analog_output_eu_0(request: web.Request, io_name, body) -> web.Response:
    """write_analog_output_eu_0

    Sets the value of the specified analog output point

    :param io_name: Name of the analog output point to write
    :type io_name: str
    :param body: Value to write
    :type body: dict | bytes

    """
    body = FloatValueObject.from_dict(body)
    return web.Response(status=200)


async def write_digital_output_state_0(request: web.Request, io_name, body) -> web.Response:
    """write_digital_output_state_0

    Sets the value of the specified digital output point

    :param io_name: Name of the digital output point to write
    :type io_name: str
    :param body: Value to write
    :type body: dict | bytes

    """
    body = DigitalPointStateObject.from_dict(body)
    return web.Response(status=200)
