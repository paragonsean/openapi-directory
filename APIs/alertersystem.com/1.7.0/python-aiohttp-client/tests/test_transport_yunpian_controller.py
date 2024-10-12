# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_yunpian_get_collection200_response import ApiTransportYunpianGetCollection200Response
from openapi_server.models.transport_yunpian_get import TransportYunpianGet
from openapi_server.models.transport_yunpian_jsonld_get import TransportYunpianJsonldGet
from openapi_server.models.transport_yunpian_jsonld_post import TransportYunpianJsonldPost
from openapi_server.models.transport_yunpian_jsonld_put import TransportYunpianJsonldPut
from openapi_server.models.transport_yunpian_patch import TransportYunpianPatch
from openapi_server.models.transport_yunpian_post import TransportYunpianPost
from openapi_server.models.transport_yunpian_put import TransportYunpianPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_yunpian_get_collection(client):
    """Test case for api_transport_yunpian_get_collection

    Retrieves the collection of TransportYunpian resources.
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
        path='/api/transport-yunpian',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_yunpian_id_delete(client):
    """Test case for api_transport_yunpian_id_delete

    Removes the TransportYunpian resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-yunpian/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_yunpian_id_get(client):
    """Test case for api_transport_yunpian_id_get

    Retrieves a TransportYunpian resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-yunpian/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_yunpian_id_patch(client):
    """Test case for api_transport_yunpian_id_patch

    Updates the TransportYunpian resource.
    """
    body = openapi_server.TransportYunpianPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-yunpian/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_yunpian_id_put(client):
    """Test case for api_transport_yunpian_id_put

    Replaces the TransportYunpian resource.
    """
    body = openapi_server.TransportYunpianPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-yunpian/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_yunpian_post(client):
    """Test case for api_transport_yunpian_post

    Creates a TransportYunpian resource.
    """
    body = openapi_server.TransportYunpianPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-yunpian',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

