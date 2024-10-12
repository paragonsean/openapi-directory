from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_version_set_list_by_service_default_response import ApiVersionSetListByServiceDefaultResponse
from openapi_server import util


async def api_version_set_delete(request: web.Request, resource_group_name, service_name, version_set_id, if_match, api_version, subscription_id) -> web.Response:
    """api_version_set_delete

    Deletes specific Api Version Set.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param version_set_id: Api Version Set identifier. Must be unique in the current API Management service instance.
    :type version_set_id: str
    :param if_match: ETag of the Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
