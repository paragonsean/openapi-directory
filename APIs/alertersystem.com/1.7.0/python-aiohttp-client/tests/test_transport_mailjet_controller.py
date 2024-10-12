# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_mailjet_get_collection200_response import ApiTransportMailjetGetCollection200Response
from openapi_server.models.transport_mailjet_get import TransportMailjetGet
from openapi_server.models.transport_mailjet_jsonld_get import TransportMailjetJsonldGet
from openapi_server.models.transport_mailjet_jsonld_post import TransportMailjetJsonldPost
from openapi_server.models.transport_mailjet_jsonld_put import TransportMailjetJsonldPut
from openapi_server.models.transport_mailjet_patch import TransportMailjetPatch
from openapi_server.models.transport_mailjet_post import TransportMailjetPost
from openapi_server.models.transport_mailjet_put import TransportMailjetPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_mailjet_get_collection(client):
    """Test case for api_transport_mailjet_get_collection

    Retrieves the collection of TransportMailjet resources.
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
        path='/api/transport-mailjet',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_mailjet_id_delete(client):
    """Test case for api_transport_mailjet_id_delete

    Removes the TransportMailjet resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-mailjet/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_mailjet_id_get(client):
    """Test case for api_transport_mailjet_id_get

    Retrieves a TransportMailjet resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-mailjet/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_mailjet_id_patch(client):
    """Test case for api_transport_mailjet_id_patch

    Updates the TransportMailjet resource.
    """
    body = openapi_server.TransportMailjetPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-mailjet/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_mailjet_id_put(client):
    """Test case for api_transport_mailjet_id_put

    Replaces the TransportMailjet resource.
    """
    body = openapi_server.TransportMailjetPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-mailjet/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_mailjet_post(client):
    """Test case for api_transport_mailjet_post

    Creates a TransportMailjet resource.
    """
    body = openapi_server.TransportMailjetPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-mailjet',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

