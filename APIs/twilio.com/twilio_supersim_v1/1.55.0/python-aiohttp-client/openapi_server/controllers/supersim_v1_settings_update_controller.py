from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_settings_update_response import ListSettingsUpdateResponse
from openapi_server.models.settings_update_enum_status import SettingsUpdateEnumStatus
from openapi_server import util


async def list_settings_update(request: web.Request, sim=None, status=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_settings_update

    Retrieve a list of Settings Updates.

    :param sim: Filter the Settings Updates by a Super SIM&#39;s SID or UniqueName.
    :type sim: str
    :param status: Filter the Settings Updates by status. Can be &#x60;scheduled&#x60;, &#x60;in-progress&#x60;, &#x60;successful&#x60;, or &#x60;failed&#x60;.
    :type status: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
