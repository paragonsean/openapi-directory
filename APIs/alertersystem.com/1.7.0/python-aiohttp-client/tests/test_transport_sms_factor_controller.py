# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_sms_factor_get_collection200_response import ApiTransportSmsFactorGetCollection200Response
from openapi_server.models.transport_sms_factor_get import TransportSmsFactorGet
from openapi_server.models.transport_sms_factor_jsonld_get import TransportSmsFactorJsonldGet
from openapi_server.models.transport_sms_factor_jsonld_post import TransportSmsFactorJsonldPost
from openapi_server.models.transport_sms_factor_jsonld_put import TransportSmsFactorJsonldPut
from openapi_server.models.transport_sms_factor_patch import TransportSmsFactorPatch
from openapi_server.models.transport_sms_factor_post import TransportSmsFactorPost
from openapi_server.models.transport_sms_factor_put import TransportSmsFactorPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_sms_factor_get_collection(client):
    """Test case for api_transport_sms_factor_get_collection

    Retrieves the collection of TransportSmsFactor resources.
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
        path='/api/transport-sms-factor',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_sms_factor_id_delete(client):
    """Test case for api_transport_sms_factor_id_delete

    Removes the TransportSmsFactor resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-sms-factor/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_sms_factor_id_get(client):
    """Test case for api_transport_sms_factor_id_get

    Retrieves a TransportSmsFactor resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-sms-factor/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_sms_factor_id_patch(client):
    """Test case for api_transport_sms_factor_id_patch

    Updates the TransportSmsFactor resource.
    """
    body = openapi_server.TransportSmsFactorPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-sms-factor/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_sms_factor_id_put(client):
    """Test case for api_transport_sms_factor_id_put

    Replaces the TransportSmsFactor resource.
    """
    body = openapi_server.TransportSmsFactorPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-sms-factor/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_sms_factor_post(client):
    """Test case for api_transport_sms_factor_post

    Creates a TransportSmsFactor resource.
    """
    body = openapi_server.TransportSmsFactorPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-sms-factor',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

