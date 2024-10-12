from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def base_read(request: web.Request, ) -> web.Response:
    """Root

    #### Returns A JSON object with &#x60;meta&#x60; and &#x60;links&#x60; keys.  The &#x60;meta&#x60; key contains information such as a welcome message from the API, the specified version of the request, and the full representation of the current user, if authentication credentials were provided in the request.  The &#x60;links&#x60; key contains links to the following entity collections: [addons](#tag/Addons), [collections](), [institutions](#tag/Institutions), [licenses](#tag/Licenses), [registration schemas](#tag/Registration Schemas), [nodes](#tag/Nodes), [registrations](#tag/Registrations), [users](#tag/Users)


    """
    return web.Response(status=200)
