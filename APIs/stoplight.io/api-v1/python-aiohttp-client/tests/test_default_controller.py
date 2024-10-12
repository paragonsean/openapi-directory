# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.post_versions_publish_anon200_response import POSTVersionsPublishAnon200Response
from openapi_server.models.post_versions_publish_anon_request import POSTVersionsPublishAnonRequest


pytestmark = pytest.mark.asyncio

async def test_p_ost_versions_publish_anon(client):
    """Test case for p_ost_versions_publish_anon

    Publish Anonymous
    """
    body = openapi_server.POSTVersionsPublishAnonRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/versions/publish/anon',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

