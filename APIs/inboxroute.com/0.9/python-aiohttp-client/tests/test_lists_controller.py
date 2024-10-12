# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.contact_list_page import ContactListPage
from openapi_server.models.contact_list_update import ContactListUpdate
from openapi_server.models.contacts_get401_response_inner import ContactsGet401ResponseInner
from openapi_server.models.contacts_get404_response_inner import ContactsGet404ResponseInner
from openapi_server.models.contacts_get422_response_inner import ContactsGet422ResponseInner
from openapi_server.models.new_id import NewId


pytestmark = pytest.mark.asyncio

async def test_contacts_lists_get(client):
    """Test case for contacts_lists_get

    
    """
    params = [('offset', 56),
                    ('limit', 56),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
        'mqApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/contacts/lists',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contacts_lists_listid_delete(client):
    """Test case for contacts_lists_listid_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'mqApiKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/contacts/lists/{listid}'.format(listid='listid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contacts_lists_listid_put(client):
    """Test case for contacts_lists_listid_put

    
    """
    contactlist = {"name":"name","eventcustomizations":[{"redirecturl":"redirecturl","type":6},{"redirecturl":"redirecturl","type":6}],"customfields":[{"label":"label","type":0,"key":"key","required":True},{"label":"label","type":0,"key":"key","required":True}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'mqApiKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/contacts/lists/{listid}'.format(listid='listid_example'),
        headers=headers,
        json=contactlist,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contacts_lists_post(client):
    """Test case for contacts_lists_post

    
    """
    contactlist = {"name":"name","eventcustomizations":[{"redirecturl":"redirecturl","type":6},{"redirecturl":"redirecturl","type":6}],"customfields":[{"label":"label","type":0,"key":"key","required":True},{"label":"label","type":0,"key":"key","required":True}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'mqApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/contacts/lists',
        headers=headers,
        json=contactlist,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

