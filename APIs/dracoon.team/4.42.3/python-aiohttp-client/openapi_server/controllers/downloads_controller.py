from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def download_avatar(request: web.Request, user_id, uuid) -> web.Response:
    """Download avatar

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.11.0&lt;/h3&gt;  ### Description: Download avatar for given user ID and UUID.  ### Precondition: Valid UUID.  ### Postcondition: Stream is returned.  ### Further Information: None.

    :param user_id: User ID
    :type user_id: int
    :param uuid: UUID of the avatar
    :type uuid: str

    """
    return web.Response(status=200)


async def download_file_via_token(request: web.Request, token, range=None, generic_mimetype=None, inline=None) -> web.Response:
    """Download file

    ### Description: Download a file.  ### Precondition: Valid download token.  ### Postcondition: Stream is returned.  ### Further Information: Range requests are supported.

    :param token: Download token
    :type token: str
    :param range: Range   e.g. &#x60;bytes&#x3D;0-999&#x60;
    :type range: str
    :param generic_mimetype: Always return &#x60;application/octet-stream&#x60; instead of specific mimetype
    :type generic_mimetype: bool
    :param inline: Use Content-Disposition: &#x60;inline&#x60; instead of &#x60;attachment&#x60;
    :type inline: bool

    """
    return web.Response(status=200)


async def download_file_via_token1(request: web.Request, token, range=None, generic_mimetype=None, inline=None) -> web.Response:
    """Download file

    ### Description: Download a file.  ### Precondition: Valid download token.  ### Postcondition: Stream is returned.  ### Further Information: Range requests are supported.

    :param token: Download token
    :type token: str
    :param range: Range   e.g. &#x60;bytes&#x3D;0-999&#x60;
    :type range: str
    :param generic_mimetype: Always return &#x60;application/octet-stream&#x60; instead of specific mimetype
    :type generic_mimetype: bool
    :param inline: Use Content-Disposition: &#x60;inline&#x60; instead of &#x60;attachment&#x60;
    :type inline: bool

    """
    return web.Response(status=200)


async def download_zip_archive_via_token(request: web.Request, token) -> web.Response:
    """Download ZIP archive

    ### Description: Download multiple files in a ZIP archive.  ### Precondition: Valid download token.  ### Postcondition: Stream is returned.  ### Further Information: Create a download token with &#x60;POST /nodes/zip&#x60; API.

    :param token: Download token
    :type token: str

    """
    return web.Response(status=200)
