# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.check_name_result import CheckNameResult
from openapi_server.models.cloud_error import CloudError
from openapi_server.models.database import Database
from openapi_server.models.database_check_name_request import DatabaseCheckNameRequest
from openapi_server.models.database_list_result import DatabaseListResult
from openapi_server.models.database_principal_list_request import DatabasePrincipalListRequest
from openapi_server.models.database_principal_list_result import DatabasePrincipalListResult
from openapi_server.models.database_update import DatabaseUpdate


pytestmark = pytest.mark.asyncio

async def test_databases_add_principals(client):
    """Test case for databases_add_principals

    
    """
    database_principals_to_add = {"value":[{"fqn":"fqn","role":"Admin","tenantName":"tenantName","appId":"appId","name":"name","type":"App","email":"email"},{"fqn":"fqn","role":"Admin","tenantName":"tenantName","appId":"appId","name":"name","type":"App","email":"email"}]}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Kusto/clusters/{cluster_name}/databases/{database_name}/addPrincipals'.format(resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', database_name='database_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=database_principals_to_add,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_databases_check_name_availability(client):
    """Test case for databases_check_name_availability

    
    """
    database_name = {"name":"name","type":"Microsoft.Kusto/clusters/databases"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Kusto/clusters/{cluster_name}/checkNameAvailability'.format(resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=database_name,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_databases_create_or_update(client):
    """Test case for databases_create_or_update

    
    """
    parameters = {"location":"location","properties":{"hotCachePeriod":"hotCachePeriod","softDeletePeriod":"softDeletePeriod","provisioningState":"Running","statistics":{"size":0.8008281904610115}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Kusto/clusters/{cluster_name}/databases/{database_name}'.format(resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', database_name='database_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_databases_delete(client):
    """Test case for databases_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Kusto/clusters/{cluster_name}/databases/{database_name}'.format(resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', database_name='database_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_databases_get(client):
    """Test case for databases_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Kusto/clusters/{cluster_name}/databases/{database_name}'.format(resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', database_name='database_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_databases_list_by_cluster(client):
    """Test case for databases_list_by_cluster

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Kusto/clusters/{cluster_name}/databases'.format(resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_databases_list_principals(client):
    """Test case for databases_list_principals

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Kusto/clusters/{cluster_name}/databases/{database_name}/listPrincipals'.format(resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', database_name='database_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_databases_remove_principals(client):
    """Test case for databases_remove_principals

    
    """
    database_principals_to_remove = {"value":[{"fqn":"fqn","role":"Admin","tenantName":"tenantName","appId":"appId","name":"name","type":"App","email":"email"},{"fqn":"fqn","role":"Admin","tenantName":"tenantName","appId":"appId","name":"name","type":"App","email":"email"}]}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Kusto/clusters/{cluster_name}/databases/{database_name}/removePrincipals'.format(resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', database_name='database_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=database_principals_to_remove,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_databases_update(client):
    """Test case for databases_update

    
    """
    parameters = {"location":"location","properties":{"hotCachePeriod":"hotCachePeriod","softDeletePeriod":"softDeletePeriod","provisioningState":"Running","statistics":{"size":0.8008281904610115}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Kusto/clusters/{cluster_name}/databases/{database_name}'.format(resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', database_name='database_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

