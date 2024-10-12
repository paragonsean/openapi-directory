from typing import List, Dict
from aiohttp import web

from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.procedure_details_resource import ProcedureDetailsResource
from openapi_server.models.procedure_resource_collection import ProcedureResourceCollection
from openapi_server import util


async def get_procedures_by_id_v1(request: web.Request, id) -> web.Response:
    """Returns procedure by ID.

    

    :param id: Procedure with the ID specified
    :type id: str

    """
    return web.Response(status=200)


async def get_procedures_v1(request: web.Request, ) -> web.Response:
    """Returns all procedures.

    


    """
    return web.Response(status=200)
