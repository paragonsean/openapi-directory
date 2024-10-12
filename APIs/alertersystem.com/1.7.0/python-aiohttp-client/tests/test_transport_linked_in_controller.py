# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_linked_in_get_collection200_response import ApiTransportLinkedInGetCollection200Response
from openapi_server.models.transport_linked_in_get import TransportLinkedInGet
from openapi_server.models.transport_linked_in_jsonld_get import TransportLinkedInJsonldGet
from openapi_server.models.transport_linked_in_jsonld_post import TransportLinkedInJsonldPost
from openapi_server.models.transport_linked_in_jsonld_put import TransportLinkedInJsonldPut
from openapi_server.models.transport_linked_in_patch import TransportLinkedInPatch
from openapi_server.models.transport_linked_in_post import TransportLinkedInPost
from openapi_server.models.transport_linked_in_put import TransportLinkedInPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_linked_in_get_collection(client):
    """Test case for api_transport_linked_in_get_collection

    Retrieves the collection of TransportLinkedIn resources.
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
        path='/api/transport-linked-in',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_linked_in_id_delete(client):
    """Test case for api_transport_linked_in_id_delete

    Removes the TransportLinkedIn resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-linked-in/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_linked_in_id_get(client):
    """Test case for api_transport_linked_in_id_get

    Retrieves a TransportLinkedIn resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-linked-in/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_linked_in_id_patch(client):
    """Test case for api_transport_linked_in_id_patch

    Updates the TransportLinkedIn resource.
    """
    body = openapi_server.TransportLinkedInPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-linked-in/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_linked_in_id_put(client):
    """Test case for api_transport_linked_in_id_put

    Replaces the TransportLinkedIn resource.
    """
    body = openapi_server.TransportLinkedInPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-linked-in/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_linked_in_post(client):
    """Test case for api_transport_linked_in_post

    Creates a TransportLinkedIn resource.
    """
    body = openapi_server.TransportLinkedInPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-linked-in',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

