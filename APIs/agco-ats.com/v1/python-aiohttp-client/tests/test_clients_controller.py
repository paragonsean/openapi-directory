# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.api_paged_response_update_system_models_available_update_group_subscription import APIPagedResponseUpdateSystemModelsAvailableUpdateGroupSubscription
from openapi_server.models.api_paged_response_update_system_models_client import APIPagedResponseUpdateSystemModelsClient
from openapi_server.models.api_paged_response_update_system_models_update_group_subscription import APIPagedResponseUpdateSystemModelsUpdateGroupSubscription
from openapi_server.models.update_system_models_client import UpdateSystemModelsClient


pytestmark = pytest.mark.asyncio

async def test_api_v2_clients_idget(client):
    """Test case for api_v2_clients_idget

    Get a Client in the Update System.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/Clients/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clients_get(client):
    """Test case for clients_get

    Get a List of Clients in the Update System.
    """
    params = [('Tag', 'tag_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/Clients',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clients_get_available_subscriptions(client):
    """Test case for clients_get_available_subscriptions

    Get a Client's Available Update Group Subscriptions
    """
    params = [('UpdateGroupID', 'update_group_id_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/Clients/{id}/AvailableUpdateGroupSubscriptions'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clients_get_subscriptions(client):
    """Test case for clients_get_subscriptions

    Get a Client's Current Update Group Subscriptions
    """
    params = [('UpdateGroupID', 'update_group_id_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/Clients/{id}/UpdateGroupSubscriptions'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_clients_put(client):
    """Test case for clients_put

    Update a Client.
    """
    body = openapi_server.UpdateSystemModelsClient()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/Clients/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

