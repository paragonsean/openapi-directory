# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_bulk_delete_contacts(client):
    """Test case for bulk_delete_contacts

    Bulk delete contacts
    """
    body = {"id":["id","id"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/contacts/bulkDelete',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contacts_contact_id_delete(client):
    """Test case for contacts_contact_id_delete

    Delete a contact
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/contacts/{contact_id}'.format(contact_id='contact_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contacts_contact_id_get(client):
    """Test case for contacts_contact_id_get

    Details of 1 contact
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/contacts/{contact_id}'.format(contact_id='contact_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contacts_contact_id_put(client):
    """Test case for contacts_contact_id_put

    Edit a contact
    """
    body = openapi_server.ContactsPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/contacts/{contact_id}'.format(contact_id='contact_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contacts_get(client):
    """Test case for contacts_get

    Get a list of contacts
    """
    params = [('name', 'name_example'),
                    ('cvr', 'cvr_example'),
                    ('ean', 'ean_example'),
                    ('erp_id', 'erp_id_example'),
                    ('contact_type', 'contact_type_example'),
                    ('city', 'city_example'),
                    ('modified_gte', 'modified_gte_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/contacts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contacts_post(client):
    """Test case for contacts_post

    Add a new contact
    """
    body = openapi_server.ContactsPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/contacts',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

