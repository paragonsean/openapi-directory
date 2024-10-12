from typing import List, Dict
from aiohttp import web

from openapi_server.models.download_history_data_list import DownloadHistoryDataList
from openapi_server.models.editorial_video_category_results import EditorialVideoCategoryResults
from openapi_server.models.editorial_video_content import EditorialVideoContent
from openapi_server.models.editorial_video_search_results import EditorialVideoSearchResults
from openapi_server.models.license_editorial_content_results import LicenseEditorialContentResults
from openapi_server.models.license_editorial_video_content_request import LicenseEditorialVideoContentRequest
from openapi_server import util


async def get_editorial_video(request: web.Request, id, country, search_id=None) -> web.Response:
    """Get editorial video content details

    This endpoint shows information about an editorial image, including a URL to a preview image and the sizes that it is available in.

    :param id: Editorial ID
    :type id: str
    :param country: Returns only if the content is available for distribution in a certain country
    :type country: str
    :param search_id: The ID of the search that is related to this request
    :type search_id: str

    """
    return web.Response(status=200)


async def get_editorial_video_license_list(request: web.Request, video_id=None, license=None, page=None, per_page=None, sort=None, username=None, start_date=None, end_date=None, download_availability=None, team_history=None) -> web.Response:
    """List editorial video licenses

    This endpoint lists existing editorial video licenses.

    :param video_id: Show licenses for the specified editorial video ID
    :type video_id: str
    :param license: Show editorial videos that are available with the specified license name
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
    :param download_availability: Filter licenses by download availability
    :type download_availability: str
    :param team_history: Set to true to see license history for all members of your team.
    :type team_history: bool

    """
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    return web.Response(status=200)


async def license_editorial_video(request: web.Request, body) -> web.Response:
    """License editorial video content

    This endpoint gets licenses for one or more editorial videos. You must specify the country and one or more editorial videos to license. The download links in the response are valid for 8 hours.

    :param body: License editorial video content
    :type body: dict | bytes

    """
    body = LicenseEditorialVideoContentRequest.from_dict(body)
    return web.Response(status=200)


async def list_editorial_video_categories(request: web.Request, ) -> web.Response:
    """List editorial video categories

    This endpoint lists the categories that editorial videos can belong to, which are separate from the categories that other types of assets can belong to.


    """
    return web.Response(status=200)


async def search_editorial_videos(request: web.Request, country, query=None, sort=None, category=None, supplier_code=None, date_start=None, date_end=None, resolution=None, fps=None, per_page=None, cursor=None) -> web.Response:
    """Search editorial video content

    This endpoint searches for editorial videos. If you specify more than one search parameter, the API uses an AND condition. For example, if you set the &#x60;category&#x60; parameter to \&quot;Alone,Performing\&quot; and also specify a &#x60;query&#x60; parameter, the results include only videos that match the query and are in both the Alone and Performing categories.  You can also filter search terms out in the &#x60;query&#x60; parameter by prefixing the term with NOT.

    :param country: Show only editorial video content that is available for distribution in a certain country
    :type country: str
    :param query: One or more search terms separated by spaces
    :type query: str
    :param sort: Sort by
    :type sort: str
    :param category: Show editorial content with each of the specified editorial categories; specify category names in a comma-separated list
    :type category: str
    :param supplier_code: Show only editorial video content from certain suppliers
    :type supplier_code: List[str]
    :param date_start: Show only editorial video content generated on or after a specific date
    :type date_start: str
    :param date_end: Show only editorial video content generated on or before a specific date
    :type date_end: str
    :param resolution: Show only editorial video content with specific resolution
    :type resolution: str
    :param fps: Show only editorial video content generated with specific frames per second
    :type fps: 
    :param per_page: Number of results per page
    :type per_page: int
    :param cursor: The cursor of the page with which to start fetching results; this cursor is returned from previous requests
    :type cursor: str

    """
    date_start = util.deserialize_date(date_start)
    date_end = util.deserialize_date(date_end)
    return web.Response(status=200)
