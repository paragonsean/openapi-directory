# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_termii_get_collection200_response import ApiTransportTermiiGetCollection200Response
from openapi_server.models.transport_termii_get import TransportTermiiGet
from openapi_server.models.transport_termii_jsonld_get import TransportTermiiJsonldGet
from openapi_server.models.transport_termii_jsonld_post import TransportTermiiJsonldPost
from openapi_server.models.transport_termii_jsonld_put import TransportTermiiJsonldPut
from openapi_server.models.transport_termii_patch import TransportTermiiPatch
from openapi_server.models.transport_termii_post import TransportTermiiPost
from openapi_server.models.transport_termii_put import TransportTermiiPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_termii_get_collection(client):
    """Test case for api_transport_termii_get_collection

    Retrieves the collection of TransportTermii resources.
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
        path='/api/transport-termii',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_termii_id_delete(client):
    """Test case for api_transport_termii_id_delete

    Removes the TransportTermii resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-termii/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_termii_id_get(client):
    """Test case for api_transport_termii_id_get

    Retrieves a TransportTermii resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-termii/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_termii_id_patch(client):
    """Test case for api_transport_termii_id_patch

    Updates the TransportTermii resource.
    """
    body = openapi_server.TransportTermiiPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-termii/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_termii_id_put(client):
    """Test case for api_transport_termii_id_put

    Replaces the TransportTermii resource.
    """
    body = openapi_server.TransportTermiiPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-termii/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_termii_post(client):
    """Test case for api_transport_termii_post

    Creates a TransportTermii resource.
    """
    body = openapi_server.TransportTermiiPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-termii',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

