from typing import List, Dict
from aiohttp import web

from openapi_server.models.esim_profile_enum_status import EsimProfileEnumStatus
from openapi_server.models.list_esim_profile_response import ListEsimProfileResponse
from openapi_server.models.supersim_v1_esim_profile import SupersimV1EsimProfile
from openapi_server import util


async def create_esim_profile(request: web.Request, callback_method=None, callback_url=None, eid=None, generate_matching_id=None) -> web.Response:
    """create_esim_profile

    Order an eSIM Profile.

    :param callback_method: The HTTP method we should use to call &#x60;callback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and the default is POST.
    :type callback_method: str
    :param callback_url: The URL we should call using the &#x60;callback_method&#x60; when the status of the eSIM Profile changes. At this stage of the eSIM Profile pilot, the a request to the URL will only be called when the ESimProfile resource changes from &#x60;reserving&#x60; to &#x60;available&#x60;.
    :type callback_url: str
    :param eid: Identifier of the eUICC that will claim the eSIM Profile.
    :type eid: str
    :param generate_matching_id: When set to &#x60;true&#x60;, a value for &#x60;Eid&#x60; does not need to be provided. Instead, when the eSIM profile is reserved, a matching ID will be generated and returned via the &#x60;matching_id&#x60; property. This identifies the specific eSIM profile that can be used by any capable device to claim and download the profile.
    :type generate_matching_id: bool

    """
    return web.Response(status=200)


async def fetch_esim_profile(request: web.Request, sid) -> web.Response:
    """fetch_esim_profile

    Fetch an eSIM Profile.

    :param sid: The SID of the eSIM Profile resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_esim_profile(request: web.Request, eid=None, sim_sid=None, status=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_esim_profile

    Retrieve a list of eSIM Profiles.

    :param eid: List the eSIM Profiles that have been associated with an EId.
    :type eid: str
    :param sim_sid: Find the eSIM Profile resource related to a [Sim](https://www.twilio.com/docs/iot/supersim/api/sim-resource) resource by providing the SIM SID. Will always return an array with either 1 or 0 records.
    :type sim_sid: str
    :param status: List the eSIM Profiles that are in a given status.
    :type status: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
