# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.endpoint_headers_in import EndpointHeadersIn
from openapi_server.models.endpoint_headers_out import EndpointHeadersOut
from openapi_server.models.endpoint_headers_patch_in import EndpointHeadersPatchIn
from openapi_server.models.endpoint_in import EndpointIn
from openapi_server.models.endpoint_out import EndpointOut
from openapi_server.models.endpoint_secret_out import EndpointSecretOut
from openapi_server.models.endpoint_secret_rotate_in import EndpointSecretRotateIn
from openapi_server.models.endpoint_stats import EndpointStats
from openapi_server.models.endpoint_transformation_in import EndpointTransformationIn
from openapi_server.models.endpoint_transformation_out import EndpointTransformationOut
from openapi_server.models.endpoint_update import EndpointUpdate
from openapi_server.models.event_example_in import EventExampleIn
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.http_error_out import HttpErrorOut
from openapi_server.models.list_response_endpoint_out import ListResponseEndpointOut
from openapi_server.models.message_out import MessageOut
from openapi_server.models.ordering import Ordering
from openapi_server.models.recover_in import RecoverIn
from openapi_server.models.recover_out import RecoverOut
from openapi_server.models.replay_in import ReplayIn
from openapi_server.models.replay_out import ReplayOut


pytestmark = pytest.mark.asyncio

async def test_create_endpoint_api_v1_app_app_id_endpoint_post(client):
    """Test case for create_endpoint_api_v1_app_app_id_endpoint_post

    Create Endpoint
    """
    body = {"uid":"unique-endpoint-identifier","metadata":{"key":"metadata"},"rateLimit":1000,"channels":["project_123","group_2"],"description":"An example endpoint name","disabled":False,"secret":"whsec_C2FVsBQIhrscChlQIMV+b5sSYspob7oD","filterTypes":["user.signup","user.deleted"],"version":1,"url":"https://example.com/webhook/"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'idempotency_key': 'idempotency_key_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/app/{app_id}/endpoint'.format(app_id='app_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_endpoint_api_v1_app_app_id_endpoint_endpoint_id_delete(client):
    """Test case for delete_endpoint_api_v1_app_app_id_endpoint_endpoint_id_delete

    Delete Endpoint
    """
    headers = { 
        'Accept': 'application/json',
        'idempotency_key': 'idempotency_key_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/app/{app_id}/endpoint/{endpoint_id}'.format(endpoint_id='ep_1srOrx2ZWZBpBUvZwXKQmoEYga2', app_id='app_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_endpoint_api_v1_app_app_id_endpoint_endpoint_id_get(client):
    """Test case for get_endpoint_api_v1_app_app_id_endpoint_endpoint_id_get

    Get Endpoint
    """
    headers = { 
        'Accept': 'application/json',
        'idempotency_key': 'idempotency_key_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/app/{app_id}/endpoint/{endpoint_id}'.format(endpoint_id='ep_1srOrx2ZWZBpBUvZwXKQmoEYga2', app_id='app_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_endpoint_headers_api_v1_app_app_id_endpoint_endpoint_id_headers_get(client):
    """Test case for get_endpoint_headers_api_v1_app_app_id_endpoint_endpoint_id_headers_get

    Get Endpoint Headers
    """
    headers = { 
        'Accept': 'application/json',
        'idempotency_key': 'idempotency_key_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/app/{app_id}/endpoint/{endpoint_id}/headers'.format(endpoint_id='ep_1srOrx2ZWZBpBUvZwXKQmoEYga2', app_id='app_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_endpoint_secret_api_v1_app_app_id_endpoint_endpoint_id_secret_get(client):
    """Test case for get_endpoint_secret_api_v1_app_app_id_endpoint_endpoint_id_secret_get

    Get Endpoint Secret
    """
    headers = { 
        'Accept': 'application/json',
        'idempotency_key': 'idempotency_key_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/app/{app_id}/endpoint/{endpoint_id}/secret'.format(endpoint_id='ep_1srOrx2ZWZBpBUvZwXKQmoEYga2', app_id='app_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_endpoint_stats_api_v1_app_app_id_endpoint_endpoint_id_stats_get(client):
    """Test case for get_endpoint_stats_api_v1_app_app_id_endpoint_endpoint_id_stats_get

    Get Endpoint Stats
    """
    params = [('since', '2013-10-20T19:20:30+01:00'),
                    ('until', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'idempotency_key': 'idempotency_key_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/app/{app_id}/endpoint/{endpoint_id}/stats'.format(endpoint_id='ep_1srOrx2ZWZBpBUvZwXKQmoEYga2', app_id='app_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_endpoint_transformation_api_v1_app_app_id_endpoint_endpoint_id_transformation_get(client):
    """Test case for get_endpoint_transformation_api_v1_app_app_id_endpoint_endpoint_id_transformation_get

    Get Endpoint Transformation
    """
    headers = { 
        'Accept': 'application/json',
        'idempotency_key': 'idempotency_key_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/app/{app_id}/endpoint/{endpoint_id}/transformation'.format(endpoint_id='ep_1srOrx2ZWZBpBUvZwXKQmoEYga2', app_id='app_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_endpoints_api_v1_app_app_id_endpoint_get(client):
    """Test case for list_endpoints_api_v1_app_app_id_endpoint_get

    List Endpoints
    """
    params = [('iterator', 'ep_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
                    ('limit', 50),
                    ('order', openapi_server.Ordering())]
    headers = { 
        'Accept': 'application/json',
        'idempotency_key': 'idempotency_key_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/app/{app_id}/endpoint'.format(app_id='app_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_endpoint_headers_api_v1_app_app_id_endpoint_endpoint_id_headers_patch(client):
    """Test case for patch_endpoint_headers_api_v1_app_app_id_endpoint_endpoint_id_headers_patch

    Patch Endpoint Headers
    """
    body = {"headers":{"X-Example":"123","X-Foobar":"Bar"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'idempotency_key': 'idempotency_key_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/app/{app_id}/endpoint/{endpoint_id}/headers'.format(app_id='app_1srOrx2ZWZBpBUvZwXKQmoEYga2', endpoint_id='ep_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recover_failed_webhooks_api_v1_app_app_id_endpoint_endpoint_id_recover_post(client):
    """Test case for recover_failed_webhooks_api_v1_app_app_id_endpoint_endpoint_id_recover_post

    Recover Failed Webhooks
    """
    body = {"until":"2000-01-23T04:56:07.000+00:00","since":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'idempotency_key': 'idempotency_key_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/app/{app_id}/endpoint/{endpoint_id}/recover'.format(app_id='app_1srOrx2ZWZBpBUvZwXKQmoEYga2', endpoint_id='ep_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replay_missing_webhooks_api_v1_app_app_id_endpoint_endpoint_id_replay_missing_post(client):
    """Test case for replay_missing_webhooks_api_v1_app_app_id_endpoint_endpoint_id_replay_missing_post

    Replay Missing Webhooks
    """
    body = {"until":"2000-01-23T04:56:07.000+00:00","since":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'idempotency_key': 'idempotency_key_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/app/{app_id}/endpoint/{endpoint_id}/replay-missing'.format(app_id='app_1srOrx2ZWZBpBUvZwXKQmoEYga2', endpoint_id='ep_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rotate_endpoint_secret_api_v1_app_app_id_endpoint_endpoint_id_secret_rotate_post(client):
    """Test case for rotate_endpoint_secret_api_v1_app_app_id_endpoint_endpoint_id_secret_rotate_post

    Rotate Endpoint Secret
    """
    body = {"key":"whsec_C2FVsBQIhrscChlQIMV+b5sSYspob7oD"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'idempotency_key': 'idempotency_key_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/app/{app_id}/endpoint/{endpoint_id}/secret/rotate'.format(endpoint_id='ep_1srOrx2ZWZBpBUvZwXKQmoEYga2', app_id='app_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_send_event_type_example_message_api_v1_app_app_id_endpoint_endpoint_id_send_example_post(client):
    """Test case for send_event_type_example_message_api_v1_app_app_id_endpoint_endpoint_id_send_example_post

    Send Event Type Example Message
    """
    body = {"eventType":"user.signup"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'idempotency_key': 'idempotency_key_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/app/{app_id}/endpoint/{endpoint_id}/send-example'.format(app_id='app_1srOrx2ZWZBpBUvZwXKQmoEYga2', endpoint_id='ep_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_endpoint_transformation_api_v1_app_app_id_endpoint_endpoint_id_transformation_patch(client):
    """Test case for set_endpoint_transformation_api_v1_app_app_id_endpoint_endpoint_id_transformation_patch

    Set Endpoint Transformation
    """
    body = {"code":"code","enabled":False}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'idempotency_key': 'idempotency_key_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/app/{app_id}/endpoint/{endpoint_id}/transformation'.format(app_id='app_1srOrx2ZWZBpBUvZwXKQmoEYga2', endpoint_id='ep_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_endpoint_api_v1_app_app_id_endpoint_endpoint_id_put(client):
    """Test case for update_endpoint_api_v1_app_app_id_endpoint_endpoint_id_put

    Update Endpoint
    """
    body = {"uid":"unique-endpoint-identifier","metadata":{"key":"metadata"},"rateLimit":1000,"channels":["project_123","group_2"],"description":"An example endpoint name","disabled":False,"filterTypes":["user.signup","user.deleted"],"version":1,"url":"https://example.com/webhook/"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'idempotency_key': 'idempotency_key_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/app/{app_id}/endpoint/{endpoint_id}'.format(endpoint_id='ep_1srOrx2ZWZBpBUvZwXKQmoEYga2', app_id='app_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_endpoint_headers_api_v1_app_app_id_endpoint_endpoint_id_headers_put(client):
    """Test case for update_endpoint_headers_api_v1_app_app_id_endpoint_endpoint_id_headers_put

    Update Endpoint Headers
    """
    body = {"headers":{"X-Example":"123","X-Foobar":"Bar"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'idempotency_key': 'idempotency_key_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/app/{app_id}/endpoint/{endpoint_id}/headers'.format(app_id='app_1srOrx2ZWZBpBUvZwXKQmoEYga2', endpoint_id='ep_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

