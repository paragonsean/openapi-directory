# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.admin_mappings_get200_response_mappings_inner_request import AdminMappingsGet200ResponseMappingsInnerRequest
from openapi_server.models.admin_near_misses_request_post200_response import AdminNearMissesRequestPost200Response
from openapi_server.models.admin_near_misses_request_post_request import AdminNearMissesRequestPostRequest


pytestmark = pytest.mark.asyncio

async def test_admin_near_misses_request_pattern_post(client):
    """Test case for admin_near_misses_request_pattern_post

    Find near misses matching request pattern
    """
    body = {"headers":{"Content-Type":{"matches":".*/xml"}},"method":"POST","url":"/resource"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/__admin/near-misses/request-pattern',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_near_misses_request_post(client):
    """Test case for admin_near_misses_request_post

    Find near misses matching specific request
    """
    body = {"absoluteUrl":"http://localhost:8080/actual","body":"","bodyAsBase64":"","browserProxyRequest":false,"clientIp":"0:0:0:0:0:0:0:1","cookies":{},"headers":{"Accept":"*/*","Host":"localhost:8080","User-Agent":"curl/7.30.0"},"loggedDate":1467402464520,"loggedDateString":"2016-07-01T19:47:44Z","method":"GET","url":"/actual"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/__admin/near-misses/request',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_requests_unmatched_near_misses_get(client):
    """Test case for admin_requests_unmatched_near_misses_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/__admin/requests/unmatched/near-misses',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

