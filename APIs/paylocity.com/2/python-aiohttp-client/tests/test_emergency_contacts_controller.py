# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.emergency_contact import EmergencyContact
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_add_or_update_emergency_contacts(client):
    """Test case for add_or_update_emergency_contacts

    Add/update emergency contacts
    """
    body = openapi_server.EmergencyContact()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/companies/{company_id}/employees/{employee_id}/emergencyContacts'.format(company_id='company_id_example', employee_id='employee_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

