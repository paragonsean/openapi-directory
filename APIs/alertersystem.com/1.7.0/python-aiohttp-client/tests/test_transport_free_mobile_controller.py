# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_free_mobile_get_collection200_response import ApiTransportFreeMobileGetCollection200Response
from openapi_server.models.transport_free_mobile_get import TransportFreeMobileGet
from openapi_server.models.transport_free_mobile_jsonld_get import TransportFreeMobileJsonldGet
from openapi_server.models.transport_free_mobile_jsonld_post import TransportFreeMobileJsonldPost
from openapi_server.models.transport_free_mobile_jsonld_put import TransportFreeMobileJsonldPut
from openapi_server.models.transport_free_mobile_patch import TransportFreeMobilePatch
from openapi_server.models.transport_free_mobile_post import TransportFreeMobilePost
from openapi_server.models.transport_free_mobile_put import TransportFreeMobilePut


pytestmark = pytest.mark.asyncio

async def test_api_transport_free_mobile_get_collection(client):
    """Test case for api_transport_free_mobile_get_collection

    Retrieves the collection of TransportFreeMobile resources.
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
        path='/api/transport-free-mobile',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_free_mobile_id_delete(client):
    """Test case for api_transport_free_mobile_id_delete

    Removes the TransportFreeMobile resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-free-mobile/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_free_mobile_id_get(client):
    """Test case for api_transport_free_mobile_id_get

    Retrieves a TransportFreeMobile resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-free-mobile/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_free_mobile_id_patch(client):
    """Test case for api_transport_free_mobile_id_patch

    Updates the TransportFreeMobile resource.
    """
    body = openapi_server.TransportFreeMobilePatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-free-mobile/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_free_mobile_id_put(client):
    """Test case for api_transport_free_mobile_id_put

    Replaces the TransportFreeMobile resource.
    """
    body = openapi_server.TransportFreeMobilePut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-free-mobile/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_free_mobile_post(client):
    """Test case for api_transport_free_mobile_post

    Creates a TransportFreeMobile resource.
    """
    body = openapi_server.TransportFreeMobilePost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-free-mobile',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

