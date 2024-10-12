# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_gateway_api_get_collection200_response import ApiTransportGatewayApiGetCollection200Response
from openapi_server.models.transport_gateway_api_get import TransportGatewayApiGet
from openapi_server.models.transport_gateway_api_jsonld_get import TransportGatewayApiJsonldGet
from openapi_server.models.transport_gateway_api_jsonld_post import TransportGatewayApiJsonldPost
from openapi_server.models.transport_gateway_api_jsonld_put import TransportGatewayApiJsonldPut
from openapi_server.models.transport_gateway_api_patch import TransportGatewayApiPatch
from openapi_server.models.transport_gateway_api_post import TransportGatewayApiPost
from openapi_server.models.transport_gateway_api_put import TransportGatewayApiPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_gateway_api_get_collection(client):
    """Test case for api_transport_gateway_api_get_collection

    Retrieves the collection of TransportGatewayApi resources.
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
        path='/api/transport-gateway-api',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_gateway_api_id_delete(client):
    """Test case for api_transport_gateway_api_id_delete

    Removes the TransportGatewayApi resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-gateway-api/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_gateway_api_id_get(client):
    """Test case for api_transport_gateway_api_id_get

    Retrieves a TransportGatewayApi resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-gateway-api/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_gateway_api_id_patch(client):
    """Test case for api_transport_gateway_api_id_patch

    Updates the TransportGatewayApi resource.
    """
    body = openapi_server.TransportGatewayApiPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-gateway-api/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_gateway_api_id_put(client):
    """Test case for api_transport_gateway_api_id_put

    Replaces the TransportGatewayApi resource.
    """
    body = openapi_server.TransportGatewayApiPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-gateway-api/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_gateway_api_post(client):
    """Test case for api_transport_gateway_api_post

    Creates a TransportGatewayApi resource.
    """
    body = openapi_server.TransportGatewayApiPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-gateway-api',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

