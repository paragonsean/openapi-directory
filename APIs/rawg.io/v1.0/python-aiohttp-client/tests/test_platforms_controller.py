# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.platform_single import PlatformSingle
from openapi_server.models.platforms_list200_response import PlatformsList200Response
from openapi_server.models.platforms_lists_parents_list200_response import PlatformsListsParentsList200Response


pytestmark = pytest.mark.asyncio

async def test_platforms_list(client):
    """Test case for platforms_list

    Get a list of video game platforms.
    """
    params = [('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/platforms',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_platforms_lists_parents_list(client):
    """Test case for platforms_lists_parents_list

    Get a list of parent platforms.
    """
    params = [('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/platforms/lists/parents',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_platforms_read(client):
    """Test case for platforms_read

    Get details of the platform.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/platforms/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

