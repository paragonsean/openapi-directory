# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.http_error_out import HttpErrorOut
from openapi_server.models.integration_in import IntegrationIn
from openapi_server.models.integration_key_out import IntegrationKeyOut
from openapi_server.models.integration_out import IntegrationOut
from openapi_server.models.integration_update import IntegrationUpdate
from openapi_server.models.list_response_integration_out import ListResponseIntegrationOut


pytestmark = pytest.mark.asyncio

async def test_create_integration_api_v1_app_app_id_integration_post(client):
    """Test case for create_integration_api_v1_app_app_id_integration_post

    Create Integration
    """
    body = {"name":"Example Integration"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'idempotency_key': 'idempotency_key_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/app/{app_id}/integration'.format(app_id='app_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_integration_api_v1_app_app_id_integration_integ_id_delete(client):
    """Test case for delete_integration_api_v1_app_app_id_integration_integ_id_delete

    Delete Integration
    """
    headers = { 
        'Accept': 'application/json',
        'idempotency_key': 'idempotency_key_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/app/{app_id}/integration/{integ_id}'.format(integ_id='integ_1srOrx2ZWZBpBUvZwXKQmoEYga2', app_id='app_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_integration_api_v1_app_app_id_integration_integ_id_get(client):
    """Test case for get_integration_api_v1_app_app_id_integration_integ_id_get

    Get Integration
    """
    headers = { 
        'Accept': 'application/json',
        'idempotency_key': 'idempotency_key_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/app/{app_id}/integration/{integ_id}'.format(integ_id='integ_1srOrx2ZWZBpBUvZwXKQmoEYga2', app_id='app_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_integration_key_api_v1_app_app_id_integration_integ_id_key_get(client):
    """Test case for get_integration_key_api_v1_app_app_id_integration_integ_id_key_get

    Get Integration Key
    """
    headers = { 
        'Accept': 'application/json',
        'idempotency_key': 'idempotency_key_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/app/{app_id}/integration/{integ_id}/key'.format(integ_id='integ_1srOrx2ZWZBpBUvZwXKQmoEYga2', app_id='app_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_integrations_api_v1_app_app_id_integration_get(client):
    """Test case for list_integrations_api_v1_app_app_id_integration_get

    List Integrations
    """
    params = [('iterator', 'integ_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
                    ('limit', 50)]
    headers = { 
        'Accept': 'application/json',
        'idempotency_key': 'idempotency_key_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/app/{app_id}/integration'.format(app_id='app_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rotate_integration_key_api_v1_app_app_id_integration_integ_id_key_rotate_post(client):
    """Test case for rotate_integration_key_api_v1_app_app_id_integration_integ_id_key_rotate_post

    Rotate Integration Key
    """
    headers = { 
        'Accept': 'application/json',
        'idempotency_key': 'idempotency_key_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/app/{app_id}/integration/{integ_id}/key/rotate'.format(integ_id='integ_1srOrx2ZWZBpBUvZwXKQmoEYga2', app_id='app_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_integration_api_v1_app_app_id_integration_integ_id_put(client):
    """Test case for update_integration_api_v1_app_app_id_integration_integ_id_put

    Update Integration
    """
    body = {"name":"Example Integration"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'idempotency_key': 'idempotency_key_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/app/{app_id}/integration/{integ_id}'.format(integ_id='integ_1srOrx2ZWZBpBUvZwXKQmoEYga2', app_id='app_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

