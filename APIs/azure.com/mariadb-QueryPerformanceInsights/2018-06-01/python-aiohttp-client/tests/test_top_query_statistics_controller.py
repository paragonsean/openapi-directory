# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.query_statistic import QueryStatistic
from openapi_server.models.top_query_statistics_input import TopQueryStatisticsInput
from openapi_server.models.top_query_statistics_result_list import TopQueryStatisticsResultList


pytestmark = pytest.mark.asyncio

async def test_top_query_statistics_get(client):
    """Test case for top_query_statistics_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DBforMariaDB/servers/{server_name}/topQueryStatistics/{query_statistic_id}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', server_name='server_name_example', query_statistic_id='query_statistic_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_top_query_statistics_list_by_server(client):
    """Test case for top_query_statistics_list_by_server

    
    """
    parameters = {"properties":{"numberOfTopQueries":0,"observedMetric":"observedMetric","aggregationWindow":"aggregationWindow","aggregationFunction":"aggregationFunction","observationStartTime":"2000-01-23T04:56:07.000+00:00","observationEndTime":"2000-01-23T04:56:07.000+00:00"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DBforMariaDB/servers/{server_name}/topQueryStatistics'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', server_name='server_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

