from typing import List, Dict
from aiohttp import web

from openapi_server.models.taxonomy import Taxonomy
from openapi_server import util


async def taxonomies_list(request: web.Request, ) -> web.Response:
    """List all taxonomies

     A paginated list of all [bepress disciplines taxonomies](https://www.bepress.com/wp-content/uploads/2016/12/Digital-Commons-Disciplines-taxonomy-2017-01.pdf). Note: this API endpoint is under active development, and is subject to change in the future. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of up to 10 taxonomies. Each resource in the array is a separate taxonomy object.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  This request should never return an error. #### Filtering You can optionally request that the response only include taxonomies that match your filters by utilizing the &#x60;filter&#x60; query parameter, e.g. https://api.osf.io/v2/taxonomies/?filter[&#39;id&#39;]&#x3D;&#39;{taxonomy_id}&#39;.  Taxonomies may be filtered by their &#x60;id&#x60;, &#x60;parents&#x60;, and &#x60;text&#x60;.


    """
    return web.Response(status=200)


async def taxonomies_read(request: web.Request, taxonomy_id) -> web.Response:
    """Retrieve a taxonomy

    Retrieves the details of a taxonomy. #### Returns  Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested taxonomy, if the request is successful.  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

    :param taxonomy_id: The unique identifier of the taxonomy.
    :type taxonomy_id: str

    """
    return web.Response(status=200)
