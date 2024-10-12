# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_google_chat_get_collection200_response import ApiTransportGoogleChatGetCollection200Response
from openapi_server.models.transport_google_chat_get import TransportGoogleChatGet
from openapi_server.models.transport_google_chat_jsonld_get import TransportGoogleChatJsonldGet
from openapi_server.models.transport_google_chat_jsonld_post import TransportGoogleChatJsonldPost
from openapi_server.models.transport_google_chat_jsonld_put import TransportGoogleChatJsonldPut
from openapi_server.models.transport_google_chat_patch import TransportGoogleChatPatch
from openapi_server.models.transport_google_chat_post import TransportGoogleChatPost
from openapi_server.models.transport_google_chat_put import TransportGoogleChatPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_google_chat_get_collection(client):
    """Test case for api_transport_google_chat_get_collection

    Retrieves the collection of TransportGoogleChat resources.
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
        path='/api/transport-google-chat',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_google_chat_id_delete(client):
    """Test case for api_transport_google_chat_id_delete

    Removes the TransportGoogleChat resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-google-chat/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_google_chat_id_get(client):
    """Test case for api_transport_google_chat_id_get

    Retrieves a TransportGoogleChat resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-google-chat/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_google_chat_id_patch(client):
    """Test case for api_transport_google_chat_id_patch

    Updates the TransportGoogleChat resource.
    """
    body = openapi_server.TransportGoogleChatPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-google-chat/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_google_chat_id_put(client):
    """Test case for api_transport_google_chat_id_put

    Replaces the TransportGoogleChat resource.
    """
    body = openapi_server.TransportGoogleChatPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-google-chat/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_google_chat_post(client):
    """Test case for api_transport_google_chat_post

    Creates a TransportGoogleChat resource.
    """
    body = openapi_server.TransportGoogleChatPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-google-chat',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

