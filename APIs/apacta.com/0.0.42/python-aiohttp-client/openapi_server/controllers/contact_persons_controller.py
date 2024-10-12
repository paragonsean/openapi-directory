from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_contact_person_request import AddContactPersonRequest
from openapi_server.models.clocking_records_clocking_record_id_delete200_response import ClockingRecordsClockingRecordIdDelete200Response
from openapi_server.models.clocking_records_clocking_record_id_put200_response import ClockingRecordsClockingRecordIdPut200Response
from openapi_server.models.clocking_records_post201_response import ClockingRecordsPost201Response
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.get_contact_person200_response import GetContactPerson200Response
from openapi_server.models.get_contact_persons_list200_response import GetContactPersonsList200Response
from openapi_server import util


async def add_contact_person(request: web.Request, contact_id, body=None) -> web.Response:
    """Add a new contact person to a contact

    

    :param contact_id: 
    :type contact_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = AddContactPersonRequest.from_dict(body)
    return web.Response(status=200)


async def contacts_contact_id_contact_persons_contact_person_id_delete(request: web.Request, contact_id, contact_person_id) -> web.Response:
    """Delete a contact person

    

    :param contact_id: 
    :type contact_id: str
    :param contact_person_id: 
    :type contact_person_id: str

    """
    return web.Response(status=200)


async def edit_contact_person(request: web.Request, contact_id, contact_person_id, body=None) -> web.Response:
    """Edit a contact person

    

    :param contact_id: 
    :type contact_id: str
    :param contact_person_id: 
    :type contact_person_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = AddContactPersonRequest.from_dict(body)
    return web.Response(status=200)


async def get_contact_person(request: web.Request, contact_id, contact_person_id) -> web.Response:
    """Get a contact person

    

    :param contact_id: 
    :type contact_id: str
    :param contact_person_id: 
    :type contact_person_id: str

    """
    return web.Response(status=200)


async def get_contact_persons_list(request: web.Request, contact_id, q=None, created_gte=None, created_lte=None) -> web.Response:
    """Get a list of contact people

    Get a list of contact people associated with a contact

    :param contact_id: 
    :type contact_id: str
    :param q: 
    :type q: str
    :param created_gte: 
    :type created_gte: str
    :param created_lte: 
    :type created_lte: str

    """
    created_gte = util.deserialize_date(created_gte)
    created_lte = util.deserialize_date(created_lte)
    return web.Response(status=200)
