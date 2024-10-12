# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_message_media_get_collection200_response import ApiTransportMessageMediaGetCollection200Response
from openapi_server.models.transport_message_media_get import TransportMessageMediaGet
from openapi_server.models.transport_message_media_jsonld_get import TransportMessageMediaJsonldGet
from openapi_server.models.transport_message_media_jsonld_post import TransportMessageMediaJsonldPost
from openapi_server.models.transport_message_media_jsonld_put import TransportMessageMediaJsonldPut
from openapi_server.models.transport_message_media_patch import TransportMessageMediaPatch
from openapi_server.models.transport_message_media_post import TransportMessageMediaPost
from openapi_server.models.transport_message_media_put import TransportMessageMediaPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_message_media_get_collection(client):
    """Test case for api_transport_message_media_get_collection

    Retrieves the collection of TransportMessageMedia resources.
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
        path='/api/transport-message-media',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_message_media_id_delete(client):
    """Test case for api_transport_message_media_id_delete

    Removes the TransportMessageMedia resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-message-media/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_message_media_id_get(client):
    """Test case for api_transport_message_media_id_get

    Retrieves a TransportMessageMedia resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-message-media/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_message_media_id_patch(client):
    """Test case for api_transport_message_media_id_patch

    Updates the TransportMessageMedia resource.
    """
    body = openapi_server.TransportMessageMediaPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-message-media/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_message_media_id_put(client):
    """Test case for api_transport_message_media_id_put

    Replaces the TransportMessageMedia resource.
    """
    body = openapi_server.TransportMessageMediaPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-message-media/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_message_media_post(client):
    """Test case for api_transport_message_media_post

    Creates a TransportMessageMedia resource.
    """
    body = openapi_server.TransportMessageMediaPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-message-media',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

