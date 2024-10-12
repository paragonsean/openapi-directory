from typing import List, Dict
from aiohttp import web

from openapi_server.models.business_item_resource_collection import BusinessItemResourceCollection
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.proposed_negative_statutory_instrument_resource import ProposedNegativeStatutoryInstrumentResource
from openapi_server.models.proposed_negative_statutory_instrument_resource_collection import ProposedNegativeStatutoryInstrumentResourceCollection
from openapi_server import util


async def get_business_items_by_proposed_negative_statutory_instrument_id(request: web.Request, id) -> web.Response:
    """Returns business items belonging to a proposed negative statutory instrument.

    

    :param id: Business items belonging to proposed negative statutory instrument with the ID specified
    :type id: str

    """
    return web.Response(status=200)


async def get_proposed_negative_statutory_instrument_by_id(request: web.Request, id) -> web.Response:
    """Returns proposed negative statutory instrument by ID.

    

    :param id: Proposed negative statutory instrument with the ID specified
    :type id: str

    """
    return web.Response(status=200)


async def get_proposed_negative_statutory_instruments(request: web.Request, name=None, recommended_for_procedure_change=None, department_id=None, laying_body_id=None, skip=None, take=None) -> web.Response:
    """Returns a list of proposed negative statutory instruments.

    

    :param name: Proposed negative statutory instruments with the name provided
    :type name: str
    :param recommended_for_procedure_change: Proposed negative statutory instruments recommended for procedure change
    :type recommended_for_procedure_change: bool
    :param department_id: Proposed negative statutory instruments with the department ID specified
    :type department_id: int
    :param laying_body_id: Proposed negative statutory instruments with the laying body ID specified
    :type laying_body_id: str
    :param skip: The number of records to skip from the first, default is 0
    :type skip: int
    :param take: The number of records to return, default is 20
    :type take: int

    """
    return web.Response(status=200)
