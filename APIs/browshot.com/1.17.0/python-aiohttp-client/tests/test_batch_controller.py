# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.batch import Batch
from openapi_server.models.batch_error import BatchError


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_create_batch(client):
    """Test case for create_batch

    Requests thousands of screenshtos at once
    """
    params = [('hosting', 'hosting_example'),
                    ('hosting_height', 56),
                    ('hosting_width', 56),
                    ('hosting_scale', 1.0),
                    ('hosting_bucket', 'hosting_bucket_example'),
                    ('hosting_file', 'hosting_file_example'),
                    ('hosting_headers', 'hosting_headers_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'apiKeyQuery': 'special-key',
    }
    data = FormData()
    data.add_field('instance_id', 56)
    data.add_field('file', '/path/to/file')
    data.add_field('size', screen)
    data.add_field('name', 'name_example')
    data.add_field('width', 1024)
    data.add_field('height', 56)
    data.add_field('delay', 5)
    data.add_field('flash_delay', 10)
    data.add_field('screen_width', 1024)
    data.add_field('screen_height', 768)
    data.add_field('priority', 56)
    data.add_field('referer', 'referer_example')
    data.add_field('post_data', 'post_data_example')
    data.add_field('cookie', 'cookie_example')
    data.add_field('script', 'script_example')
    data.add_field('details', 2)
    data.add_field('html', 0)
    data.add_field('max_wait', 0)
    data.add_field('headers', 'headers_example')
    data.add_field('format', png)
    response = await client.request(
        method='POST',
        path='/api/v1/batch/ceate',
        headers=headers,
        data=data,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_batch_info(client):
    """Test case for get_batch_info

    Get the batch status
    """
    params = [('id', 56)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/batch/info',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

