# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.assets_funding_goal_model import AssetsFundingGoalModel
from openapi_server.models.needs_vs_abilities_model import NeedsVsAbilitiesModel


pytestmark = pytest.mark.asyncio

async def test_projected_goals_get_assets_funding_goals_by_planid(client):
    """Test case for projected_goals_get_assets_funding_goals_by_planid

    Retrieve assets funding goals over time
    """
    params = [('planId', 'plan_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plan/api/ProjectedGoals/AssetsFundingGoals',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projected_goals_get_needs_vs_abilities_by_planid(client):
    """Test case for projected_goals_get_needs_vs_abilities_by_planid

    Retrieve needs vs abilities data
    """
    params = [('planId', 'plan_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plan/api/ProjectedGoals/NeedsVsAbilities',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

