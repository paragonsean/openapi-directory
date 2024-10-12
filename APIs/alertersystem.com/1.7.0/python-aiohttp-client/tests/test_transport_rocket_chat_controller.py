# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_rocket_chat_get_collection200_response import ApiTransportRocketChatGetCollection200Response
from openapi_server.models.transport_rocket_chat_get import TransportRocketChatGet
from openapi_server.models.transport_rocket_chat_jsonld_get import TransportRocketChatJsonldGet
from openapi_server.models.transport_rocket_chat_jsonld_post import TransportRocketChatJsonldPost
from openapi_server.models.transport_rocket_chat_jsonld_put import TransportRocketChatJsonldPut
from openapi_server.models.transport_rocket_chat_patch import TransportRocketChatPatch
from openapi_server.models.transport_rocket_chat_post import TransportRocketChatPost
from openapi_server.models.transport_rocket_chat_put import TransportRocketChatPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_rocket_chat_get_collection(client):
    """Test case for api_transport_rocket_chat_get_collection

    Retrieves the collection of TransportRocketChat resources.
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
        path='/api/transport-rocket-chat',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_rocket_chat_id_delete(client):
    """Test case for api_transport_rocket_chat_id_delete

    Removes the TransportRocketChat resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-rocket-chat/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_rocket_chat_id_get(client):
    """Test case for api_transport_rocket_chat_id_get

    Retrieves a TransportRocketChat resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-rocket-chat/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_rocket_chat_id_patch(client):
    """Test case for api_transport_rocket_chat_id_patch

    Updates the TransportRocketChat resource.
    """
    body = openapi_server.TransportRocketChatPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-rocket-chat/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_rocket_chat_id_put(client):
    """Test case for api_transport_rocket_chat_id_put

    Replaces the TransportRocketChat resource.
    """
    body = openapi_server.TransportRocketChatPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-rocket-chat/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_rocket_chat_post(client):
    """Test case for api_transport_rocket_chat_post

    Creates a TransportRocketChat resource.
    """
    body = openapi_server.TransportRocketChatPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-rocket-chat',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

