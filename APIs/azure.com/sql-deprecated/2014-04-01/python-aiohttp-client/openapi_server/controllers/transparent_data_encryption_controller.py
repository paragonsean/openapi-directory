from typing import List, Dict
from aiohttp import web

from openapi_server.models.transparent_data_encryption_list_result import TransparentDataEncryptionListResult
from openapi_server import util


async def transparent_data_encryption_configurations_list_by_database(request: web.Request, api_version, subscription_id, resource_group_name, server_name, database_name) -> web.Response:
    """transparent_data_encryption_configurations_list_by_database

    Gets a list of a database&#39;s transparent data encryption configurations. There is only ever one element, named &#39;current&#39;, so GetTransparentDataEncryptionConfiguration should be used instead.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database for which the transparent data encryption applies.
    :type database_name: str

    """
    return web.Response(status=200)
