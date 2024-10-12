from typing import List, Dict
from aiohttp import web

from openapi_server.models.azure_vm_resource_feature_support_response import AzureVMResourceFeatureSupportResponse
from openapi_server.models.feature_support_request import FeatureSupportRequest
from openapi_server import util


async def feature_support_validate(request: web.Request, api_version, azure_region, subscription_id, parameters) -> web.Response:
    """It will validate if given feature with resource properties is supported in service

    

    :param api_version: Client Api Version.
    :type api_version: str
    :param azure_region: Azure region to hit Api
    :type azure_region: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param parameters: Feature support request object
    :type parameters: dict | bytes

    """
    parameters = FeatureSupportRequest.from_dict(parameters)
    return web.Response(status=200)
