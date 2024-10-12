# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_twilio_get_collection200_response import ApiTransportTwilioGetCollection200Response
from openapi_server.models.transport_twilio_get import TransportTwilioGet
from openapi_server.models.transport_twilio_jsonld_get import TransportTwilioJsonldGet
from openapi_server.models.transport_twilio_jsonld_post import TransportTwilioJsonldPost
from openapi_server.models.transport_twilio_jsonld_put import TransportTwilioJsonldPut
from openapi_server.models.transport_twilio_patch import TransportTwilioPatch
from openapi_server.models.transport_twilio_post import TransportTwilioPost
from openapi_server.models.transport_twilio_put import TransportTwilioPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_twilio_get_collection(client):
    """Test case for api_transport_twilio_get_collection

    Retrieves the collection of TransportTwilio resources.
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
        path='/api/transport-twilio',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_twilio_id_delete(client):
    """Test case for api_transport_twilio_id_delete

    Removes the TransportTwilio resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-twilio/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_twilio_id_get(client):
    """Test case for api_transport_twilio_id_get

    Retrieves a TransportTwilio resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-twilio/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_twilio_id_patch(client):
    """Test case for api_transport_twilio_id_patch

    Updates the TransportTwilio resource.
    """
    body = openapi_server.TransportTwilioPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-twilio/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_twilio_id_put(client):
    """Test case for api_transport_twilio_id_put

    Replaces the TransportTwilio resource.
    """
    body = openapi_server.TransportTwilioPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-twilio/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_twilio_post(client):
    """Test case for api_transport_twilio_post

    Creates a TransportTwilio resource.
    """
    body = openapi_server.TransportTwilioPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-twilio',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

