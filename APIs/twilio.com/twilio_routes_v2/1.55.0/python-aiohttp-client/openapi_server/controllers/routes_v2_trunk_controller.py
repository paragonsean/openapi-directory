from typing import List, Dict
from aiohttp import web

from openapi_server.models.routes_v2_trunks import RoutesV2Trunks
from openapi_server import util


async def fetch_trunks(request: web.Request, sip_trunk_domain) -> web.Response:
    """fetch_trunks

    Fetch the Inbound Processing Region assigned to a SIP Trunk.

    :param sip_trunk_domain: The absolute URL of the SIP Trunk
    :type sip_trunk_domain: str

    """
    return web.Response(status=200)


async def update_trunks(request: web.Request, sip_trunk_domain, friendly_name=None, voice_region=None) -> web.Response:
    """update_trunks

    Assign an Inbound Processing Region to a SIP Trunk

    :param sip_trunk_domain: The absolute URL of the SIP Trunk
    :type sip_trunk_domain: str
    :param friendly_name: A human readable description of this resource, up to 64 characters.
    :type friendly_name: str
    :param voice_region: The Inbound Processing Region used for this SIP Trunk for voice
    :type voice_region: str

    """
    return web.Response(status=200)
