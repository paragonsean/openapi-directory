from typing import List, Dict
from aiohttp import web

from openapi_server.models.library_response import LibraryResponse
from openapi_server import util


async def get_library(request: web.Request, organization_uuid, event_log_uuid=None, limit=None, offset=None, all=None) -> web.Response:
    """Retrieve the entire library

    Will return the entire library for the authenticated user. If size of the library exceeds server preferences (normally 500) or the value of the optional limit parameter, the result will be paginated. Paginated responses return a Link header, indicating the next URI to fetch. The resulting header value will look something like:  &lt;https://products.izettle.com/organizations/self/library?limit&#x3D;X&amp;offset&#x3D;Y&gt;; rel&#x3D;\&quot;next\&quot;  where limit is number of items in response, and offset is the current position in pagination. The rel-part in the header is the links relation to the data previously recieved. The idea is that as long as this header is present there are still items remaining to be fetched. When either the header is not present or it&#39;s value doesn&#39;t contain any \&quot;next\&quot; value, all items have been sent to the client.  Note: The client should NOT try to extract query parameters from the URI, but rather use it as-is for the next request. Also, clients should be perpared that one Link header might contain multiple other IRIs that are not \&quot;next\&quot; (there will never be more than one \&quot;next\&quot; though). See more at:      IETF: https://tools.ietf.org/html/rfc5988     GitHub: https://developer.github.com/guides/traversing-with-pagination/  If eventLogUuid is provided, the response will only include events affecting the library since that event. Such responses are normally quite small and would be a preferred method for most fat clients after retrieving the initial full library. 

    :param organization_uuid: 
    :type organization_uuid: str
    :type organization_uuid: str
    :param event_log_uuid: 
    :type event_log_uuid: str
    :type event_log_uuid: str
    :param limit: 
    :type limit: int
    :param offset: 
    :type offset: str
    :param all: 
    :type all: bool

    """
    return web.Response(status=200)
