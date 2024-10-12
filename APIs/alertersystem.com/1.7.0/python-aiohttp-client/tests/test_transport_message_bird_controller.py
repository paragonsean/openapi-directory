# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_message_bird_get_collection200_response import ApiTransportMessageBirdGetCollection200Response
from openapi_server.models.transport_message_bird_get import TransportMessageBirdGet
from openapi_server.models.transport_message_bird_jsonld_get import TransportMessageBirdJsonldGet
from openapi_server.models.transport_message_bird_jsonld_post import TransportMessageBirdJsonldPost
from openapi_server.models.transport_message_bird_jsonld_put import TransportMessageBirdJsonldPut
from openapi_server.models.transport_message_bird_patch import TransportMessageBirdPatch
from openapi_server.models.transport_message_bird_post import TransportMessageBirdPost
from openapi_server.models.transport_message_bird_put import TransportMessageBirdPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_message_bird_get_collection(client):
    """Test case for api_transport_message_bird_get_collection

    Retrieves the collection of TransportMessageBird resources.
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
        path='/api/transport-message-bird',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_message_bird_id_delete(client):
    """Test case for api_transport_message_bird_id_delete

    Removes the TransportMessageBird resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-message-bird/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_message_bird_id_get(client):
    """Test case for api_transport_message_bird_id_get

    Retrieves a TransportMessageBird resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-message-bird/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_message_bird_id_patch(client):
    """Test case for api_transport_message_bird_id_patch

    Updates the TransportMessageBird resource.
    """
    body = openapi_server.TransportMessageBirdPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-message-bird/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_message_bird_id_put(client):
    """Test case for api_transport_message_bird_id_put

    Replaces the TransportMessageBird resource.
    """
    body = openapi_server.TransportMessageBirdPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-message-bird/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_message_bird_post(client):
    """Test case for api_transport_message_bird_post

    Creates a TransportMessageBird resource.
    """
    body = openapi_server.TransportMessageBirdPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-message-bird',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

