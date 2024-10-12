# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_key import ApiKey
from openapi_server.models.api_key_list_result import ApiKeyListResult
from openapi_server.models.configuration_store import ConfigurationStore
from openapi_server.models.configuration_store_list_result import ConfigurationStoreListResult
from openapi_server.models.configuration_store_update_parameters import ConfigurationStoreUpdateParameters
from openapi_server.models.error import Error
from openapi_server.models.key_value import KeyValue
from openapi_server.models.list_key_value_parameters import ListKeyValueParameters
from openapi_server.models.regenerate_key_parameters import RegenerateKeyParameters


pytestmark = pytest.mark.asyncio

async def test_configuration_stores_create(client):
    """Test case for configuration_stores_create

    
    """
    config_store_creation_parameters = {"properties":{"endpoint":"endpoint","provisioningState":"Creating","creationDate":"2000-01-23T04:56:07.000+00:00"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.AppConfiguration/configurationStores/{config_store_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', config_store_name='config_store_name_example'),
        headers=headers,
        json=config_store_creation_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_configuration_stores_delete(client):
    """Test case for configuration_stores_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.AppConfiguration/configurationStores/{config_store_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', config_store_name='config_store_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_configuration_stores_get(client):
    """Test case for configuration_stores_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.AppConfiguration/configurationStores/{config_store_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', config_store_name='config_store_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_configuration_stores_list(client):
    """Test case for configuration_stores_list

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$skipToken', 'skip_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.AppConfiguration/configurationStores'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_configuration_stores_list_by_resource_group(client):
    """Test case for configuration_stores_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$skipToken', 'skip_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.AppConfiguration/configurationStores'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_configuration_stores_list_key_value(client):
    """Test case for configuration_stores_list_key_value

    
    """
    list_key_value_parameters = {"label":"label","key":"key"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.AppConfiguration/configurationStores/{config_store_name}/listKeyValue'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', config_store_name='config_store_name_example'),
        headers=headers,
        json=list_key_value_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_configuration_stores_list_keys(client):
    """Test case for configuration_stores_list_keys

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$skipToken', 'skip_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.AppConfiguration/configurationStores/{config_store_name}/ListKeys'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', config_store_name='config_store_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_configuration_stores_regenerate_key(client):
    """Test case for configuration_stores_regenerate_key

    
    """
    regenerate_key_parameters = {"id":"id"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.AppConfiguration/configurationStores/{config_store_name}/RegenerateKey'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', config_store_name='config_store_name_example'),
        headers=headers,
        json=regenerate_key_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_configuration_stores_update(client):
    """Test case for configuration_stores_update

    
    """
    config_store_update_parameters = {"properties":"{}","tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.AppConfiguration/configurationStores/{config_store_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', config_store_name='config_store_name_example'),
        headers=headers,
        json=config_store_update_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

