# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_all_my_sms_get_collection200_response import ApiTransportAllMySmsGetCollection200Response
from openapi_server.models.transport_all_my_sms_get import TransportAllMySmsGet
from openapi_server.models.transport_all_my_sms_jsonld_get import TransportAllMySmsJsonldGet
from openapi_server.models.transport_all_my_sms_jsonld_post import TransportAllMySmsJsonldPost
from openapi_server.models.transport_all_my_sms_jsonld_put import TransportAllMySmsJsonldPut
from openapi_server.models.transport_all_my_sms_patch import TransportAllMySmsPatch
from openapi_server.models.transport_all_my_sms_post import TransportAllMySmsPost
from openapi_server.models.transport_all_my_sms_put import TransportAllMySmsPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_all_my_sms_get_collection(client):
    """Test case for api_transport_all_my_sms_get_collection

    Retrieves the collection of TransportAllMySms resources.
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
        path='/api/transport-all-my-sms',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_all_my_sms_id_delete(client):
    """Test case for api_transport_all_my_sms_id_delete

    Removes the TransportAllMySms resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-all-my-sms/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_all_my_sms_id_get(client):
    """Test case for api_transport_all_my_sms_id_get

    Retrieves a TransportAllMySms resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-all-my-sms/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_all_my_sms_id_patch(client):
    """Test case for api_transport_all_my_sms_id_patch

    Updates the TransportAllMySms resource.
    """
    body = openapi_server.TransportAllMySmsPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-all-my-sms/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_all_my_sms_id_put(client):
    """Test case for api_transport_all_my_sms_id_put

    Replaces the TransportAllMySms resource.
    """
    body = openapi_server.TransportAllMySmsPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-all-my-sms/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_all_my_sms_post(client):
    """Test case for api_transport_all_my_sms_post

    Creates a TransportAllMySms resource.
    """
    body = openapi_server.TransportAllMySmsPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-all-my-sms',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

