from typing import List, Dict
from aiohttp import web

from openapi_server.models.product_secret import ProductSecret
from openapi_server.models.product_secrets_list import ProductSecretsList
from openapi_server.models.secret_parameters import SecretParameters
from openapi_server import util


async def product_secrets_get(request: web.Request, subscription_id, product_id, api_version, secret_name) -> web.Response:
    """product_secrets_get

    Retrieves the specific product secret details.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param product_id: The product identifier.
    :type product_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param secret_name: The secret name.
    :type secret_name: str

    """
    return web.Response(status=200)


async def product_secrets_import(request: web.Request, subscription_id, product_id, secret_name, api_version, secret_parameters) -> web.Response:
    """product_secrets_import

    Imports a product secret.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param product_id: The product identifier.
    :type product_id: str
    :param secret_name: The secret name.
    :type secret_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param secret_parameters: The parameters required for creating/updating a product secret.
    :type secret_parameters: dict | bytes

    """
    secret_parameters = SecretParameters.from_dict(secret_parameters)
    return web.Response(status=200)


async def product_secrets_list(request: web.Request, subscription_id, api_version, product_id) -> web.Response:
    """product_secrets_list

    Returns an array of product secrets.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param product_id: The product identifier.
    :type product_id: str

    """
    return web.Response(status=200)


async def product_secrets_validate(request: web.Request, subscription_id, product_id, secret_name, api_version, secret_parameters) -> web.Response:
    """product_secrets_validate

    Validates a product secret.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param product_id: The product identifier.
    :type product_id: str
    :param secret_name: The secret name.
    :type secret_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param secret_parameters: The parameters required for creating/updating a product secret.
    :type secret_parameters: dict | bytes

    """
    secret_parameters = SecretParameters.from_dict(secret_parameters)
    return web.Response(status=200)
