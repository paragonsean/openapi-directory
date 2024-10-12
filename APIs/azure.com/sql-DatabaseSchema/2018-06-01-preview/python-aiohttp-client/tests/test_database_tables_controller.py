# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.database_table import DatabaseTable
from openapi_server.models.database_table_list_result import DatabaseTableListResult


pytestmark = pytest.mark.asyncio

async def test_database_tables_get(client):
    """Test case for database_tables_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/schemas/{schema_name}/tables/{table_name}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', schema_name='schema_name_example', table_name='table_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_database_tables_list_by_schema(client):
    """Test case for database_tables_list_by_schema

    
    """
    params = [('$filter', 'filter_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/schemas/{schema_name}/tables'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', schema_name='schema_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

