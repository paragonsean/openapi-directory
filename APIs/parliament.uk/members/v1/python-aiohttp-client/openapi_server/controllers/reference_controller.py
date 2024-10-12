from typing import List, Dict
from aiohttp import web

from openapi_server.models.answering_body import AnsweringBody
from openapi_server.models.generic_reference_data import GenericReferenceData
from openapi_server.models.government_department import GovernmentDepartment
from openapi_server import util


async def api_reference_answering_bodies_get(request: web.Request, id=None, name_contains=None) -> web.Response:
    """Returns a list of answering bodies.

    

    :param id: 
    :type id: int
    :param name_contains: 
    :type name_contains: str

    """
    return web.Response(status=200)


async def api_reference_departments_get(request: web.Request, id=None, name_contains=None) -> web.Response:
    """Returns a list of departments.

    

    :param id: 
    :type id: int
    :param name_contains: 
    :type name_contains: str

    """
    return web.Response(status=200)


async def api_reference_departments_id_logo_get(request: web.Request, id) -> web.Response:
    """Returns department logo.

    

    :param id: Logo by department ID
    :type id: int

    """
    return web.Response(status=200)


async def api_reference_policy_interests_get(request: web.Request, ) -> web.Response:
    """Returns a list of policy interest.

    


    """
    return web.Response(status=200)
