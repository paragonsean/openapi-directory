from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def api_v20_database_scheme_loci_get(request: web.Request, database, scheme2, barcode=None, locus=None, offset=None, create_time=None, only_fields=None, limit=None, scheme=None) -> web.Response:
    """api_v20_database_scheme_loci_get

    Loci 

    :param database: Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
    :type database: str
    :param scheme2: 
    :type scheme2: str
    :param barcode: Unique barcode for Strain records, &lt;database prefix&gt;_&lt;ID code&gt; e.g. SAL_AA0001AA
    :type barcode: List[str]
    :param locus: 
    :type locus: str
    :param offset: 
    :type offset: int
    :param create_time: 
    :type create_time: str
    :param only_fields: 
    :type only_fields: List[str]
    :param limit: 
    :type limit: int
    :param scheme: 
    :type scheme: str

    """
    create_time = util.deserialize_datetime(create_time)
    return web.Response(status=200)
