from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_segment(request: web.Request, ) -> web.Response:
    """Get Segment

    You can add certain public fields in the query string and the system will attempt to fulfill it. Values such as &#x60;cultureInfo&#x60; and &#x60;utm&#x60; are overwriteable, just keep in mind such changes will not be reflected in the client&#39;s session.    If you wish to change the value on the session (and thus be reflected on the segment without special query strings), then use the PATCH request to session.


    """
    return web.Response(status=200)
