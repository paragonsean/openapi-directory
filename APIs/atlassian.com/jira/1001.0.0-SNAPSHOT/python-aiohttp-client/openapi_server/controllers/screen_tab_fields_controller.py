from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_field_bean import AddFieldBean
from openapi_server.models.move_field_bean import MoveFieldBean
from openapi_server.models.screenable_field import ScreenableField
from openapi_server import util


async def add_screen_tab_field(request: web.Request, screen_id, tab_id, body) -> web.Response:
    """Add screen tab field

    Adds a field to a screen tab.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param screen_id: The ID of the screen.
    :type screen_id: int
    :param tab_id: The ID of the screen tab.
    :type tab_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = AddFieldBean.from_dict(body)
    return web.Response(status=200)


async def get_all_screen_tab_fields(request: web.Request, screen_id, tab_id, project_key=None) -> web.Response:
    """Get all screen tab fields

    Returns all fields for a screen tab.  **[Permissions](#permissions) required:**   *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).  *  *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) when the project key is specified, providing that the screen is associated with the project through a Screen Scheme and Issue Type Screen Scheme.

    :param screen_id: The ID of the screen.
    :type screen_id: int
    :param tab_id: The ID of the screen tab.
    :type tab_id: int
    :param project_key: The key of the project.
    :type project_key: str

    """
    return web.Response(status=200)


async def move_screen_tab_field(request: web.Request, screen_id, tab_id, id, body) -> web.Response:
    """Move screen tab field

    Moves a screen tab field.  If &#x60;after&#x60; and &#x60;position&#x60; are provided in the request, &#x60;position&#x60; is ignored.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param screen_id: The ID of the screen.
    :type screen_id: int
    :param tab_id: The ID of the screen tab.
    :type tab_id: int
    :param id: The ID of the field.
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = MoveFieldBean.from_dict(body)
    return web.Response(status=200)


async def remove_screen_tab_field(request: web.Request, screen_id, tab_id, id) -> web.Response:
    """Remove screen tab field

    Removes a field from a screen tab.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param screen_id: The ID of the screen.
    :type screen_id: int
    :param tab_id: The ID of the screen tab.
    :type tab_id: int
    :param id: The ID of the field.
    :type id: str

    """
    return web.Response(status=200)
