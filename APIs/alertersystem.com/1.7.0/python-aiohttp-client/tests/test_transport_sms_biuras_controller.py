# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_sms_biuras_get_collection200_response import ApiTransportSmsBiurasGetCollection200Response
from openapi_server.models.transport_sms_biuras_get import TransportSmsBiurasGet
from openapi_server.models.transport_sms_biuras_jsonld_get import TransportSmsBiurasJsonldGet
from openapi_server.models.transport_sms_biuras_jsonld_post import TransportSmsBiurasJsonldPost
from openapi_server.models.transport_sms_biuras_jsonld_put import TransportSmsBiurasJsonldPut
from openapi_server.models.transport_sms_biuras_patch import TransportSmsBiurasPatch
from openapi_server.models.transport_sms_biuras_post import TransportSmsBiurasPost
from openapi_server.models.transport_sms_biuras_put import TransportSmsBiurasPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_sms_biuras_get_collection(client):
    """Test case for api_transport_sms_biuras_get_collection

    Retrieves the collection of TransportSmsBiuras resources.
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
        path='/api/transport-sms-biuras',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_sms_biuras_id_delete(client):
    """Test case for api_transport_sms_biuras_id_delete

    Removes the TransportSmsBiuras resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-sms-biuras/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_sms_biuras_id_get(client):
    """Test case for api_transport_sms_biuras_id_get

    Retrieves a TransportSmsBiuras resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-sms-biuras/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_sms_biuras_id_patch(client):
    """Test case for api_transport_sms_biuras_id_patch

    Updates the TransportSmsBiuras resource.
    """
    body = openapi_server.TransportSmsBiurasPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-sms-biuras/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_sms_biuras_id_put(client):
    """Test case for api_transport_sms_biuras_id_put

    Replaces the TransportSmsBiuras resource.
    """
    body = openapi_server.TransportSmsBiurasPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-sms-biuras/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_sms_biuras_post(client):
    """Test case for api_transport_sms_biuras_post

    Creates a TransportSmsBiuras resource.
    """
    body = openapi_server.TransportSmsBiurasPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-sms-biuras',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

