from typing import List, Dict
from aiohttp import web

from openapi_server.models.wiki import Wiki
from openapi_server import util


async def wiki_content(request: web.Request, wiki_id) -> web.Response:
    """Retrieve the Content of a Wiki

    Retrieves the plaintext content of a wiki in markdown format. #### Returns Returns &#x60;text/markdown&#x60; of the wiki content itself. If the request is unsuccessful, plaintext with the error message will be displayed.

    :param wiki_id: The unique identifier of the wiki.
    :type wiki_id: str

    """
    return web.Response(status=200)


async def wiki_read(request: web.Request, wiki_id) -> web.Response:
    """Retrieve a Wiki

    Retrieves the details about a specific wiki. A wiki is a collection of markdown text pages that can be used to describe the project or dataset of contained in the attached node. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested wiki, if the request was successful.  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

    :param wiki_id: The unique identifier of the wiki.
    :type wiki_id: str

    """
    return web.Response(status=200)
