# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_gitter_get_collection200_response import ApiTransportGitterGetCollection200Response
from openapi_server.models.transport_gitter_get import TransportGitterGet
from openapi_server.models.transport_gitter_jsonld_get import TransportGitterJsonldGet
from openapi_server.models.transport_gitter_jsonld_post import TransportGitterJsonldPost
from openapi_server.models.transport_gitter_jsonld_put import TransportGitterJsonldPut
from openapi_server.models.transport_gitter_patch import TransportGitterPatch
from openapi_server.models.transport_gitter_post import TransportGitterPost
from openapi_server.models.transport_gitter_put import TransportGitterPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_gitter_get_collection(client):
    """Test case for api_transport_gitter_get_collection

    Retrieves the collection of TransportGitter resources.
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
        path='/api/transport-gitter',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_gitter_id_delete(client):
    """Test case for api_transport_gitter_id_delete

    Removes the TransportGitter resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-gitter/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_gitter_id_get(client):
    """Test case for api_transport_gitter_id_get

    Retrieves a TransportGitter resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-gitter/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_gitter_id_patch(client):
    """Test case for api_transport_gitter_id_patch

    Updates the TransportGitter resource.
    """
    body = openapi_server.TransportGitterPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-gitter/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_gitter_id_put(client):
    """Test case for api_transport_gitter_id_put

    Replaces the TransportGitter resource.
    """
    body = openapi_server.TransportGitterPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-gitter/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_gitter_post(client):
    """Test case for api_transport_gitter_post

    Creates a TransportGitter resource.
    """
    body = openapi_server.TransportGitterPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-gitter',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

