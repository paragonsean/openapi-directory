# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.contact_page import ContactPage
from openapi_server.models.contact_update import ContactUpdate
from openapi_server.models.contacts_get401_response_inner import ContactsGet401ResponseInner
from openapi_server.models.contacts_get404_response_inner import ContactsGet404ResponseInner
from openapi_server.models.contacts_get422_response_inner import ContactsGet422ResponseInner


pytestmark = pytest.mark.asyncio

async def test_contacts_contactid_delete(client):
    """Test case for contacts_contactid_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'mqApiKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/contacts/{contactid}'.format(contactid='contactid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contacts_contactid_put(client):
    """Test case for contacts_contactid_put

    
    """
    contact = {"ip":"ip","confirmed":"2000-01-23T04:56:07.000+00:00","customfields":"{}","email":"email","status":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'mqApiKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/contacts/{contactid}'.format(contactid='contactid_example'),
        headers=headers,
        json=contact,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contacts_get(client):
    """Test case for contacts_get

    
    """
    params = [('listid', 'listid_example'),
                    ('offset', 56),
                    ('limit', 56),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
        'mqApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/contacts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

