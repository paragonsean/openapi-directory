from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_sim_response import ListSimResponse
from openapi_server.models.sim_enum_reset_status import SimEnumResetStatus
from openapi_server.models.sim_enum_status import SimEnumStatus
from openapi_server.models.wireless_v1_sim import WirelessV1Sim
from openapi_server import util


async def delete_sim(request: web.Request, sid) -> web.Response:
    """delete_sim

    Delete a Sim resource on your Account.

    :param sid: The SID or the &#x60;unique_name&#x60; of the Sim resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_sim(request: web.Request, sid) -> web.Response:
    """fetch_sim

    Fetch a Sim resource on your Account.

    :param sid: The SID or the &#x60;unique_name&#x60; of the Sim resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_sim(request: web.Request, status=None, iccid=None, rate_plan=None, eid=None, sim_registration_code=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_sim

    Retrieve a list of Sim resources on your Account.

    :param status: Only return Sim resources with this status.
    :type status: str
    :param iccid: Only return Sim resources with this ICCID. This will return a list with a maximum size of 1.
    :type iccid: str
    :param rate_plan: The SID or unique name of a [RatePlan resource](https://www.twilio.com/docs/iot/wireless/api/rateplan-resource). Only return Sim resources assigned to this RatePlan resource.
    :type rate_plan: str
    :param eid: Deprecated.
    :type eid: str
    :param sim_registration_code: Only return Sim resources with this registration code. This will return a list with a maximum size of 1.
    :type sim_registration_code: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_sim(request: web.Request, sid, account_sid=None, callback_method=None, callback_url=None, commands_callback_method=None, commands_callback_url=None, friendly_name=None, rate_plan=None, reset_status=None, sms_fallback_method=None, sms_fallback_url=None, sms_method=None, sms_url=None, status=None, unique_name=None, voice_fallback_method=None, voice_fallback_url=None, voice_method=None, voice_url=None) -> web.Response:
    """update_sim

    Updates the given properties of a Sim resource on your Account.

    :param sid: The SID or the &#x60;unique_name&#x60; of the Sim resource to update.
    :type sid: str
    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) to which the Sim resource should belong. The Account SID can only be that of the requesting Account or that of a [Subaccount](https://www.twilio.com/docs/iam/api/subaccounts) of the requesting Account. Only valid when the Sim resource&#39;s status is &#x60;new&#x60;. For more information, see the [Move SIMs between Subaccounts documentation](https://www.twilio.com/docs/iot/wireless/api/sim-resource#move-sims-between-subaccounts).
    :type account_sid: str
    :param callback_method: The HTTP method we should use to call &#x60;callback_url&#x60;. Can be: &#x60;POST&#x60; or &#x60;GET&#x60;. The default is &#x60;POST&#x60;.
    :type callback_method: str
    :param callback_url: The URL we should call using the &#x60;callback_url&#x60; when the SIM has finished updating. When the SIM transitions from &#x60;new&#x60; to &#x60;ready&#x60; or from any status to &#x60;deactivated&#x60;, we call this URL when the status changes to an intermediate status (&#x60;ready&#x60; or &#x60;deactivated&#x60;) and again when the status changes to its final status (&#x60;active&#x60; or &#x60;canceled&#x60;).
    :type callback_url: str
    :param commands_callback_method: The HTTP method we should use to call &#x60;commands_callback_url&#x60;. Can be: &#x60;POST&#x60; or &#x60;GET&#x60;. The default is &#x60;POST&#x60;.
    :type commands_callback_method: str
    :param commands_callback_url: The URL we should call using the &#x60;commands_callback_method&#x60; when the SIM sends a [Command](https://www.twilio.com/docs/iot/wireless/api/command-resource). Your server should respond with an HTTP status code in the 200 range; any response body is ignored.
    :type commands_callback_url: str
    :param friendly_name: A descriptive string that you create to describe the Sim resource. It does not need to be unique.
    :type friendly_name: str
    :param rate_plan: The SID or unique name of the [RatePlan resource](https://www.twilio.com/docs/iot/wireless/api/rateplan-resource) to which the Sim resource should be assigned.
    :type rate_plan: str
    :param reset_status: 
    :type reset_status: str
    :param sms_fallback_method: The HTTP method we should use to call &#x60;sms_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. Default is &#x60;POST&#x60;.
    :type sms_fallback_method: str
    :param sms_fallback_url: The URL we should call using the &#x60;sms_fallback_method&#x60; when an error occurs while retrieving or executing the TwiML requested from &#x60;sms_url&#x60;.
    :type sms_fallback_url: str
    :param sms_method: The HTTP method we should use to call &#x60;sms_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. Default is &#x60;POST&#x60;.
    :type sms_method: str
    :param sms_url: The URL we should call using the &#x60;sms_method&#x60; when the SIM-connected device sends an SMS message that is not a [Command](https://www.twilio.com/docs/iot/wireless/api/command-resource).
    :type sms_url: str
    :param status: 
    :type status: str
    :param unique_name: An application-defined string that uniquely identifies the resource. It can be used in place of the &#x60;sid&#x60; in the URL path to address the resource.
    :type unique_name: str
    :param voice_fallback_method: Deprecated.
    :type voice_fallback_method: str
    :param voice_fallback_url: Deprecated.
    :type voice_fallback_url: str
    :param voice_method: Deprecated.
    :type voice_method: str
    :param voice_url: Deprecated.
    :type voice_url: str

    """
    return web.Response(status=200)
