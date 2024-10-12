# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.thumbnail_set_response import ThumbnailSetResponse


pytestmark = pytest.mark.asyncio

async def test_youtube_thumbnails_set(client):
    """Test case for youtube_thumbnails_set

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('videoId', 'video_id_example'),
                    ('onBehalfOfContentOwner', 'on_behalf_of_content_owner_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/youtube/v3/thumbnails/set',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

