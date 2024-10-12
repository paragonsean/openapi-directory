# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.analytics_data_count_swagger_model import AnalyticsDataCountSwaggerModel
from openapi_server.models.analytics_data_swagger_model import AnalyticsDataSwaggerModel
from openapi_server.models.message_model import MessageModel


pytestmark = pytest.mark.asyncio

async def test_get_analytics_data_using_get(client):
    """Test case for get_analytics_data_using_get

    Returns the results of executed query defined by the parameters passed in
    """
    params = [('stage', 'stage_example'),
                    ('dataType', 'data_type_example'),
                    ('precision', 'precision_example'),
                    ('startDate', '2013-10-20'),
                    ('endDate', '2013-10-20'),
                    ('keys', 'keys_example')]
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/restv2/game/{api_key}/admin/analytics'.format(api_key='api_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_data_count_using_get(client):
    """Test case for get_data_count_using_get

    Returns the count of executed query
    """
    params = [('stage', 'stage_example'),
                    ('queryName', 'query_name_example')]
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/restv2/game/{api_key}/admin/analytics/count'.format(api_key='api_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_retention_using_get(client):
    """Test case for get_retention_using_get

    Returns the percentage of user retention over the last 30 days
    """
    params = [('stage', 'stage_example')]
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/restv2/game/{api_key}/admin/analytics/rollingRetention'.format(api_key='api_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

