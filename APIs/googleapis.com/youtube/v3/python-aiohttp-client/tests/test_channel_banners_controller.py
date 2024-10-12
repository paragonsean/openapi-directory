# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.channel_banner_resource import ChannelBannerResource


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_youtube_channel_banners_insert(client):
    """Test case for youtube_channel_banners_insert

    
    """
    body = openapi_server.ChannelBannerResource()
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
                    ('channelId', 'channel_id_example'),
                    ('onBehalfOfContentOwner', 'on_behalf_of_content_owner_example'),
                    ('onBehalfOfContentOwnerChannel', 'on_behalf_of_content_owner_channel_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/octet-stream',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/youtube/v3/channelBanners/insert',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

