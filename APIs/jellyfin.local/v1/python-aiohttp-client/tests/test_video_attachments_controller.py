# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.problem_details import ProblemDetails


pytestmark = pytest.mark.asyncio

async def test_get_attachment(client):
    """Test case for get_attachment

    Get video attachment.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Videos/{video_id}/{media_source_id}/Attachments/{index}'.format(video_id='video_id_example', media_source_id='media_source_id_example', index=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

