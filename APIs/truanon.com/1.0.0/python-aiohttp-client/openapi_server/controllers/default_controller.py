from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_profile(request: web.Request, id=None, service=None) -> web.Response:
    """Get Profile

    get_profile Private API: Request confirmed profile data for your unique member ID

    :param id: This is your unique username or member ID
    :type id: str
    :param service: The service name given to you by TruAnon
    :type service: str

    """
    return web.Response(status=200)


async def get_token(request: web.Request, id=None, service=None) -> web.Response:
    """Get Token

    request_token Private API: Request a Proof token to let the member confirm in a popup interface          {\&quot;id\&quot;:\&quot;qjgblv72bzzio\&quot;,\&quot;type\&quot;:\&quot;Proof\&quot;,\&quot;active\&quot;:true,\&quot;name\&quot;:\&quot;New Proof\&quot;}  Step 2. Create a verifyProfile Public Web link: Use the Proof token id as the token argument in your public URL used to open a new target popup. This activity is where members may confirm immediately.              https://staging.truanon.com/verifyProfile?id&#x3D;john_doe&amp;service&#x3D;securecannabisalliance&amp;token&#x3D;qjgblv72bzzio

    :param id: This is your unique username or member ID
    :type id: str
    :param service: The service name given to you by TruAnon
    :type service: str

    """
    return web.Response(status=200)
