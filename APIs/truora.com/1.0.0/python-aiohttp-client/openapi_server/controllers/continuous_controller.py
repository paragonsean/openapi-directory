from typing import List, Dict
from aiohttp import web

from openapi_server.models.continuous_check import ContinuousCheck
from openapi_server.models.error import Error
from openapi_server.models.get_contiuous_check_history_output import GetContiuousCheckHistoryOutput
from openapi_server.models.list_continuous_checks_output import ListContinuousChecksOutput
from openapi_server import util


async def create_continuous_check(request: web.Request, check_id=None, frequency=None, status=None) -> web.Response:
    """create_continuous_check

    Creates a continuous check that will run background checks recurrently according to the frequency provided.

    :param check_id: Background checks to be processed recurrently
    :type check_id: str
    :param frequency: Time between background checks. It can be daily, weekly, monthly, yearly or have a custom frequency written as a number accompanied by d: day, w: week, m: month, y: year for instance: 3d: every three days, 2w: every two weeks
    :type frequency: str
    :param status: Indicates whether the background checks must be processed recurrently (enabled | disabled)
    :type status: str

    """
    return web.Response(status=200)


async def get_continuous_check(request: web.Request, continuous_check_id) -> web.Response:
    """get_continuous_check

    Lists history associated with a Check. It can be paginated

    :param continuous_check_id: ID resulting from calling CreateContinuousCheck
    :type continuous_check_id: 

    """
    return web.Response(status=200)


async def list_continuous_checks(request: web.Request, ) -> web.Response:
    """list_continuous_checks

    Lists all continuous checks


    """
    return web.Response(status=200)


async def update_continuous_check(request: web.Request, continuous_check_id, frequency, status) -> web.Response:
    """update_continuous_check

    Updates a continuous check

    :param continuous_check_id: ID resulting from calling CreateContinuousCheck
    :type continuous_check_id: 
    :param frequency: Time between background checks
    :type frequency: str
    :param status: Indicates whether the background checks must be processed recurrently
    :type status: str

    """
    return web.Response(status=200)


async def v1_continuous_checks_continuous_check_id_history_get(request: web.Request, continuous_check_id) -> web.Response:
    """v1_continuous_checks_continuous_check_id_history_get

    Lists background check logs. It can be paginated  

    :param continuous_check_id: 
    :type continuous_check_id: str

    """
    return web.Response(status=200)
