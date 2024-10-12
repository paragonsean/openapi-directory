# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.category_info import CategoryInfo
from openapi_server.models.category_metrics import CategoryMetrics
from openapi_server.models.category_subscription_info import CategorySubscriptionInfo
from openapi_server.models.error_response_content import ErrorResponseContent


pytestmark = pytest.mark.asyncio

async def test_categories_images_get(client):
    """Test case for categories_images_get

    Gets the names of all alert category images.  You can get the image by going to account.signl4.com/images/alerts/categoryImageName.svg
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/categories/images',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_categories_team_id_category_id_delete(client):
    """Test case for categories_team_id_category_id_delete

    Delete an existing category
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/categories/{team_id}/{category_id}'.format(team_id='team_id_example', category_id='category_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_categories_team_id_category_id_get(client):
    """Test case for categories_team_id_category_id_get

    Get a specific category
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/categories/{team_id}/{category_id}'.format(team_id='team_id_example', category_id='category_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_categories_team_id_category_id_metrics_get(client):
    """Test case for categories_team_id_category_id_metrics_get

    Get metrics for a specific category
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/categories/{team_id}/{category_id}/metrics'.format(team_id='team_id_example', category_id='category_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_categories_team_id_category_id_put(client):
    """Test case for categories_team_id_category_id_put

    Update an existing category
    """
    body = {"augmentations":[{"name":"name","type":0,"value":"value","enabled":True},{"name":"name","type":0,"value":"value","enabled":True}],"isDefault":True,"imageName":"imageName","color":"color","keywords":["keywords","keywords"],"lastMatch":"2000-01-23T04:56:07.000+00:00","keywordMatching":6,"name":"name","options":1,"id":"id","order":5}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/categories/{team_id}/{category_id}'.format(team_id='team_id_example', category_id='category_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_categories_team_id_category_id_subscriptions_get(client):
    """Test case for categories_team_id_category_id_subscriptions_get

    Get category subscriptions
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/categories/{team_id}/{category_id}/subscriptions'.format(team_id='team_id_example', category_id='category_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_categories_team_id_category_id_subscriptions_post(client):
    """Test case for categories_team_id_category_id_subscriptions_post

    Set category subscriptions
    """
    body = {"userId":"userId","status":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/categories/{team_id}/{category_id}/subscriptions'.format(team_id='team_id_example', category_id='category_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_categories_team_id_get(client):
    """Test case for categories_team_id_get

    Get all categories
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/categories/{team_id}'.format(team_id='team_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_categories_team_id_metrics_get(client):
    """Test case for categories_team_id_metrics_get

    Get metrics for all categories
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/categories/{team_id}/metrics'.format(team_id='team_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_categories_team_id_post(client):
    """Test case for categories_team_id_post

    Create a new category
    """
    body = {"augmentations":[{"name":"name","type":0,"value":"value","enabled":True},{"name":"name","type":0,"value":"value","enabled":True}],"isDefault":True,"imageName":"imageName","color":"color","keywords":["keywords","keywords"],"lastMatch":"2000-01-23T04:56:07.000+00:00","keywordMatching":6,"name":"name","options":1,"id":"id","order":5}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/categories/{team_id}'.format(team_id='team_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

