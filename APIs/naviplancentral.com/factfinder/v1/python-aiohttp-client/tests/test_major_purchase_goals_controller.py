# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.major_purchase_goal_model import MajorPurchaseGoalModel
from openapi_server.models.major_purchase_goal_with_id_model import MajorPurchaseGoalWithIdModel
from openapi_server.models.major_purchase_goals_model import MajorPurchaseGoalsModel


pytestmark = pytest.mark.asyncio

async def test_major_purchase_goals_delete_by_id(client):
    """Test case for major_purchase_goals_delete_by_id

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/factfinder/api/MajorPurchaseGoals/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_major_purchase_goals_get_by_id(client):
    """Test case for major_purchase_goals_get_by_id

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/MajorPurchaseGoals/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_major_purchase_goals_get_major_purchase_goals_by_fact_finder_id_by_factfinderid(client):
    """Test case for major_purchase_goals_get_major_purchase_goals_by_fact_finder_id_by_factfinderid

    
    """
    params = [('factFinderId', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/MajorPurchaseGoals',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_major_purchase_goals_post_by_model(client):
    """Test case for major_purchase_goals_post_by_model

    
    """
    model = {"amount":0.8008281904610115,"factFinderId":6,"targetDate":"2000-01-23T04:56:07.000+00:00","member":"Client","description":"description","externalDestinationId":"externalDestinationId","majorPurchaseGoalTypeId":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/factfinder/api/MajorPurchaseGoals',
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_major_purchase_goals_put_by_id_model(client):
    """Test case for major_purchase_goals_put_by_id_model

    
    """
    model = {"amount":0.8008281904610115,"factFinderId":6,"targetDate":"2000-01-23T04:56:07.000+00:00","member":"Client","description":"description","externalDestinationId":"externalDestinationId","majorPurchaseGoalTypeId":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/factfinder/api/MajorPurchaseGoals/{id}'.format(id=56),
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

