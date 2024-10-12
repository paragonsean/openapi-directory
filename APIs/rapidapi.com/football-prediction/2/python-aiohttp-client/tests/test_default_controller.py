# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_v2_list_federations_get200_response import ApiV2ListFederationsGet200Response
from openapi_server.models.api_v2_list_federations_get404_response import ApiV2ListFederationsGet404Response
from openapi_server.models.api_v2_list_markets_get200_response import ApiV2ListMarketsGet200Response
from openapi_server.models.api_v2_performance_stats_get200_response import ApiV2PerformanceStatsGet200Response
from openapi_server.models.api_v2_predictions_id_get200_response import ApiV2PredictionsIdGet200Response


pytestmark = pytest.mark.asyncio

async def test_api_v2_list_federations_get(client):
    """Test case for api_v2_list_federations_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_rapid_api_key': 'x_rapid_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/list-federations',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v2_list_markets_get(client):
    """Test case for api_v2_list_markets_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_rapid_api_key': 'x_rapid_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/list-markets',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v2_performance_stats_get(client):
    """Test case for api_v2_performance_stats_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_rapid_api_key': 'x_rapid_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/performance-stats',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v2_predictions_get(client):
    """Test case for api_v2_predictions_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_rapid_api_key': 'x_rapid_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/predictions',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v2_predictions_id_get(client):
    """Test case for api_v2_predictions_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/predictions/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

