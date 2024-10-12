# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.channel import Channel
from openapi_server.models.channel_list_response import ChannelListResponse


pytestmark = pytest.mark.asyncio

async def test_youtube_channels_list(client):
    """Test case for youtube_channels_list

    
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
                    ('categoryId', 'category_id_example'),
                    ('forHandle', 'for_handle_example'),
                    ('forUsername', 'for_username_example'),
                    ('hl', 'hl_example'),
                    ('id', ['id_example']),
                    ('managedByMe', True),
                    ('maxResults', 56),
                    ('mine', True),
                    ('mySubscribers', True),
                    ('onBehalfOfContentOwner', 'on_behalf_of_content_owner_example'),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/youtube/v3/channels',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_youtube_channels_update(client):
    """Test case for youtube_channels_update

    
    """
    body = {"snippet":{"customUrl":"customUrl","country":"country","defaultLanguage":"defaultLanguage","publishedAt":"2000-01-23T04:56:07.000+00:00","localized":{"description":"description","title":"title"},"description":"description","thumbnails":{"standard":{"width":6,"url":"url","height":0},"high":{"width":6,"url":"url","height":0},"maxres":{"width":6,"url":"url","height":0},"medium":{"width":6,"url":"url","height":0}},"title":"title"},"localizations":{"key":{"description":"description","title":"title"}},"kind":"youtube#channel","contentDetails":{"relatedPlaylists":{"favorites":"favorites","watchHistory":"watchHistory","watchLater":"watchLater","likes":"likes","uploads":"uploads"}},"topicDetails":{"topicIds":["topicIds","topicIds"],"topicCategories":["topicCategories","topicCategories"]},"brandingSettings":{"image":{"bannerTabletExtraHdImageUrl":"bannerTabletExtraHdImageUrl","bannerTvImageUrl":"bannerTvImageUrl","watchIconImageUrl":"watchIconImageUrl","bannerExternalUrl":"bannerExternalUrl","smallBrandedBannerImageUrl":{"defaultLanguage":{"value":"value"},"localized":[{"language":"language","value":"value"},{"language":"language","value":"value"}]},"bannerMobileLowImageUrl":"bannerMobileLowImageUrl","bannerMobileExtraHdImageUrl":"bannerMobileExtraHdImageUrl","trackingImageUrl":"trackingImageUrl","bannerMobileHdImageUrl":"bannerMobileHdImageUrl","bannerTvLowImageUrl":"bannerTvLowImageUrl","bannerTabletLowImageUrl":"bannerTabletLowImageUrl","bannerTvHighImageUrl":"bannerTvHighImageUrl","bannerTvMediumImageUrl":"bannerTvMediumImageUrl","bannerMobileMediumHdImageUrl":"bannerMobileMediumHdImageUrl","largeBrandedBannerImageUrl":{"defaultLanguage":{"value":"value"},"localized":[{"language":"language","value":"value"},{"language":"language","value":"value"}]},"bannerTabletImageUrl":"bannerTabletImageUrl","smallBrandedBannerImageImapScript":{"defaultLanguage":{"value":"value"},"localized":[{"language":"language","value":"value"},{"language":"language","value":"value"}]},"bannerImageUrl":"bannerImageUrl","largeBrandedBannerImageImapScript":{"defaultLanguage":{"value":"value"},"localized":[{"language":"language","value":"value"},{"language":"language","value":"value"}]},"bannerMobileImageUrl":"bannerMobileImageUrl","bannerTabletHdImageUrl":"bannerTabletHdImageUrl","backgroundImageUrl":{"defaultLanguage":{"value":"value"},"localized":[{"language":"language","value":"value"},{"language":"language","value":"value"}]}},"watch":{"backgroundColor":"backgroundColor","featuredPlaylistId":"featuredPlaylistId","textColor":"textColor"},"hints":[{"property":"property","value":"value"},{"property":"property","value":"value"}],"channel":{"country":"country","featuredChannelsUrls":["featuredChannelsUrls","featuredChannelsUrls"],"featuredChannelsTitle":"featuredChannelsTitle","keywords":"keywords","defaultTab":"defaultTab","showRelatedChannels":True,"description":"description","unsubscribedTrailer":"unsubscribedTrailer","title":"title","defaultLanguage":"defaultLanguage","moderateComments":True,"trackingAnalyticsAccountId":"trackingAnalyticsAccountId","showBrowseView":True,"profileColor":"profileColor"}},"contentOwnerDetails":{"contentOwner":"contentOwner","timeLinked":"2000-01-23T04:56:07.000+00:00"},"conversionPings":{"pings":[{"conversionUrl":"conversionUrl","context":"subscribe"},{"conversionUrl":"conversionUrl","context":"subscribe"}]},"auditDetails":{"contentIdClaimsGoodStanding":True,"copyrightStrikesGoodStanding":True,"communityGuidelinesGoodStanding":True},"etag":"etag","id":"id","statistics":{"videoCount":"videoCount","subscriberCount":"subscriberCount","viewCount":"viewCount","hiddenSubscriberCount":True,"commentCount":"commentCount"},"status":{"isLinked":True,"longUploadsStatus":"longUploadsUnspecified","selfDeclaredMadeForKids":True,"privacyStatus":"public","madeForKids":True}}
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
                    ('onBehalfOfContentOwner', 'on_behalf_of_content_owner_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/youtube/v3/channels',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

