# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.confirm_consent_code_input import ConfirmConsentCodeInput
from openapi_server.models.connection import Connection
from openapi_server.models.connection_collection import ConnectionCollection
from openapi_server.models.connection_secrets import ConnectionSecrets
from openapi_server.models.consent_link_input import ConsentLinkInput
from openapi_server.models.consent_link_payload import ConsentLinkPayload
from openapi_server.models.list_connection_keys_input import ListConnectionKeysInput


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_connections_confirm_consent_code(client):
    """Test case for connections_confirm_consent_code

    
    """
    content = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/connections/{connection_name}/confirmConsentCode'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', connection_name='connection_name_example'),
        headers=headers,
        json=content,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_connections_create_or_update(client):
    """Test case for connections_create_or_update

    
    """
    connection = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/connections/{connection_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', connection_name='connection_name_example'),
        headers=headers,
        json=connection,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connections_delete(client):
    """Test case for connections_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/connections/{connection_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', connection_name='connection_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connections_get(client):
    """Test case for connections_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/connections/{connection_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', connection_name='connection_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connections_list(client):
    """Test case for connections_list

    Get Connections
    """
    params = [('api-version', 'api_version_example'),
                    ('$top', 56),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/connections'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_connections_list_connection_keys(client):
    """Test case for connections_list_connection_keys

    
    """
    content = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/connections/{connection_name}/listConnectionKeys'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', connection_name='connection_name_example'),
        headers=headers,
        json=content,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_connections_list_consent_links(client):
    """Test case for connections_list_consent_links

    
    """
    content = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/connections/{connection_name}/listConsentLinks'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', connection_name='connection_name_example'),
        headers=headers,
        json=content,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

