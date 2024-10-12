# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_ring_central_get_collection200_response import ApiTransportRingCentralGetCollection200Response
from openapi_server.models.transport_ring_central_get import TransportRingCentralGet
from openapi_server.models.transport_ring_central_jsonld_get import TransportRingCentralJsonldGet
from openapi_server.models.transport_ring_central_jsonld_post import TransportRingCentralJsonldPost
from openapi_server.models.transport_ring_central_jsonld_put import TransportRingCentralJsonldPut
from openapi_server.models.transport_ring_central_patch import TransportRingCentralPatch
from openapi_server.models.transport_ring_central_post import TransportRingCentralPost
from openapi_server.models.transport_ring_central_put import TransportRingCentralPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_ring_central_get_collection(client):
    """Test case for api_transport_ring_central_get_collection

    Retrieves the collection of TransportRingCentral resources.
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
        path='/api/transport-ring-central',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_ring_central_id_delete(client):
    """Test case for api_transport_ring_central_id_delete

    Removes the TransportRingCentral resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-ring-central/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_ring_central_id_get(client):
    """Test case for api_transport_ring_central_id_get

    Retrieves a TransportRingCentral resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-ring-central/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_ring_central_id_patch(client):
    """Test case for api_transport_ring_central_id_patch

    Updates the TransportRingCentral resource.
    """
    body = openapi_server.TransportRingCentralPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-ring-central/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_ring_central_id_put(client):
    """Test case for api_transport_ring_central_id_put

    Replaces the TransportRingCentral resource.
    """
    body = openapi_server.TransportRingCentralPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-ring-central/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_ring_central_post(client):
    """Test case for api_transport_ring_central_post

    Creates a TransportRingCentral resource.
    """
    body = openapi_server.TransportRingCentralPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-ring-central',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

