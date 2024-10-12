from typing import List, Dict
from aiohttp import web

from openapi_server.models.download_history_data_list import DownloadHistoryDataList
from openapi_server.models.language import Language
from openapi_server.models.license_sfx_request import LicenseSFXRequest
from openapi_server.models.license_sfx_result_data_list import LicenseSFXResultDataList
from openapi_server.models.sfx import SFX
from openapi_server.models.sfx_data_list import SFXDataList
from openapi_server.models.sfx_search_results import SFXSearchResults
from openapi_server.models.sfx_url import SfxUrl
from openapi_server import util


async def download_sfx(request: web.Request, id) -> web.Response:
    """Download sound effects

    This endpoint redownloads sound effects that you have already received a license for. The download links in the response are valid for 8 hours.

    :param id: License ID
    :type id: str

    """
    return web.Response(status=200)


async def get_sfx_details(request: web.Request, id, language=None, view=None, library=None, search_id=None) -> web.Response:
    """Get details about sound effects

    This endpoint shows information about a sound effect.

    :param id: Audio track ID
    :type id: int
    :param language: Language for the keywords and categories in the response
    :type language: dict | bytes
    :param view: Amount of detail to render in the response
    :type view: str
    :param library: Which library to fetch from
    :type library: str
    :param search_id: The ID of the search that is related to this request
    :type search_id: str

    """
    language = .from_dict(language)
    return web.Response(status=200)


async def get_sfx_license_list(request: web.Request, sfx_id=None, license=None, page=None, per_page=None, sort=None, username=None, start_date=None, end_date=None, license_id=None, download_availability=None, team_history=None) -> web.Response:
    """List sound effects licenses

    This endpoint lists existing licenses.

    :param sfx_id: Show licenses for the specified sound effects ID
    :type sfx_id: str
    :param license: Show sound effects that are available with the specified license, such as &#x60;standard&#x60; or &#x60;enhanced&#x60;; prepending a &#x60;-&#x60; sign excludes results from that license
    :type license: str
    :param page: Page number
    :type page: int
    :param per_page: Number of results per page
    :type per_page: int
    :param sort: Sort order
    :type sort: str
    :param username: Filter licenses by username of licensee
    :type username: str
    :param start_date: Show licenses created on or after the specified date
    :type start_date: str
    :param end_date: Show licenses created before the specified date
    :type end_date: str
    :param license_id: Filter by the license ID
    :type license_id: str
    :param download_availability: Filter licenses by download availability
    :type download_availability: str
    :param team_history: Set to true to see license history for all members of your team.
    :type team_history: bool

    """
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    return web.Response(status=200)


async def get_sfx_list_details(request: web.Request, id, view=None, language=None, library=None, search_id=None) -> web.Response:
    """List details about sound effects

    This endpoint shows information about sound effects.

    :param id: One or more sound effect IDs
    :type id: List[str]
    :param view: Amount of detail to render in the response
    :type view: str
    :param language: Language for the keywords and categories in the response
    :type language: dict | bytes
    :param library: Which library to fetch from
    :type library: str
    :param search_id: The ID of the search that is related to this request
    :type search_id: str

    """
    language = .from_dict(language)
    return web.Response(status=200)


async def licenses_sfx(request: web.Request, body) -> web.Response:
    """License sound effects

    This endpoint licenses sounds effect assets.

    :param body: 
    :type body: dict | bytes

    """
    body = LicenseSFXRequest.from_dict(body)
    return web.Response(status=200)


async def search_sfx(request: web.Request, added_date=None, added_date_start=None, added_date_end=None, duration=None, duration_from=None, duration_to=None, page=None, per_page=None, query=None, safe=None, sort=None, view=None, language=None) -> web.Response:
    """Search for sound effects

    This endpoint searches for sound effects. If you specify more than one search parameter, the API uses an AND condition.

    :param added_date: Show sound effects added on the specified date
    :type added_date: str
    :param added_date_start: Show sound effects added on or after the specified date
    :type added_date_start: str
    :param added_date_end: Show sound effects added before the specified date
    :type added_date_end: str
    :param duration: Show sound effects with the specified duration in seconds
    :type duration: int
    :param duration_from: Show sound effects with the specified duration or longer in seconds
    :type duration_from: int
    :param duration_to: Show sound effects with the specified duration or shorter in seconds
    :type duration_to: int
    :param page: Page number
    :type page: int
    :param per_page: Number of results per page
    :type per_page: int
    :param query: One or more search terms separated by spaces
    :type query: str
    :param safe: Enable or disable safe search
    :type safe: bool
    :param sort: Sort by
    :type sort: str
    :param view: Amount of detail to render in the response
    :type view: str
    :param language: Set query and result language (uses Accept-Language header if not set)
    :type language: dict | bytes

    """
    added_date = util.deserialize_date(added_date)
    added_date_start = util.deserialize_date(added_date_start)
    added_date_end = util.deserialize_date(added_date_end)
    language = .from_dict(language)
    return web.Response(status=200)
