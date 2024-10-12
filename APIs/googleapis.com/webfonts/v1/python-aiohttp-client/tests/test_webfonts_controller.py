# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.webfont_list import WebfontList


pytestmark = pytest.mark.asyncio

async def test_webfonts_webfonts_list(client):
    """Test case for webfonts_webfonts_list

    
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
                    ('capability', ['capability_example']),
                    ('family', ['family_example']),
                    ('sort', 'sort_example'),
                    ('subset', 'subset_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/webfonts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

