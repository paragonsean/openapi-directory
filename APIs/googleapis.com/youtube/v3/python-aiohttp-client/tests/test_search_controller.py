# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.search_list_response import SearchListResponse


pytestmark = pytest.mark.asyncio

async def test_youtube_search_list(client):
    """Test case for youtube_search_list

    
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
                    ('channelId', 'channel_id_example'),
                    ('channelType', 'channel_type_example'),
                    ('eventType', 'event_type_example'),
                    ('forContentOwner', True),
                    ('forDeveloper', True),
                    ('forMine', True),
                    ('location', 'location_example'),
                    ('locationRadius', 'location_radius_example'),
                    ('maxResults', 56),
                    ('onBehalfOfContentOwner', 'on_behalf_of_content_owner_example'),
                    ('order', 'order_example'),
                    ('pageToken', 'page_token_example'),
                    ('publishedAfter', 'published_after_example'),
                    ('publishedBefore', 'published_before_example'),
                    ('q', 'q_example'),
                    ('regionCode', 'region_code_example'),
                    ('relevanceLanguage', 'relevance_language_example'),
                    ('safeSearch', 'safe_search_example'),
                    ('topicId', 'topic_id_example'),
                    ('type', ['type_example']),
                    ('videoCaption', 'video_caption_example'),
                    ('videoCategoryId', 'video_category_id_example'),
                    ('videoDefinition', 'video_definition_example'),
                    ('videoDimension', 'video_dimension_example'),
                    ('videoDuration', 'video_duration_example'),
                    ('videoEmbeddable', 'video_embeddable_example'),
                    ('videoLicense', 'video_license_example'),
                    ('videoPaidProductPlacement', 'video_paid_product_placement_example'),
                    ('videoSyndicated', 'video_syndicated_example'),
                    ('videoType', 'video_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/youtube/v3/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

