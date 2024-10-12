# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.client_project_stats import ClientProjectStats
from openapi_server.models.client_string_stats import ClientStringStats
from openapi_server.models.commission_stats import CommissionStats
from openapi_server.models.error import Error
from openapi_server.models.popular_language_pairs import PopularLanguagePairs
from openapi_server.models.report_filter import ReportFilter


pytestmark = pytest.mark.asyncio

async def test_get_commission_stats(client):
    """Test case for get_commission_stats

    Returns the total commissions stats.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/stats/commissions',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_commission_stats_by_filter(client):
    """Test case for get_commission_stats_by_filter

    Returns the total commissions stats by report filter.
    """
    body = {"target_languages":["target_languages","target_languages"],"budget_code":"budget_code","source_languages":["source_languages","source_languages"],"date_to":"2000-01-23T04:56:07.000+00:00","users":[0,0],"date_from":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/stats/commissions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_popular_pairs(client):
    """Test case for get_popular_pairs

    View your popular language pairs
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/stats/popular-pairs',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_stats(client):
    """Test case for get_project_stats

    View your project statistics
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/stats/projects',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_string_stats(client):
    """Test case for get_string_stats

    View your translation statistics
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/stats/strings',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

