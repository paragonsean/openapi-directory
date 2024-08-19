# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.authorization_server_collection import AuthorizationServerCollection
from openapi_server.models.authorization_servers_get_default_response import AuthorizationServersGetDefaultResponse
from openapi_server.models.o_auth2_authorization_server_contract import OAuth2AuthorizationServerContract
from openapi_server.models.o_auth2_authorization_server_update_contract import OAuth2AuthorizationServerUpdateContract


pytestmark = pytest.mark.asyncio

async def test_authorization_servers_create_or_update(client):
    """Test case for authorization_servers_create_or_update

    
    """
    parameters = {"clientId":"clientId","clientRegistrationEndpoint":"clientRegistrationEndpoint","supportState":True,"tokenBodyParameters":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"description":"description","resourceOwnerUsername":"resourceOwnerUsername","authorizationMethods":["HEAD","HEAD"],"authorizationEndpoint":"authorizationEndpoint","tokenEndpoint":"tokenEndpoint","grantTypes":["authorizationCode","authorizationCode"],"resourceOwnerPassword":"resourceOwnerPassword","name":"name","clientSecret":"clientSecret","id":"id","bearerTokenSendingMethods":["authorizationHeader","authorizationHeader"],"clientAuthenticationMethod":["Basic","Basic"],"defaultScope":"defaultScope"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
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

async def test_authorization_servers_delete(client):
    """Test case for authorization_servers_delete

    
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

async def test_authorization_servers_get(client):
    """Test case for authorization_servers_get

    
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

async def test_authorization_servers_list_by_service(client):
    """Test case for authorization_servers_list_by_service

    
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

async def test_authorization_servers_update(client):
    """Test case for authorization_servers_update

    
    """
    parameters = {"clientId":"clientId","clientRegistrationEndpoint":"clientRegistrationEndpoint","supportState":True,"tokenBodyParameters":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"description":"description","resourceOwnerUsername":"resourceOwnerUsername","authorizationMethods":["HEAD","HEAD"],"authorizationEndpoint":"authorizationEndpoint","tokenEndpoint":"tokenEndpoint","grantTypes":["authorizationCode","authorizationCode"],"resourceOwnerPassword":"resourceOwnerPassword","name":"name","clientSecret":"clientSecret","bearerTokenSendingMethods":["authorizationHeader","authorizationHeader"],"clientAuthenticationMethod":["Basic","Basic"],"defaultScope":"defaultScope"}
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

