# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.token import Token
from openapi_server.models.token_list_result import TokenListResult
from openapi_server.models.token_update_parameters import TokenUpdateParameters


pytestmark = pytest.mark.asyncio

async def test_tokens_create(client):
    """Test case for tokens_create

    
    """
    token_create_parameters = {"properties":{"credentials":{"certificates":[{"name":"certificate1","thumbprint":"thumbprint","expiry":"2000-01-23T04:56:07.000+00:00","encodedPemCertificate":"encodedPemCertificate"},{"name":"certificate1","thumbprint":"thumbprint","expiry":"2000-01-23T04:56:07.000+00:00","encodedPemCertificate":"encodedPemCertificate"}],"passwords":[{"creationTime":"2000-01-23T04:56:07.000+00:00","name":"password1","expiry":"2000-01-23T04:56:07.000+00:00","value":"value"},{"creationTime":"2000-01-23T04:56:07.000+00:00","name":"password1","expiry":"2000-01-23T04:56:07.000+00:00","value":"value"}]},"scopeMapId":"scopeMapId","provisioningState":"Creating","creationDate":"2000-01-23T04:56:07.000+00:00","objectId":"objectId","status":"enabled"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerRegistry/registries/{registry_name}/tokens/{token_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', registry_name='registry_name_example', token_name='token_name_example'),
        headers=headers,
        json=token_create_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tokens_delete(client):
    """Test case for tokens_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerRegistry/registries/{registry_name}/tokens/{token_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', registry_name='registry_name_example', token_name='token_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tokens_get(client):
    """Test case for tokens_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerRegistry/registries/{registry_name}/tokens/{token_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', registry_name='registry_name_example', token_name='token_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tokens_list(client):
    """Test case for tokens_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerRegistry/registries/{registry_name}/tokens'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', registry_name='registry_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tokens_update(client):
    """Test case for tokens_update

    
    """
    token_update_parameters = {"properties":{"credentials":{"certificates":[{"name":"certificate1","thumbprint":"thumbprint","expiry":"2000-01-23T04:56:07.000+00:00","encodedPemCertificate":"encodedPemCertificate"},{"name":"certificate1","thumbprint":"thumbprint","expiry":"2000-01-23T04:56:07.000+00:00","encodedPemCertificate":"encodedPemCertificate"}],"passwords":[{"creationTime":"2000-01-23T04:56:07.000+00:00","name":"password1","expiry":"2000-01-23T04:56:07.000+00:00","value":"value"},{"creationTime":"2000-01-23T04:56:07.000+00:00","name":"password1","expiry":"2000-01-23T04:56:07.000+00:00","value":"value"}]},"scopeMapId":"scopeMapId","status":"enabled"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerRegistry/registries/{registry_name}/tokens/{token_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', registry_name='registry_name_example', token_name='token_name_example'),
        headers=headers,
        json=token_update_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

