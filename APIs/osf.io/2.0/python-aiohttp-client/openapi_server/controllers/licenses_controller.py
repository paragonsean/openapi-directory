from typing import List, Dict
from aiohttp import web

from openapi_server.models.license import License
from openapi_server import util


async def license_list(request: web.Request, ) -> web.Response:
    """List all licenses

    A paginated list of licenses. The returned licenses are sorted by their name. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys. The &#x60;data&#x60; key contains an array of 10 licenses. Each resource in the array is a separate license object and contains the full representation of the license, meaning additional requests to a license&#39;s detail view are not necessary.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  This request should never return an error. #### Filtering You can optionally request that the response only include licenses that match your filters by utilizing the &#x60;filter&#x60; query parameter, e.g. [https://api.osf.io/v2/licenses/?filter[name]&#x3D;apache](https://api.osf.io/v2/licenses/?filter[name]&#x3D;apache).  Licenses may be filtered by their &#x60;id&#x60;, and &#x60;name&#x60;.


    """
    return web.Response(status=200)


async def licenses_read(request: web.Request, license_id) -> web.Response:
    """Retrieve a license

    Retrieves the details of a license. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested license, if the request is successful.  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

    :param license_id: The unique identifier of the license.
    :type license_id: str

    """
    return web.Response(status=200)
