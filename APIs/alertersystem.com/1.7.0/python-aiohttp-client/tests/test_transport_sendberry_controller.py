# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_sendberry_get_collection200_response import ApiTransportSendberryGetCollection200Response
from openapi_server.models.transport_sendberry_get import TransportSendberryGet
from openapi_server.models.transport_sendberry_jsonld_get import TransportSendberryJsonldGet
from openapi_server.models.transport_sendberry_jsonld_post import TransportSendberryJsonldPost
from openapi_server.models.transport_sendberry_jsonld_put import TransportSendberryJsonldPut
from openapi_server.models.transport_sendberry_patch import TransportSendberryPatch
from openapi_server.models.transport_sendberry_post import TransportSendberryPost
from openapi_server.models.transport_sendberry_put import TransportSendberryPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_sendberry_get_collection(client):
    """Test case for api_transport_sendberry_get_collection

    Retrieves the collection of TransportSendberry resources.
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
        path='/api/transport-sendberry',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_sendberry_id_delete(client):
    """Test case for api_transport_sendberry_id_delete

    Removes the TransportSendberry resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-sendberry/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_sendberry_id_get(client):
    """Test case for api_transport_sendberry_id_get

    Retrieves a TransportSendberry resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-sendberry/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_sendberry_id_patch(client):
    """Test case for api_transport_sendberry_id_patch

    Updates the TransportSendberry resource.
    """
    body = openapi_server.TransportSendberryPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-sendberry/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_sendberry_id_put(client):
    """Test case for api_transport_sendberry_id_put

    Replaces the TransportSendberry resource.
    """
    body = openapi_server.TransportSendberryPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-sendberry/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_sendberry_post(client):
    """Test case for api_transport_sendberry_post

    Creates a TransportSendberry resource.
    """
    body = openapi_server.TransportSendberryPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-sendberry',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

