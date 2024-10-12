from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_connection_policy_target_response import ListConnectionPolicyTargetResponse
from openapi_server.models.voice_v1_connection_policy_connection_policy_target import VoiceV1ConnectionPolicyConnectionPolicyTarget
from openapi_server import util


async def create_connection_policy_target(request: web.Request, connection_policy_sid, target, enabled=None, friendly_name=None, priority=None, weight=None) -> web.Response:
    """create_connection_policy_target

    

    :param connection_policy_sid: The SID of the Connection Policy that owns the Target.
    :type connection_policy_sid: str
    :param target: The SIP address you want Twilio to route your calls to. This must be a &#x60;sip:&#x60; schema. &#x60;sips&#x60; is NOT supported.
    :type target: str
    :param enabled: Whether the Target is enabled. The default is &#x60;true&#x60;.
    :type enabled: bool
    :param friendly_name: A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
    :type friendly_name: str
    :param priority: The relative importance of the target. Can be an integer from 0 to 65535, inclusive, and the default is 10. The lowest number represents the most important target.
    :type priority: int
    :param weight: The value that determines the relative share of the load the Target should receive compared to other Targets with the same priority. Can be an integer from 1 to 65535, inclusive, and the default is 10. Targets with higher values receive more load than those with lower ones with the same priority.
    :type weight: int

    """
    return web.Response(status=200)


async def delete_connection_policy_target(request: web.Request, connection_policy_sid, sid) -> web.Response:
    """delete_connection_policy_target

    

    :param connection_policy_sid: The SID of the Connection Policy that owns the Target.
    :type connection_policy_sid: str
    :param sid: The unique string that we created to identify the Target resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_connection_policy_target(request: web.Request, connection_policy_sid, sid) -> web.Response:
    """fetch_connection_policy_target

    

    :param connection_policy_sid: The SID of the Connection Policy that owns the Target.
    :type connection_policy_sid: str
    :param sid: The unique string that we created to identify the Target resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_connection_policy_target(request: web.Request, connection_policy_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_connection_policy_target

    

    :param connection_policy_sid: The SID of the Connection Policy from which to read the Targets.
    :type connection_policy_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_connection_policy_target(request: web.Request, connection_policy_sid, sid, enabled=None, friendly_name=None, priority=None, target=None, weight=None) -> web.Response:
    """update_connection_policy_target

    

    :param connection_policy_sid: The SID of the Connection Policy that owns the Target.
    :type connection_policy_sid: str
    :param sid: The unique string that we created to identify the Target resource to update.
    :type sid: str
    :param enabled: Whether the Target is enabled.
    :type enabled: bool
    :param friendly_name: A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
    :type friendly_name: str
    :param priority: The relative importance of the target. Can be an integer from 0 to 65535, inclusive. The lowest number represents the most important target.
    :type priority: int
    :param target: The SIP address you want Twilio to route your calls to. This must be a &#x60;sip:&#x60; schema. &#x60;sips&#x60; is NOT supported.
    :type target: str
    :param weight: The value that determines the relative share of the load the Target should receive compared to other Targets with the same priority. Can be an integer from 1 to 65535, inclusive. Targets with higher values receive more load than those with lower ones with the same priority.
    :type weight: int

    """
    return web.Response(status=200)
