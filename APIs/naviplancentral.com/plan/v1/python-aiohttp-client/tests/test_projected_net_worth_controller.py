# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.net_worth_projection_model import NetWorthProjectionModel
from openapi_server.models.net_worth_projections_model import NetWorthProjectionsModel


pytestmark = pytest.mark.asyncio

async def test_projected_net_worth_get_by_id_planid(client):
    """Test case for projected_net_worth_get_by_id_planid

    Retrieve projected net worth by id
    """
    params = [('planId', 'plan_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plan/api/ProjectedNetWorth/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projected_net_worth_get_by_planid(client):
    """Test case for projected_net_worth_get_by_planid

    Retrieve projected net worth
    """
    params = [('planId', 'plan_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plan/api/ProjectedNetWorth',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

