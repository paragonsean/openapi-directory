# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_infobip_get_collection200_response import ApiTransportInfobipGetCollection200Response
from openapi_server.models.transport_infobip_get import TransportInfobipGet
from openapi_server.models.transport_infobip_jsonld_get import TransportInfobipJsonldGet
from openapi_server.models.transport_infobip_jsonld_post import TransportInfobipJsonldPost
from openapi_server.models.transport_infobip_jsonld_put import TransportInfobipJsonldPut
from openapi_server.models.transport_infobip_patch import TransportInfobipPatch
from openapi_server.models.transport_infobip_post import TransportInfobipPost
from openapi_server.models.transport_infobip_put import TransportInfobipPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_infobip_get_collection(client):
    """Test case for api_transport_infobip_get_collection

    Retrieves the collection of TransportInfobip resources.
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
        path='/api/transport-infobip',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_infobip_id_delete(client):
    """Test case for api_transport_infobip_id_delete

    Removes the TransportInfobip resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-infobip/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_infobip_id_get(client):
    """Test case for api_transport_infobip_id_get

    Retrieves a TransportInfobip resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-infobip/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_infobip_id_patch(client):
    """Test case for api_transport_infobip_id_patch

    Updates the TransportInfobip resource.
    """
    body = openapi_server.TransportInfobipPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-infobip/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_infobip_id_put(client):
    """Test case for api_transport_infobip_id_put

    Replaces the TransportInfobip resource.
    """
    body = openapi_server.TransportInfobipPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-infobip/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_infobip_post(client):
    """Test case for api_transport_infobip_post

    Creates a TransportInfobip resource.
    """
    body = openapi_server.TransportInfobipPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-infobip',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

