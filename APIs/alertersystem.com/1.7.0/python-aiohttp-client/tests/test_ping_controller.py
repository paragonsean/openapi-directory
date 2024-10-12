# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_ping_get_collection200_response import ApiPingGetCollection200Response
from openapi_server.models.ping_get import PingGet
from openapi_server.models.ping_jsonld_get import PingJsonldGet
from openapi_server.models.ping_jsonld_post import PingJsonldPost
from openapi_server.models.ping_post import PingPost


pytestmark = pytest.mark.asyncio

async def test_api_ping_get_collection(client):
    """Test case for api_ping_get_collection

    Retrieves the collection of Ping resources.
    """
    params = [('page', 1),
                    ('dataSegmentCode', 'data_segment_code_example'),
                    ('dataSegmentCode[]', ['data_segment_code_example']),
                    ('monitor', 'monitor_example'),
                    ('monitor[]', ['monitor_example']),
                    ('partition', 'partition_example'),
                    ('partition[]', ['partition_example']),
                    ('properties[]', ['properties_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/ping',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_ping_id_get(client):
    """Test case for api_ping_id_get

    Retrieves a Ping resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/ping/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_ping_post(client):
    """Test case for api_ping_post

    Creates a Ping resource.
    """
    body = openapi_server.PingPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/ping',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

