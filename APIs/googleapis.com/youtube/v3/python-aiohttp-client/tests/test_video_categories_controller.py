# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.video_category_list_response import VideoCategoryListResponse


pytestmark = pytest.mark.asyncio

async def test_youtube_video_categories_list(client):
    """Test case for youtube_video_categories_list

    
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
                    ('part', ['part_example']),
                    ('hl', 'hl_example'),
                    ('id', ['id_example']),
                    ('regionCode', 'region_code_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/youtube/v3/videoCategories',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

