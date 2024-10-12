# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.api_definition import APIDefinition
from openapi_server.models.o_auth_client import OAuthClient
from openapi_server.models.session_object import SessionObject
from openapi_server.models.tyk_apis_api_id_delete200_response import TykApisApiIDDelete200Response
from openapi_server.models.tyk_apis_post200_response import TykApisPost200Response
from openapi_server.models.tyk_health_get200_response import TykHealthGet200Response
from openapi_server.models.tyk_keys_create_post200_response import TykKeysCreatePost200Response
from openapi_server.models.tyk_keys_get200_response import TykKeysGet200Response
from openapi_server.models.tyk_keys_key_id_post200_response import TykKeysKeyIdPost200Response
from openapi_server.models.tyk_keys_key_id_put200_response import TykKeysKeyIdPut200Response
from openapi_server.models.tyk_oauth_authorize_client_post200_response import TykOauthAuthorizeClientPost200Response
from openapi_server.models.tyk_oauth_clients_create_post_request import TykOauthClientsCreatePostRequest
from openapi_server.models.tyk_reload_get200_response import TykReloadGet200Response


pytestmark = pytest.mark.asyncio

async def test_tyk_apis_api_iddelete(client):
    """Test case for tyk_apis_api_iddelete

    
    """
    headers = { 
        'Accept': '*/*',
        'x_tyk_authorization': 'x_tyk_authorization_example',
    }
    response = await client.request(
        method='DELETE',
        path='/tyk/apis/{api_id}'.format(api_id='api_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tyk_apis_api_idget(client):
    """Test case for tyk_apis_api_idget

    
    """
    headers = { 
        'Accept': '*/*',
        'x_tyk_authorization': 'x_tyk_authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/tyk/apis/{api_id}'.format(api_id='api_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_tyk_apis_api_idput(client):
    """Test case for tyk_apis_api_idput

    
    """
    api_definition = openapi_server.APIDefinition()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'x_tyk_authorization': 'x_tyk_authorization_example',
    }
    response = await client.request(
        method='PUT',
        path='/tyk/apis/{api_id}'.format(api_id='api_id_example'),
        headers=headers,
        json=api_definition,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tyk_apis_get(client):
    """Test case for tyk_apis_get

    
    """
    headers = { 
        'Accept': '*/*',
        'x_tyk_authorization': 'x_tyk_authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/tyk/apis/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_tyk_apis_post(client):
    """Test case for tyk_apis_post

    
    """
    api_definition = openapi_server.APIDefinition()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/tyk/apis/',
        headers=headers,
        json=api_definition,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tyk_health_get(client):
    """Test case for tyk_health_get

    
    """
    params = [('api_id', 'api_id_example')]
    headers = { 
        'Accept': '*/*',
        'x_tyk_authorization': 'x_tyk_authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/tyk/health/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_tyk_keys_create_post(client):
    """Test case for tyk_keys_create_post

    
    """
    session_object = openapi_server.SessionObject()
    params = [('suppress_reset', 3.4)]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'x_tyk_authorization': 'x_tyk_authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/tyk/keys/create',
        headers=headers,
        json=session_object,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tyk_keys_get(client):
    """Test case for tyk_keys_get

    
    """
    params = [('api_id', 'api_id_example')]
    headers = { 
        'Accept': '*/*',
        'x_tyk_authorization': 'x_tyk_authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/tyk/keys/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tyk_keys_key_id_delete(client):
    """Test case for tyk_keys_key_id_delete

    
    """
    params = [('api_id', 'api_id_example')]
    headers = { 
        'Accept': '*/*',
        'x_tyk_authorization': 'x_tyk_authorization_example',
    }
    response = await client.request(
        method='DELETE',
        path='/tyk/keys/{key_id}'.format(key_id='key_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_tyk_keys_key_id_post(client):
    """Test case for tyk_keys_key_id_post

    
    """
    session_object = openapi_server.SessionObject()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'x_tyk_authorization': 'x_tyk_authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/tyk/keys/{key_id}'.format(key_id='key_id_example'),
        headers=headers,
        json=session_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_tyk_keys_key_id_put(client):
    """Test case for tyk_keys_key_id_put

    
    """
    session_object = openapi_server.SessionObject()
    params = [('suppress_reset', 3.4),
                    ('api_id', 'api_id_example')]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'x_tyk_authorization': 'x_tyk_authorization_example',
    }
    response = await client.request(
        method='PUT',
        path='/tyk/keys/{key_id}'.format(key_id='key_id_example'),
        headers=headers,
        json=session_object,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_tyk_oauth_authorize_client_post(client):
    """Test case for tyk_oauth_authorize_client_post

    
    """
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'multipart/form-data',
        'x_tyk_authorization': 'x_tyk_authorization_example',
    }
    data = FormData()
    data.add_field('response_type', 'response_type_example')
    data.add_field('client_id', 'client_id_example')
    data.add_field('redirect_uri', 'redirect_uri_example')
    data.add_field('key_rules', 'key_rules_example')
    response = await client.request(
        method='POST',
        path='/tyk/oauth/authorize-client/',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tyk_oauth_clients_api_id_client_id_delete(client):
    """Test case for tyk_oauth_clients_api_id_client_id_delete

    
    """
    headers = { 
        'Accept': '*/*',
        'x_tyk_authorization': 'x_tyk_authorization_example',
    }
    response = await client.request(
        method='DELETE',
        path='/tyk/oauth/clients/{api_id}/{client_id}'.format(api_id='api_id_example', client_id='client_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tyk_oauth_clients_api_id_get(client):
    """Test case for tyk_oauth_clients_api_id_get

    
    """
    headers = { 
        'Accept': '*/*',
        'x_tyk_authorization': 'x_tyk_authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/tyk/oauth/clients/{api_id}'.format(api_id='api_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_tyk_oauth_clients_create_post(client):
    """Test case for tyk_oauth_clients_create_post

    
    """
    oauth_client = openapi_server.TykOauthClientsCreatePostRequest()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'x_tyk_authorization': 'x_tyk_authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/tyk/oauth/clients/create',
        headers=headers,
        json=oauth_client,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tyk_oauth_refresh_key_id_delete(client):
    """Test case for tyk_oauth_refresh_key_id_delete

    
    """
    params = [('apiID', 'api_id_example')]
    headers = { 
        'Accept': '*/*',
        'x_tyk_authorization': 'x_tyk_authorization_example',
    }
    response = await client.request(
        method='DELETE',
        path='/tyk/oauth/refresh/{key_id}'.format(key_id='key_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tyk_reload_get(client):
    """Test case for tyk_reload_get

    
    """
    headers = { 
        'Accept': '*/*',
        'x_tyk_authorization': 'x_tyk_authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/tyk/reload/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tyk_reload_group_get(client):
    """Test case for tyk_reload_group_get

    
    """
    headers = { 
        'Accept': '*/*',
        'x_tyk_authorization': 'x_tyk_authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/tyk/reload/group',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

