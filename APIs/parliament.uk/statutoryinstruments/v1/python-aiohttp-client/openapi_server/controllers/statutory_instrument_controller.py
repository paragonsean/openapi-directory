from typing import List, Dict
from aiohttp import web

from openapi_server.models.business_item_resource_collection import BusinessItemResourceCollection
from openapi_server.models.house import House
from openapi_server.models.parliamentary_process import ParliamentaryProcess
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.statutory_instrument_resource import StatutoryInstrumentResource
from openapi_server.models.statutory_instrument_resource_collection import StatutoryInstrumentResourceCollection
from openapi_server.models.statutory_instrument_type import StatutoryInstrumentType
from openapi_server import util


async def get_business_items_by_statutory_instrument_id(request: web.Request, id) -> web.Response:
    """Returns business items belonging to statutory instrument with ID.

    

    :param id: Business items belonging to statutory instrument with the ID specified
    :type id: str

    """
    return web.Response(status=200)


async def get_statutory_instrument_by_id(request: web.Request, id) -> web.Response:
    """Returns a statutory instrument by ID.

    

    :param id: Statutory instrument with the ID specified
    :type id: str

    """
    return web.Response(status=200)


async def get_statutory_instruments(request: web.Request, name=None, statutory_instrument_type=None, scheduled_debate=None, motion_to_stop=None, concerns_raised_by_committee=None, parliamentary_process_concluded=None, department_id=None, laying_body_id=None, house=None, skip=None, take=None) -> web.Response:
    """Returns a list of statutory instruments.

    

    :param name: Statutory instruments with the name specified
    :type name: str
    :param statutory_instrument_type: Statutory instruments where the statutory instrument type is the type provided
    :type statutory_instrument_type: dict | bytes
    :param scheduled_debate: Statutory instrument which contains a scheduled debate
    :type scheduled_debate: bool
    :param motion_to_stop: Statutory instruments which contains a motion to stop
    :type motion_to_stop: bool
    :param concerns_raised_by_committee: Statutory instruments which contains concerns raised by committee
    :type concerns_raised_by_committee: bool
    :param parliamentary_process_concluded: Statutory instruments where the parliamentary process is concluded or notconcluded
    :type parliamentary_process_concluded: dict | bytes
    :param department_id: Statutory instruments with the department ID specified
    :type department_id: int
    :param laying_body_id: Statutory instruments with the laying body ID specified
    :type laying_body_id: str
    :param house: Statutory instruments laid in the house specified
    :type house: dict | bytes
    :param skip: The number of records to skip from the first, default is 0
    :type skip: int
    :param take: The number of records to return, default is 20
    :type take: int

    """
    statutory_instrument_type = .from_dict(statutory_instrument_type)
    parliamentary_process_concluded = .from_dict(parliamentary_process_concluded)
    house = .from_dict(house)
    return web.Response(status=200)
