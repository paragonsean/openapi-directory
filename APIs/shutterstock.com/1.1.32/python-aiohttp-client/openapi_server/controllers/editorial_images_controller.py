from typing import List, Dict
from aiohttp import web

from openapi_server.models.download_history_data_list import DownloadHistoryDataList
from openapi_server.models.editorial_category_results import EditorialCategoryResults
from openapi_server.models.editorial_content import EditorialContent
from openapi_server.models.editorial_content_data_list import EditorialContentDataList
from openapi_server.models.editorial_image_category_results import EditorialImageCategoryResults
from openapi_server.models.editorial_image_content_data_list import EditorialImageContentDataList
from openapi_server.models.editorial_image_livefeed import EditorialImageLivefeed
from openapi_server.models.editorial_image_livefeed_list import EditorialImageLivefeedList
from openapi_server.models.editorial_livefeed import EditorialLivefeed
from openapi_server.models.editorial_livefeed_list import EditorialLivefeedList
from openapi_server.models.editorial_search_results import EditorialSearchResults
from openapi_server.models.editorial_updated_results import EditorialUpdatedResults
from openapi_server.models.license_editorial_content_request import LicenseEditorialContentRequest
from openapi_server.models.license_editorial_content_results import LicenseEditorialContentResults
from openapi_server import util


async def get_editorial_categories(request: web.Request, ) -> web.Response:
    """(Deprecated) List editorial categories

    Deprecated; use &#x60;GET /v2/editorial/images/categories&#x60; instead. This endpoint lists the categories that editorial images can belong to, which are separate from the categories that other types of assets can belong to.


    """
    return web.Response(status=200)


async def get_editorial_image(request: web.Request, id, country) -> web.Response:
    """Get editorial content details

    This endpoint shows information about an editorial image, including a URL to a preview image and the sizes that it is available in.

    :param id: Editorial ID
    :type id: str
    :param country: Returns only if the content is available for distribution in a certain country
    :type country: str

    """
    return web.Response(status=200)


async def get_editorial_image_license_list(request: web.Request, image_id=None, license=None, page=None, per_page=None, sort=None, username=None, start_date=None, end_date=None, download_availability=None, team_history=None) -> web.Response:
    """List editorial image licenses

    This endpoint lists existing editorial image licenses.

    :param image_id: Show licenses for the specified editorial image ID
    :type image_id: str
    :param license: Show editorial images that are available with the specified license name
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


async def get_editorial_image_livefeed(request: web.Request, id, country) -> web.Response:
    """Get editorial livefeed

    

    :param id: Editorial livefeed ID; must be an URI encoded string
    :type id: str
    :param country: Returns only if the livefeed is available for distribution in a certain country
    :type country: str

    """
    return web.Response(status=200)


async def get_editorial_image_livefeed_items(request: web.Request, id, country) -> web.Response:
    """Get editorial livefeed items

    

    :param id: Editorial livefeed ID; must be an URI encoded string
    :type id: str
    :param country: Returns only if the livefeed items are available for distribution in a certain country
    :type country: str

    """
    return web.Response(status=200)


async def get_editorial_image_livefeed_list(request: web.Request, country, page=None, per_page=None) -> web.Response:
    """Get editorial livefeed list

    

    :param country: Returns only livefeeds that are available for distribution in a certain country
    :type country: str
    :param page: Page number
    :type page: int
    :param per_page: Number of results per page
    :type per_page: int

    """
    return web.Response(status=200)


async def get_editorial_livefeed(request: web.Request, id, country) -> web.Response:
    """(Deprecated) Get editorial livefeed

    Deprecated: use &#x60;GET /v2/editorial/images/livefeeds/{id}&#x60; instead to get an editorial livefeed.

    :param id: Editorial livefeed ID; must be an URI encoded string
    :type id: str
    :param country: Returns only if the livefeed is available for distribution in a certain country
    :type country: str

    """
    return web.Response(status=200)


async def get_editorial_livefeed_items(request: web.Request, id, country) -> web.Response:
    """(Deprecated) Get editorial livefeed items

    Deprecated; use &#x60;GET /v2/editorial/images/livefeeds/{id}/items&#x60; instead to get editorial livefeed items.

    :param id: Editorial livefeed ID; must be an URI encoded string
    :type id: str
    :param country: Returns only if the livefeed items are available for distribution in a certain country
    :type country: str

    """
    return web.Response(status=200)


async def get_editorial_livefeed_list(request: web.Request, country, page=None, per_page=None) -> web.Response:
    """(Deprecated) Get editorial livefeed list

    Deprecated; use &#x60;GET /v2/editorial/images/livefeeds&#x60; instead to get a list of editorial livefeeds.

    :param country: Returns only livefeeds that are available for distribution in a certain country
    :type country: str
    :param page: Page number
    :type page: int
    :param per_page: Number of results per page
    :type per_page: int

    """
    return web.Response(status=200)


async def get_updated_editorial_image(request: web.Request, type, date_updated_start, date_updated_end, country, date_taken_start=None, date_taken_end=None, cursor=None, sort=None, supplier_code=None, per_page=None) -> web.Response:
    """(Deprecated) List updated content

    Deprecated; use &#x60;GET /v2/editorial/images/updated&#x60; instead to get recently updated items.

    :param type: Specify &#x60;addition&#x60; to return only images that were added or &#x60;edit&#x60; to return only images that were edited or deleted
    :type type: str
    :param date_updated_start: Show images images added, edited, or deleted after the specified date. Acceptable range is 1970-01-01T00:00:01 to 2038-01-19T00:00:00.
    :type date_updated_start: str
    :param date_updated_end: Show images images added, edited, or deleted before the specified date. Acceptable range is 1970-01-01T00:00:01 to 2038-01-19T00:00:00.
    :type date_updated_end: str
    :param country: Show only editorial content that is available for distribution in a certain country
    :type country: str
    :param date_taken_start: Show images that were taken on or after the specified date; use this parameter if you want recently created images from the collection instead of updated older assets
    :type date_taken_start: str
    :param date_taken_end: Show images that were taken before the specified date
    :type date_taken_end: str
    :param cursor: The cursor of the page with which to start fetching results; this cursor is returned from previous requests
    :type cursor: str
    :param sort: Sort by
    :type sort: str
    :param supplier_code: Show only editorial content from certain suppliers
    :type supplier_code: List[str]
    :param per_page: Number of results per page
    :type per_page: int

    """
    date_updated_start = util.deserialize_datetime(date_updated_start)
    date_updated_end = util.deserialize_datetime(date_updated_end)
    date_taken_start = util.deserialize_date(date_taken_start)
    date_taken_end = util.deserialize_date(date_taken_end)
    return web.Response(status=200)


async def get_updated_editorial_images(request: web.Request, type, date_updated_start, date_updated_end, country, date_taken_start=None, date_taken_end=None, cursor=None, sort=None, supplier_code=None, per_page=None) -> web.Response:
    """List updated content

    This endpoint lists editorial images that have been updated in the specified time period to update content management systems (CMS) or digital asset management (DAM) systems. In most cases, use the date_updated_start and date_updated_end parameters to specify a range updates based on when the updates happened. You can also use the date_taken_start and date_taken_end parameters to specify a range of updates based on when the image was taken.

    :param type: Specify &#x60;addition&#x60; to return only images that were added or &#x60;edit&#x60; to return only images that were edited or deleted
    :type type: str
    :param date_updated_start: Show images images added, edited, or deleted after the specified date. Acceptable range is 1970-01-01T00:00:01 to 2038-01-19T00:00:00.
    :type date_updated_start: str
    :param date_updated_end: Show images images added, edited, or deleted before the specified date. Acceptable range is 1970-01-01T00:00:01 to 2038-01-19T00:00:00.
    :type date_updated_end: str
    :param country: Show only editorial content that is available for distribution in a certain country
    :type country: str
    :param date_taken_start: Show images that were taken on or after the specified date; use this parameter if you want recently created images from the collection instead of updated older assets
    :type date_taken_start: str
    :param date_taken_end: Show images that were taken before the specified date
    :type date_taken_end: str
    :param cursor: The cursor of the page with which to start fetching results; this cursor is returned from previous requests
    :type cursor: str
    :param sort: Sort by
    :type sort: str
    :param supplier_code: Show only editorial content from certain suppliers
    :type supplier_code: List[str]
    :param per_page: Number of results per page
    :type per_page: int

    """
    date_updated_start = util.deserialize_datetime(date_updated_start)
    date_updated_end = util.deserialize_datetime(date_updated_end)
    date_taken_start = util.deserialize_date(date_taken_start)
    date_taken_end = util.deserialize_date(date_taken_end)
    return web.Response(status=200)


async def license_editorial_image(request: web.Request, body) -> web.Response:
    """(Deprecated) License editorial content

    Deprecated; use &#x60;POST /v2/editorial/images/licenses&#x60; instead to get licenses for one or more editorial images. You must specify the country and one or more editorial images to license. The download links in the response are valid for 8 hours.

    :param body: License editorial content
    :type body: dict | bytes

    """
    body = LicenseEditorialContentRequest.from_dict(body)
    return web.Response(status=200)


async def license_editorial_images(request: web.Request, body) -> web.Response:
    """License editorial content

    This endpoint gets licenses for one or more editorial images. You must specify the country and one or more editorial images to license. The download links in the response are valid for 8 hours.

    :param body: License editorial content
    :type body: dict | bytes

    """
    body = LicenseEditorialContentRequest.from_dict(body)
    return web.Response(status=200)


async def list_editorial_image_categories(request: web.Request, ) -> web.Response:
    """List editorial categories

    This endpoint lists the categories that editorial images can belong to, which are separate from the categories that other types of assets can belong to.


    """
    return web.Response(status=200)


async def search_editorial(request: web.Request, country, query=None, sort=None, category=None, supplier_code=None, date_start=None, date_end=None, per_page=None, cursor=None) -> web.Response:
    """(Deprecated) Search editorial content

    Deprecated; use &#x60;GET /v2/editorial/images/search&#x60; instead to search for editorial images.

    :param country: Show only editorial content that is available for distribution in a certain country
    :type country: str
    :param query: One or more search terms separated by spaces
    :type query: str
    :param sort: Sort by
    :type sort: str
    :param category: Show editorial content within a certain editorial category; specify by category name
    :type category: str
    :param supplier_code: Show only editorial content from certain suppliers
    :type supplier_code: List[str]
    :param date_start: Show only editorial content generated on or after a specific date
    :type date_start: str
    :param date_end: Show only editorial content generated on or before a specific date
    :type date_end: str
    :param per_page: Number of results per page
    :type per_page: int
    :param cursor: The cursor of the page with which to start fetching results; this cursor is returned from previous requests
    :type cursor: str

    """
    date_start = util.deserialize_date(date_start)
    date_end = util.deserialize_date(date_end)
    return web.Response(status=200)


async def search_editorial_images(request: web.Request, country, query=None, sort=None, category=None, supplier_code=None, date_start=None, date_end=None, per_page=None, cursor=None) -> web.Response:
    """Search editorial images

    This endpoint searches for editorial images. If you specify more than one search parameter, the API uses an AND condition. For example, if you set the &#x60;category&#x60; parameter to \&quot;Alone,Performing\&quot; and also specify a &#x60;query&#x60; parameter, the results include only images that match the query and are in both the Alone and Performing categories. You can also filter search terms out in the &#x60;query&#x60; parameter by prefixing the term with NOT.

    :param country: Show only editorial content that is available for distribution in a certain country
    :type country: str
    :param query: One or more search terms separated by spaces
    :type query: str
    :param sort: Sort by
    :type sort: str
    :param category: Show editorial content with each of the specified editorial categories; specify category names in a comma-separated list
    :type category: str
    :param supplier_code: Show only editorial content from certain suppliers
    :type supplier_code: List[str]
    :param date_start: Show only editorial content generated on or after a specific date
    :type date_start: str
    :param date_end: Show only editorial content generated on or before a specific date
    :type date_end: str
    :param per_page: Number of results per page
    :type per_page: int
    :param cursor: The cursor of the page with which to start fetching results; this cursor is returned from previous requests
    :type cursor: str

    """
    date_start = util.deserialize_date(date_start)
    date_end = util.deserialize_date(date_end)
    return web.Response(status=200)


async def v2_editorial_id_get(request: web.Request, id, country, search_id=None) -> web.Response:
    """(Deprecated) Get editorial content details

    Deprecated; use &#x60;GET /v2/editorial/images/{id}&#x60; instead to show information about an editorial image, including a URL to a preview image and the sizes that it is available in.

    :param id: Editorial ID
    :type id: str
    :param country: Returns only if the content is available for distribution in a certain country
    :type country: str
    :param search_id: The ID of the search that is related to this request
    :type search_id: str

    """
    return web.Response(status=200)
