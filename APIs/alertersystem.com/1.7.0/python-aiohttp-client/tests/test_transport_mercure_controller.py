# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_mercure_get_collection200_response import ApiTransportMercureGetCollection200Response
from openapi_server.models.transport_mercure_get import TransportMercureGet
from openapi_server.models.transport_mercure_jsonld_get import TransportMercureJsonldGet
from openapi_server.models.transport_mercure_jsonld_post import TransportMercureJsonldPost
from openapi_server.models.transport_mercure_jsonld_put import TransportMercureJsonldPut
from openapi_server.models.transport_mercure_patch import TransportMercurePatch
from openapi_server.models.transport_mercure_post import TransportMercurePost
from openapi_server.models.transport_mercure_put import TransportMercurePut


pytestmark = pytest.mark.asyncio

async def test_api_transport_mercure_get_collection(client):
    """Test case for api_transport_mercure_get_collection

    Retrieves the collection of TransportMercure resources.
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
        path='/api/transport-mercure',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_mercure_id_delete(client):
    """Test case for api_transport_mercure_id_delete

    Removes the TransportMercure resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-mercure/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_mercure_id_get(client):
    """Test case for api_transport_mercure_id_get

    Retrieves a TransportMercure resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-mercure/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_mercure_id_patch(client):
    """Test case for api_transport_mercure_id_patch

    Updates the TransportMercure resource.
    """
    body = openapi_server.TransportMercurePatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-mercure/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_mercure_id_put(client):
    """Test case for api_transport_mercure_id_put

    Replaces the TransportMercure resource.
    """
    body = openapi_server.TransportMercurePut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-mercure/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_mercure_post(client):
    """Test case for api_transport_mercure_post

    Creates a TransportMercure resource.
    """
    body = openapi_server.TransportMercurePost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-mercure',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

