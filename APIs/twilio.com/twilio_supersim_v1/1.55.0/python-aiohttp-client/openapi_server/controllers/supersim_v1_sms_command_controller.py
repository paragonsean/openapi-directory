from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_sms_command_response import ListSmsCommandResponse
from openapi_server.models.sms_command_enum_direction import SmsCommandEnumDirection
from openapi_server.models.sms_command_enum_status import SmsCommandEnumStatus
from openapi_server.models.supersim_v1_sms_command import SupersimV1SmsCommand
from openapi_server import util


async def create_sms_command(request: web.Request, payload, sim, callback_method=None, callback_url=None) -> web.Response:
    """create_sms_command

    Send SMS Command to a Sim.

    :param payload: The message body of the SMS Command.
    :type payload: str
    :param sim: The &#x60;sid&#x60; or &#x60;unique_name&#x60; of the [SIM](https://www.twilio.com/docs/iot/supersim/api/sim-resource) to send the SMS Command to.
    :type sim: str
    :param callback_method: The HTTP method we should use to call &#x60;callback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and the default is POST.
    :type callback_method: str
    :param callback_url: The URL we should call using the &#x60;callback_method&#x60; after we have sent the command.
    :type callback_url: str

    """
    return web.Response(status=200)


async def fetch_sms_command(request: web.Request, sid) -> web.Response:
    """fetch_sms_command

    Fetch SMS Command instance from your account.

    :param sid: The SID of the SMS Command resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_sms_command(request: web.Request, sim=None, status=None, direction=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_sms_command

    Retrieve a list of SMS Commands from your account.

    :param sim: The SID or unique name of the Sim resource that SMS Command was sent to or from.
    :type sim: str
    :param status: The status of the SMS Command. Can be: &#x60;queued&#x60;, &#x60;sent&#x60;, &#x60;delivered&#x60;, &#x60;received&#x60; or &#x60;failed&#x60;. See the [SMS Command Status Values](https://www.twilio.com/docs/iot/supersim/api/smscommand-resource#status-values) for a description of each.
    :type status: str
    :param direction: The direction of the SMS Command. Can be &#x60;to_sim&#x60; or &#x60;from_sim&#x60;. The value of &#x60;to_sim&#x60; is synonymous with the term &#x60;mobile terminated&#x60;, and &#x60;from_sim&#x60; is synonymous with the term &#x60;mobile originated&#x60;.
    :type direction: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
