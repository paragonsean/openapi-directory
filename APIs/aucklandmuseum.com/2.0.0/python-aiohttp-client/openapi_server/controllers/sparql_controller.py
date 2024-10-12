from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_sparql(request: web.Request, query, param_callback=None, infer=None) -> web.Response:
    """Auckland Museum SPARQL endpoint

    You can execute your [SPARQL](http://www.w3.org/TR/rdf-sparql-query/) queries against this endpoint.  The sparql query should be provided as the value of the request parameter &#x60;query&#x60;. Set the &#x60;Accept&#x60; header to &#x60;application/sparql-results+xml&#x60; to get results in XML. Set it to &#x60;application/sparql-results+json&#x60; to get results in JSON.   **Note:** This endpoints supports [JSON-P](http://json-p.org/). In order to get a JSON-P response, set the query parameter &#x60;callback&#x60; to your preferred callback function name. The default function name is &#x60;callback()&#x60;. When using JSON-P, there is no need to set the &#x60;Accept&#x60; header because the response will always be in &#x60;application/javascript&#x60;. 

    :param query: sparql query
    :type query: str
    :param param_callback: The [JSON-P](http://json-p.org/) callback parameter
    :type param_callback: str
    :param infer: Whether to get inferred results in the response
    :type infer: bool

    """
    return web.Response(status=200)


async def post_sparql(request: web.Request, query, infer=None) -> web.Response:
    """Auckland Museum SPARQL endpoint

    You can execute your [SPARQL](http://www.w3.org/TR/rdf-sparql-query/) queries against this endpoint. The sparql query should be provided as the value of the request parameter &#x60;query&#x60;. Set the &#x60;Accept&#x60; header to &#x60;application/sparql-results+xml&#x60; to get results in XML. Set it to &#x60;application/sparql-results+json&#x60; to get results in JSON.  

    :param query: sparql query
    :type query: str
    :param infer: Whether to get inferred results in the response
    :type infer: bool

    """
    return web.Response(status=200)
