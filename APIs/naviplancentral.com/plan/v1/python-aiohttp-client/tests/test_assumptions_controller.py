# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.assumptions_model import AssumptionsModel


pytestmark = pytest.mark.asyncio

async def test_assumptions_get_by_planid(client):
    """Test case for assumptions_get_by_planid

    Retrieve plan assumptions
    """
    params = [('planId', 'plan_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plan/api/Assumptions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

