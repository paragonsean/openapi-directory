from typing import List, Dict
from aiohttp import web

from openapi_server.models.solr_response import SolrResponse
from openapi_server.models.solrquery_post_request import SolrqueryPostRequest
from openapi_server import util


async def solrquery_get(request: web.Request, q=None, fq=None, fl=None, start=None, rows=None, wt=None) -> web.Response:
    """Apache Solr powered search

    GET is simpler to use, but imposes restrictions on the complexity and the lenght of the parameters.

    :param q: The query
    :type q: str
    :param fq: Filter query
    :type fq: str
    :param fl: Field list
    :type fl: str
    :param start: Starting page
    :type start: int
    :param rows: Page size
    :type rows: int
    :param wt: Response format
    :type wt: str

    """
    return web.Response(status=200)


async def solrquery_post(request: web.Request, wt=None, body=None) -> web.Response:
    """Apache Solr powered search

    POST is more complex to use, but also allows for much for complex and lengthy queries.

    :param wt: Response format
    :type wt: str
    :param body: a JSON object with Solr query parameters
    :type body: dict | bytes

    """
    body = SolrqueryPostRequest.from_dict(body)
    return web.Response(status=200)
