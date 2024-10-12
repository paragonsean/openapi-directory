# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_sms77_get_collection200_response import ApiTransportSms77GetCollection200Response
from openapi_server.models.transport_sms77_get import TransportSms77Get
from openapi_server.models.transport_sms77_jsonld_get import TransportSms77JsonldGet
from openapi_server.models.transport_sms77_jsonld_post import TransportSms77JsonldPost
from openapi_server.models.transport_sms77_jsonld_put import TransportSms77JsonldPut
from openapi_server.models.transport_sms77_patch import TransportSms77Patch
from openapi_server.models.transport_sms77_post import TransportSms77Post
from openapi_server.models.transport_sms77_put import TransportSms77Put


pytestmark = pytest.mark.asyncio

async def test_api_transport_sms77_get_collection(client):
    """Test case for api_transport_sms77_get_collection

    Retrieves the collection of TransportSms77 resources.
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
        path='/api/transport-sms77',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_sms77_id_delete(client):
    """Test case for api_transport_sms77_id_delete

    Removes the TransportSms77 resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-sms77/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_sms77_id_get(client):
    """Test case for api_transport_sms77_id_get

    Retrieves a TransportSms77 resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-sms77/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_sms77_id_patch(client):
    """Test case for api_transport_sms77_id_patch

    Updates the TransportSms77 resource.
    """
    body = openapi_server.TransportSms77Patch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-sms77/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_sms77_id_put(client):
    """Test case for api_transport_sms77_id_put

    Replaces the TransportSms77 resource.
    """
    body = openapi_server.TransportSms77Put()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-sms77/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_sms77_post(client):
    """Test case for api_transport_sms77_post

    Creates a TransportSms77 resource.
    """
    body = openapi_server.TransportSms77Post()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-sms77',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

