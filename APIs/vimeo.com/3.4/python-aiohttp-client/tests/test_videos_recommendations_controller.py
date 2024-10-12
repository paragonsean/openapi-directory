# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.video import Video


pytestmark = pytest.mark.asyncio

async def test_get_related_videos(client):
    """Test case for get_related_videos

    Get all the related videos of a video
    """
    params = [('filter', 'filter_example'),
                    ('page', 1),
                    ('per_page', 10)]
    headers = { 
        'Accept': 'application/vnd.vimeo.video+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/videos/{video_id}/videos'.format(video_id=258684937),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

