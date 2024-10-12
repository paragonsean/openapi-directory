# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.identity_provider_get200_response import IdentityProviderGet200Response
from openapi_server.models.identity_provider_list_by_service200_response import IdentityProviderListByService200Response
from openapi_server.models.identity_provider_list_by_service_default_response import IdentityProviderListByServiceDefaultResponse
from openapi_server.models.identity_provider_update_request import IdentityProviderUpdateRequest


pytestmark = pytest.mark.asyncio

async def test_identity_provider_create_or_update(client):
    """Test case for identity_provider_create_or_update

    
    """
    parameters = openapi_server.IdentityProviderGet200Response()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/identityProviders/{identity_provider_name}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', identity_provider_name='identity_provider_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_identity_provider_delete(client):
    """Test case for identity_provider_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/identityProviders/{identity_provider_name}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', identity_provider_name='identity_provider_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_identity_provider_get(client):
    """Test case for identity_provider_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/identityProviders/{identity_provider_name}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', identity_provider_name='identity_provider_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_identity_provider_get_entity_tag(client):
    """Test case for identity_provider_get_entity_tag

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='HEAD',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/identityProviders/{identity_provider_name}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', identity_provider_name='identity_provider_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_identity_provider_list_by_service(client):
    """Test case for identity_provider_list_by_service

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/identityProviders'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_identity_provider_update(client):
    """Test case for identity_provider_update

    
    """
    parameters = openapi_server.IdentityProviderUpdateRequest()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/identityProviders/{identity_provider_name}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', identity_provider_name='identity_provider_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

