# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.analytics_data_link_interface import AnalyticsDataLinkInterface
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_analytics_link_provider_v1_get_get(client):
    """Test case for analytics_link_provider_v1_get_get

    analytics/link
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/analytics/link',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

