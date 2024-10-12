from typing import List, Dict
from aiohttp import web

from openapi_server.models.csm_move_resource_envelope import CsmMoveResourceEnvelope
from openapi_server import util


async def global_resource_groups_move_resources(request: web.Request, resource_group_name, subscription_id, api_version, move_resource_envelope) -> web.Response:
    """global_resource_groups_move_resources

    

    :param resource_group_name: 
    :type resource_group_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param move_resource_envelope: 
    :type move_resource_envelope: dict | bytes

    """
    move_resource_envelope = CsmMoveResourceEnvelope.from_dict(move_resource_envelope)
    return web.Response(status=200)
