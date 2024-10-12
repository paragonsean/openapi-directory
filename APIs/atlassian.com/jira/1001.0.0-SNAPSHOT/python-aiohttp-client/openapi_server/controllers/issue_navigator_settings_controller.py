from typing import List, Dict
from aiohttp import web

from openapi_server.models.column_item import ColumnItem
from openapi_server import util


async def get_issue_navigator_default_columns(request: web.Request, ) -> web.Response:
    """Get issue navigator default columns

    Returns the default issue navigator columns.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).


    """
    return web.Response(status=200)


async def set_issue_navigator_default_columns(request: web.Request, body=None) -> web.Response:
    """Set issue navigator default columns

    Sets the default issue navigator columns.  The &#x60;columns&#x60; parameter accepts a navigable field value and is expressed as HTML form data. To specify multiple columns, pass multiple &#x60;columns&#x60; parameters. For example, in curl:  &#x60;curl -X PUT -d columns&#x3D;summary -d columns&#x3D;description https://your-domain.atlassian.net/rest/api/3/settings/columns&#x60;  If no column details are sent, then all default columns are removed.  A navigable field is one that can be used as a column on the issue navigator. Find details of navigable issue columns using [Get fields](#api-rest-api-3-field-get).  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param body: A navigable field value.
    :type body: List[str]

    """
    return web.Response(status=200)
