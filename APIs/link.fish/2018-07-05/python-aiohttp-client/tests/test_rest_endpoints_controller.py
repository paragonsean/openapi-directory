# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_respons_error import ApiResponsError
from openapi_server.models.apps import Apps
from openapi_server.models.data_raw import DataRaw
from openapi_server.models.data_tabular import DataTabular
from openapi_server.models.geo_coordinates import GeoCoordinates
from openapi_server.models.social_media import SocialMedia
from openapi_server.models.url import Url
from openapi_server.models.url_browser import UrlBrowser


pytestmark = pytest.mark.asyncio

async def test_urls_apps_get(client):
    """Test case for urls_apps_get

    Get mobile apps
    """
    params = [('url', 'url_example'),
                    ('return_urls', False),
                    ('browser_render', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/Urls/apps',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_urls_browser_data_get(client):
    """Test case for urls_browser_data_get

    Extract data (browser)
    """
    params = [('url', 'url_example'),
                    ('item_format', normal),
                    ('simplify_special_types', False),
                    ('include_raw_html', False),
                    ('screenshot', none),
                    ('screenshot_width', 640),
                    ('screenshot_file_format', png)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/Urls/browser-data',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_urls_browser_screenshot_get(client):
    """Test case for urls_browser_screenshot_get

    Generate screenshot (browser)
    """
    params = [('url', 'url_example'),
                    ('type', normal),
                    ('file_format', png),
                    ('width', 640)]
    headers = { 
        'Accept': 'image/jpeg',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/Urls/browser-screenshot',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_urls_data_get(client):
    """Test case for urls_data_get

    Extract data
    """
    params = [('url', 'url_example'),
                    ('item_format', normal),
                    ('simplify_special_types', False),
                    ('include_raw_html', False),
                    ('browser_render', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/Urls/data',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_urls_data_raw_get(client):
    """Test case for urls_data_raw_get

    Return data of JSON/XML
    """
    params = [('url', 'url_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/Urls/data-raw',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_urls_data_tabular_get(client):
    """Test case for urls_data_tabular_get

    Return tabular data
    """
    params = [('url', 'url_example'),
                    ('selector', 'selector_example'),
                    ('browser_render', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/Urls/data-tabular',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_urls_geo_coordinates_get(client):
    """Test case for urls_geo_coordinates_get

    Get geo coordinates
    """
    params = [('url', 'url_example'),
                    ('browser_render', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/Urls/geo-coordinates',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_urls_social_media_get(client):
    """Test case for urls_social_media_get

    Get social media accounts
    """
    params = [('url', 'url_example'),
                    ('return_urls', False),
                    ('browser_render', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/Urls/social-media',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

