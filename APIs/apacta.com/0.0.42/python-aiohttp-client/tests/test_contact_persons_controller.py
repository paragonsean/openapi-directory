# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_contact_person_request import AddContactPersonRequest
from openapi_server.models.clocking_records_clocking_record_id_delete200_response import ClockingRecordsClockingRecordIdDelete200Response
from openapi_server.models.clocking_records_clocking_record_id_put200_response import ClockingRecordsClockingRecordIdPut200Response
from openapi_server.models.clocking_records_post201_response import ClockingRecordsPost201Response
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.get_contact_person200_response import GetContactPerson200Response
from openapi_server.models.get_contact_persons_list200_response import GetContactPersonsList200Response


pytestmark = pytest.mark.asyncio

async def test_add_contact_person(client):
    """Test case for add_contact_person

    Add a new contact person to a contact
    """
    body = openapi_server.AddContactPersonRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/contacts/{contact_id}/contact_persons'.format(contact_id='contact_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contacts_contact_id_contact_persons_contact_person_id_delete(client):
    """Test case for contacts_contact_id_contact_persons_contact_person_id_delete

    Delete a contact person
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/contacts/{contact_id}/contact_persons/{contact_person_id}'.format(contact_id='contact_id_example', contact_person_id='contact_person_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_edit_contact_person(client):
    """Test case for edit_contact_person

    Edit a contact person
    """
    body = openapi_server.AddContactPersonRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/contacts/{contact_id}/contact_persons/{contact_person_id}'.format(contact_id='contact_id_example', contact_person_id='contact_person_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_contact_person(client):
    """Test case for get_contact_person

    Get a contact person
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/contacts/{contact_id}/contact_persons/{contact_person_id}'.format(contact_id='contact_id_example', contact_person_id='contact_person_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_contact_persons_list(client):
    """Test case for get_contact_persons_list

    Get a list of contact people
    """
    params = [('q', 'q_example'),
                    ('created_gte', '2013-10-20'),
                    ('created_lte', '2013-10-20')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/contacts/{contact_id}/contact_persons'.format(contact_id='contact_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

