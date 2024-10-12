# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cash_flow_projection_model import CashFlowProjectionModel
from openapi_server.models.cash_flow_projections_model import CashFlowProjectionsModel


pytestmark = pytest.mark.asyncio

async def test_projected_cash_flow_get_by_id_planid(client):
    """Test case for projected_cash_flow_get_by_id_planid

    Retrieve projected cash flow by id
    """
    params = [('planId', 'plan_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plan/api/ProjectedCashFlow/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projected_cash_flow_get_by_planid(client):
    """Test case for projected_cash_flow_get_by_planid

    Retrieve projected cash flow
    """
    params = [('planId', 'plan_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plan/api/ProjectedCashFlow',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

