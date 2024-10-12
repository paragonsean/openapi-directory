# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.artistic_image_post_request import ArtisticImagePostRequest
from openapi_server.models.task import Task


pytestmark = pytest.mark.asyncio

async def test_artistic_image_post(client):
    """Test case for artistic_image_post

    Create an artistic image [ image_url, style_url -> id ]
    """
    body = openapi_server.ArtisticImagePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/v2.1/artistic_image',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_artistic_image_task_id_get(client):
    """Test case for artistic_image_task_id_get

    Gets a artistic image by task id [ id -> artistic image task ]
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2.1/artistic_image/{task_id}'.format(task_id='task_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

