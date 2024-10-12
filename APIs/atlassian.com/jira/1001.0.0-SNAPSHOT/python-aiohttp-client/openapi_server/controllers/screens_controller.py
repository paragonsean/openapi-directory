from typing import List, Dict
from aiohttp import web

from openapi_server.models.page_bean_screen import PageBeanScreen
from openapi_server.models.page_bean_screen_with_tab import PageBeanScreenWithTab
from openapi_server.models.screen import Screen
from openapi_server.models.screen_details import ScreenDetails
from openapi_server.models.screenable_field import ScreenableField
from openapi_server.models.update_screen_details import UpdateScreenDetails
from openapi_server import util


async def add_field_to_default_screen(request: web.Request, field_id) -> web.Response:
    """Add field to default screen

    Adds a field to the default tab of the default screen.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param field_id: The ID of the field.
    :type field_id: str

    """
    return web.Response(status=200)


async def create_screen(request: web.Request, body) -> web.Response:
    """Create screen

    Creates a screen with a default field tab.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param body: 
    :type body: dict | bytes

    """
    body = ScreenDetails.from_dict(body)
    return web.Response(status=200)


async def delete_screen(request: web.Request, screen_id) -> web.Response:
    """Delete screen

    Deletes a screen. A screen cannot be deleted if it is used in a screen scheme, workflow, or workflow draft.  Only screens used in classic projects can be deleted.

    :param screen_id: The ID of the screen.
    :type screen_id: int

    """
    return web.Response(status=200)


async def get_available_screen_fields(request: web.Request, screen_id) -> web.Response:
    """Get available screen fields

    Returns the fields that can be added to a tab on a screen.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param screen_id: The ID of the screen.
    :type screen_id: int

    """
    return web.Response(status=200)


async def get_screens(request: web.Request, start_at=None, max_results=None, id=None, query_string=None, scope=None, order_by=None) -> web.Response:
    """Get screens

    Returns a [paginated](#pagination) list of all screens or those specified by one or more screen IDs.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param start_at: The index of the first item to return in a page of results (page offset).
    :type start_at: int
    :param max_results: The maximum number of items to return per page.
    :type max_results: int
    :param id: The list of screen IDs. To include multiple IDs, provide an ampersand-separated list. For example, &#x60;id&#x3D;10000&amp;id&#x3D;10001&#x60;.
    :type id: List[int]
    :param query_string: String used to perform a case-insensitive partial match with screen name.
    :type query_string: str
    :param scope: The scope filter string. To filter by multiple scope, provide an ampersand-separated list. For example, &#x60;scope&#x3D;GLOBAL&amp;scope&#x3D;PROJECT&#x60;.
    :type scope: List[str]
    :param order_by: [Order](#ordering) the results by a field:   *  &#x60;id&#x60; Sorts by screen ID.  *  &#x60;name&#x60; Sorts by screen name.
    :type order_by: str

    """
    return web.Response(status=200)


async def get_screens_for_field(request: web.Request, field_id, start_at=None, max_results=None, expand=None) -> web.Response:
    """Get screens for a field

    Returns a [paginated](#pagination) list of the screens a field is used in.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param field_id: The ID of the field to return screens for.
    :type field_id: str
    :param start_at: The index of the first item to return in a page of results (page offset).
    :type start_at: int
    :param max_results: The maximum number of items to return per page.
    :type max_results: int
    :param expand: Use [expand](#expansion) to include additional information about screens in the response. This parameter accepts &#x60;tab&#x60; which returns details about the screen tabs the field is used in.
    :type expand: str

    """
    return web.Response(status=200)


async def update_screen(request: web.Request, screen_id, body) -> web.Response:
    """Update screen

    Updates a screen. Only screens used in classic projects can be updated.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param screen_id: The ID of the screen.
    :type screen_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateScreenDetails.from_dict(body)
    return web.Response(status=200)
