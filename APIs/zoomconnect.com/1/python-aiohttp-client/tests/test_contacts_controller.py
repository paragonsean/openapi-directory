# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.web_service_contact import WebServiceContact
from openapi_server.models.web_service_contacts import WebServiceContacts


pytestmark = pytest.mark.asyncio

async def test_api_rest_v1_contacts_all_get(client):
    """Test case for api_rest_v1_contacts_all_get

    all
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/app/api/rest/v1/contacts/all',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_rest_v1_contacts_contact_id_add_from_group_group_id_get(client):
    """Test case for api_rest_v1_contacts_contact_id_add_from_group_group_id_get

    removeFromGroup
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/app/api/rest/v1/contacts/{contact_id}/addFromGroup/{group_id}'.format(contact_id='contact_id_example', group_id='group_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_rest_v1_contacts_contact_id_add_from_group_group_id_post(client):
    """Test case for api_rest_v1_contacts_contact_id_add_from_group_group_id_post

    removeFromGroup
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/app/api/rest/v1/contacts/{contact_id}/addFromGroup/{group_id}'.format(contact_id='contact_id_example', group_id='group_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_rest_v1_contacts_contact_id_add_to_group_group_id_get(client):
    """Test case for api_rest_v1_contacts_contact_id_add_to_group_group_id_get

    addToGroup
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/app/api/rest/v1/contacts/{contact_id}/addToGroup/{group_id}'.format(contact_id='contact_id_example', group_id='group_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_rest_v1_contacts_contact_id_add_to_group_group_id_post(client):
    """Test case for api_rest_v1_contacts_contact_id_add_to_group_group_id_post

    addToGroup
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/app/api/rest/v1/contacts/{contact_id}/addToGroup/{group_id}'.format(contact_id='contact_id_example', group_id='group_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_rest_v1_contacts_contact_id_delete(client):
    """Test case for api_rest_v1_contacts_contact_id_delete

    delete
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/app/api/rest/v1/contacts/{contact_id}'.format(contact_id='contact_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_rest_v1_contacts_contact_id_get(client):
    """Test case for api_rest_v1_contacts_contact_id_get

    get
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/app/api/rest/v1/contacts/{contact_id}'.format(contact_id='contact_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_rest_v1_contacts_contact_id_post(client):
    """Test case for api_rest_v1_contacts_contact_id_post

    update
    """
    body = {"firstName":"firstName","lastName":"lastName","contactId":"contactId","contactNumber":"contactNumber","links":[{"templated":True,"rel":"rel","href":"href"},{"templated":True,"rel":"rel","href":"href"}],"title":"title"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/app/api/rest/v1/contacts/{contact_id}'.format(contact_id='contact_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_rest_v1_contacts_create_post(client):
    """Test case for api_rest_v1_contacts_create_post

    create
    """
    body = {"firstName":"firstName","lastName":"lastName","contactId":"contactId","contactNumber":"contactNumber","links":[{"templated":True,"rel":"rel","href":"href"},{"templated":True,"rel":"rel","href":"href"}],"title":"title"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/app/api/rest/v1/contacts/create',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

