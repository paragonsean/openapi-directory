from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def api_v20_database_scheme_alleles_get(request: web.Request, locus, database, scheme, barcode=None, offset=None, allele_id=None, only_fields=None, seq=None, reldate=None, limit=None) -> web.Response:
    """api_v20_database_scheme_alleles_get

    Alleles  data 

    :param locus: 
    :type locus: str
    :param database: Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
    :type database: str
    :param scheme: 
    :type scheme: str
    :param barcode: Unique barcode for Strain records, &lt;database prefix&gt;_&lt;ID code&gt; e.g. SAL_AA0001AA
    :type barcode: List[str]
    :param offset: 
    :type offset: int
    :param allele_id: 
    :type allele_id: str
    :param only_fields: 
    :type only_fields: List[str]
    :param seq: 
    :type seq: str
    :param reldate: 
    :type reldate: int
    :param limit: 
    :type limit: int

    """
    return web.Response(status=200)
