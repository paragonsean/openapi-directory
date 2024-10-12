from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_sim_response import ListSimResponse
from openapi_server.models.sim_enum_status import SimEnumStatus
from openapi_server.models.sim_enum_status_update import SimEnumStatusUpdate
from openapi_server.models.supersim_v1_sim import SupersimV1Sim
from openapi_server import util


async def create_sim(request: web.Request, iccid, registration_code) -> web.Response:
    """create_sim

    Register a Super SIM to your Account

    :param iccid: The [ICCID](https://en.wikipedia.org/wiki/Subscriber_identity_module#ICCID) of the Super SIM to be added to your Account.
    :type iccid: str
    :param registration_code: The 10-digit code required to claim the Super SIM for your Account.
    :type registration_code: str

    """
    return web.Response(status=200)


async def fetch_sim(request: web.Request, sid) -> web.Response:
    """fetch_sim

    Fetch a Super SIM instance from your account.

    :param sid: The SID of the Sim resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_sim(request: web.Request, status=None, fleet=None, iccid=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_sim

    Retrieve a list of Super SIMs from your account.

    :param status: The status of the Sim resources to read. Can be &#x60;new&#x60;, &#x60;ready&#x60;, &#x60;active&#x60;, &#x60;inactive&#x60;, or &#x60;scheduled&#x60;.
    :type status: str
    :param fleet: The SID or unique name of the Fleet to which a list of Sims are assigned.
    :type fleet: str
    :param iccid: The [ICCID](https://en.wikipedia.org/wiki/Subscriber_identity_module#ICCID) associated with a Super SIM to filter the list by. Passing this parameter will always return a list containing zero or one SIMs.
    :type iccid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_sim(request: web.Request, sid, account_sid=None, callback_method=None, callback_url=None, fleet=None, status=None, unique_name=None) -> web.Response:
    """update_sim

    Updates the given properties of a Super SIM instance from your account.

    :param sid: The SID of the Sim resource to update.
    :type sid: str
    :param account_sid: The SID of the Account to which the Sim resource should belong. The Account SID can only be that of the requesting Account or that of a Subaccount of the requesting Account. Only valid when the Sim resource&#39;s status is new.
    :type account_sid: str
    :param callback_method: The HTTP method we should use to call &#x60;callback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and the default is POST.
    :type callback_method: str
    :param callback_url: The URL we should call using the &#x60;callback_method&#x60; after an asynchronous update has finished.
    :type callback_url: str
    :param fleet: The SID or unique name of the Fleet to which the SIM resource should be assigned.
    :type fleet: str
    :param status: 
    :type status: str
    :param unique_name: An application-defined string that uniquely identifies the resource. It can be used in place of the resource&#39;s &#x60;sid&#x60; in the URL to address the resource.
    :type unique_name: str

    """
    return web.Response(status=200)
