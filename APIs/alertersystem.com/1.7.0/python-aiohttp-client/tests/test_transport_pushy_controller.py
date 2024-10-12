# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_pushy_get_collection200_response import ApiTransportPushyGetCollection200Response
from openapi_server.models.transport_pushy_get import TransportPushyGet
from openapi_server.models.transport_pushy_jsonld_get import TransportPushyJsonldGet
from openapi_server.models.transport_pushy_jsonld_post import TransportPushyJsonldPost
from openapi_server.models.transport_pushy_jsonld_put import TransportPushyJsonldPut
from openapi_server.models.transport_pushy_patch import TransportPushyPatch
from openapi_server.models.transport_pushy_post import TransportPushyPost
from openapi_server.models.transport_pushy_put import TransportPushyPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_pushy_get_collection(client):
    """Test case for api_transport_pushy_get_collection

    Retrieves the collection of TransportPushy resources.
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
        path='/api/transport-pushy',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_pushy_id_delete(client):
    """Test case for api_transport_pushy_id_delete

    Removes the TransportPushy resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-pushy/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_pushy_id_get(client):
    """Test case for api_transport_pushy_id_get

    Retrieves a TransportPushy resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-pushy/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_pushy_id_patch(client):
    """Test case for api_transport_pushy_id_patch

    Updates the TransportPushy resource.
    """
    body = openapi_server.TransportPushyPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-pushy/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_pushy_id_put(client):
    """Test case for api_transport_pushy_id_put

    Replaces the TransportPushy resource.
    """
    body = openapi_server.TransportPushyPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-pushy/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_pushy_post(client):
    """Test case for api_transport_pushy_post

    Creates a TransportPushy resource.
    """
    body = openapi_server.TransportPushyPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-pushy',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

