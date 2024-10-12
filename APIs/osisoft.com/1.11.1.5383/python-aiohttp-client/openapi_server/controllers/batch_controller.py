from typing import List, Dict
from aiohttp import web

from openapi_server.models.request import Request
from openapi_server.models.response import Response
from openapi_server import util


async def batch_execute(request: web.Request, batch) -> web.Response:
    """Execute a batch of requests against the service. As shown in the Sample Request, the input is a dictionary with IDs as keys and request objects as values. Each request object specifies the HTTP method and the resource and, optionally, the content and a list of parent IDs. The list of parent IDs specifies which other requests must complete before the given request will be executed. The example first creates an element, then gets the element by the response&#39;s Location header, then creates an attribute for the element. Note that the resource can be an absolute URL or a JsonPath that references the response to the parent request. The batch&#39;s response is a dictionary uses keys corresponding those provided in the request, with response objects containing a status code, response headers, and the response body. A request can alternatively specify a request template in place of a resource. In this case, a single JsonPath may select multiple tokens, and a separate subrequest will be made from the template for each token. The responses of these subrequests will returned as the content of a single outer response.

    

    :param batch: The batch of requests.
    :type batch: dict | bytes

    """
    batch = {k: Request.from_dict(v) for k, v in batch}
    return web.Response(status=200)
