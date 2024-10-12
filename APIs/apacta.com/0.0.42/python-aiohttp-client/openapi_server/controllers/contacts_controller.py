from typing import List, Dict
from aiohttp import web

from openapi_server.models.bulk_action_request_body import BulkActionRequestBody
from openapi_server.models.clocking_records_clocking_record_id_delete200_response import ClockingRecordsClockingRecordIdDelete200Response
from openapi_server.models.clocking_records_clocking_record_id_put200_response import ClockingRecordsClockingRecordIdPut200Response
from openapi_server.models.clocking_records_post201_response import ClockingRecordsPost201Response
from openapi_server.models.contacts_contact_id_get200_response import ContactsContactIdGet200Response
from openapi_server.models.contacts_get200_response import ContactsGet200Response
from openapi_server.models.contacts_post_request import ContactsPostRequest
from openapi_server.models.empty_success_response import EmptySuccessResponse
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.error_validation import ErrorValidation
from openapi_server import util


async def bulk_delete_contacts(request: web.Request, body) -> web.Response:
    """Bulk delete contacts

    

    :param body: Contact ids
    :type body: dict | bytes

    """
    body = BulkActionRequestBody.from_dict(body)
    return web.Response(status=200)


async def contacts_contact_id_delete(request: web.Request, contact_id) -> web.Response:
    """Delete a contact

    

    :param contact_id: 
    :type contact_id: str

    """
    return web.Response(status=200)


async def contacts_contact_id_get(request: web.Request, contact_id) -> web.Response:
    """Details of 1 contact

    

    :param contact_id: 
    :type contact_id: str

    """
    return web.Response(status=200)


async def contacts_contact_id_put(request: web.Request, contact_id, body=None) -> web.Response:
    """Edit a contact

    

    :param contact_id: 
    :type contact_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ContactsPostRequest.from_dict(body)
    return web.Response(status=200)


async def contacts_get(request: web.Request, name=None, cvr=None, ean=None, erp_id=None, contact_type=None, city=None, modified_gte=None) -> web.Response:
    """Get a list of contacts

    

    :param name: Used to search for a contact with a specific name
    :type name: str
    :param cvr: Search for values in CVR field
    :type cvr: str
    :param ean: Search for values in EAN field
    :type ean: str
    :param erp_id: Search for values in ERP id field
    :type erp_id: str
    :param contact_type: Used to show only contacts with with one specific &#x60;ContactType&#x60;
    :type contact_type: str
    :type contact_type: str
    :param city: Used to show only contacts with with one specific &#x60;City&#x60;
    :type city: str
    :param modified_gte: 
    :type modified_gte: str

    """
    return web.Response(status=200)


async def contacts_post(request: web.Request, body=None) -> web.Response:
    """Add a new contact

    

    :param body: 
    :type body: dict | bytes

    """
    body = ContactsPostRequest.from_dict(body)
    return web.Response(status=200)
