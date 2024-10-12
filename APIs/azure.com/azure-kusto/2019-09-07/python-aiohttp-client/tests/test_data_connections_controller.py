# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.check_name_result import CheckNameResult
from openapi_server.models.cloud_error import CloudError
from openapi_server.models.data_connection import DataConnection
from openapi_server.models.data_connection_check_name_request import DataConnectionCheckNameRequest
from openapi_server.models.data_connection_list_result import DataConnectionListResult
from openapi_server.models.data_connection_validation import DataConnectionValidation
from openapi_server.models.data_connection_validation_list_result import DataConnectionValidationListResult


pytestmark = pytest.mark.asyncio

async def test_data_connections_check_name_availability(client):
    """Test case for data_connections_check_name_availability

    
    """
    data_connection_name = {"name":"name","type":"Microsoft.Kusto/clusters/databases/dataConnections"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Kusto/clusters/{cluster_name}/databases/{database_name}/checkNameAvailability'.format(resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', database_name='database_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=data_connection_name,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_connections_create_or_update(client):
    """Test case for data_connections_create_or_update

    
    """
    parameters = {"kind":"EventHub","location":"location"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Kusto/clusters/{cluster_name}/databases/{database_name}/dataConnections/{data_connection_name}'.format(resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', database_name='database_name_example', data_connection_name='data_connection_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_connections_data_connection_validation(client):
    """Test case for data_connections_data_connection_validation

    
    """
    parameters = {"dataConnectionName":"dataConnectionName","properties":{"kind":"EventHub","location":"location"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Kusto/clusters/{cluster_name}/databases/{database_name}/dataConnectionValidation'.format(resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', database_name='database_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_connections_delete(client):
    """Test case for data_connections_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Kusto/clusters/{cluster_name}/databases/{database_name}/dataConnections/{data_connection_name}'.format(resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', database_name='database_name_example', data_connection_name='data_connection_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_connections_get(client):
    """Test case for data_connections_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Kusto/clusters/{cluster_name}/databases/{database_name}/dataConnections/{data_connection_name}'.format(resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', database_name='database_name_example', data_connection_name='data_connection_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_connections_list_by_database(client):
    """Test case for data_connections_list_by_database

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Kusto/clusters/{cluster_name}/databases/{database_name}/dataConnections'.format(resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', database_name='database_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_connections_update(client):
    """Test case for data_connections_update

    
    """
    parameters = {"kind":"EventHub","location":"location"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Kusto/clusters/{cluster_name}/databases/{database_name}/dataConnections/{data_connection_name}'.format(resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', database_name='database_name_example', data_connection_name='data_connection_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

