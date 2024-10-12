# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_sendinblue_get_collection200_response import ApiTransportSendinblueGetCollection200Response
from openapi_server.models.transport_sendinblue_get import TransportSendinblueGet
from openapi_server.models.transport_sendinblue_jsonld_get import TransportSendinblueJsonldGet
from openapi_server.models.transport_sendinblue_jsonld_post import TransportSendinblueJsonldPost
from openapi_server.models.transport_sendinblue_jsonld_put import TransportSendinblueJsonldPut
from openapi_server.models.transport_sendinblue_patch import TransportSendinbluePatch
from openapi_server.models.transport_sendinblue_post import TransportSendinbluePost
from openapi_server.models.transport_sendinblue_put import TransportSendinbluePut


pytestmark = pytest.mark.asyncio

async def test_api_transport_sendinblue_get_collection(client):
    """Test case for api_transport_sendinblue_get_collection

    Retrieves the collection of TransportSendinblue resources.
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
        path='/api/transport-sendinblue',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_sendinblue_id_delete(client):
    """Test case for api_transport_sendinblue_id_delete

    Removes the TransportSendinblue resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-sendinblue/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_sendinblue_id_get(client):
    """Test case for api_transport_sendinblue_id_get

    Retrieves a TransportSendinblue resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-sendinblue/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_sendinblue_id_patch(client):
    """Test case for api_transport_sendinblue_id_patch

    Updates the TransportSendinblue resource.
    """
    body = openapi_server.TransportSendinbluePatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-sendinblue/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_sendinblue_id_put(client):
    """Test case for api_transport_sendinblue_id_put

    Replaces the TransportSendinblue resource.
    """
    body = openapi_server.TransportSendinbluePut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-sendinblue/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_sendinblue_post(client):
    """Test case for api_transport_sendinblue_post

    Creates a TransportSendinblue resource.
    """
    body = openapi_server.TransportSendinbluePost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-sendinblue',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

