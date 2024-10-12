from typing import List, Dict
from aiohttp import web

from openapi_server.models.tde_certificate import TdeCertificate
from openapi_server import util


async def tde_certificates_create(request: web.Request, resource_group_name, server_name, subscription_id, api_version, parameters) -> web.Response:
    """tde_certificates_create

    Creates a TDE certificate for a given server.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param parameters: The requested TDE certificate to be created or updated.
    :type parameters: dict | bytes

    """
    parameters = TdeCertificate.from_dict(parameters)
    return web.Response(status=200)
