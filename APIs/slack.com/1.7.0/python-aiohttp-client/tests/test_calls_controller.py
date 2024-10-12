# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.default_error_template import DefaultErrorTemplate
from openapi_server.models.default_success_template import DefaultSuccessTemplate


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_calls_add(client):
    """Test case for calls_add

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'created_by': 'created_by_example',
        'date_start': 56,
        'desktop_app_join_url': 'desktop_app_join_url_example',
        'external_display_id': 'external_display_id_example',
        'external_unique_id': 'external_unique_id_example',
        'join_url': 'join_url_example',
        'title': 'title_example',
        'users': 'users_example'
        }
    response = await client.request(
        method='POST',
        path='/api/calls.add',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_calls_end(client):
    """Test case for calls_end

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'duration': 56,
        'id': 'id_example'
        }
    response = await client.request(
        method='POST',
        path='/api/calls.end',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calls_info(client):
    """Test case for calls_info

    
    """
    params = [('id', 'id_example')]
    headers = { 
        'Accept': 'application/json',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/calls.info',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_calls_participants_add_0(client):
    """Test case for calls_participants_add_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'id': 'id_example',
        'users': 'users_example'
        }
    response = await client.request(
        method='POST',
        path='/api/calls.participants.add',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_calls_participants_remove_0(client):
    """Test case for calls_participants_remove_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'id': 'id_example',
        'users': 'users_example'
        }
    response = await client.request(
        method='POST',
        path='/api/calls.participants.remove',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_calls_update(client):
    """Test case for calls_update

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'desktop_app_join_url': 'desktop_app_join_url_example',
        'id': 'id_example',
        'join_url': 'join_url_example',
        'title': 'title_example'
        }
    response = await client.request(
        method='POST',
        path='/api/calls.update',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

