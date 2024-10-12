# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_iqsms_get_collection200_response import ApiTransportIqsmsGetCollection200Response
from openapi_server.models.transport_iqsms_get import TransportIqsmsGet
from openapi_server.models.transport_iqsms_jsonld_get import TransportIqsmsJsonldGet
from openapi_server.models.transport_iqsms_jsonld_post import TransportIqsmsJsonldPost
from openapi_server.models.transport_iqsms_jsonld_put import TransportIqsmsJsonldPut
from openapi_server.models.transport_iqsms_patch import TransportIqsmsPatch
from openapi_server.models.transport_iqsms_post import TransportIqsmsPost
from openapi_server.models.transport_iqsms_put import TransportIqsmsPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_iqsms_get_collection(client):
    """Test case for api_transport_iqsms_get_collection

    Retrieves the collection of TransportIqsms resources.
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
        path='/api/transport-iqsms',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_iqsms_id_delete(client):
    """Test case for api_transport_iqsms_id_delete

    Removes the TransportIqsms resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-iqsms/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_iqsms_id_get(client):
    """Test case for api_transport_iqsms_id_get

    Retrieves a TransportIqsms resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-iqsms/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_iqsms_id_patch(client):
    """Test case for api_transport_iqsms_id_patch

    Updates the TransportIqsms resource.
    """
    body = openapi_server.TransportIqsmsPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-iqsms/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_iqsms_id_put(client):
    """Test case for api_transport_iqsms_id_put

    Replaces the TransportIqsms resource.
    """
    body = openapi_server.TransportIqsmsPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-iqsms/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_iqsms_post(client):
    """Test case for api_transport_iqsms_post

    Creates a TransportIqsms resource.
    """
    body = openapi_server.TransportIqsmsPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-iqsms',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

