from typing import List, Dict
from aiohttp import web

from openapi_server.models.count_result import CountResult
from openapi_server.models.error_result import ErrorResult
from openapi_server import util


async def transit(request: web.Request, _from, to, uniques, from_type=None, to_type=None) -> web.Response:
    """Transit between basic residential units

    Get count of objects that were moving between basic residential units or objects that were visiting these basic residential units. Specific object&#39;s occurence type in the base residential unit can be requested. If none occurence type is present in the request or both occurence types are zero, the result will be aggregation of all types of occurence for given base residential units. More about base residential units can be found at https://www.czso.cz/csu/rso/zsj_rso (czech).

    :param _from: source basic residential unit
    :type _from: str
    :param to: destination basic residential unit
    :type to: str
    :param uniques: all or only uniques (0 - all, 1 - uniques)
    :type uniques: str
    :param from_type: occurence type in the source basic residential unit (1 - transit, 2 - visit, 0 - both)
    :type from_type: str
    :param to_type: occurence type in the destination basic residential unit (1 - transit, 2 - visit, 0 - both)
    :type to_type: str

    """
    return web.Response(status=200)
