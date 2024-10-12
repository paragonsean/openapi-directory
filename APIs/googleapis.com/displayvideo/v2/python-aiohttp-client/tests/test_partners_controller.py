# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.assigned_targeting_option import AssignedTargetingOption
from openapi_server.models.bulk_edit_partner_assigned_targeting_options_request import BulkEditPartnerAssignedTargetingOptionsRequest
from openapi_server.models.bulk_edit_partner_assigned_targeting_options_response import BulkEditPartnerAssignedTargetingOptionsResponse
from openapi_server.models.bulk_edit_sites_request import BulkEditSitesRequest
from openapi_server.models.bulk_edit_sites_response import BulkEditSitesResponse
from openapi_server.models.channel import Channel
from openapi_server.models.list_channels_response import ListChannelsResponse
from openapi_server.models.list_partner_assigned_targeting_options_response import ListPartnerAssignedTargetingOptionsResponse
from openapi_server.models.list_partners_response import ListPartnersResponse
from openapi_server.models.list_sites_response import ListSitesResponse
from openapi_server.models.partner import Partner
from openapi_server.models.replace_sites_request import ReplaceSitesRequest
from openapi_server.models.replace_sites_response import ReplaceSitesResponse


pytestmark = pytest.mark.asyncio

async def test_displayvideo_partners_channels_create(client):
    """Test case for displayvideo_partners_channels_create

    
    """
    body = {"positivelyTargetedLineItemCount":"positivelyTargetedLineItemCount","displayName":"displayName","name":"name","negativelyTargetedLineItemCount":"negativelyTargetedLineItemCount","partnerId":"partnerId","channelId":"channelId","advertiserId":"advertiserId"}
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
                    ('advertiserId', 'advertiser_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/partners/{partner_id}/channels'.format(partner_id='partner_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_partners_channels_list(client):
    """Test case for displayvideo_partners_channels_list

    
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
                    ('advertiserId', 'advertiser_id_example'),
                    ('filter', 'filter_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/partners/{partner_id}/channels'.format(partner_id='partner_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_partners_channels_patch(client):
    """Test case for displayvideo_partners_channels_patch

    
    """
    body = {"positivelyTargetedLineItemCount":"positivelyTargetedLineItemCount","displayName":"displayName","name":"name","negativelyTargetedLineItemCount":"negativelyTargetedLineItemCount","partnerId":"partnerId","channelId":"channelId","advertiserId":"advertiserId"}
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
                    ('advertiserId', 'advertiser_id_example'),
                    ('updateMask', 'update_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v2/partners/{partner_id}/channels/{channel_id}'.format(partner_id='partner_id_example', channel_id='channel_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_partners_channels_sites_bulk_edit(client):
    """Test case for displayvideo_partners_channels_sites_bulk_edit

    
    """
    body = {"createdSites":[{"name":"name","urlOrAppId":"urlOrAppId"},{"name":"name","urlOrAppId":"urlOrAppId"}],"deletedSites":["deletedSites","deletedSites"],"partnerId":"partnerId","advertiserId":"advertiserId"}
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
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/partners/{partner_id}/channels/{channel_id}/sites:bulkEdit'.format(partner_id='partner_id_example', channel_id='channel_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_partners_channels_sites_delete(client):
    """Test case for displayvideo_partners_channels_sites_delete

    
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
                    ('advertiserId', 'advertiser_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/partners/{partner_id}/channels/{channel_id}/sites/{url_or_app_id}'.format(partner_id='partner_id_example', channel_id='channel_id_example', url_or_app_id='url_or_app_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_partners_channels_sites_list(client):
    """Test case for displayvideo_partners_channels_sites_list

    
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
                    ('advertiserId', 'advertiser_id_example'),
                    ('filter', 'filter_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/partners/{partner_id}/channels/{channel_id}/sites'.format(partner_id='partner_id_example', channel_id='channel_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_partners_channels_sites_replace(client):
    """Test case for displayvideo_partners_channels_sites_replace

    
    """
    body = {"newSites":[{"name":"name","urlOrAppId":"urlOrAppId"},{"name":"name","urlOrAppId":"urlOrAppId"}],"partnerId":"partnerId","advertiserId":"advertiserId"}
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
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/partners/{partner_id}/channels/{channel_id}/sites:replace'.format(partner_id='partner_id_example', channel_id='channel_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_partners_edit_assigned_targeting_options(client):
    """Test case for displayvideo_partners_edit_assigned_targeting_options

    
    """
    body = {"createRequests":[{"assignedTargetingOptions":[{"inheritance":"INHERITANCE_UNSPECIFIED","householdIncomeDetails":{"householdIncome":"HOUSEHOLD_INCOME_UNSPECIFIED"},"assignedTargetingOptionId":"assignedTargetingOptionId","inventorySourceGroupDetails":{"inventorySourceGroupId":"inventorySourceGroupId"},"channelDetails":{"negative":True,"channelId":"channelId"},"omidDetails":{"omid":"OMID_UNSPECIFIED"},"contentInstreamPositionDetails":{"adType":"AD_TYPE_UNSPECIFIED","contentInstreamPosition":"CONTENT_INSTREAM_POSITION_UNSPECIFIED"},"browserDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"audienceGroupDetails":{"includedGoogleAudienceGroup":{"settings":[{"googleAudienceId":"googleAudienceId"},{"googleAudienceId":"googleAudienceId"}]},"includedCustomListGroup":{"settings":[{"customListId":"customListId"},{"customListId":"customListId"}]},"includedCombinedAudienceGroup":{"settings":[{"combinedAudienceId":"combinedAudienceId"},{"combinedAudienceId":"combinedAudienceId"}]},"excludedGoogleAudienceGroup":{"settings":[{"googleAudienceId":"googleAudienceId"},{"googleAudienceId":"googleAudienceId"}]},"excludedFirstAndThirdPartyAudienceGroup":{"settings":[{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"},{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"}]},"includedFirstAndThirdPartyAudienceGroups":[{"settings":[{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"},{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"}]},{"settings":[{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"},{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"}]}]},"nativeContentPositionDetails":{"contentPosition":"NATIVE_CONTENT_POSITION_UNSPECIFIED"},"dayAndTimeDetails":{"endHour":6,"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startHour":1,"timeZoneResolution":"TIME_ZONE_RESOLUTION_UNSPECIFIED"},"exchangeDetails":{"exchange":"EXCHANGE_UNSPECIFIED"},"keywordDetails":{"negative":True,"keyword":"keyword"},"targetingType":"TARGETING_TYPE_UNSPECIFIED","assignedTargetingOptionIdAlias":"assignedTargetingOptionIdAlias","deviceMakeModelDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"digitalContentLabelExclusionDetails":{"excludedContentRatingTier":"CONTENT_RATING_TIER_UNSPECIFIED"},"poiDetails":{"proximityRadiusAmount":7.061401241503109,"proximityRadiusUnit":"DISTANCE_UNIT_UNSPECIFIED","displayName":"displayName","latitude":5.637376656633329,"targetingOptionId":"targetingOptionId","longitude":2.3021358869347655},"environmentDetails":{"environment":"ENVIRONMENT_UNSPECIFIED"},"subExchangeDetails":{"targetingOptionId":"targetingOptionId"},"appCategoryDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"contentDurationDetails":{"contentDuration":"CONTENT_DURATION_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"deviceTypeDetails":{"deviceType":"DEVICE_TYPE_UNSPECIFIED","youtubeAndPartnersBidMultiplier":5.962133916683182},"youtubeChannelDetails":{"negative":True,"channelId":"channelId"},"appDetails":{"negative":True,"appPlatform":"APP_PLATFORM_UNSPECIFIED","displayName":"displayName","appId":"appId"},"name":"name","viewabilityDetails":{"viewability":"VIEWABILITY_UNSPECIFIED"},"contentGenreDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"authorizedSellerStatusDetails":{"targetingOptionId":"targetingOptionId","authorizedSellerStatus":"AUTHORIZED_SELLER_STATUS_UNSPECIFIED"},"contentStreamTypeDetails":{"contentStreamType":"CONTENT_STREAM_TYPE_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"geoRegionDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId","geoRegionType":"GEO_REGION_TYPE_UNKNOWN"},"businessChainDetails":{"proximityRadiusAmount":0.8008281904610115,"proximityRadiusUnit":"DISTANCE_UNIT_UNSPECIFIED","displayName":"displayName","targetingOptionId":"targetingOptionId"},"parentalStatusDetails":{"parentalStatus":"PARENTAL_STATUS_UNSPECIFIED"},"negativeKeywordListDetails":{"negativeKeywordListId":"negativeKeywordListId"},"categoryDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"urlDetails":{"negative":True,"url":"url"},"youtubeVideoDetails":{"negative":True,"videoId":"videoId"},"operatingSystemDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"sensitiveCategoryExclusionDetails":{"excludedSensitiveCategory":"SENSITIVE_CATEGORY_UNSPECIFIED"},"proximityLocationListDetails":{"proximityRadiusUnit":"PROXIMITY_RADIUS_UNIT_UNSPECIFIED","proximityRadius":9.301444243932576,"proximityLocationListId":"proximityLocationListId"},"onScreenPositionDetails":{"adType":"AD_TYPE_UNSPECIFIED","targetingOptionId":"targetingOptionId","onScreenPosition":"ON_SCREEN_POSITION_UNSPECIFIED"},"contentOutstreamPositionDetails":{"adType":"AD_TYPE_UNSPECIFIED","contentOutstreamPosition":"CONTENT_OUTSTREAM_POSITION_UNSPECIFIED"},"audioContentTypeDetails":{"audioContentType":"AUDIO_CONTENT_TYPE_UNSPECIFIED"},"genderDetails":{"gender":"GENDER_UNSPECIFIED"},"inventorySourceDetails":{"inventorySourceId":"inventorySourceId"},"languageDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"thirdPartyVerifierDetails":{"doubleVerify":{"appStarRating":{"avoidInsufficientStarRating":True,"avoidedStarRating":"APP_STAR_RATE_UNSPECIFIED"},"customSegmentId":"customSegmentId","brandSafetyCategories":{"avoidUnknownBrandSafetyCategory":True,"avoidedMediumSeverityCategories":["MEDIUM_SEVERITY_UNSPECIFIED","MEDIUM_SEVERITY_UNSPECIFIED"],"avoidedHighSeverityCategories":["HIGHER_SEVERITY_UNSPECIFIED","HIGHER_SEVERITY_UNSPECIFIED"]},"fraudInvalidTraffic":{"avoidInsufficientOption":True,"avoidedFraudOption":"FRAUD_UNSPECIFIED"},"avoidedAgeRatings":["AGE_RATING_UNSPECIFIED","AGE_RATING_UNSPECIFIED"],"videoViewability":{"videoViewableRate":"VIDEO_VIEWABLE_RATE_UNSPECIFIED","playerImpressionRate":"PLAYER_SIZE_400X300_UNSPECIFIED","videoIab":"VIDEO_IAB_UNSPECIFIED"},"displayViewability":{"viewableDuring":"AVERAGE_VIEW_DURATION_UNSPECIFIED","iab":"IAB_VIEWED_RATE_UNSPECIFIED"}},"adloox":{"excludedAdlooxCategories":["ADLOOX_UNSPECIFIED","ADLOOX_UNSPECIFIED"]},"integralAdScience":{"excludeUnrateable":True,"excludedViolenceRisk":"VIOLENCE_UNSPECIFIED","excludedIllegalDownloadsRisk":"ILLEGAL_DOWNLOADS_UNSPECIFIED","excludedOffensiveLanguageRisk":"OFFENSIVE_LANGUAGE_UNSPECIFIED","videoViewability":"VIDEO_VIEWABILITY_UNSPECIFIED","excludedGamblingRisk":"GAMBLING_UNSPECIFIED","displayViewability":"PERFORMANCE_VIEWABILITY_UNSPECIFIED","customSegmentId":["customSegmentId","customSegmentId"],"excludedDrugsRisk":"DRUGS_UNSPECIFIED","excludedAlcoholRisk":"ALCOHOL_UNSPECIFIED","excludedHateSpeechRisk":"HATE_SPEECH_UNSPECIFIED","excludedAdFraudRisk":"SUSPICIOUS_ACTIVITY_UNSPECIFIED","traqScoreOption":"TRAQ_UNSPECIFIED","excludedAdultRisk":"ADULT_UNSPECIFIED"}},"sessionPositionDetails":{"sessionPosition":"SESSION_POSITION_UNSPECIFIED"},"videoPlayerSizeDetails":{"videoPlayerSize":"VIDEO_PLAYER_SIZE_UNSPECIFIED"},"carrierAndIspDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"userRewardedContentDetails":{"targetingOptionId":"targetingOptionId","userRewardedContent":"USER_REWARDED_CONTENT_UNSPECIFIED"},"ageRangeDetails":{"ageRange":"AGE_RANGE_UNSPECIFIED"},"regionalLocationListDetails":{"negative":True,"regionalLocationListId":"regionalLocationListId"}},{"inheritance":"INHERITANCE_UNSPECIFIED","householdIncomeDetails":{"householdIncome":"HOUSEHOLD_INCOME_UNSPECIFIED"},"assignedTargetingOptionId":"assignedTargetingOptionId","inventorySourceGroupDetails":{"inventorySourceGroupId":"inventorySourceGroupId"},"channelDetails":{"negative":True,"channelId":"channelId"},"omidDetails":{"omid":"OMID_UNSPECIFIED"},"contentInstreamPositionDetails":{"adType":"AD_TYPE_UNSPECIFIED","contentInstreamPosition":"CONTENT_INSTREAM_POSITION_UNSPECIFIED"},"browserDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"audienceGroupDetails":{"includedGoogleAudienceGroup":{"settings":[{"googleAudienceId":"googleAudienceId"},{"googleAudienceId":"googleAudienceId"}]},"includedCustomListGroup":{"settings":[{"customListId":"customListId"},{"customListId":"customListId"}]},"includedCombinedAudienceGroup":{"settings":[{"combinedAudienceId":"combinedAudienceId"},{"combinedAudienceId":"combinedAudienceId"}]},"excludedGoogleAudienceGroup":{"settings":[{"googleAudienceId":"googleAudienceId"},{"googleAudienceId":"googleAudienceId"}]},"excludedFirstAndThirdPartyAudienceGroup":{"settings":[{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"},{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"}]},"includedFirstAndThirdPartyAudienceGroups":[{"settings":[{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"},{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"}]},{"settings":[{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"},{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"}]}]},"nativeContentPositionDetails":{"contentPosition":"NATIVE_CONTENT_POSITION_UNSPECIFIED"},"dayAndTimeDetails":{"endHour":6,"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startHour":1,"timeZoneResolution":"TIME_ZONE_RESOLUTION_UNSPECIFIED"},"exchangeDetails":{"exchange":"EXCHANGE_UNSPECIFIED"},"keywordDetails":{"negative":True,"keyword":"keyword"},"targetingType":"TARGETING_TYPE_UNSPECIFIED","assignedTargetingOptionIdAlias":"assignedTargetingOptionIdAlias","deviceMakeModelDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"digitalContentLabelExclusionDetails":{"excludedContentRatingTier":"CONTENT_RATING_TIER_UNSPECIFIED"},"poiDetails":{"proximityRadiusAmount":7.061401241503109,"proximityRadiusUnit":"DISTANCE_UNIT_UNSPECIFIED","displayName":"displayName","latitude":5.637376656633329,"targetingOptionId":"targetingOptionId","longitude":2.3021358869347655},"environmentDetails":{"environment":"ENVIRONMENT_UNSPECIFIED"},"subExchangeDetails":{"targetingOptionId":"targetingOptionId"},"appCategoryDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"contentDurationDetails":{"contentDuration":"CONTENT_DURATION_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"deviceTypeDetails":{"deviceType":"DEVICE_TYPE_UNSPECIFIED","youtubeAndPartnersBidMultiplier":5.962133916683182},"youtubeChannelDetails":{"negative":True,"channelId":"channelId"},"appDetails":{"negative":True,"appPlatform":"APP_PLATFORM_UNSPECIFIED","displayName":"displayName","appId":"appId"},"name":"name","viewabilityDetails":{"viewability":"VIEWABILITY_UNSPECIFIED"},"contentGenreDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"authorizedSellerStatusDetails":{"targetingOptionId":"targetingOptionId","authorizedSellerStatus":"AUTHORIZED_SELLER_STATUS_UNSPECIFIED"},"contentStreamTypeDetails":{"contentStreamType":"CONTENT_STREAM_TYPE_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"geoRegionDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId","geoRegionType":"GEO_REGION_TYPE_UNKNOWN"},"businessChainDetails":{"proximityRadiusAmount":0.8008281904610115,"proximityRadiusUnit":"DISTANCE_UNIT_UNSPECIFIED","displayName":"displayName","targetingOptionId":"targetingOptionId"},"parentalStatusDetails":{"parentalStatus":"PARENTAL_STATUS_UNSPECIFIED"},"negativeKeywordListDetails":{"negativeKeywordListId":"negativeKeywordListId"},"categoryDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"urlDetails":{"negative":True,"url":"url"},"youtubeVideoDetails":{"negative":True,"videoId":"videoId"},"operatingSystemDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"sensitiveCategoryExclusionDetails":{"excludedSensitiveCategory":"SENSITIVE_CATEGORY_UNSPECIFIED"},"proximityLocationListDetails":{"proximityRadiusUnit":"PROXIMITY_RADIUS_UNIT_UNSPECIFIED","proximityRadius":9.301444243932576,"proximityLocationListId":"proximityLocationListId"},"onScreenPositionDetails":{"adType":"AD_TYPE_UNSPECIFIED","targetingOptionId":"targetingOptionId","onScreenPosition":"ON_SCREEN_POSITION_UNSPECIFIED"},"contentOutstreamPositionDetails":{"adType":"AD_TYPE_UNSPECIFIED","contentOutstreamPosition":"CONTENT_OUTSTREAM_POSITION_UNSPECIFIED"},"audioContentTypeDetails":{"audioContentType":"AUDIO_CONTENT_TYPE_UNSPECIFIED"},"genderDetails":{"gender":"GENDER_UNSPECIFIED"},"inventorySourceDetails":{"inventorySourceId":"inventorySourceId"},"languageDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"thirdPartyVerifierDetails":{"doubleVerify":{"appStarRating":{"avoidInsufficientStarRating":True,"avoidedStarRating":"APP_STAR_RATE_UNSPECIFIED"},"customSegmentId":"customSegmentId","brandSafetyCategories":{"avoidUnknownBrandSafetyCategory":True,"avoidedMediumSeverityCategories":["MEDIUM_SEVERITY_UNSPECIFIED","MEDIUM_SEVERITY_UNSPECIFIED"],"avoidedHighSeverityCategories":["HIGHER_SEVERITY_UNSPECIFIED","HIGHER_SEVERITY_UNSPECIFIED"]},"fraudInvalidTraffic":{"avoidInsufficientOption":True,"avoidedFraudOption":"FRAUD_UNSPECIFIED"},"avoidedAgeRatings":["AGE_RATING_UNSPECIFIED","AGE_RATING_UNSPECIFIED"],"videoViewability":{"videoViewableRate":"VIDEO_VIEWABLE_RATE_UNSPECIFIED","playerImpressionRate":"PLAYER_SIZE_400X300_UNSPECIFIED","videoIab":"VIDEO_IAB_UNSPECIFIED"},"displayViewability":{"viewableDuring":"AVERAGE_VIEW_DURATION_UNSPECIFIED","iab":"IAB_VIEWED_RATE_UNSPECIFIED"}},"adloox":{"excludedAdlooxCategories":["ADLOOX_UNSPECIFIED","ADLOOX_UNSPECIFIED"]},"integralAdScience":{"excludeUnrateable":True,"excludedViolenceRisk":"VIOLENCE_UNSPECIFIED","excludedIllegalDownloadsRisk":"ILLEGAL_DOWNLOADS_UNSPECIFIED","excludedOffensiveLanguageRisk":"OFFENSIVE_LANGUAGE_UNSPECIFIED","videoViewability":"VIDEO_VIEWABILITY_UNSPECIFIED","excludedGamblingRisk":"GAMBLING_UNSPECIFIED","displayViewability":"PERFORMANCE_VIEWABILITY_UNSPECIFIED","customSegmentId":["customSegmentId","customSegmentId"],"excludedDrugsRisk":"DRUGS_UNSPECIFIED","excludedAlcoholRisk":"ALCOHOL_UNSPECIFIED","excludedHateSpeechRisk":"HATE_SPEECH_UNSPECIFIED","excludedAdFraudRisk":"SUSPICIOUS_ACTIVITY_UNSPECIFIED","traqScoreOption":"TRAQ_UNSPECIFIED","excludedAdultRisk":"ADULT_UNSPECIFIED"}},"sessionPositionDetails":{"sessionPosition":"SESSION_POSITION_UNSPECIFIED"},"videoPlayerSizeDetails":{"videoPlayerSize":"VIDEO_PLAYER_SIZE_UNSPECIFIED"},"carrierAndIspDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"userRewardedContentDetails":{"targetingOptionId":"targetingOptionId","userRewardedContent":"USER_REWARDED_CONTENT_UNSPECIFIED"},"ageRangeDetails":{"ageRange":"AGE_RANGE_UNSPECIFIED"},"regionalLocationListDetails":{"negative":True,"regionalLocationListId":"regionalLocationListId"}}],"targetingType":"TARGETING_TYPE_UNSPECIFIED"},{"assignedTargetingOptions":[{"inheritance":"INHERITANCE_UNSPECIFIED","householdIncomeDetails":{"householdIncome":"HOUSEHOLD_INCOME_UNSPECIFIED"},"assignedTargetingOptionId":"assignedTargetingOptionId","inventorySourceGroupDetails":{"inventorySourceGroupId":"inventorySourceGroupId"},"channelDetails":{"negative":True,"channelId":"channelId"},"omidDetails":{"omid":"OMID_UNSPECIFIED"},"contentInstreamPositionDetails":{"adType":"AD_TYPE_UNSPECIFIED","contentInstreamPosition":"CONTENT_INSTREAM_POSITION_UNSPECIFIED"},"browserDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"audienceGroupDetails":{"includedGoogleAudienceGroup":{"settings":[{"googleAudienceId":"googleAudienceId"},{"googleAudienceId":"googleAudienceId"}]},"includedCustomListGroup":{"settings":[{"customListId":"customListId"},{"customListId":"customListId"}]},"includedCombinedAudienceGroup":{"settings":[{"combinedAudienceId":"combinedAudienceId"},{"combinedAudienceId":"combinedAudienceId"}]},"excludedGoogleAudienceGroup":{"settings":[{"googleAudienceId":"googleAudienceId"},{"googleAudienceId":"googleAudienceId"}]},"excludedFirstAndThirdPartyAudienceGroup":{"settings":[{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"},{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"}]},"includedFirstAndThirdPartyAudienceGroups":[{"settings":[{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"},{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"}]},{"settings":[{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"},{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"}]}]},"nativeContentPositionDetails":{"contentPosition":"NATIVE_CONTENT_POSITION_UNSPECIFIED"},"dayAndTimeDetails":{"endHour":6,"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startHour":1,"timeZoneResolution":"TIME_ZONE_RESOLUTION_UNSPECIFIED"},"exchangeDetails":{"exchange":"EXCHANGE_UNSPECIFIED"},"keywordDetails":{"negative":True,"keyword":"keyword"},"targetingType":"TARGETING_TYPE_UNSPECIFIED","assignedTargetingOptionIdAlias":"assignedTargetingOptionIdAlias","deviceMakeModelDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"digitalContentLabelExclusionDetails":{"excludedContentRatingTier":"CONTENT_RATING_TIER_UNSPECIFIED"},"poiDetails":{"proximityRadiusAmount":7.061401241503109,"proximityRadiusUnit":"DISTANCE_UNIT_UNSPECIFIED","displayName":"displayName","latitude":5.637376656633329,"targetingOptionId":"targetingOptionId","longitude":2.3021358869347655},"environmentDetails":{"environment":"ENVIRONMENT_UNSPECIFIED"},"subExchangeDetails":{"targetingOptionId":"targetingOptionId"},"appCategoryDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"contentDurationDetails":{"contentDuration":"CONTENT_DURATION_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"deviceTypeDetails":{"deviceType":"DEVICE_TYPE_UNSPECIFIED","youtubeAndPartnersBidMultiplier":5.962133916683182},"youtubeChannelDetails":{"negative":True,"channelId":"channelId"},"appDetails":{"negative":True,"appPlatform":"APP_PLATFORM_UNSPECIFIED","displayName":"displayName","appId":"appId"},"name":"name","viewabilityDetails":{"viewability":"VIEWABILITY_UNSPECIFIED"},"contentGenreDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"authorizedSellerStatusDetails":{"targetingOptionId":"targetingOptionId","authorizedSellerStatus":"AUTHORIZED_SELLER_STATUS_UNSPECIFIED"},"contentStreamTypeDetails":{"contentStreamType":"CONTENT_STREAM_TYPE_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"geoRegionDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId","geoRegionType":"GEO_REGION_TYPE_UNKNOWN"},"businessChainDetails":{"proximityRadiusAmount":0.8008281904610115,"proximityRadiusUnit":"DISTANCE_UNIT_UNSPECIFIED","displayName":"displayName","targetingOptionId":"targetingOptionId"},"parentalStatusDetails":{"parentalStatus":"PARENTAL_STATUS_UNSPECIFIED"},"negativeKeywordListDetails":{"negativeKeywordListId":"negativeKeywordListId"},"categoryDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"urlDetails":{"negative":True,"url":"url"},"youtubeVideoDetails":{"negative":True,"videoId":"videoId"},"operatingSystemDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"sensitiveCategoryExclusionDetails":{"excludedSensitiveCategory":"SENSITIVE_CATEGORY_UNSPECIFIED"},"proximityLocationListDetails":{"proximityRadiusUnit":"PROXIMITY_RADIUS_UNIT_UNSPECIFIED","proximityRadius":9.301444243932576,"proximityLocationListId":"proximityLocationListId"},"onScreenPositionDetails":{"adType":"AD_TYPE_UNSPECIFIED","targetingOptionId":"targetingOptionId","onScreenPosition":"ON_SCREEN_POSITION_UNSPECIFIED"},"contentOutstreamPositionDetails":{"adType":"AD_TYPE_UNSPECIFIED","contentOutstreamPosition":"CONTENT_OUTSTREAM_POSITION_UNSPECIFIED"},"audioContentTypeDetails":{"audioContentType":"AUDIO_CONTENT_TYPE_UNSPECIFIED"},"genderDetails":{"gender":"GENDER_UNSPECIFIED"},"inventorySourceDetails":{"inventorySourceId":"inventorySourceId"},"languageDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"thirdPartyVerifierDetails":{"doubleVerify":{"appStarRating":{"avoidInsufficientStarRating":True,"avoidedStarRating":"APP_STAR_RATE_UNSPECIFIED"},"customSegmentId":"customSegmentId","brandSafetyCategories":{"avoidUnknownBrandSafetyCategory":True,"avoidedMediumSeverityCategories":["MEDIUM_SEVERITY_UNSPECIFIED","MEDIUM_SEVERITY_UNSPECIFIED"],"avoidedHighSeverityCategories":["HIGHER_SEVERITY_UNSPECIFIED","HIGHER_SEVERITY_UNSPECIFIED"]},"fraudInvalidTraffic":{"avoidInsufficientOption":True,"avoidedFraudOption":"FRAUD_UNSPECIFIED"},"avoidedAgeRatings":["AGE_RATING_UNSPECIFIED","AGE_RATING_UNSPECIFIED"],"videoViewability":{"videoViewableRate":"VIDEO_VIEWABLE_RATE_UNSPECIFIED","playerImpressionRate":"PLAYER_SIZE_400X300_UNSPECIFIED","videoIab":"VIDEO_IAB_UNSPECIFIED"},"displayViewability":{"viewableDuring":"AVERAGE_VIEW_DURATION_UNSPECIFIED","iab":"IAB_VIEWED_RATE_UNSPECIFIED"}},"adloox":{"excludedAdlooxCategories":["ADLOOX_UNSPECIFIED","ADLOOX_UNSPECIFIED"]},"integralAdScience":{"excludeUnrateable":True,"excludedViolenceRisk":"VIOLENCE_UNSPECIFIED","excludedIllegalDownloadsRisk":"ILLEGAL_DOWNLOADS_UNSPECIFIED","excludedOffensiveLanguageRisk":"OFFENSIVE_LANGUAGE_UNSPECIFIED","videoViewability":"VIDEO_VIEWABILITY_UNSPECIFIED","excludedGamblingRisk":"GAMBLING_UNSPECIFIED","displayViewability":"PERFORMANCE_VIEWABILITY_UNSPECIFIED","customSegmentId":["customSegmentId","customSegmentId"],"excludedDrugsRisk":"DRUGS_UNSPECIFIED","excludedAlcoholRisk":"ALCOHOL_UNSPECIFIED","excludedHateSpeechRisk":"HATE_SPEECH_UNSPECIFIED","excludedAdFraudRisk":"SUSPICIOUS_ACTIVITY_UNSPECIFIED","traqScoreOption":"TRAQ_UNSPECIFIED","excludedAdultRisk":"ADULT_UNSPECIFIED"}},"sessionPositionDetails":{"sessionPosition":"SESSION_POSITION_UNSPECIFIED"},"videoPlayerSizeDetails":{"videoPlayerSize":"VIDEO_PLAYER_SIZE_UNSPECIFIED"},"carrierAndIspDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"userRewardedContentDetails":{"targetingOptionId":"targetingOptionId","userRewardedContent":"USER_REWARDED_CONTENT_UNSPECIFIED"},"ageRangeDetails":{"ageRange":"AGE_RANGE_UNSPECIFIED"},"regionalLocationListDetails":{"negative":True,"regionalLocationListId":"regionalLocationListId"}},{"inheritance":"INHERITANCE_UNSPECIFIED","householdIncomeDetails":{"householdIncome":"HOUSEHOLD_INCOME_UNSPECIFIED"},"assignedTargetingOptionId":"assignedTargetingOptionId","inventorySourceGroupDetails":{"inventorySourceGroupId":"inventorySourceGroupId"},"channelDetails":{"negative":True,"channelId":"channelId"},"omidDetails":{"omid":"OMID_UNSPECIFIED"},"contentInstreamPositionDetails":{"adType":"AD_TYPE_UNSPECIFIED","contentInstreamPosition":"CONTENT_INSTREAM_POSITION_UNSPECIFIED"},"browserDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"audienceGroupDetails":{"includedGoogleAudienceGroup":{"settings":[{"googleAudienceId":"googleAudienceId"},{"googleAudienceId":"googleAudienceId"}]},"includedCustomListGroup":{"settings":[{"customListId":"customListId"},{"customListId":"customListId"}]},"includedCombinedAudienceGroup":{"settings":[{"combinedAudienceId":"combinedAudienceId"},{"combinedAudienceId":"combinedAudienceId"}]},"excludedGoogleAudienceGroup":{"settings":[{"googleAudienceId":"googleAudienceId"},{"googleAudienceId":"googleAudienceId"}]},"excludedFirstAndThirdPartyAudienceGroup":{"settings":[{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"},{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"}]},"includedFirstAndThirdPartyAudienceGroups":[{"settings":[{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"},{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"}]},{"settings":[{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"},{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"}]}]},"nativeContentPositionDetails":{"contentPosition":"NATIVE_CONTENT_POSITION_UNSPECIFIED"},"dayAndTimeDetails":{"endHour":6,"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startHour":1,"timeZoneResolution":"TIME_ZONE_RESOLUTION_UNSPECIFIED"},"exchangeDetails":{"exchange":"EXCHANGE_UNSPECIFIED"},"keywordDetails":{"negative":True,"keyword":"keyword"},"targetingType":"TARGETING_TYPE_UNSPECIFIED","assignedTargetingOptionIdAlias":"assignedTargetingOptionIdAlias","deviceMakeModelDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"digitalContentLabelExclusionDetails":{"excludedContentRatingTier":"CONTENT_RATING_TIER_UNSPECIFIED"},"poiDetails":{"proximityRadiusAmount":7.061401241503109,"proximityRadiusUnit":"DISTANCE_UNIT_UNSPECIFIED","displayName":"displayName","latitude":5.637376656633329,"targetingOptionId":"targetingOptionId","longitude":2.3021358869347655},"environmentDetails":{"environment":"ENVIRONMENT_UNSPECIFIED"},"subExchangeDetails":{"targetingOptionId":"targetingOptionId"},"appCategoryDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"contentDurationDetails":{"contentDuration":"CONTENT_DURATION_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"deviceTypeDetails":{"deviceType":"DEVICE_TYPE_UNSPECIFIED","youtubeAndPartnersBidMultiplier":5.962133916683182},"youtubeChannelDetails":{"negative":True,"channelId":"channelId"},"appDetails":{"negative":True,"appPlatform":"APP_PLATFORM_UNSPECIFIED","displayName":"displayName","appId":"appId"},"name":"name","viewabilityDetails":{"viewability":"VIEWABILITY_UNSPECIFIED"},"contentGenreDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"authorizedSellerStatusDetails":{"targetingOptionId":"targetingOptionId","authorizedSellerStatus":"AUTHORIZED_SELLER_STATUS_UNSPECIFIED"},"contentStreamTypeDetails":{"contentStreamType":"CONTENT_STREAM_TYPE_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"geoRegionDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId","geoRegionType":"GEO_REGION_TYPE_UNKNOWN"},"businessChainDetails":{"proximityRadiusAmount":0.8008281904610115,"proximityRadiusUnit":"DISTANCE_UNIT_UNSPECIFIED","displayName":"displayName","targetingOptionId":"targetingOptionId"},"parentalStatusDetails":{"parentalStatus":"PARENTAL_STATUS_UNSPECIFIED"},"negativeKeywordListDetails":{"negativeKeywordListId":"negativeKeywordListId"},"categoryDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"urlDetails":{"negative":True,"url":"url"},"youtubeVideoDetails":{"negative":True,"videoId":"videoId"},"operatingSystemDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"sensitiveCategoryExclusionDetails":{"excludedSensitiveCategory":"SENSITIVE_CATEGORY_UNSPECIFIED"},"proximityLocationListDetails":{"proximityRadiusUnit":"PROXIMITY_RADIUS_UNIT_UNSPECIFIED","proximityRadius":9.301444243932576,"proximityLocationListId":"proximityLocationListId"},"onScreenPositionDetails":{"adType":"AD_TYPE_UNSPECIFIED","targetingOptionId":"targetingOptionId","onScreenPosition":"ON_SCREEN_POSITION_UNSPECIFIED"},"contentOutstreamPositionDetails":{"adType":"AD_TYPE_UNSPECIFIED","contentOutstreamPosition":"CONTENT_OUTSTREAM_POSITION_UNSPECIFIED"},"audioContentTypeDetails":{"audioContentType":"AUDIO_CONTENT_TYPE_UNSPECIFIED"},"genderDetails":{"gender":"GENDER_UNSPECIFIED"},"inventorySourceDetails":{"inventorySourceId":"inventorySourceId"},"languageDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"thirdPartyVerifierDetails":{"doubleVerify":{"appStarRating":{"avoidInsufficientStarRating":True,"avoidedStarRating":"APP_STAR_RATE_UNSPECIFIED"},"customSegmentId":"customSegmentId","brandSafetyCategories":{"avoidUnknownBrandSafetyCategory":True,"avoidedMediumSeverityCategories":["MEDIUM_SEVERITY_UNSPECIFIED","MEDIUM_SEVERITY_UNSPECIFIED"],"avoidedHighSeverityCategories":["HIGHER_SEVERITY_UNSPECIFIED","HIGHER_SEVERITY_UNSPECIFIED"]},"fraudInvalidTraffic":{"avoidInsufficientOption":True,"avoidedFraudOption":"FRAUD_UNSPECIFIED"},"avoidedAgeRatings":["AGE_RATING_UNSPECIFIED","AGE_RATING_UNSPECIFIED"],"videoViewability":{"videoViewableRate":"VIDEO_VIEWABLE_RATE_UNSPECIFIED","playerImpressionRate":"PLAYER_SIZE_400X300_UNSPECIFIED","videoIab":"VIDEO_IAB_UNSPECIFIED"},"displayViewability":{"viewableDuring":"AVERAGE_VIEW_DURATION_UNSPECIFIED","iab":"IAB_VIEWED_RATE_UNSPECIFIED"}},"adloox":{"excludedAdlooxCategories":["ADLOOX_UNSPECIFIED","ADLOOX_UNSPECIFIED"]},"integralAdScience":{"excludeUnrateable":True,"excludedViolenceRisk":"VIOLENCE_UNSPECIFIED","excludedIllegalDownloadsRisk":"ILLEGAL_DOWNLOADS_UNSPECIFIED","excludedOffensiveLanguageRisk":"OFFENSIVE_LANGUAGE_UNSPECIFIED","videoViewability":"VIDEO_VIEWABILITY_UNSPECIFIED","excludedGamblingRisk":"GAMBLING_UNSPECIFIED","displayViewability":"PERFORMANCE_VIEWABILITY_UNSPECIFIED","customSegmentId":["customSegmentId","customSegmentId"],"excludedDrugsRisk":"DRUGS_UNSPECIFIED","excludedAlcoholRisk":"ALCOHOL_UNSPECIFIED","excludedHateSpeechRisk":"HATE_SPEECH_UNSPECIFIED","excludedAdFraudRisk":"SUSPICIOUS_ACTIVITY_UNSPECIFIED","traqScoreOption":"TRAQ_UNSPECIFIED","excludedAdultRisk":"ADULT_UNSPECIFIED"}},"sessionPositionDetails":{"sessionPosition":"SESSION_POSITION_UNSPECIFIED"},"videoPlayerSizeDetails":{"videoPlayerSize":"VIDEO_PLAYER_SIZE_UNSPECIFIED"},"carrierAndIspDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"userRewardedContentDetails":{"targetingOptionId":"targetingOptionId","userRewardedContent":"USER_REWARDED_CONTENT_UNSPECIFIED"},"ageRangeDetails":{"ageRange":"AGE_RANGE_UNSPECIFIED"},"regionalLocationListDetails":{"negative":True,"regionalLocationListId":"regionalLocationListId"}}],"targetingType":"TARGETING_TYPE_UNSPECIFIED"}],"deleteRequests":[{"targetingType":"TARGETING_TYPE_UNSPECIFIED","assignedTargetingOptionIds":["assignedTargetingOptionIds","assignedTargetingOptionIds"]},{"targetingType":"TARGETING_TYPE_UNSPECIFIED","assignedTargetingOptionIds":["assignedTargetingOptionIds","assignedTargetingOptionIds"]}]}
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
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/partners/{partner_idedit_assigned_targeting_option}'.format(partner_id='partner_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_partners_get(client):
    """Test case for displayvideo_partners_get

    
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
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/partners/{partner_id}'.format(partner_id='partner_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_partners_list(client):
    """Test case for displayvideo_partners_list

    
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
                    ('filter', 'filter_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/partners',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_partners_targeting_types_assigned_targeting_options_create(client):
    """Test case for displayvideo_partners_targeting_types_assigned_targeting_options_create

    
    """
    body = {"inheritance":"INHERITANCE_UNSPECIFIED","householdIncomeDetails":{"householdIncome":"HOUSEHOLD_INCOME_UNSPECIFIED"},"assignedTargetingOptionId":"assignedTargetingOptionId","inventorySourceGroupDetails":{"inventorySourceGroupId":"inventorySourceGroupId"},"channelDetails":{"negative":True,"channelId":"channelId"},"omidDetails":{"omid":"OMID_UNSPECIFIED"},"contentInstreamPositionDetails":{"adType":"AD_TYPE_UNSPECIFIED","contentInstreamPosition":"CONTENT_INSTREAM_POSITION_UNSPECIFIED"},"browserDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"audienceGroupDetails":{"includedGoogleAudienceGroup":{"settings":[{"googleAudienceId":"googleAudienceId"},{"googleAudienceId":"googleAudienceId"}]},"includedCustomListGroup":{"settings":[{"customListId":"customListId"},{"customListId":"customListId"}]},"includedCombinedAudienceGroup":{"settings":[{"combinedAudienceId":"combinedAudienceId"},{"combinedAudienceId":"combinedAudienceId"}]},"excludedGoogleAudienceGroup":{"settings":[{"googleAudienceId":"googleAudienceId"},{"googleAudienceId":"googleAudienceId"}]},"excludedFirstAndThirdPartyAudienceGroup":{"settings":[{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"},{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"}]},"includedFirstAndThirdPartyAudienceGroups":[{"settings":[{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"},{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"}]},{"settings":[{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"},{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"}]}]},"nativeContentPositionDetails":{"contentPosition":"NATIVE_CONTENT_POSITION_UNSPECIFIED"},"dayAndTimeDetails":{"endHour":6,"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startHour":1,"timeZoneResolution":"TIME_ZONE_RESOLUTION_UNSPECIFIED"},"exchangeDetails":{"exchange":"EXCHANGE_UNSPECIFIED"},"keywordDetails":{"negative":True,"keyword":"keyword"},"targetingType":"TARGETING_TYPE_UNSPECIFIED","assignedTargetingOptionIdAlias":"assignedTargetingOptionIdAlias","deviceMakeModelDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"digitalContentLabelExclusionDetails":{"excludedContentRatingTier":"CONTENT_RATING_TIER_UNSPECIFIED"},"poiDetails":{"proximityRadiusAmount":7.061401241503109,"proximityRadiusUnit":"DISTANCE_UNIT_UNSPECIFIED","displayName":"displayName","latitude":5.637376656633329,"targetingOptionId":"targetingOptionId","longitude":2.3021358869347655},"environmentDetails":{"environment":"ENVIRONMENT_UNSPECIFIED"},"subExchangeDetails":{"targetingOptionId":"targetingOptionId"},"appCategoryDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"contentDurationDetails":{"contentDuration":"CONTENT_DURATION_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"deviceTypeDetails":{"deviceType":"DEVICE_TYPE_UNSPECIFIED","youtubeAndPartnersBidMultiplier":5.962133916683182},"youtubeChannelDetails":{"negative":True,"channelId":"channelId"},"appDetails":{"negative":True,"appPlatform":"APP_PLATFORM_UNSPECIFIED","displayName":"displayName","appId":"appId"},"name":"name","viewabilityDetails":{"viewability":"VIEWABILITY_UNSPECIFIED"},"contentGenreDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"authorizedSellerStatusDetails":{"targetingOptionId":"targetingOptionId","authorizedSellerStatus":"AUTHORIZED_SELLER_STATUS_UNSPECIFIED"},"contentStreamTypeDetails":{"contentStreamType":"CONTENT_STREAM_TYPE_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"geoRegionDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId","geoRegionType":"GEO_REGION_TYPE_UNKNOWN"},"businessChainDetails":{"proximityRadiusAmount":0.8008281904610115,"proximityRadiusUnit":"DISTANCE_UNIT_UNSPECIFIED","displayName":"displayName","targetingOptionId":"targetingOptionId"},"parentalStatusDetails":{"parentalStatus":"PARENTAL_STATUS_UNSPECIFIED"},"negativeKeywordListDetails":{"negativeKeywordListId":"negativeKeywordListId"},"categoryDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"urlDetails":{"negative":True,"url":"url"},"youtubeVideoDetails":{"negative":True,"videoId":"videoId"},"operatingSystemDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"sensitiveCategoryExclusionDetails":{"excludedSensitiveCategory":"SENSITIVE_CATEGORY_UNSPECIFIED"},"proximityLocationListDetails":{"proximityRadiusUnit":"PROXIMITY_RADIUS_UNIT_UNSPECIFIED","proximityRadius":9.301444243932576,"proximityLocationListId":"proximityLocationListId"},"onScreenPositionDetails":{"adType":"AD_TYPE_UNSPECIFIED","targetingOptionId":"targetingOptionId","onScreenPosition":"ON_SCREEN_POSITION_UNSPECIFIED"},"contentOutstreamPositionDetails":{"adType":"AD_TYPE_UNSPECIFIED","contentOutstreamPosition":"CONTENT_OUTSTREAM_POSITION_UNSPECIFIED"},"audioContentTypeDetails":{"audioContentType":"AUDIO_CONTENT_TYPE_UNSPECIFIED"},"genderDetails":{"gender":"GENDER_UNSPECIFIED"},"inventorySourceDetails":{"inventorySourceId":"inventorySourceId"},"languageDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"thirdPartyVerifierDetails":{"doubleVerify":{"appStarRating":{"avoidInsufficientStarRating":True,"avoidedStarRating":"APP_STAR_RATE_UNSPECIFIED"},"customSegmentId":"customSegmentId","brandSafetyCategories":{"avoidUnknownBrandSafetyCategory":True,"avoidedMediumSeverityCategories":["MEDIUM_SEVERITY_UNSPECIFIED","MEDIUM_SEVERITY_UNSPECIFIED"],"avoidedHighSeverityCategories":["HIGHER_SEVERITY_UNSPECIFIED","HIGHER_SEVERITY_UNSPECIFIED"]},"fraudInvalidTraffic":{"avoidInsufficientOption":True,"avoidedFraudOption":"FRAUD_UNSPECIFIED"},"avoidedAgeRatings":["AGE_RATING_UNSPECIFIED","AGE_RATING_UNSPECIFIED"],"videoViewability":{"videoViewableRate":"VIDEO_VIEWABLE_RATE_UNSPECIFIED","playerImpressionRate":"PLAYER_SIZE_400X300_UNSPECIFIED","videoIab":"VIDEO_IAB_UNSPECIFIED"},"displayViewability":{"viewableDuring":"AVERAGE_VIEW_DURATION_UNSPECIFIED","iab":"IAB_VIEWED_RATE_UNSPECIFIED"}},"adloox":{"excludedAdlooxCategories":["ADLOOX_UNSPECIFIED","ADLOOX_UNSPECIFIED"]},"integralAdScience":{"excludeUnrateable":True,"excludedViolenceRisk":"VIOLENCE_UNSPECIFIED","excludedIllegalDownloadsRisk":"ILLEGAL_DOWNLOADS_UNSPECIFIED","excludedOffensiveLanguageRisk":"OFFENSIVE_LANGUAGE_UNSPECIFIED","videoViewability":"VIDEO_VIEWABILITY_UNSPECIFIED","excludedGamblingRisk":"GAMBLING_UNSPECIFIED","displayViewability":"PERFORMANCE_VIEWABILITY_UNSPECIFIED","customSegmentId":["customSegmentId","customSegmentId"],"excludedDrugsRisk":"DRUGS_UNSPECIFIED","excludedAlcoholRisk":"ALCOHOL_UNSPECIFIED","excludedHateSpeechRisk":"HATE_SPEECH_UNSPECIFIED","excludedAdFraudRisk":"SUSPICIOUS_ACTIVITY_UNSPECIFIED","traqScoreOption":"TRAQ_UNSPECIFIED","excludedAdultRisk":"ADULT_UNSPECIFIED"}},"sessionPositionDetails":{"sessionPosition":"SESSION_POSITION_UNSPECIFIED"},"videoPlayerSizeDetails":{"videoPlayerSize":"VIDEO_PLAYER_SIZE_UNSPECIFIED"},"carrierAndIspDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"userRewardedContentDetails":{"targetingOptionId":"targetingOptionId","userRewardedContent":"USER_REWARDED_CONTENT_UNSPECIFIED"},"ageRangeDetails":{"ageRange":"AGE_RANGE_UNSPECIFIED"},"regionalLocationListDetails":{"negative":True,"regionalLocationListId":"regionalLocationListId"}}
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
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/partners/{partner_id}/targetingTypes/{targeting_type}/assignedTargetingOptions'.format(partner_id='partner_id_example', targeting_type='targeting_type_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_partners_targeting_types_assigned_targeting_options_delete(client):
    """Test case for displayvideo_partners_targeting_types_assigned_targeting_options_delete

    
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
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/partners/{partner_id}/targetingTypes/{targeting_type}/assignedTargetingOptions/{assigned_targeting_option_id}'.format(partner_id='partner_id_example', targeting_type='targeting_type_example', assigned_targeting_option_id='assigned_targeting_option_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_partners_targeting_types_assigned_targeting_options_get(client):
    """Test case for displayvideo_partners_targeting_types_assigned_targeting_options_get

    
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
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/partners/{partner_id}/targetingTypes/{targeting_type}/assignedTargetingOptions/{assigned_targeting_option_id}'.format(partner_id='partner_id_example', targeting_type='targeting_type_example', assigned_targeting_option_id='assigned_targeting_option_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_partners_targeting_types_assigned_targeting_options_list(client):
    """Test case for displayvideo_partners_targeting_types_assigned_targeting_options_list

    
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
                    ('filter', 'filter_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/partners/{partner_id}/targetingTypes/{targeting_type}/assignedTargetingOptions'.format(partner_id='partner_id_example', targeting_type='targeting_type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

