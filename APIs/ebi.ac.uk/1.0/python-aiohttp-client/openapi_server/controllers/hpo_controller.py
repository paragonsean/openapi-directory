from typing import List, Dict
from aiohttp import web

from openapi_server.models.hpo_entities import HpoEntities
from openapi_server import util


async def get_hpo_using_get(request: web.Request, genesymbol=None, hpotermname=None, limit=None, page=None, synonym=None) -> web.Response:
    """Get HPO phenotypes data

    

    :param genesymbol: genesymbol
    :type genesymbol: List[str]
    :param hpotermname: hpotermname
    :type hpotermname: List[str]
    :param limit: limit
    :type limit: int
    :param page: page
    :type page: int
    :param synonym: synonym
    :type synonym: List[str]

    """
    return web.Response(status=200)
