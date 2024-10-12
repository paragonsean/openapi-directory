from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_v20_database_schemes_barcode_get_request import ApiV20DatabaseSchemesBarcodeGetRequest
from openapi_server import util


async def api_v20_database_schemes_barcode_get(request: web.Request, database, barcode, body=None) -> web.Response:
    """api_v20_database_schemes_barcode_get

    Genotyping schemes

    :param database: Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
    :type database: str
    :param barcode: Unique barcode for Strain records, &lt;database prefix&gt;_&lt;ID code&gt; e.g. SAL_AA0001AA
    :type barcode: str
    :param body: 
    :type body: dict | bytes

    """
    body = ApiV20DatabaseSchemesBarcodeGetRequest.from_dict(body)
    return web.Response(status=200)


async def api_v20_database_schemes_barcode_post(request: web.Request, database, barcode, body=None) -> web.Response:
    """api_v20_database_schemes_barcode_post

    Genotyping schemes

    :param database: Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
    :type database: str
    :param barcode: Unique barcode for Strain records, &lt;database prefix&gt;_&lt;ID code&gt; e.g. SAL_AA0001AA
    :type barcode: str
    :param body: 
    :type body: dict | bytes

    """
    body = ApiV20DatabaseSchemesBarcodeGetRequest.from_dict(body)
    return web.Response(status=200)


async def api_v20_database_schemes_barcode_put(request: web.Request, database, barcode, body=None) -> web.Response:
    """api_v20_database_schemes_barcode_put

    Genotyping schemes

    :param database: Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
    :type database: str
    :param barcode: Unique barcode for Strain records, &lt;database prefix&gt;_&lt;ID code&gt; e.g. SAL_AA0001AA
    :type barcode: str
    :param body: 
    :type body: dict | bytes

    """
    body = ApiV20DatabaseSchemesBarcodeGetRequest.from_dict(body)
    return web.Response(status=200)


async def api_v20_database_schemes_get(request: web.Request, database, barcode=None, orderby=None, offset=None, label=None, only_fields=None, created=None, lastmodified=None, sortorder=None, limit=None, scheme_name=None, version=None) -> web.Response:
    """api_v20_database_schemes_get

    Genotyping schemes

    :param database: Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
    :type database: str
    :param barcode: Unique barcode for Strain records, &lt;database prefix&gt;_&lt;ID code&gt; e.g. SAL_AA0001AA
    :type barcode: List[str]
    :param orderby: Field to order by. Default: barcode
    :type orderby: str
    :param offset: Cursor position in results
    :type offset: int
    :param label: 
    :type label: str
    :param only_fields: 
    :type only_fields: List[str]
    :param created: 
    :type created: str
    :param lastmodified: 
    :type lastmodified: str
    :param sortorder: Order of search results: asc or desc
    :type sortorder: str
    :param limit: Number of results per page
    :type limit: int
    :param scheme_name: 
    :type scheme_name: str
    :param version: 
    :type version: int

    """
    created = util.deserialize_datetime(created)
    lastmodified = util.deserialize_datetime(lastmodified)
    return web.Response(status=200)
