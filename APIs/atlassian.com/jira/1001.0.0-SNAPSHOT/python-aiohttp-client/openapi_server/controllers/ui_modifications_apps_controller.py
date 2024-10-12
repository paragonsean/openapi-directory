from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_ui_modification_details import CreateUiModificationDetails
from openapi_server.models.page_bean_ui_modification_details import PageBeanUiModificationDetails
from openapi_server.models.ui_modification_identifiers import UiModificationIdentifiers
from openapi_server.models.update_ui_modification_details import UpdateUiModificationDetails
from openapi_server import util


async def create_ui_modification(request: web.Request, body) -> web.Response:
    """Create UI modification

    Creates a UI modification. UI modification can only be created by Forge apps.  Each app can define up to 100 UI modifications. Each UI modification can define up to 1000 contexts.  **[Permissions](#permissions) required:**   *  *None* if the UI modification is created without contexts.  *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for one or more projects, if the UI modification is created with contexts.

    :param body: Details of the UI modification.
    :type body: dict | bytes

    """
    body = CreateUiModificationDetails.from_dict(body)
    return web.Response(status=200)


async def delete_ui_modification(request: web.Request, ui_modification_id) -> web.Response:
    """Delete UI modification

    Deletes a UI modification. All the contexts that belong to the UI modification are deleted too. UI modification can only be deleted by Forge apps.  **[Permissions](#permissions) required:** None.

    :param ui_modification_id: The ID of the UI modification.
    :type ui_modification_id: str

    """
    return web.Response(status=200)


async def get_ui_modifications(request: web.Request, start_at=None, max_results=None, expand=None) -> web.Response:
    """Get UI modifications

    Gets UI modifications. UI modifications can only be retrieved by Forge apps.  **[Permissions](#permissions) required:** None.

    :param start_at: The index of the first item to return in a page of results (page offset).
    :type start_at: int
    :param max_results: The maximum number of items to return per page.
    :type max_results: int
    :param expand: Use expand to include additional information in the response. This parameter accepts a comma-separated list. Expand options include:   *  &#x60;data&#x60; Returns UI modification data.  *  &#x60;contexts&#x60; Returns UI modification contexts.
    :type expand: str

    """
    return web.Response(status=200)


async def update_ui_modification(request: web.Request, ui_modification_id, body) -> web.Response:
    """Update UI modification

    Updates a UI modification. UI modification can only be updated by Forge apps.  Each UI modification can define up to 1000 contexts.  **[Permissions](#permissions) required:**   *  *None* if the UI modification is created without contexts.  *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for one or more projects, if the UI modification is created with contexts.

    :param ui_modification_id: The ID of the UI modification.
    :type ui_modification_id: str
    :param body: Details of the UI modification.
    :type body: dict | bytes

    """
    body = UpdateUiModificationDetails.from_dict(body)
    return web.Response(status=200)
