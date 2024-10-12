from typing import List, Dict
from aiohttp import web

from openapi_server.models.comment import Comment
from openapi_server import util


async def comments_delete(request: web.Request, comment_id) -> web.Response:
    """Delete a comment

    Deletes a comment. This action can be undone by setting deleted to False in a comment update request. #### Returns If the request is successful, no content is returned.  If the request is unsuccessful, a JSON object with an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

    :param comment_id: The unique identifier of the comment you wish to delete.
    :type comment_id: str

    """
    return web.Response(status=200)


async def comments_put(request: web.Request, comment_id, body) -> web.Response:
    """Update a comment

    Updates the specified comment by setting the values of the parameters passed. Any parameters not provided will be left unchanged. #### Returns Returns JSON with a &#x60;data&#x60; key containing the new representation of the updated comment, if the request is successful.  If the request is unsuccessful, JSON with an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

    :param comment_id: The unique identifier of the comment you wish to update.
    :type comment_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def comments_read(request: web.Request, comment_id) -> web.Response:
    """Retrieve a comment

    Retrieves the details of a comment #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested comment, if the request was successful.  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

    :param comment_id: The unique identifier of the comment you wish to retrieve.
    :type comment_id: str

    """
    return web.Response(status=200)
