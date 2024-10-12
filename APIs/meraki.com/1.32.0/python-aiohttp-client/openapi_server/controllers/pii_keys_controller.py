from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_network_pii_pii_keys_2(request: web.Request, network_id, username=None, email=None, mac=None, serial=None, imei=None, bluetooth_mac=None) -> web.Response:
    """List the keys required to access Personally Identifiable Information (PII) for a given identifier

    List the keys required to access Personally Identifiable Information (PII) for a given identifier. Exactly one identifier will be accepted. If the organization contains org-wide Systems Manager users matching the key provided then there will be an entry with the key \&quot;0\&quot; containing the applicable keys.  ## ALTERNATE PATH  &#x60;&#x60;&#x60; /organizations/{organizationId}/pii/piiKeys &#x60;&#x60;&#x60;

    :param network_id: 
    :type network_id: str
    :param username: The username of a Systems Manager user
    :type username: str
    :param email: The email of a network user account or a Systems Manager device
    :type email: str
    :param mac: The MAC of a network client device or a Systems Manager device
    :type mac: str
    :param serial: The serial of a Systems Manager device
    :type serial: str
    :param imei: The IMEI of a Systems Manager device
    :type imei: str
    :param bluetooth_mac: The MAC of a Bluetooth client
    :type bluetooth_mac: str

    """
    return web.Response(status=200)
