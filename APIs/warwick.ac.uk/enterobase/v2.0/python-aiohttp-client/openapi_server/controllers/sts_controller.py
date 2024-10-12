from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def api_v20_database_scheme_sts_get(request: web.Request, database, scheme2, barcode=None, st_id=None, offset=None, show_alleles=None, only_fields=None, reldate=None, limit=None, scheme=None) -> web.Response:
    """api_v20_database_scheme_sts_get

    ST profile data

    :param database: Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
    :type database: str
    :param scheme2: 
    :type scheme2: str
    :param barcode: Unique barcode for Strain records, &lt;database prefix&gt;_&lt;ID code&gt; e.g. SAL_AA0001AA
    :type barcode: List[str]
    :param st_id: 
    :type st_id: str
    :param offset: 
    :type offset: int
    :param show_alleles: 
    :type show_alleles: bool
    :param only_fields: 
    :type only_fields: List[str]
    :param reldate: 
    :type reldate: int
    :param limit: 
    :type limit: int
    :param scheme: 
    :type scheme: str

    """
    return web.Response(status=200)
