# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_pushbullet_get_collection200_response import ApiTransportPushbulletGetCollection200Response
from openapi_server.models.transport_pushbullet_get import TransportPushbulletGet
from openapi_server.models.transport_pushbullet_jsonld_get import TransportPushbulletJsonldGet
from openapi_server.models.transport_pushbullet_jsonld_post import TransportPushbulletJsonldPost
from openapi_server.models.transport_pushbullet_jsonld_put import TransportPushbulletJsonldPut
from openapi_server.models.transport_pushbullet_patch import TransportPushbulletPatch
from openapi_server.models.transport_pushbullet_post import TransportPushbulletPost
from openapi_server.models.transport_pushbullet_put import TransportPushbulletPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_pushbullet_get_collection(client):
    """Test case for api_transport_pushbullet_get_collection

    Retrieves the collection of TransportPushbullet resources.
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
        path='/api/transport-pushbullet',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_pushbullet_id_delete(client):
    """Test case for api_transport_pushbullet_id_delete

    Removes the TransportPushbullet resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-pushbullet/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_pushbullet_id_get(client):
    """Test case for api_transport_pushbullet_id_get

    Retrieves a TransportPushbullet resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-pushbullet/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_pushbullet_id_patch(client):
    """Test case for api_transport_pushbullet_id_patch

    Updates the TransportPushbullet resource.
    """
    body = openapi_server.TransportPushbulletPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-pushbullet/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_pushbullet_id_put(client):
    """Test case for api_transport_pushbullet_id_put

    Replaces the TransportPushbullet resource.
    """
    body = openapi_server.TransportPushbulletPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-pushbullet/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_pushbullet_post(client):
    """Test case for api_transport_pushbullet_post

    Creates a TransportPushbullet resource.
    """
    body = openapi_server.TransportPushbulletPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-pushbullet',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

