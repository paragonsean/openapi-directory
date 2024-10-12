from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_v20_database_assemblies_barcode_get_request import ApiV20DatabaseAssembliesBarcodeGetRequest
from openapi_server import util


async def api_v20_database_assemblies_barcode_get(request: web.Request, database, barcode, body=None) -> web.Response:
    """api_v20_database_assemblies_barcode_get

    Genome assemblies

    :param database: Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
    :type database: str
    :param barcode: Unique barcode for Traces records, &lt;database prefix&gt;_&lt;ID code&gt;_AS e.g. SAL_AA0001AA_AS
    :type barcode: str
    :param body: 
    :type body: dict | bytes

    """
    body = ApiV20DatabaseAssembliesBarcodeGetRequest.from_dict(body)
    return web.Response(status=200)


async def api_v20_database_assemblies_barcode_post(request: web.Request, database, barcode, body=None) -> web.Response:
    """api_v20_database_assemblies_barcode_post

    Genome assemblies

    :param database: Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
    :type database: str
    :param barcode: Unique barcode for Traces records, &lt;database prefix&gt;_&lt;ID code&gt;_AS e.g. SAL_AA0001AA_AS
    :type barcode: str
    :param body: 
    :type body: dict | bytes

    """
    body = ApiV20DatabaseAssembliesBarcodeGetRequest.from_dict(body)
    return web.Response(status=200)


async def api_v20_database_assemblies_barcode_put(request: web.Request, database, barcode, body=None) -> web.Response:
    """api_v20_database_assemblies_barcode_put

    Genome assemblies

    :param database: Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
    :type database: str
    :param barcode: Unique barcode for Traces records, &lt;database prefix&gt;_&lt;ID code&gt;_AS e.g. SAL_AA0001AA_AS
    :type barcode: str
    :param body: 
    :type body: dict | bytes

    """
    body = ApiV20DatabaseAssembliesBarcodeGetRequest.from_dict(body)
    return web.Response(status=200)


async def api_v20_database_assemblies_get(request: web.Request, database, n50=None, barcode=None, orderby=None, offset=None, assembly_status=None, uberstrain=None, top_species=None, only_fields=None, reldate=None, sortorder=None, limit=None, version=None) -> web.Response:
    """api_v20_database_assemblies_get

    Genome assemblies

    :param database: Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
    :type database: str
    :param n50: 
    :type n50: int
    :param barcode: Unique barcode for Traces records, &lt;database prefix&gt;_&lt;ID code&gt;_AS e.g. SAL_AA0001AA_AS
    :type barcode: List[str]
    :param orderby: Field to order by. Default: barcode
    :type orderby: str
    :param offset: Cursor position in results
    :type offset: int
    :param assembly_status: 
    :type assembly_status: str
    :param uberstrain: 
    :type uberstrain: str
    :param top_species: 
    :type top_species: str
    :param only_fields: 
    :type only_fields: List[str]
    :param reldate: 
    :type reldate: int
    :param sortorder: Order of search results: asc or desc
    :type sortorder: str
    :param limit: Number of results per page
    :type limit: int
    :param version: 
    :type version: int

    """
    return web.Response(status=200)
