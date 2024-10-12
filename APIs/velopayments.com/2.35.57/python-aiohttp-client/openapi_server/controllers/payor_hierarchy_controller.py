from typing import List, Dict
from aiohttp import web

from openapi_server.models.inline_response400 import InlineResponse400
from openapi_server.models.inline_response403 import InlineResponse403
from openapi_server.models.inline_response404 import InlineResponse404
from openapi_server.models.payor_links_response import PayorLinksResponse
from openapi_server import util


async def payor_links_v1(request: web.Request, descendants_of_payor=None, parent_of_payor=None, fields=None) -> web.Response:
    """List Payor Links

    &lt;p&gt;If the payor is set up as part of a hierarchy you can use this API to traverse the hierarchy&lt;/p&gt; 

    :param descendants_of_payor: The Payor ID from which to start the query to show all descendants
    :type descendants_of_payor: str
    :type descendants_of_payor: str
    :param parent_of_payor: Query for the parent payor details for this payor id
    :type parent_of_payor: str
    :type parent_of_payor: str
    :param fields: &lt;p&gt;List of additional Payor fields to include in the response for each Payor&lt;/p&gt; &lt;p&gt;The values of payorId and payorName are always included for each Payor by default&lt;/p&gt; &lt;p&gt;You can add fields to the response for each payor by including them in the fields parameter separated by commas&lt;/p&gt; &lt;p&gt;The supported fields are any combination of: primaryContactEmail,kycState&lt;/p&gt; 
    :type fields: str

    """
    return web.Response(status=200)
