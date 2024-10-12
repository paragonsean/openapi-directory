from typing import List, Dict
from aiohttp import web

from openapi_server.models.page_bean_screen_scheme import PageBeanScreenScheme
from openapi_server.models.screen_scheme_details import ScreenSchemeDetails
from openapi_server.models.screen_scheme_id import ScreenSchemeId
from openapi_server.models.update_screen_scheme_details import UpdateScreenSchemeDetails
from openapi_server import util


async def create_screen_scheme(request: web.Request, body) -> web.Response:
    """Create screen scheme

    Creates a screen scheme.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param body: 
    :type body: dict | bytes

    """
    body = ScreenSchemeDetails.from_dict(body)
    return web.Response(status=200)


async def delete_screen_scheme(request: web.Request, screen_scheme_id) -> web.Response:
    """Delete screen scheme

    Deletes a screen scheme. A screen scheme cannot be deleted if it is used in an issue type screen scheme.  Only screens schemes used in classic projects can be deleted.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param screen_scheme_id: The ID of the screen scheme.
    :type screen_scheme_id: str

    """
    return web.Response(status=200)


async def get_screen_schemes(request: web.Request, start_at=None, max_results=None, id=None, expand=None, query_string=None, order_by=None) -> web.Response:
    """Get screen schemes

    Returns a [paginated](#pagination) list of screen schemes.  Only screen schemes used in classic projects are returned.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param start_at: The index of the first item to return in a page of results (page offset).
    :type start_at: int
    :param max_results: The maximum number of items to return per page.
    :type max_results: int
    :param id: The list of screen scheme IDs. To include multiple IDs, provide an ampersand-separated list. For example, &#x60;id&#x3D;10000&amp;id&#x3D;10001&#x60;.
    :type id: List[int]
    :param expand: Use [expand](#expansion) include additional information in the response. This parameter accepts &#x60;issueTypeScreenSchemes&#x60; that, for each screen schemes, returns information about the issue type screen scheme the screen scheme is assigned to.
    :type expand: str
    :param query_string: String used to perform a case-insensitive partial match with screen scheme name.
    :type query_string: str
    :param order_by: [Order](#ordering) the results by a field:   *  &#x60;id&#x60; Sorts by screen scheme ID.  *  &#x60;name&#x60; Sorts by screen scheme name.
    :type order_by: str

    """
    return web.Response(status=200)


async def update_screen_scheme(request: web.Request, screen_scheme_id, body) -> web.Response:
    """Update screen scheme

    Updates a screen scheme. Only screen schemes used in classic projects can be updated.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param screen_scheme_id: The ID of the screen scheme.
    :type screen_scheme_id: str
    :param body: The screen scheme update details.
    :type body: dict | bytes

    """
    body = UpdateScreenSchemeDetails.from_dict(body)
    return web.Response(status=200)
