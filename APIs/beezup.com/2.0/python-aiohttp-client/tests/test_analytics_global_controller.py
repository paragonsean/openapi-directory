# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.analytics_index import AnalyticsIndex
from openapi_server.models.analytics_store_index import AnalyticsStoreIndex
from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage


pytestmark = pytest.mark.asyncio

async def test_analytics_index(client):
    """Test case for analytics_index

    Get the Analytics API operation index
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/analytics/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analytics_store_index(client):
    """Test case for analytics_store_index

    Get the Analytics API operation index for one store
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/analytics/{store_id}'.format(store_id='store_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

