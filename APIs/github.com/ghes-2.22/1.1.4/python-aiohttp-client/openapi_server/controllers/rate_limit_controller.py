from typing import List, Dict
from aiohttp import web

from openapi_server.models.basic_error import BasicError
from openapi_server.models.rate_limit_overview import RateLimitOverview
from openapi_server import util


async def rate_limit_get(request: web.Request, ) -> web.Response:
    """Get rate limit status for the authenticated user

    **Note:** Accessing this endpoint does not count against your REST API rate limit.  **Note:** The &#x60;rate&#x60; object is deprecated. If you&#39;re writing new API client code or updating existing code, you should use the &#x60;core&#x60; object instead of the &#x60;rate&#x60; object. The &#x60;core&#x60; object contains the same information that is present in the &#x60;rate&#x60; object.


    """
    return web.Response(status=200)
