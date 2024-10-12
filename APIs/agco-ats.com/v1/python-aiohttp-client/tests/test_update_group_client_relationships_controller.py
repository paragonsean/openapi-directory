# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.api_paged_response_update_system_models_update_group_client_relationship import APIPagedResponseUpdateSystemModelsUpdateGroupClientRelationship
from openapi_server.models.update_system_models_update_group_client_relationship import UpdateSystemModelsUpdateGroupClientRelationship


pytestmark = pytest.mark.asyncio

async def test_update_group_client_relationships_get_subscription(client):
    """Test case for update_group_client_relationships_get_subscription

    Get a subscription by RelationshipID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/UpdateGroupClientRelationships/{relationship_id}'.format(relationship_id='relationship_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_group_client_relationships_get_subscriptions(client):
    """Test case for update_group_client_relationships_get_subscriptions

    Get a list of current Client Subscriptions.
    """
    params = [('ClientID', 'client_id_example'),
                    ('UpdateGroupID', 'update_group_id_example'),
                    ('limit', 56),
                    ('offset', 56),
                    ('Active', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/UpdateGroupClientRelationships',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_group_client_relationships_post_subscription(client):
    """Test case for update_group_client_relationships_post_subscription

    Add a subscription
    """
    body = openapi_server.UpdateSystemModelsUpdateGroupClientRelationship()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/UpdateGroupClientRelationships',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_group_client_relationships_put_subscription(client):
    """Test case for update_group_client_relationships_put_subscription

    Updates a Subscription
    """
    body = openapi_server.UpdateSystemModelsUpdateGroupClientRelationship()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/UpdateGroupClientRelationships/{relationship_id}'.format(relationship_id='relationship_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_group_client_relationships_put_subscription_by_client_id_update_group_id(client):
    """Test case for update_group_client_relationships_put_subscription_by_client_id_update_group_id

    DEPRECATED. Set client subscription status for an update group.
    """
    params = [('ClientID', 'client_id_example'),
                    ('UpdateGroupID', 'update_group_id_example'),
                    ('Active', True)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/UpdateGroupClientRelationships',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

