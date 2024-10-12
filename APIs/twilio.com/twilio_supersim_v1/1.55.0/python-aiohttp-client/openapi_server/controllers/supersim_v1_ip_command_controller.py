from typing import List, Dict
from aiohttp import web

from openapi_server.models.ip_command_enum_direction import IpCommandEnumDirection
from openapi_server.models.ip_command_enum_payload_type import IpCommandEnumPayloadType
from openapi_server.models.ip_command_enum_status import IpCommandEnumStatus
from openapi_server.models.list_ip_command_response import ListIpCommandResponse
from openapi_server.models.supersim_v1_ip_command import SupersimV1IpCommand
from openapi_server import util


async def create_ip_command(request: web.Request, device_port, payload, sim, callback_method=None, callback_url=None, payload_type=None) -> web.Response:
    """create_ip_command

    Send an IP Command to a Super SIM.

    :param device_port: The device port to which the IP Command will be sent.
    :type device_port: int
    :param payload: The data that will be sent to the device. The payload cannot exceed 1300 bytes. If the PayloadType is set to text, the payload is encoded in UTF-8. If PayloadType is set to binary, the payload is encoded in Base64.
    :type payload: str
    :param sim: The &#x60;sid&#x60; or &#x60;unique_name&#x60; of the [Super SIM](https://www.twilio.com/docs/iot/supersim/api/sim-resource) to send the IP Command to.
    :type sim: str
    :param callback_method: The HTTP method we should use to call &#x60;callback_url&#x60;. Can be &#x60;GET&#x60; or &#x60;POST&#x60;, and the default is &#x60;POST&#x60;.
    :type callback_method: str
    :param callback_url: The URL we should call using the &#x60;callback_method&#x60; after we have sent the IP Command.
    :type callback_url: str
    :param payload_type: 
    :type payload_type: str

    """
    return web.Response(status=200)


async def fetch_ip_command(request: web.Request, sid) -> web.Response:
    """fetch_ip_command

    Fetch IP Command instance from your account.

    :param sid: The SID of the IP Command resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_ip_command(request: web.Request, sim=None, sim_iccid=None, status=None, direction=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_ip_command

    Retrieve a list of IP Commands from your account.

    :param sim: The SID or unique name of the Sim resource that IP Command was sent to or from.
    :type sim: str
    :param sim_iccid: The ICCID of the Sim resource that IP Command was sent to or from.
    :type sim_iccid: str
    :param status: The status of the IP Command. Can be: &#x60;queued&#x60;, &#x60;sent&#x60;, &#x60;received&#x60; or &#x60;failed&#x60;. See the [IP Command Status Values](https://www.twilio.com/docs/iot/supersim/api/ipcommand-resource#status-values) for a description of each.
    :type status: str
    :param direction: The direction of the IP Command. Can be &#x60;to_sim&#x60; or &#x60;from_sim&#x60;. The value of &#x60;to_sim&#x60; is synonymous with the term &#x60;mobile terminated&#x60;, and &#x60;from_sim&#x60; is synonymous with the term &#x60;mobile originated&#x60;.
    :type direction: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
