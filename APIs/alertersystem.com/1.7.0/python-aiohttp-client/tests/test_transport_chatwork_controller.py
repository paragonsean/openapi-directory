# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_chatwork_get_collection200_response import ApiTransportChatworkGetCollection200Response
from openapi_server.models.transport_chatwork_get import TransportChatworkGet
from openapi_server.models.transport_chatwork_jsonld_get import TransportChatworkJsonldGet
from openapi_server.models.transport_chatwork_jsonld_post import TransportChatworkJsonldPost
from openapi_server.models.transport_chatwork_jsonld_put import TransportChatworkJsonldPut
from openapi_server.models.transport_chatwork_patch import TransportChatworkPatch
from openapi_server.models.transport_chatwork_post import TransportChatworkPost
from openapi_server.models.transport_chatwork_put import TransportChatworkPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_chatwork_get_collection(client):
    """Test case for api_transport_chatwork_get_collection

    Retrieves the collection of TransportChatwork resources.
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
        path='/api/transport-chatwork',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_chatwork_id_delete(client):
    """Test case for api_transport_chatwork_id_delete

    Removes the TransportChatwork resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-chatwork/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_chatwork_id_get(client):
    """Test case for api_transport_chatwork_id_get

    Retrieves a TransportChatwork resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-chatwork/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_chatwork_id_patch(client):
    """Test case for api_transport_chatwork_id_patch

    Updates the TransportChatwork resource.
    """
    body = openapi_server.TransportChatworkPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-chatwork/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_chatwork_id_put(client):
    """Test case for api_transport_chatwork_id_put

    Replaces the TransportChatwork resource.
    """
    body = openapi_server.TransportChatworkPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-chatwork/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_chatwork_post(client):
    """Test case for api_transport_chatwork_post

    Creates a TransportChatwork resource.
    """
    body = openapi_server.TransportChatworkPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-chatwork',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

