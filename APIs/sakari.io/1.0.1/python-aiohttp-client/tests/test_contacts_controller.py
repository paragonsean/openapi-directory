# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.campaigns_remove200_response import CampaignsRemove200Response
from openapi_server.models.contact_request import ContactRequest
from openapi_server.models.contact_response import ContactResponse
from openapi_server.models.contacts_create201_response import ContactsCreate201Response
from openapi_server.models.contacts_response import ContactsResponse
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_contacts_create(client):
    """Test case for contacts_create

    Create contact
    """
    body = {"firstName":"Chris","lastName":"Bloggs","mobile":{"country":"country","number":"123-456-7890"},"id":"id","email":"chris@sakari.io","tags":[{"visible":True,"tag":"tag"},{"visible":True,"tag":"tag"}]}
    params = [('mergeStrategy', 'merge_strategy_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/accounts/{account_id}/contacts'.format(account_id='account_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contacts_fetch(client):
    """Test case for contacts_fetch

    Fetch contact by ID
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/accounts/{account_id}/contacts/{contact_id}'.format(account_id='account_id_example', contact_id='contact_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contacts_fetch_all(client):
    """Test case for contacts_fetch_all

    Fetch contacts
    """
    params = [('offset', 56),
                    ('limit', 56),
                    ('firstName', 'first_name_example'),
                    ('lastName', 'last_name_example'),
                    ('mobile', 'mobile_example'),
                    ('email', 'email_example'),
                    ('tags', 'tags_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/accounts/{account_id}/contacts'.format(account_id='account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contacts_remove(client):
    """Test case for contacts_remove

    Deletes a contact
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/accounts/{account_id}/contacts/{contact_id}'.format(account_id='account_id_example', contact_id='contact_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contacts_update(client):
    """Test case for contacts_update

    Updates a contact
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/accounts/{account_id}/contacts/{contact_id}'.format(account_id='account_id_example', contact_id='contact_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

