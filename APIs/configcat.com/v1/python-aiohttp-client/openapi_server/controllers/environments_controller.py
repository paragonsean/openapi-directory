from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_environment_model import CreateEnvironmentModel
from openapi_server.models.environment_model import EnvironmentModel
from openapi_server.models.environment_model_haljson import EnvironmentModelHaljson
from openapi_server.models.update_environment_model import UpdateEnvironmentModel
from openapi_server import util


async def create_environment(request: web.Request, product_id, body) -> web.Response:
    """Create Environment

    This endpoint creates a new Environment in a specified Product  identified by the &#x60;productId&#x60; parameter, which can be obtained from the [List Products](#operation/get-products) endpoint.

    :param product_id: The identifier of the Product.
    :type product_id: str
    :type product_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateEnvironmentModel.from_dict(body)
    return web.Response(status=200)


async def delete_environment(request: web.Request, environment_id) -> web.Response:
    """Delete Environment

    This endpoint removes an Environment identified by the &#x60;environmentId&#x60; parameter.

    :param environment_id: The identifier of the Environment.
    :type environment_id: str
    :type environment_id: str

    """
    return web.Response(status=200)


async def get_environment(request: web.Request, environment_id) -> web.Response:
    """Get Environment

    This endpoint returns the metadata of an Environment  identified by the &#x60;environmentId&#x60;.

    :param environment_id: The identifier of the Environment.
    :type environment_id: str
    :type environment_id: str

    """
    return web.Response(status=200)


async def get_environments(request: web.Request, product_id) -> web.Response:
    """List Environments

    This endpoint returns the list of the Environments that belongs to the given Product identified by the &#x60;productId&#x60; parameter, which can be obtained from the [List Products](#operation/get-products) endpoint.

    :param product_id: The identifier of the Product.
    :type product_id: str
    :type product_id: str

    """
    return web.Response(status=200)


async def update_environment(request: web.Request, environment_id, body) -> web.Response:
    """Update Environment

    This endpoint updates an Environment identified by the &#x60;environmentId&#x60; parameter.

    :param environment_id: The identifier of the Environment.
    :type environment_id: str
    :type environment_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateEnvironmentModel.from_dict(body)
    return web.Response(status=200)
