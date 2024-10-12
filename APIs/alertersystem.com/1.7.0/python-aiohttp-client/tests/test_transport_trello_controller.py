# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_trello_get_collection200_response import ApiTransportTrelloGetCollection200Response
from openapi_server.models.transport_trello_get import TransportTrelloGet
from openapi_server.models.transport_trello_jsonld_get import TransportTrelloJsonldGet
from openapi_server.models.transport_trello_jsonld_post import TransportTrelloJsonldPost
from openapi_server.models.transport_trello_jsonld_put import TransportTrelloJsonldPut
from openapi_server.models.transport_trello_patch import TransportTrelloPatch
from openapi_server.models.transport_trello_post import TransportTrelloPost
from openapi_server.models.transport_trello_put import TransportTrelloPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_trello_get_collection(client):
    """Test case for api_transport_trello_get_collection

    Retrieves the collection of TransportTrello resources.
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
        path='/api/transport-trello',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_trello_id_delete(client):
    """Test case for api_transport_trello_id_delete

    Removes the TransportTrello resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-trello/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_trello_id_get(client):
    """Test case for api_transport_trello_id_get

    Retrieves a TransportTrello resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-trello/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_trello_id_patch(client):
    """Test case for api_transport_trello_id_patch

    Updates the TransportTrello resource.
    """
    body = openapi_server.TransportTrelloPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-trello/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_trello_id_put(client):
    """Test case for api_transport_trello_id_put

    Replaces the TransportTrello resource.
    """
    body = openapi_server.TransportTrelloPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-trello/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_trello_post(client):
    """Test case for api_transport_trello_post

    Creates a TransportTrello resource.
    """
    body = openapi_server.TransportTrelloPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-trello',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

