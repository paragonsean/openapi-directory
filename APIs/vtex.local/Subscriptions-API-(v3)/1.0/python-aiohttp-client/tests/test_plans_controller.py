# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.store_plan import StorePlan


pytestmark = pytest.mark.asyncio

async def test_api_rns_pvt_plans_get(client):
    """Test case for api_rns_pvt_plans_get

    List plans
    """
    params = [('periodicity', 'periodicity_example'),
                    ('interval', 'interval_example'),
                    ('page', 1),
                    ('size', 15)]
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/rns/pvt/plans',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_rns_pvt_plans_id_get(client):
    """Test case for api_rns_pvt_plans_id_get

    Get plan details
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/rns/pvt/plans/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

