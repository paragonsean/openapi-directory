# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_smsmode_get_collection200_response import ApiTransportSmsmodeGetCollection200Response
from openapi_server.models.transport_smsmode_get import TransportSmsmodeGet
from openapi_server.models.transport_smsmode_jsonld_get import TransportSmsmodeJsonldGet
from openapi_server.models.transport_smsmode_jsonld_post import TransportSmsmodeJsonldPost
from openapi_server.models.transport_smsmode_jsonld_put import TransportSmsmodeJsonldPut
from openapi_server.models.transport_smsmode_patch import TransportSmsmodePatch
from openapi_server.models.transport_smsmode_post import TransportSmsmodePost
from openapi_server.models.transport_smsmode_put import TransportSmsmodePut


pytestmark = pytest.mark.asyncio

async def test_api_transport_smsmode_get_collection(client):
    """Test case for api_transport_smsmode_get_collection

    Retrieves the collection of TransportSmsmode resources.
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
        path='/api/transport-smsmode',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_smsmode_id_delete(client):
    """Test case for api_transport_smsmode_id_delete

    Removes the TransportSmsmode resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-smsmode/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_smsmode_id_get(client):
    """Test case for api_transport_smsmode_id_get

    Retrieves a TransportSmsmode resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-smsmode/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_smsmode_id_patch(client):
    """Test case for api_transport_smsmode_id_patch

    Updates the TransportSmsmode resource.
    """
    body = openapi_server.TransportSmsmodePatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-smsmode/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_smsmode_id_put(client):
    """Test case for api_transport_smsmode_id_put

    Replaces the TransportSmsmode resource.
    """
    body = openapi_server.TransportSmsmodePut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-smsmode/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_smsmode_post(client):
    """Test case for api_transport_smsmode_post

    Creates a TransportSmsmode resource.
    """
    body = openapi_server.TransportSmsmodePost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-smsmode',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

