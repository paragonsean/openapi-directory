# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.check_name_availability_input import CheckNameAvailabilityInput
from openapi_server.models.check_name_availability_output import CheckNameAvailabilityOutput
from openapi_server.models.media_service import MediaService
from openapi_server.models.media_service_collection import MediaServiceCollection
from openapi_server.models.operation_list_result import OperationListResult
from openapi_server.models.regenerate_key_input import RegenerateKeyInput
from openapi_server.models.regenerate_key_output import RegenerateKeyOutput
from openapi_server.models.service_keys import ServiceKeys
from openapi_server.models.sync_storage_keys_input import SyncStorageKeysInput


pytestmark = pytest.mark.asyncio

async def test_media_service_check_name_availability(client):
    """Test case for media_service_check_name_availability

    
    """
    parameters = {"name":"contosomedia","type":"mediaservices"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Media/CheckNameAvailability'.format(subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_media_service_create(client):
    """Test case for media_service_create

    
    """
    parameters = {"properties":{"storageAccounts":[{"id":"/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/contosoresources/providers/Microsoft.Storage/storageAccounts/contosomedia","isPrimary":True},{"id":"/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/contosoresources/providers/Microsoft.Storage/storageAccounts/contosomedia","isPrimary":True}],"apiEndpoints":[{"endpoint":"https://wamsbayclus001rest-hs.cloudapp.net/api/","majorVersion":"2"},{"endpoint":"https://wamsbayclus001rest-hs.cloudapp.net/api/","majorVersion":"2"}]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaservices/{media_service_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', media_service_name='media_service_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_media_service_delete(client):
    """Test case for media_service_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaservices/{media_service_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', media_service_name='media_service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_media_service_get(client):
    """Test case for media_service_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaservices/{media_service_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', media_service_name='media_service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_media_service_list_by_resource_group(client):
    """Test case for media_service_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaservices'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_media_service_list_keys(client):
    """Test case for media_service_list_keys

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaservices/{media_service_name}/listKeys'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', media_service_name='media_service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_media_service_regenerate_key(client):
    """Test case for media_service_regenerate_key

    
    """
    parameters = {"keyType":"Primary"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaservices/{media_service_name}/regenerateKey'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', media_service_name='media_service_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_media_service_sync_storage_keys(client):
    """Test case for media_service_sync_storage_keys

    
    """
    parameters = {"id":"/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/contosoresources/providers/Microsoft.Storage/storageAccounts/contosomedia"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaservices/{media_service_name}/syncStorageKeys'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', media_service_name='media_service_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_media_service_update(client):
    """Test case for media_service_update

    
    """
    parameters = {"properties":{"storageAccounts":[{"id":"/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/contosoresources/providers/Microsoft.Storage/storageAccounts/contosomedia","isPrimary":True},{"id":"/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/contosoresources/providers/Microsoft.Storage/storageAccounts/contosomedia","isPrimary":True}],"apiEndpoints":[{"endpoint":"https://wamsbayclus001rest-hs.cloudapp.net/api/","majorVersion":"2"},{"endpoint":"https://wamsbayclus001rest-hs.cloudapp.net/api/","majorVersion":"2"}]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaservices/{media_service_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', media_service_name='media_service_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_operations_list(client):
    """Test case for operations_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Media/operations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

