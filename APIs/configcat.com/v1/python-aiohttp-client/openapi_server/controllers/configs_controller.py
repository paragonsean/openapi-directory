from typing import List, Dict
from aiohttp import web

from openapi_server.models.config_model import ConfigModel
from openapi_server.models.config_model_haljson import ConfigModelHaljson
from openapi_server.models.create_config_request import CreateConfigRequest
from openapi_server.models.update_config_request import UpdateConfigRequest
from openapi_server import util


async def create_config(request: web.Request, product_id, body) -> web.Response:
    """Create Config

    This endpoint creates a new Config in a specified Product  identified by the &#x60;productId&#x60; parameter, which can be obtained from the [List Products](#operation/get-products) endpoint.

    :param product_id: The identifier of the Product.
    :type product_id: str
    :type product_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateConfigRequest.from_dict(body)
    return web.Response(status=200)


async def delete_config(request: web.Request, config_id) -> web.Response:
    """Delete Config

    This endpoint removes a Config identified by the &#x60;configId&#x60; parameter.

    :param config_id: The identifier of the Config.
    :type config_id: str
    :type config_id: str

    """
    return web.Response(status=200)


async def get_config(request: web.Request, config_id) -> web.Response:
    """Get Config

    This endpoint returns the metadata of a Config identified by the &#x60;configId&#x60;.

    :param config_id: The identifier of the Config.
    :type config_id: str
    :type config_id: str

    """
    return web.Response(status=200)


async def get_configs(request: web.Request, product_id) -> web.Response:
    """List Configs

    This endpoint returns the list of the Configs that belongs to the given Product identified by the &#x60;productId&#x60; parameter, which can be obtained from the [List Products](#operation/get-products) endpoint.

    :param product_id: The identifier of the Product.
    :type product_id: str
    :type product_id: str

    """
    return web.Response(status=200)


async def update_config(request: web.Request, config_id, body) -> web.Response:
    """Update Config

    This endpoint updates a Config identified by the &#x60;configId&#x60; parameter.

    :param config_id: The identifier of the Config.
    :type config_id: str
    :type config_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateConfigRequest.from_dict(body)
    return web.Response(status=200)
