from typing import List, Dict
from aiohttp import web

from openapi_server.models.district_dto import DistrictDTO
from openapi_server.models.states_dto import StatesDTO
from openapi_server import util


async def get_districts_in_state_using_get(request: web.Request, state_code, accept_language=None) -> web.Response:
    """Get a list of districts in a given  State as per LGD.

    

    :param state_code: stateCode
    :type state_code: str
    :param accept_language: 
    :type accept_language: str

    """
    return web.Response(status=200)


async def get_states_using_get(request: web.Request, accept_language=None) -> web.Response:
    """Get a list of states as per LGD.

    

    :param accept_language: 
    :type accept_language: str

    """
    return web.Response(status=200)
