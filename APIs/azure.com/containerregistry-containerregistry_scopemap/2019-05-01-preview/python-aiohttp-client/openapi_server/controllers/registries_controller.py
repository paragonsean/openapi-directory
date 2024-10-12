from typing import List, Dict
from aiohttp import web

from openapi_server.models.generate_credentials_parameters import GenerateCredentialsParameters
from openapi_server.models.generate_credentials_result import GenerateCredentialsResult
from openapi_server import util


async def registries_generate_credentials(request: web.Request, api_version, subscription_id, resource_group_name, registry_name, generate_credentials_parameters) -> web.Response:
    """registries_generate_credentials

    Generate keys for a token of a specified container registry.

    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param registry_name: The name of the container registry.
    :type registry_name: str
    :param generate_credentials_parameters: The parameters for generating credentials.
    :type generate_credentials_parameters: dict | bytes

    """
    generate_credentials_parameters = GenerateCredentialsParameters.from_dict(generate_credentials_parameters)
    return web.Response(status=200)
