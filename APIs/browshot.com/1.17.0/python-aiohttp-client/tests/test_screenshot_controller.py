# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.screenshot import Screenshot
from openapi_server.models.screenshot_error import ScreenshotError
from openapi_server.models.screenshot_host import ScreenshotHost
from openapi_server.models.screenshot_info_error import ScreenshotInfoError
from openapi_server.models.screenshot_list import ScreenshotList
from openapi_server.models.screenshot_short import ScreenshotShort


pytestmark = pytest.mark.asyncio

async def test_create_multiple_screenshots(client):
    """Test case for create_multiple_screenshots

    Request multiple screenshots
    """
    params = [('url', 'url_example'),
                    ('instance_id', 56),
                    ('size', screen),
                    ('cache', 86400),
                    ('delay', 5),
                    ('flash_delay', 10),
                    ('screen_width', 1024),
                    ('screen_height', 768),
                    ('priority', 56),
                    ('referer', 'referer_example'),
                    ('post_data', 'post_data_example'),
                    ('cookie', 'cookie_example'),
                    ('script', 'script_example'),
                    ('details', 2),
                    ('html', 0),
                    ('max_wait', 0),
                    ('headers', 'headers_example'),
                    ('hosting', 'hosting_example'),
                    ('hosting_height', 56),
                    ('hosting_width', 56),
                    ('hosting_scale', 1.0),
                    ('hosting_bucket', 'hosting_bucket_example'),
                    ('hosting_file', 'hosting_file_example'),
                    ('hosting_headers', 'hosting_headers_example')]
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/screenshot/multiple',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_screenshot(client):
    """Test case for create_screenshot

    Request a screenshot
    """
    params = [('url', 'url_example'),
                    ('instance_id', 56),
                    ('size', screen),
                    ('cache', 86400),
                    ('delay', 5),
                    ('flash_delay', 10),
                    ('screen_width', 1024),
                    ('screen_height', 768),
                    ('priority', 56),
                    ('referer', 'referer_example'),
                    ('post_data', 'post_data_example'),
                    ('cookie', 'cookie_example'),
                    ('script', 'script_example'),
                    ('details', 2),
                    ('html', 0),
                    ('max_wait', 0),
                    ('headers', 'headers_example'),
                    ('shots', 1),
                    ('shot_interval', 5),
                    ('hosting', 'hosting_example'),
                    ('hosting_height', 56),
                    ('hosting_width', 56),
                    ('hosting_scale', 1.0),
                    ('hosting_bucket', 'hosting_bucket_example'),
                    ('hosting_file', 'hosting_file_example'),
                    ('hosting_headers', 'hosting_headers_example')]
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/screenshot/create',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_screenshot(client):
    """Test case for delete_screenshot

    Delete screenshot data
    """
    params = [('id', 56),
                    ('data', 'image')]
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/screenshot/delete',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_html(client):
    """Test case for get_html

    Get the HTML code
    """
    params = [('id', 56)]
    headers = { 
        'apiKeyQuery': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/screenshot/html',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_multiple_screenshots_info(client):
    """Test case for get_multiple_screenshots_info

    Get information about screenshots
    """
    params = [('limit', 100),
                    ('status', 'status_example')]
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/screenshot/list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_screenshot_info(client):
    """Test case for get_screenshot_info

    Query screenshot status
    """
    params = [('id', 56),
                    ('details', 2)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/screenshot/info',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_thumbnail(client):
    """Test case for get_thumbnail

    Retrieve a thumbnail image
    """
    params = [('id', 56),
                    ('width', 56),
                    ('height', 56),
                    ('scale', 1.0),
                    ('zoom', 100),
                    ('ratio', fit),
                    ('left', 0),
                    ('right', 0),
                    ('top', 0),
                    ('bottom', 56),
                    ('format', png),
                    ('shot', 1),
                    ('quality', 100)]
    headers = { 
        'apiKeyQuery': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/screenshot/thumbnail',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_host_screenshot(client):
    """Test case for host_screenshot

    Host thumbnails on your own S3 account or on Browshot.
    """
    params = [('id', 56),
                    ('hosting', 'hosting_example'),
                    ('width', 56),
                    ('height', 56),
                    ('scale', 1.0),
                    ('bucket', 'bucket_example'),
                    ('file', 'file_example'),
                    ('headers', 'headers_example')]
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/screenshot/host',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_screenshot(client):
    """Test case for search_screenshot

    Search for screenshots
    """
    params = [('url', 'url_example'),
                    ('limit', 50),
                    ('status', 'status_example')]
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/screenshot/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_share_screenshot(client):
    """Test case for share_screenshot

    Share a screenshot
    """
    params = [('id', 56),
                    ('note', 'note_example')]
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/screenshot/share',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

