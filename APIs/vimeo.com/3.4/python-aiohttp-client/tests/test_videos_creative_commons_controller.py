# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.creative_commons import CreativeCommons


pytestmark = pytest.mark.asyncio

async def test_get_cc_licenses(client):
    """Test case for get_cc_licenses

    Get all Creative Commons licenses
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.creativecommons+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/creativecommons',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

