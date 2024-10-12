# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.performance_test_config import PerformanceTestConfig
from openapi_server.models.preference import Preference


pytestmark = pytest.mark.asyncio

async def test_id_delete_load_preferences(client):
    """Test case for id_delete_load_preferences

    Handle DELETE request for load test preferences
    """
    params = [('uuid', 'uuid_example')]
    headers = { 
        'token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/user/prefs/perf',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_id_get_load_preferences(client):
    """Test case for id_get_load_preferences

    Handle GET request for load test preferences
    """
    params = [('uuid', 'uuid_example')]
    headers = { 
        'Accept': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/user/prefs/perf',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_id_get_token_provider(client):
    """Test case for id_get_token_provider

    Handle GET request for tokens
    """
    headers = { 
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/user/token',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_id_get_user_login(client):
    """Test case for id_get_user_login

    Handlers GET request for User login
    """
    headers = { 
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/user/login',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_id_get_user_logout(client):
    """Test case for id_get_user_logout

    Handlers GET request for User logout
    """
    headers = { 
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/user/logout',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_id_get_user_test_prefs(client):
    """Test case for id_get_user_test_prefs

    Handle GET for User Load Test Preferences
    """
    headers = { 
        'Accept': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/user/prefs',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_id_post_load_preferences(client):
    """Test case for id_post_load_preferences

    Handle POST request for load test preferences
    """
    body = {"duration":"duration","clients":[{"headers":{"key":"headers"},"internal":True,"protocol":6,"content_type":"content_type","rps":1,"endpoint_urls":["endpoint_urls","endpoint_urls"],"load_generator":"load_generator","body":"body","connections":0,"cookies":{"key":"cookies"}},{"headers":{"key":"headers"},"internal":True,"protocol":6,"content_type":"content_type","rps":1,"endpoint_urls":["endpoint_urls","endpoint_urls"],"load_generator":"load_generator","body":"body","connections":0,"cookies":{"key":"cookies"}}],"name":"name","smp_version":"smp_version","id":"id","labels":{"key":"labels"}}
    headers = { 
        'Content-Type': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/user/prefs/perf',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_id_post_token_provider(client):
    """Test case for id_post_token_provider

    Handle POST request for tokens
    """
    headers = { 
        'token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/user/token',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_id_post_user_test_prefs(client):
    """Test case for id_post_user_test_prefs

    Handle GET for User Load Test Preferences
    """
    headers = { 
        'Accept': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/user/prefs',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

