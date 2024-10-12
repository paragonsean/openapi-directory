from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_subject(request: web.Request, identifier) -> web.Response:
    """Explore details about a given subject node

    Gets information about a &#x60;subject&#x60; identified by the &#x60;identifier&#x60;.  The response format depends upon the &#x60;Accept&#x60; header.   - &#x60;text/html&#x60; - the default response type. Returned data can be easily viewed in any modern Internet Browser   - &#x60;application/ld+json&#x60; - the response will be in [JSON-LD](http://json-ld.org/)   - &#x60;application/json&#x60; - the response will be a simple JSON Object with keys (predicates) and values (objects). 

    :param identifier: The identifier path of the &#x60;subject&#x60; you&#39;re looking for 
    :type identifier: str

    """
    return web.Response(status=200)
