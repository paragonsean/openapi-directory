from typing import List, Dict
from aiohttp import web

from openapi_server.models.screenable_tab import ScreenableTab
from openapi_server import util


async def add_screen_tab(request: web.Request, screen_id, body) -> web.Response:
    """Create screen tab

    Creates a tab for a screen.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param screen_id: The ID of the screen.
    :type screen_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ScreenableTab.from_dict(body)
    return web.Response(status=200)


async def delete_screen_tab(request: web.Request, screen_id, tab_id) -> web.Response:
    """Delete screen tab

    Deletes a screen tab.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param screen_id: The ID of the screen.
    :type screen_id: int
    :param tab_id: The ID of the screen tab.
    :type tab_id: int

    """
    return web.Response(status=200)


async def get_all_screen_tabs(request: web.Request, screen_id, project_key=None) -> web.Response:
    """Get all screen tabs

    Returns the list of tabs for a screen.  **[Permissions](#permissions) required:**   *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).  *  *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) when the project key is specified, providing that the screen is associated with the project through a Screen Scheme and Issue Type Screen Scheme.

    :param screen_id: The ID of the screen.
    :type screen_id: int
    :param project_key: The key of the project.
    :type project_key: str

    """
    return web.Response(status=200)


async def move_screen_tab(request: web.Request, screen_id, tab_id, pos) -> web.Response:
    """Move screen tab

    Moves a screen tab.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param screen_id: The ID of the screen.
    :type screen_id: int
    :param tab_id: The ID of the screen tab.
    :type tab_id: int
    :param pos: The position of tab. The base index is 0.
    :type pos: int

    """
    return web.Response(status=200)


async def rename_screen_tab(request: web.Request, screen_id, tab_id, body) -> web.Response:
    """Update screen tab

    Updates the name of a screen tab.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param screen_id: The ID of the screen.
    :type screen_id: int
    :param tab_id: The ID of the screen tab.
    :type tab_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ScreenableTab.from_dict(body)
    return web.Response(status=200)
