# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.generate_sso_url_result import GenerateSsoUrlResult
from openapi_server.models.user_collection import UserCollection
from openapi_server.models.user_contract import UserContract
from openapi_server.models.user_create_parameters import UserCreateParameters
from openapi_server.models.user_token_parameters import UserTokenParameters
from openapi_server.models.user_token_result import UserTokenResult
from openapi_server.models.user_update_parameters import UserUpdateParameters
from openapi_server.models.users_list_by_service_default_response import UsersListByServiceDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_users_create_or_update(client):
    """Test case for users_create_or_update

    
    """
    parameters = {"firstName":"firstName","lastName":"lastName","note":"note","password":"password","state":"Active","email":"email"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/users/{uid}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', uid='uid_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_delete(client):
    """Test case for users_delete

    
    """
    params = [('deleteSubscriptions', True),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/users/{uid}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', uid='uid_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_generate_sso_url(client):
    """Test case for users_generate_sso_url

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/users/{uid}/generateSsoUrl'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', uid='uid_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_get(client):
    """Test case for users_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/users/{uid}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', uid='uid_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_get_shared_access_token(client):
    """Test case for users_get_shared_access_token

    
    """
    parameters = {"expiry":"2000-01-23T04:56:07.000+00:00","keyType":"primary"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/users/{uid}/token'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', uid='uid_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_list_by_service(client):
    """Test case for users_list_by_service

    
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/users'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_update(client):
    """Test case for users_update

    
    """
    parameters = {"firstName":"firstName","lastName":"lastName","note":"note","password":"password","state":"Active","email":"email"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/users/{uid}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', uid='uid_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

