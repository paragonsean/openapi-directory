# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_amazon_sns_get_collection200_response import ApiTransportAmazonSnsGetCollection200Response
from openapi_server.models.transport_amazon_sns_get import TransportAmazonSnsGet
from openapi_server.models.transport_amazon_sns_jsonld_get import TransportAmazonSnsJsonldGet
from openapi_server.models.transport_amazon_sns_jsonld_post import TransportAmazonSnsJsonldPost
from openapi_server.models.transport_amazon_sns_jsonld_put import TransportAmazonSnsJsonldPut
from openapi_server.models.transport_amazon_sns_patch import TransportAmazonSnsPatch
from openapi_server.models.transport_amazon_sns_post import TransportAmazonSnsPost
from openapi_server.models.transport_amazon_sns_put import TransportAmazonSnsPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_amazon_sns_get_collection(client):
    """Test case for api_transport_amazon_sns_get_collection

    Retrieves the collection of TransportAmazonSns resources.
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
        path='/api/transport-amazon-sns',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_amazon_sns_id_delete(client):
    """Test case for api_transport_amazon_sns_id_delete

    Removes the TransportAmazonSns resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-amazon-sns/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_amazon_sns_id_get(client):
    """Test case for api_transport_amazon_sns_id_get

    Retrieves a TransportAmazonSns resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-amazon-sns/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_amazon_sns_id_patch(client):
    """Test case for api_transport_amazon_sns_id_patch

    Updates the TransportAmazonSns resource.
    """
    body = openapi_server.TransportAmazonSnsPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-amazon-sns/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_amazon_sns_id_put(client):
    """Test case for api_transport_amazon_sns_id_put

    Replaces the TransportAmazonSns resource.
    """
    body = openapi_server.TransportAmazonSnsPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-amazon-sns/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_amazon_sns_post(client):
    """Test case for api_transport_amazon_sns_post

    Creates a TransportAmazonSns resource.
    """
    body = openapi_server.TransportAmazonSnsPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-amazon-sns',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

