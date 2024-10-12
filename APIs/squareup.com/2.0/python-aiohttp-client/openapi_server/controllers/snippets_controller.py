from typing import List, Dict
from aiohttp import web

from openapi_server.models.delete_snippet_response import DeleteSnippetResponse
from openapi_server.models.retrieve_snippet_response import RetrieveSnippetResponse
from openapi_server.models.upsert_snippet_request import UpsertSnippetRequest
from openapi_server.models.upsert_snippet_response import UpsertSnippetResponse
from openapi_server import util


async def delete_snippet(request: web.Request, site_id) -> web.Response:
    """DeleteSnippet

    Removes your snippet from a Square Online site.  You can call [ListSites](https://developer.squareup.com/reference/square_2021-08-18/sites-api/list-sites) to get the IDs of the sites that belong to a seller.   __Note:__ Square Online APIs are publicly available as part of an early access program. For more information, see [Early access program for Square Online APIs](https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis).

    :param site_id: The ID of the site that contains the snippet.
    :type site_id: str

    """
    return web.Response(status=200)


async def retrieve_snippet(request: web.Request, site_id) -> web.Response:
    """RetrieveSnippet

    Retrieves your snippet from a Square Online site. A site can contain snippets from multiple snippet applications, but you can retrieve only the snippet that was added by your application.  You can call [ListSites](https://developer.squareup.com/reference/square_2021-08-18/sites-api/list-sites) to get the IDs of the sites that belong to a seller.   __Note:__ Square Online APIs are publicly available as part of an early access program. For more information, see [Early access program for Square Online APIs](https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis).

    :param site_id: The ID of the site that contains the snippet.
    :type site_id: str

    """
    return web.Response(status=200)


async def upsert_snippet(request: web.Request, site_id, body) -> web.Response:
    """UpsertSnippet

    Adds a snippet to a Square Online site or updates the existing snippet on the site.  The snippet code is appended to the end of the &#x60;head&#x60; element on every page of the site, except checkout pages. A snippet application can add one snippet to a given site.   You can call [ListSites](https://developer.squareup.com/reference/square_2021-08-18/sites-api/list-sites) to get the IDs of the sites that belong to a seller.   __Note:__ Square Online APIs are publicly available as part of an early access program. For more information, see [Early access program for Square Online APIs](https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis).

    :param site_id: The ID of the site where you want to add or update the snippet.
    :type site_id: str
    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = UpsertSnippetRequest.from_dict(body)
    return web.Response(status=200)
