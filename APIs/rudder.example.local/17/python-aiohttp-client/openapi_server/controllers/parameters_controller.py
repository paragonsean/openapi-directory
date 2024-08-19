from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_parameter200_response import CreateParameter200Response
from openapi_server.models.delete_parameter200_response import DeleteParameter200Response
from openapi_server.models.delete_parameter500_response import DeleteParameter500Response
from openapi_server.models.list_parameters200_response import ListParameters200Response
from openapi_server.models.parameter import Parameter
from openapi_server.models.parameter_details200_response import ParameterDetails200Response
from openapi_server.models.update_parameter200_response import UpdateParameter200Response
from openapi_server import util


async def create_parameter(request: web.Request, body) -> web.Response:
    """Create a new parameter

    Create a new global parameter

    :param body: 
    :type body: dict | bytes

    """
    body = Parameter.from_dict(body)
    return web.Response(status=200)


async def delete_parameter(request: web.Request, parameter_id) -> web.Response:
    """Delete a parameter

    Delete an existing parameter

    :param parameter_id: Id of the parameter to manage
    :type parameter_id: str

    """
    return web.Response(status=200)


async def list_parameters(request: web.Request, ) -> web.Response:
    """List all global parameters

    Get the current value of all the global parameters


    """
    return web.Response(status=200)


async def parameter_details(request: web.Request, parameter_id) -> web.Response:
    """Get the value of a parameter

    Get the current value of a given parameter

    :param parameter_id: Id of the parameter to manage
    :type parameter_id: str

    """
    return web.Response(status=200)


async def update_parameter(request: web.Request, parameter_id) -> web.Response:
    """Update a parameter&#39;s value

    Update the properties of a parameter

    :param parameter_id: Id of the parameter to manage
    :type parameter_id: str

    """
    return web.Response(status=200)
