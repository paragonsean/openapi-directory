# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.goal_model import GoalModel
from openapi_server.models.goals_model import GoalsModel


pytestmark = pytest.mark.asyncio

async def test_goals_get_by_id_planid(client):
    """Test case for goals_get_by_id_planid

    Retrieve goals
    """
    params = [('planId', 'plan_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plan/api/Goals/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_goals_get_by_planid(client):
    """Test case for goals_get_by_planid

    Retrieve goals
    """
    params = [('planId', 'plan_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plan/api/Goals',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

