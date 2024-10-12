# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_clickatell_get_collection200_response import ApiTransportClickatellGetCollection200Response
from openapi_server.models.transport_clickatell_get import TransportClickatellGet
from openapi_server.models.transport_clickatell_jsonld_get import TransportClickatellJsonldGet
from openapi_server.models.transport_clickatell_jsonld_post import TransportClickatellJsonldPost
from openapi_server.models.transport_clickatell_jsonld_put import TransportClickatellJsonldPut
from openapi_server.models.transport_clickatell_patch import TransportClickatellPatch
from openapi_server.models.transport_clickatell_post import TransportClickatellPost
from openapi_server.models.transport_clickatell_put import TransportClickatellPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_clickatell_get_collection(client):
    """Test case for api_transport_clickatell_get_collection

    Retrieves the collection of TransportClickatell resources.
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
        path='/api/transport-clickatell',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_clickatell_id_delete(client):
    """Test case for api_transport_clickatell_id_delete

    Removes the TransportClickatell resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-clickatell/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_clickatell_id_get(client):
    """Test case for api_transport_clickatell_id_get

    Retrieves a TransportClickatell resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-clickatell/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_clickatell_id_patch(client):
    """Test case for api_transport_clickatell_id_patch

    Updates the TransportClickatell resource.
    """
    body = openapi_server.TransportClickatellPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-clickatell/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_clickatell_id_put(client):
    """Test case for api_transport_clickatell_id_put

    Replaces the TransportClickatell resource.
    """
    body = openapi_server.TransportClickatellPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-clickatell/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_clickatell_post(client):
    """Test case for api_transport_clickatell_post

    Creates a TransportClickatell resource.
    """
    body = openapi_server.TransportClickatellPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-clickatell',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

