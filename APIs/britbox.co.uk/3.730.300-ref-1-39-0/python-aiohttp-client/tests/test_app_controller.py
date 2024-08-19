# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.app_config import AppConfig
from openapi_server.models.page import Page
from openapi_server.models.service_error import ServiceError


pytestmark = pytest.mark.asyncio

async def test_get_app_config(client):
    """Test case for get_app_config

    
    """
    params = [('include', ['include_example']),
                    ('system', 'system_example'),
                    ('device', 'web_browser'),
                    ('sub', 'sub_example'),
                    ('segments', ['segments_example']),
                    ('ff', ['ff_example']),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/config',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_itv_page(client):
    """Test case for get_itv_page

    
    """
    params = [('path', 'path_example'),
                    ('list_page_size', 12),
                    ('list_page_size_large', 50),
                    ('max_list_prefetch', 2),
                    ('item_detail_expand', 'item_detail_expand_example'),
                    ('item_detail_select_season', 'item_detail_select_season_example'),
                    ('text_entry_format', markdown),
                    ('max_rating', 'max_rating_example'),
                    ('device', 'web_browser'),
                    ('sub', 'sub_example'),
                    ('segments', ['segments_example']),
                    ('ff', ['ff_example']),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/itv/page',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_page(client):
    """Test case for get_page

    
    """
    params = [('path', 'path_example'),
                    ('list_page_size', 12),
                    ('list_page_size_large', 50),
                    ('max_list_prefetch', 2),
                    ('item_detail_expand', 'item_detail_expand_example'),
                    ('item_detail_select_season', 'item_detail_select_season_example'),
                    ('text_entry_format', markdown),
                    ('max_rating', 'max_rating_example'),
                    ('device', 'web_browser'),
                    ('sub', 'sub_example'),
                    ('segments', ['segments_example']),
                    ('ff', ['ff_example']),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/page',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

