from typing import List, Dict
from aiohttp import web

from openapi_server.models.command_enum_command_mode import CommandEnumCommandMode
from openapi_server.models.command_enum_direction import CommandEnumDirection
from openapi_server.models.command_enum_status import CommandEnumStatus
from openapi_server.models.command_enum_transport import CommandEnumTransport
from openapi_server.models.list_command_response import ListCommandResponse
from openapi_server.models.wireless_v1_command import WirelessV1Command
from openapi_server import util


async def create_command(request: web.Request, command, callback_method=None, callback_url=None, command_mode=None, delivery_receipt_requested=None, include_sid=None, sim=None) -> web.Response:
    """create_command

    Send a Command to a Sim.

    :param command: The message body of the Command. Can be plain text in text mode or a Base64 encoded byte string in binary mode.
    :type command: str
    :param callback_method: The HTTP method we use to call &#x60;callback_url&#x60;. Can be: &#x60;POST&#x60; or &#x60;GET&#x60;, and the default is &#x60;POST&#x60;.
    :type callback_method: str
    :param callback_url: The URL we call using the &#x60;callback_url&#x60; when the Command has finished sending, whether the command was delivered or it failed.
    :type callback_url: str
    :param command_mode: 
    :type command_mode: str
    :param delivery_receipt_requested: Whether to request delivery receipt from the recipient. For Commands that request delivery receipt, the Command state transitions to &#39;delivered&#39; once the server has received a delivery receipt from the device. The default value is &#x60;true&#x60;.
    :type delivery_receipt_requested: bool
    :param include_sid: Whether to include the SID of the command in the message body. Can be: &#x60;none&#x60;, &#x60;start&#x60;, or &#x60;end&#x60;, and the default behavior is &#x60;none&#x60;. When sending a Command to a SIM in text mode, we can automatically include the SID of the Command in the message body, which could be used to ensure that the device does not process the same Command more than once.  A value of &#x60;start&#x60; will prepend the message with the Command SID, and &#x60;end&#x60; will append it to the end, separating the Command SID from the message body with a space. The length of the Command SID is included in the 160 character limit so the SMS body must be 128 characters or less before the Command SID is included.
    :type include_sid: str
    :param sim: The &#x60;sid&#x60; or &#x60;unique_name&#x60; of the [SIM](https://www.twilio.com/docs/iot/wireless/api/sim-resource) to send the Command to.
    :type sim: str

    """
    return web.Response(status=200)


async def delete_command(request: web.Request, sid) -> web.Response:
    """delete_command

    Delete a Command instance from your account.

    :param sid: The SID of the Command resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_command(request: web.Request, sid) -> web.Response:
    """fetch_command

    Fetch a Command instance from your account.

    :param sid: The SID of the Command resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_command(request: web.Request, sim=None, status=None, direction=None, transport=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_command

    Retrieve a list of Commands from your account.

    :param sim: The &#x60;sid&#x60; or &#x60;unique_name&#x60; of the [Sim resources](https://www.twilio.com/docs/iot/wireless/api/sim-resource) to read.
    :type sim: str
    :param status: The status of the resources to read. Can be: &#x60;queued&#x60;, &#x60;sent&#x60;, &#x60;delivered&#x60;, &#x60;received&#x60;, or &#x60;failed&#x60;.
    :type status: str
    :param direction: Only return Commands with this direction value.
    :type direction: str
    :param transport: Only return Commands with this transport value. Can be: &#x60;sms&#x60; or &#x60;ip&#x60;.
    :type transport: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
