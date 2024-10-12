from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_v20_database_traces_barcode_get_request import ApiV20DatabaseTracesBarcodeGetRequest
from openapi_server import util


async def api_v20_database_traces_barcode_get(request: web.Request, database, barcode, body=None) -> web.Response:
    """api_v20_database_traces_barcode_get

    Traces (sequence-reads) metadata

    :param database: Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
    :type database: str
    :param barcode: Unique barcode for Traces records, &lt;database prefix&gt;_&lt;ID code&gt;_TR e.g. SAL_AA0001AA_TR
    :type barcode: str
    :param body: 
    :type body: dict | bytes

    """
    body = ApiV20DatabaseTracesBarcodeGetRequest.from_dict(body)
    return web.Response(status=200)


async def api_v20_database_traces_barcode_post(request: web.Request, database, barcode, body=None) -> web.Response:
    """api_v20_database_traces_barcode_post

    Traces (sequence-reads) metadata

    :param database: Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
    :type database: str
    :param barcode: Unique barcode for Traces records, &lt;database prefix&gt;_&lt;ID code&gt;_TR e.g. SAL_AA0001AA_TR
    :type barcode: str
    :param body: 
    :type body: dict | bytes

    """
    body = ApiV20DatabaseTracesBarcodeGetRequest.from_dict(body)
    return web.Response(status=200)


async def api_v20_database_traces_barcode_put(request: web.Request, database, barcode, body=None) -> web.Response:
    """api_v20_database_traces_barcode_put

    Traces (sequence-reads) metadata

    :param database: Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
    :type database: str
    :param barcode: Unique barcode for Traces records, &lt;database prefix&gt;_&lt;ID code&gt;_TR e.g. SAL_AA0001AA_TR
    :type barcode: str
    :param body: 
    :type body: dict | bytes

    """
    body = ApiV20DatabaseTracesBarcodeGetRequest.from_dict(body)
    return web.Response(status=200)


async def api_v20_database_traces_get(request: web.Request, database, barcode=None, orderby=None, offset=None, only_fields=None, sortorder=None, limit=None) -> web.Response:
    """api_v20_database_traces_get

    Traces (sequence-reads) metadata

    :param database: Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
    :type database: str
    :param barcode: Unique barcode for Traces records, &lt;database prefix&gt;_&lt;ID code&gt;_TR e.g. SAL_AA0001AA_TR
    :type barcode: List[str]
    :param orderby: Field to order by. Default: barcode
    :type orderby: str
    :param offset: Cursor position in results
    :type offset: int
    :param only_fields: 
    :type only_fields: List[str]
    :param sortorder: Order of search results: asc or desc
    :type sortorder: str
    :param limit: Number of results per page
    :type limit: int

    """
    return web.Response(status=200)
