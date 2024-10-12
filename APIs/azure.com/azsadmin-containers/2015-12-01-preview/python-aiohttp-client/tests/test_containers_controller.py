# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.container import Container
from openapi_server.models.containers_list_destination_shares200_response_inner import ContainersListDestinationShares200ResponseInner
from openapi_server.models.migration_parameters import MigrationParameters
from openapi_server.models.migration_result import MigrationResult


pytestmark = pytest.mark.asyncio

async def test_containers_cancel_migration(client):
    """Test case for containers_cancel_migration

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Storage.Admin/farms/{farm_id}/shares/operationresults/{operation_id}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', farm_id='farm_id_example', operation_id='operation_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containers_list(client):
    """Test case for containers_list

    
    """
    params = [('api-version', 'api_version_example'),
                    ('Intent', 'intent_example'),
                    ('MaxCount', 56),
                    ('StartIndex', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Storage.Admin/farms/{farm_id}/shares/{share_name}/containers'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', farm_id='farm_id_example', share_name='share_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containers_list_destination_shares(client):
    """Test case for containers_list_destination_shares

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Storage.Admin/farms/{farm_id}/shares/{share_name}/destinationshares'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', farm_id='farm_id_example', share_name='share_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containers_migrate(client):
    """Test case for containers_migrate

    
    """
    migration_parameters = {"destinationShareUncPath":"destinationShareUncPath","containerName":"containerName","storageAccountName":"storageAccountName"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Storage.Admin/farms/{farm_id}/shares/{share_name}/migrate'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', farm_id='farm_id_example', share_name='share_name_example'),
        headers=headers,
        json=migration_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containers_migration_status(client):
    """Test case for containers_migration_status

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Storage.Admin/farms/{farm_id}/shares/operationresults/{operation_id}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', farm_id='farm_id_example', operation_id='operation_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

