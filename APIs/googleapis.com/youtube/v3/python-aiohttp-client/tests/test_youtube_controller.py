# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.comment_thread import CommentThread


pytestmark = pytest.mark.asyncio

async def test_youtube_youtube_v3_update_comment_threads(client):
    """Test case for youtube_youtube_v3_update_comment_threads

    
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
    }
    response = await client.request(
        method='PUT',
        path='/youtube/v3/commentThreads',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

