# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_orange_sms_get_collection200_response import ApiTransportOrangeSmsGetCollection200Response
from openapi_server.models.transport_orange_sms_get import TransportOrangeSmsGet
from openapi_server.models.transport_orange_sms_jsonld_get import TransportOrangeSmsJsonldGet
from openapi_server.models.transport_orange_sms_jsonld_post import TransportOrangeSmsJsonldPost
from openapi_server.models.transport_orange_sms_jsonld_put import TransportOrangeSmsJsonldPut
from openapi_server.models.transport_orange_sms_patch import TransportOrangeSmsPatch
from openapi_server.models.transport_orange_sms_post import TransportOrangeSmsPost
from openapi_server.models.transport_orange_sms_put import TransportOrangeSmsPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_orange_sms_get_collection(client):
    """Test case for api_transport_orange_sms_get_collection

    Retrieves the collection of TransportOrangeSms resources.
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
        path='/api/transport-orange-sms',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_orange_sms_id_delete(client):
    """Test case for api_transport_orange_sms_id_delete

    Removes the TransportOrangeSms resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-orange-sms/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_orange_sms_id_get(client):
    """Test case for api_transport_orange_sms_id_get

    Retrieves a TransportOrangeSms resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-orange-sms/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_orange_sms_id_patch(client):
    """Test case for api_transport_orange_sms_id_patch

    Updates the TransportOrangeSms resource.
    """
    body = openapi_server.TransportOrangeSmsPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-orange-sms/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_orange_sms_id_put(client):
    """Test case for api_transport_orange_sms_id_put

    Replaces the TransportOrangeSms resource.
    """
    body = openapi_server.TransportOrangeSmsPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-orange-sms/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_orange_sms_post(client):
    """Test case for api_transport_orange_sms_post

    Creates a TransportOrangeSms resource.
    """
    body = openapi_server.TransportOrangeSmsPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-orange-sms',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

