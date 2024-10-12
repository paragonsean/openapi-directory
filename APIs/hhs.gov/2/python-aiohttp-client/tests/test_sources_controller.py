# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.media_item_wrapped import MediaItemWrapped
from openapi_server.models.source_wrapped import SourceWrapped


pytestmark = pytest.mark.asyncio

async def test_resources_sources_id_json_get(client):
    """Test case for resources_sources_id_json_get

    Get Source by ID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/resources/sources/{id_jso}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resources_sources_id_syndicate_format_get(client):
    """Test case for resources_sources_id_syndicate_format_get

    Get MediaItems for Source
    """
    params = [('displayMethod', 'display_method_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/resources/sources/{id}/syndicate.{format}'.format(id=56, format='format_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resources_sources_json_get(client):
    """Test case for resources_sources_json_get

    Get Sources
    """
    params = [('max', 56),
                    ('offset', 56),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/resources/sources.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

