# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.web_service_group import WebServiceGroup
from openapi_server.models.web_service_groups import WebServiceGroups


pytestmark = pytest.mark.asyncio

async def test_api_rest_v1_groups_all_get(client):
    """Test case for api_rest_v1_groups_all_get

    all
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/app/api/rest/v1/groups/all',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_rest_v1_groups_create_post(client):
    """Test case for api_rest_v1_groups_create_post

    create
    """
    body = {"groupId":"groupId","name":"name","links":[{"templated":True,"rel":"rel","href":"href"},{"templated":True,"rel":"rel","href":"href"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/app/api/rest/v1/groups/create',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_rest_v1_groups_group_id_add_contact_contact_id_get(client):
    """Test case for api_rest_v1_groups_group_id_add_contact_contact_id_get

    addContact
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/app/api/rest/v1/groups/{group_id}/addContact/{contact_id}'.format(group_id='group_id_example', contact_id='contact_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_rest_v1_groups_group_id_add_contact_contact_id_post(client):
    """Test case for api_rest_v1_groups_group_id_add_contact_contact_id_post

    addContact
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/app/api/rest/v1/groups/{group_id}/addContact/{contact_id}'.format(group_id='group_id_example', contact_id='contact_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_rest_v1_groups_group_id_delete(client):
    """Test case for api_rest_v1_groups_group_id_delete

    delete
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/app/api/rest/v1/groups/{group_id}'.format(group_id='group_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_rest_v1_groups_group_id_get(client):
    """Test case for api_rest_v1_groups_group_id_get

    get
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/app/api/rest/v1/groups/{group_id}'.format(group_id='group_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_rest_v1_groups_group_id_post(client):
    """Test case for api_rest_v1_groups_group_id_post

    update
    """
    body = {"groupId":"groupId","name":"name","links":[{"templated":True,"rel":"rel","href":"href"},{"templated":True,"rel":"rel","href":"href"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/app/api/rest/v1/groups/{group_id}'.format(group_id='group_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_rest_v1_groups_group_id_remove_contact_contact_id_get(client):
    """Test case for api_rest_v1_groups_group_id_remove_contact_contact_id_get

    removeContact
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/app/api/rest/v1/groups/{group_id}/removeContact/{contact_id}'.format(group_id='group_id_example', contact_id='contact_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_rest_v1_groups_group_id_remove_contact_contact_id_post(client):
    """Test case for api_rest_v1_groups_group_id_remove_contact_contact_id_post

    removeContact
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/app/api/rest/v1/groups/{group_id}/removeContact/{contact_id}'.format(group_id='group_id_example', contact_id='contact_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

