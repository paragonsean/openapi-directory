# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.clocking_records_post201_response import ClockingRecordsPost201Response
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.wall_comments_post_request import WallCommentsPostRequest
from openapi_server.models.wall_comments_wall_comment_id_get200_response import WallCommentsWallCommentIdGet200Response


pytestmark = pytest.mark.asyncio

async def test_wall_comments_post(client):
    """Test case for wall_comments_post

    Add wall comment
    """
    body = openapi_server.WallCommentsPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/wall_comments',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wall_comments_wall_comment_id_get(client):
    """Test case for wall_comments_wall_comment_id_get

    View wall comment
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/wall_comments/{wall_comment_id}'.format(wall_comment_id='wall_comment_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

