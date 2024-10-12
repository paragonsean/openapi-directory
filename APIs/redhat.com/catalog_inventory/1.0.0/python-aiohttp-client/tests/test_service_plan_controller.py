# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.service_plan import ServicePlan
from openapi_server.models.service_plans_collection import ServicePlansCollection


pytestmark = pytest.mark.asyncio

async def test_list_service_plans(client):
    """Test case for list_service_plans

    List ServicePlans
    """
    params = [('limit', 100),
                    ('offset', 0),
                    ('filter', None),
                    ('sort_by', None)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='//api/catalog-inventory/v1.0/service_plans',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_show_service_plan(client):
    """Test case for show_service_plan

    Show an existing ServicePlan
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='//api/catalog-inventory/v1.0/service_plans/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

