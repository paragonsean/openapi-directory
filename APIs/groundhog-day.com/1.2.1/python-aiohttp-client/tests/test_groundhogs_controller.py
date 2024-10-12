# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.groundhog200_response import Groundhog200Response
from openapi_server.models.groundhog400_response import Groundhog400Response
from openapi_server.models.groundhogs200_response import Groundhogs200Response


pytestmark = pytest.mark.asyncio

async def test_groundhog(client):
    """Test case for groundhog

    Get a groundhog by slug
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/pcraig3/groundhog-day-api/1.2.1/api/v1/groundhogs/{slug}'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_groundhogs(client):
    """Test case for groundhogs

    Get all groundhogs
    """
    params = [('country', 'Canada or USA'),
                    ('isGroundhog', 'is_groundhog_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/pcraig3/groundhog-day-api/1.2.1/api/v1/groundhogs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

