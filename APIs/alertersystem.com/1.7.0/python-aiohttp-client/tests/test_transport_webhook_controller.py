# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_webhook_get_collection200_response import ApiTransportWebhookGetCollection200Response
from openapi_server.models.transport_webhook_get import TransportWebhookGet
from openapi_server.models.transport_webhook_jsonld_get import TransportWebhookJsonldGet
from openapi_server.models.transport_webhook_jsonld_post import TransportWebhookJsonldPost
from openapi_server.models.transport_webhook_jsonld_put import TransportWebhookJsonldPut
from openapi_server.models.transport_webhook_patch import TransportWebhookPatch
from openapi_server.models.transport_webhook_post import TransportWebhookPost
from openapi_server.models.transport_webhook_put import TransportWebhookPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_webhook_get_collection(client):
    """Test case for api_transport_webhook_get_collection

    Retrieves the collection of TransportWebhook resources.
    """
    params = [('page', 1),
                    ('dataSegmentCode', 'data_segment_code_example'),
                    ('dataSegmentCode[]', ['data_segment_code_example']),
                    ('partition', 'partition_example'),
                    ('partition[]', ['partition_example']),
                    ('properties[]', ['properties_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-webhook',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_webhook_id_delete(client):
    """Test case for api_transport_webhook_id_delete

    Removes the TransportWebhook resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-webhook/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_webhook_id_get(client):
    """Test case for api_transport_webhook_id_get

    Retrieves a TransportWebhook resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-webhook/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_webhook_id_patch(client):
    """Test case for api_transport_webhook_id_patch

    Updates the TransportWebhook resource.
    """
    body = openapi_server.TransportWebhookPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-webhook/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_webhook_id_put(client):
    """Test case for api_transport_webhook_id_put

    Replaces the TransportWebhook resource.
    """
    body = openapi_server.TransportWebhookPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-webhook/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_webhook_post(client):
    """Test case for api_transport_webhook_post

    Creates a TransportWebhook resource.
    """
    body = openapi_server.TransportWebhookPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-webhook',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

