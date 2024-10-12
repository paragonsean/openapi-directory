# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.portfolio_model import PortfolioModel


pytestmark = pytest.mark.asyncio

async def test_report_performance_planning_level_id_get(client):
    """Test case for report_performance_planning_level_id_get

    Month over month performance per planning level
    """
    headers = { 
        'token': 'token_example',
    }
    response = await client.request(
        method='GET',
        path='/report/performance/{planning_level_id}'.format(planning_level_id='planning_level_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_report_performance_sku_rationalization_planning_level_id_get(client):
    """Test case for report_performance_sku_rationalization_planning_level_id_get

    SKU rationalization report
    """
    headers = { 
        'Accept': 'application/json',
        'token': 'token_example',
    }
    response = await client.request(
        method='GET',
        path='/report/performance/sku-rationalization/{planning_level_id}'.format(planning_level_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_report_planning_level_organization_get(client):
    """Test case for report_planning_level_organization_get

    Get list of plannign levels by organization
    """
    headers = { 
        'token': 'token_example',
    }
    response = await client.request(
        method='GET',
        path='/report/planning-level/organization',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_report_planning_level_user_get(client):
    """Test case for report_planning_level_user_get

    Get list of plannign levels by user
    """
    headers = { 
        'token': 'token_example',
    }
    response = await client.request(
        method='GET',
        path='/report/planning-level/user',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_report_user_get(client):
    """Test case for report_user_get

    Get usage statistics per user
    """
    headers = { 
        'token': 'token_example',
    }
    response = await client.request(
        method='GET',
        path='/report/user',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

