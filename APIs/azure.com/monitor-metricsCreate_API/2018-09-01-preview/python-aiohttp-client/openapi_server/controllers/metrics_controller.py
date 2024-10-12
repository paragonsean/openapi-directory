from typing import List, Dict
from aiohttp import web

from openapi_server.models.azure_metrics_document import AzureMetricsDocument
from openapi_server.models.azure_metrics_result import AzureMetricsResult
from openapi_server import util


async def metrics_create(request: web.Request, content_type, content_length, authorization, subscription_id, resource_group_name, resource_provider, resource_type_name, resource_name, body) -> web.Response:
    """metrics_create

    **Post the metric values for a resource**.

    :param content_type: Supports application/json and application/x-ndjson
    :type content_type: str
    :param content_length: Content length of the payload
    :type content_length: int
    :param authorization: Authorization token issue for issued for audience \&quot;https:\\\\monitoring.azure.com\\\&quot;
    :type authorization: str
    :param subscription_id: The azure subscription id
    :type subscription_id: str
    :param resource_group_name: The ARM resource group name
    :type resource_group_name: str
    :param resource_provider: The ARM resource provider name
    :type resource_provider: str
    :param resource_type_name: The ARM resource type name
    :type resource_type_name: str
    :param resource_name: The ARM resource name
    :type resource_name: str
    :param body: The Azure metrics document json payload
    :type body: dict | bytes

    """
    body = AzureMetricsDocument.from_dict(body)
    return web.Response(status=200)
