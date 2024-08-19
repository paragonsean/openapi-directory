# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.authorization_server_collection import AuthorizationServerCollection
from openapi_server.models.authorization_server_contract import AuthorizationServerContract
from openapi_server.models.authorization_server_get_default_response import AuthorizationServerGetDefaultResponse
from openapi_server.models.authorization_server_update_contract import AuthorizationServerUpdateContract


pytestmark = pytest.mark.asyncio

async def test_authorization_server_create_or_update(client):
    """Test case for authorization_server_create_or_update

    
    """
    parameters = {"properties":{"grantTypes":["authorizationCode","authorizationCode"],"clientId":"clientId","clientRegistrationEndpoint":"clientRegistrationEndpoint","displayName":"displayName","authorizationEndpoint":"authorizationEndpoint"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/authorizationServers/{authsid}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', authsid='authsid_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authorization_server_delete(client):
    """Test case for authorization_server_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/authorizationServers/{authsid}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', authsid='authsid_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authorization_server_get(client):
    """Test case for authorization_server_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/authorizationServers/{authsid}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', authsid='authsid_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authorization_server_get_entity_tag(client):
    """Test case for authorization_server_get_entity_tag

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='HEAD',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/authorizationServers/{authsid}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', authsid='authsid_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authorization_server_list_by_service(client):
    """Test case for authorization_server_list_by_service

    
    """
    params = [('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skip', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/authorizationServers'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authorization_server_update(client):
    """Test case for authorization_server_update

    
    """
    parameters = {"properties":{"grantTypes":["authorizationCode","authorizationCode"],"clientId":"clientId","clientRegistrationEndpoint":"clientRegistrationEndpoint","displayName":"displayName","authorizationEndpoint":"authorizationEndpoint"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/authorizationServers/{authsid}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', authsid='authsid_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

