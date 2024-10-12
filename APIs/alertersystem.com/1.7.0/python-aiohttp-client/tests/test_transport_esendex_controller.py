# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_esendex_get_collection200_response import ApiTransportEsendexGetCollection200Response
from openapi_server.models.transport_esendex_get import TransportEsendexGet
from openapi_server.models.transport_esendex_jsonld_get import TransportEsendexJsonldGet
from openapi_server.models.transport_esendex_jsonld_post import TransportEsendexJsonldPost
from openapi_server.models.transport_esendex_jsonld_put import TransportEsendexJsonldPut
from openapi_server.models.transport_esendex_patch import TransportEsendexPatch
from openapi_server.models.transport_esendex_post import TransportEsendexPost
from openapi_server.models.transport_esendex_put import TransportEsendexPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_esendex_get_collection(client):
    """Test case for api_transport_esendex_get_collection

    Retrieves the collection of TransportEsendex resources.
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
        path='/api/transport-esendex',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_esendex_id_delete(client):
    """Test case for api_transport_esendex_id_delete

    Removes the TransportEsendex resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-esendex/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_esendex_id_get(client):
    """Test case for api_transport_esendex_id_get

    Retrieves a TransportEsendex resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-esendex/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_esendex_id_patch(client):
    """Test case for api_transport_esendex_id_patch

    Updates the TransportEsendex resource.
    """
    body = openapi_server.TransportEsendexPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-esendex/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_esendex_id_put(client):
    """Test case for api_transport_esendex_id_put

    Replaces the TransportEsendex resource.
    """
    body = openapi_server.TransportEsendexPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-esendex/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_esendex_post(client):
    """Test case for api_transport_esendex_post

    Creates a TransportEsendex resource.
    """
    body = openapi_server.TransportEsendexPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-esendex',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

