# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.contacts_contact_id_contact_custom_field_values_get200_response import ContactsContactIdContactCustomFieldValuesGet200Response


pytestmark = pytest.mark.asyncio

async def test_contacts_contact_id_contact_custom_field_values_get(client):
    """Test case for contacts_contact_id_contact_custom_field_values_get

    Get a list of contact custom field values
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/contacts/{contact_id}/contact_custom_field_values'.format(contact_id='contact_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

