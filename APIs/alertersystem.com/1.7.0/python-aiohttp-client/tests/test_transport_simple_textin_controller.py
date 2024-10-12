# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_simple_textin_get_collection200_response import ApiTransportSimpleTextinGetCollection200Response
from openapi_server.models.transport_simple_textin_get import TransportSimpleTextinGet
from openapi_server.models.transport_simple_textin_jsonld_get import TransportSimpleTextinJsonldGet
from openapi_server.models.transport_simple_textin_jsonld_post import TransportSimpleTextinJsonldPost
from openapi_server.models.transport_simple_textin_jsonld_put import TransportSimpleTextinJsonldPut
from openapi_server.models.transport_simple_textin_patch import TransportSimpleTextinPatch
from openapi_server.models.transport_simple_textin_post import TransportSimpleTextinPost
from openapi_server.models.transport_simple_textin_put import TransportSimpleTextinPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_simple_textin_get_collection(client):
    """Test case for api_transport_simple_textin_get_collection

    Retrieves the collection of TransportSimpleTextin resources.
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
        path='/api/transport-simple-textin',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_simple_textin_id_delete(client):
    """Test case for api_transport_simple_textin_id_delete

    Removes the TransportSimpleTextin resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-simple-textin/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_simple_textin_id_get(client):
    """Test case for api_transport_simple_textin_id_get

    Retrieves a TransportSimpleTextin resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-simple-textin/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_simple_textin_id_patch(client):
    """Test case for api_transport_simple_textin_id_patch

    Updates the TransportSimpleTextin resource.
    """
    body = openapi_server.TransportSimpleTextinPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-simple-textin/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_simple_textin_id_put(client):
    """Test case for api_transport_simple_textin_id_put

    Replaces the TransportSimpleTextin resource.
    """
    body = openapi_server.TransportSimpleTextinPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-simple-textin/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_simple_textin_post(client):
    """Test case for api_transport_simple_textin_post

    Creates a TransportSimpleTextin resource.
    """
    body = openapi_server.TransportSimpleTextinPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-simple-textin',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

