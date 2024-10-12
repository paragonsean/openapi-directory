# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.describe_occupation_insight import DescribeOccupationInsight
from openapi_server.models.homevalueswithin1mi_radiusof_location import Homevalueswithin1miRadiusofLocation
from openapi_server.models.list_all_local_insights import ListAllLocalInsights


pytestmark = pytest.mark.asyncio

async def test_fetch_available_insights(client):
    """Test case for fetch_available_insights

    Fetch Available Insights
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'x_rapid_api_key': 'x_rapid_api_key_example',
        'x_rapid_api_host': 'x_rapid_api_host_example',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/data/insights',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_insight_query_parameters(client):
    """Test case for fetch_insight_query_parameters

    Fetch Insight Query Parameters
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'x_rapid_api_key': 'x_rapid_api_key_example',
        'x_rapid_api_host': 'x_rapid_api_host_example',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/data/insights/{insight_id}'.format(insight_id='insight_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_insightat_location(client):
    """Test case for query_insightat_location

    Query Insight at Location
    """
    params = [('version', 'version_example'),
                    ('location[]', 'location_example')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'x_rapid_api_key': 'x_rapid_api_key_example',
        'x_rapid_api_host': 'x_rapid_api_host_example',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/data/insights/{insight_id}/query'.format(insight_id='insight_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

