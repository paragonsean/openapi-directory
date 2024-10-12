# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.feature import Feature


pytestmark = pytest.mark.asyncio

async def test_get_features(client):
    """Test case for get_features

    Retrieve supported features
    """
    params = [('language', 'language_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/features.{content_type}'.format(content_type='content_type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

