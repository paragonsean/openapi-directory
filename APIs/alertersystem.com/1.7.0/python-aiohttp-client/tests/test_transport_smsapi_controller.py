# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_smsapi_get_collection200_response import ApiTransportSmsapiGetCollection200Response
from openapi_server.models.transport_smsapi_get import TransportSmsapiGet
from openapi_server.models.transport_smsapi_jsonld_get import TransportSmsapiJsonldGet
from openapi_server.models.transport_smsapi_jsonld_post import TransportSmsapiJsonldPost
from openapi_server.models.transport_smsapi_jsonld_put import TransportSmsapiJsonldPut
from openapi_server.models.transport_smsapi_patch import TransportSmsapiPatch
from openapi_server.models.transport_smsapi_post import TransportSmsapiPost
from openapi_server.models.transport_smsapi_put import TransportSmsapiPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_smsapi_get_collection(client):
    """Test case for api_transport_smsapi_get_collection

    Retrieves the collection of TransportSmsapi resources.
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
        path='/api/transport-smsapi',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_smsapi_id_delete(client):
    """Test case for api_transport_smsapi_id_delete

    Removes the TransportSmsapi resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-smsapi/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_smsapi_id_get(client):
    """Test case for api_transport_smsapi_id_get

    Retrieves a TransportSmsapi resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-smsapi/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_smsapi_id_patch(client):
    """Test case for api_transport_smsapi_id_patch

    Updates the TransportSmsapi resource.
    """
    body = openapi_server.TransportSmsapiPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-smsapi/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_smsapi_id_put(client):
    """Test case for api_transport_smsapi_id_put

    Replaces the TransportSmsapi resource.
    """
    body = openapi_server.TransportSmsapiPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-smsapi/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_smsapi_post(client):
    """Test case for api_transport_smsapi_post

    Creates a TransportSmsapi resource.
    """
    body = openapi_server.TransportSmsapiPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-smsapi',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

