# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.source_control import SourceControl
from openapi_server.models.source_control_collection import SourceControlCollection
from openapi_server.models.user import User


pytestmark = pytest.mark.asyncio

async def test_provider_get_publishing_user(client):
    """Test case for provider_get_publishing_user

    Gets publishing user
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Web/publishingUsers/web',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_provider_get_source_control(client):
    """Test case for provider_get_source_control

    Gets source control token
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Web/sourcecontrols/{source_control_type}'.format(source_control_type='source_control_type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_provider_get_source_controls(client):
    """Test case for provider_get_source_controls

    Gets the source controls available for Azure websites
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Web/sourcecontrols',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_provider_update_publishing_user(client):
    """Test case for provider_update_publishing_user

    Updates publishing user
    """
    request_message = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/providers/Microsoft.Web/publishingUsers/web',
        headers=headers,
        json=request_message,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_provider_update_source_control(client):
    """Test case for provider_update_source_control

    Updates source control token
    """
    request_message = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/providers/Microsoft.Web/sourcecontrols/{source_control_type}'.format(source_control_type='source_control_type_example'),
        headers=headers,
        json=request_message,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

