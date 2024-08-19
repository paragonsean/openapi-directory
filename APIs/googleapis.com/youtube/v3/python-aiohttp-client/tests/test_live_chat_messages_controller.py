# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.live_chat_message import LiveChatMessage
from openapi_server.models.live_chat_message_list_response import LiveChatMessageListResponse


pytestmark = pytest.mark.asyncio

async def test_youtube_live_chat_messages_delete(client):
    """Test case for youtube_live_chat_messages_delete

    
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
                    ('id', 'id_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/youtube/v3/liveChat/messages',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_youtube_live_chat_messages_insert(client):
    """Test case for youtube_live_chat_messages_insert

    
    """
    body = {"snippet":{"memberMilestoneChatDetails":{"userComment":"userComment","memberMonth":0,"memberLevelName":"memberLevelName"},"publishedAt":"2000-01-23T04:56:07.000+00:00","messageRetractedDetails":{"retractedMessageId":"retractedMessageId"},"superStickerDetails":{"amountDisplayString":"amountDisplayString","superStickerMetadata":{"altText":"altText","altTextLanguage":"altTextLanguage","stickerId":"stickerId"},"tier":5,"amountMicros":"amountMicros","currency":"currency"},"textMessageDetails":{"messageText":"messageText"},"authorChannelId":"authorChannelId","type":"invalidType","membershipGiftingDetails":{"giftMembershipsLevelName":"giftMembershipsLevelName","giftMembershipsCount":6},"messageDeletedDetails":{"deletedMessageId":"deletedMessageId"},"displayMessage":"displayMessage","giftMembershipReceivedDetails":{"associatedMembershipGiftingMessageId":"associatedMembershipGiftingMessageId","gifterChannelId":"gifterChannelId","memberLevelName":"memberLevelName"},"hasDisplayContent":True,"superChatDetails":{"amountDisplayString":"amountDisplayString","userComment":"userComment","tier":1,"amountMicros":"amountMicros","currency":"currency"},"liveChatId":"liveChatId","pollDetails":{"metadata":{"options":[{"optionText":"optionText","tally":"tally"},{"optionText":"optionText","tally":"tally"}],"questionText":"questionText"},"status":"unknown"},"userBannedDetails":{"bannedUserDetails":{"channelUrl":"channelUrl","displayName":"displayName","profileImageUrl":"profileImageUrl","channelId":"channelId"},"banType":"permanent","banDurationSeconds":"banDurationSeconds"},"newSponsorDetails":{"isUpgrade":True,"memberLevelName":"memberLevelName"},"fanFundingEventDetails":{"amountDisplayString":"amountDisplayString","userComment":"userComment","amountMicros":"amountMicros","currency":"currency"}},"kind":"youtube#liveChatMessage","authorDetails":{"isVerified":True,"channelUrl":"channelUrl","displayName":"displayName","isChatModerator":True,"profileImageUrl":"profileImageUrl","channelId":"channelId","isChatSponsor":True,"isChatOwner":True},"etag":"etag","id":"id"}
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
        path='/youtube/v3/liveChat/messages',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_youtube_live_chat_messages_list(client):
    """Test case for youtube_live_chat_messages_list

    
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
                    ('liveChatId', 'live_chat_id_example'),
                    ('part', ['part_example']),
                    ('hl', 'hl_example'),
                    ('maxResults', 56),
                    ('pageToken', 'page_token_example'),
                    ('profileImageSize', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/youtube/v3/liveChat/messages',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

