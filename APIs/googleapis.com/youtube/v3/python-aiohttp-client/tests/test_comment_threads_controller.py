# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.comment_thread import CommentThread
from openapi_server.models.comment_thread_list_response import CommentThreadListResponse


pytestmark = pytest.mark.asyncio

async def test_youtube_comment_threads_insert(client):
    """Test case for youtube_comment_threads_insert

    
    """
    body = {"snippet":{"canReply":True,"totalReplyCount":6,"topLevelComment":{"snippet":{"authorProfileImageUrl":"authorProfileImageUrl","textDisplay":"textDisplay","publishedAt":"2000-01-23T04:56:07.000+00:00","authorChannelId":{"value":"value"},"moderationStatus":"published","likeCount":0,"videoId":"videoId","textOriginal":"textOriginal","authorDisplayName":"authorDisplayName","parentId":"parentId","canRate":True,"authorChannelUrl":"authorChannelUrl","channelId":"channelId","updatedAt":"2000-01-23T04:56:07.000+00:00","viewerRating":"none"},"kind":"youtube#comment","etag":"etag","id":"id"},"isPublic":True,"videoId":"videoId","channelId":"channelId"},"replies":{"comments":[{"snippet":{"authorProfileImageUrl":"authorProfileImageUrl","textDisplay":"textDisplay","publishedAt":"2000-01-23T04:56:07.000+00:00","authorChannelId":{"value":"value"},"moderationStatus":"published","likeCount":0,"videoId":"videoId","textOriginal":"textOriginal","authorDisplayName":"authorDisplayName","parentId":"parentId","canRate":True,"authorChannelUrl":"authorChannelUrl","channelId":"channelId","updatedAt":"2000-01-23T04:56:07.000+00:00","viewerRating":"none"},"kind":"youtube#comment","etag":"etag","id":"id"},{"snippet":{"authorProfileImageUrl":"authorProfileImageUrl","textDisplay":"textDisplay","publishedAt":"2000-01-23T04:56:07.000+00:00","authorChannelId":{"value":"value"},"moderationStatus":"published","likeCount":0,"videoId":"videoId","textOriginal":"textOriginal","authorDisplayName":"authorDisplayName","parentId":"parentId","canRate":True,"authorChannelUrl":"authorChannelUrl","channelId":"channelId","updatedAt":"2000-01-23T04:56:07.000+00:00","viewerRating":"none"},"kind":"youtube#comment","etag":"etag","id":"id"}]},"kind":"youtube#commentThread","etag":"etag","id":"id"}
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
                    ('part', ['part_example'])]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/youtube/v3/commentThreads',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_youtube_comment_threads_list(client):
    """Test case for youtube_comment_threads_list

    
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
                    ('allThreadsRelatedToChannelId', 'all_threads_related_to_channel_id_example'),
                    ('channelId', 'channel_id_example'),
                    ('id', ['id_example']),
                    ('maxResults', 56),
                    ('moderationStatus', 'moderation_status_example'),
                    ('order', 'order_example'),
                    ('pageToken', 'page_token_example'),
                    ('searchTerms', 'search_terms_example'),
                    ('textFormat', 'text_format_example'),
                    ('videoId', 'video_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/youtube/v3/commentThreads',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

