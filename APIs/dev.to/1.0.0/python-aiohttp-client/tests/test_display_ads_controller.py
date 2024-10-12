# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.display_ad import DisplayAd


pytestmark = pytest.mark.asyncio

async def test_api_display_ads_get(client):
    """Test case for api_display_ads_get

    display ads
    """
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/api/display_ads',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_display_ads_id_get(client):
    """Test case for api_display_ads_id_get

    display ad
    """
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/api/display_ads/{id}'.format(id=123),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_display_ads_id_put(client):
    """Test case for api_display_ads_id_put

    display ads
    """
    body = {"approved":True,"body_markdown":"body_markdown","display_to":"all","tag_list":"tag_list","organization_id":1,"article_exclude_ids":"article_exclude_ids","creator_id":0,"name":"name","type_of":"in_house","id":6,"published":True,"placement_area":"sidebar_left"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api-key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/api/display_ads/{id}'.format(id=123),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_display_ads_id_unpublish_put(client):
    """Test case for api_display_ads_id_unpublish_put

    unpublish
    """
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/api/display_ads/{id}/unpublish'.format(id=123),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_display_ads_post(client):
    """Test case for api_display_ads_post

    display ads
    """
    body = {"approved":True,"body_markdown":"body_markdown","display_to":"all","tag_list":"tag_list","organization_id":1,"article_exclude_ids":"article_exclude_ids","creator_id":0,"name":"name","type_of":"in_house","id":6,"published":True,"placement_area":"sidebar_left"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api-key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/api/display_ads',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

