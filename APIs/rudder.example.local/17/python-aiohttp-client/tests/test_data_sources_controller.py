# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_data_source200_response import CreateDataSource200Response
from openapi_server.models.datasource import Datasource
from openapi_server.models.delete_data_source200_response import DeleteDataSource200Response
from openapi_server.models.get_all_data_sources200_response import GetAllDataSources200Response
from openapi_server.models.get_data_source200_response import GetDataSource200Response
from openapi_server.models.reload_all_datasources_all_nodes200_response import ReloadAllDatasourcesAllNodes200Response
from openapi_server.models.reload_all_datasources_one_node200_response import ReloadAllDatasourcesOneNode200Response
from openapi_server.models.reload_one_datasource_all_nodes200_response import ReloadOneDatasourceAllNodes200Response
from openapi_server.models.reload_one_datasource_one_node200_response import ReloadOneDatasourceOneNode200Response
from openapi_server.models.update_data_source200_response import UpdateDataSource200Response


pytestmark = pytest.mark.asyncio

async def test_create_data_source(client):
    """Test case for create_data_source

    Create a data source
    """
    body = openapi_server.Datasource()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/rudder/api/latest/datasources',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_data_source(client):
    """Test case for delete_data_source

    Delete a data source
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rudder/api/latest/datasources/{datasource_id}'.format(datasource_id='test-data-source'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_data_sources(client):
    """Test case for get_all_data_sources

    List all data sources
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/datasources',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_data_source(client):
    """Test case for get_data_source

    Get data source configuration
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/datasources/{datasource_id}'.format(datasource_id='test-data-source'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reload_all_datasources_all_nodes(client):
    """Test case for reload_all_datasources_all_nodes

    Update properties from data sources
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/datasources/reload',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reload_all_datasources_one_node(client):
    """Test case for reload_all_datasources_one_node

    Update properties for one node from all data sources
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/nodes/{node_id}/fetchData'.format(node_id='9a1773c9-0889-40b6-be89-f6504443ac1b'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reload_one_datasource_all_nodes(client):
    """Test case for reload_one_datasource_all_nodes

    Update properties from data sources
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/datasources/reload/{datasource_id}'.format(datasource_id='test-data-source'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reload_one_datasource_one_node(client):
    """Test case for reload_one_datasource_one_node

    Update properties for one node from a data source
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/nodes/{node_id}/fetchData/{datasource_id}'.format(node_id='9a1773c9-0889-40b6-be89-f6504443ac1b', datasource_id='test-data-source'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_data_source(client):
    """Test case for update_data_source

    Update a data source configuration
    """
    body = openapi_server.Datasource()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/datasources/{datasource_id}'.format(datasource_id='test-data-source'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

