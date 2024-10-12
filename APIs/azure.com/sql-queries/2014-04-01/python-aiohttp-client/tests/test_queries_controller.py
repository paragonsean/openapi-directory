# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.query_statistic_list_result import QueryStatisticListResult
from openapi_server.models.query_text_list_result import QueryTextListResult
from openapi_server.models.top_queries_list_result import TopQueriesListResult


pytestmark = pytest.mark.asyncio

async def test_queries_list_by_database(client):
    """Test case for queries_list_by_database

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/topQueries'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_statistics_list_by_query(client):
    """Test case for query_statistics_list_by_query

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/topQueries/{query_id}/statistics'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', query_id='query_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_texts_list_by_query(client):
    """Test case for query_texts_list_by_query

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/topQueries/{query_id}/queryText'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', query_id='query_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

