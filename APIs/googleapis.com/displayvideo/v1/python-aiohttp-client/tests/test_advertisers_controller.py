# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.advertiser import Advertiser
from openapi_server.models.assigned_location import AssignedLocation
from openapi_server.models.assigned_targeting_option import AssignedTargetingOption
from openapi_server.models.audit_advertiser_response import AuditAdvertiserResponse
from openapi_server.models.bulk_edit_advertiser_assigned_targeting_options_request import BulkEditAdvertiserAssignedTargetingOptionsRequest
from openapi_server.models.bulk_edit_advertiser_assigned_targeting_options_response import BulkEditAdvertiserAssignedTargetingOptionsResponse
from openapi_server.models.bulk_edit_assigned_locations_request import BulkEditAssignedLocationsRequest
from openapi_server.models.bulk_edit_assigned_locations_response import BulkEditAssignedLocationsResponse
from openapi_server.models.bulk_edit_line_item_assigned_targeting_options_request import BulkEditLineItemAssignedTargetingOptionsRequest
from openapi_server.models.bulk_edit_line_item_assigned_targeting_options_response import BulkEditLineItemAssignedTargetingOptionsResponse
from openapi_server.models.bulk_edit_negative_keywords_request import BulkEditNegativeKeywordsRequest
from openapi_server.models.bulk_edit_negative_keywords_response import BulkEditNegativeKeywordsResponse
from openapi_server.models.bulk_edit_sites_request import BulkEditSitesRequest
from openapi_server.models.bulk_edit_sites_response import BulkEditSitesResponse
from openapi_server.models.bulk_list_advertiser_assigned_targeting_options_response import BulkListAdvertiserAssignedTargetingOptionsResponse
from openapi_server.models.bulk_list_campaign_assigned_targeting_options_response import BulkListCampaignAssignedTargetingOptionsResponse
from openapi_server.models.bulk_list_insertion_order_assigned_targeting_options_response import BulkListInsertionOrderAssignedTargetingOptionsResponse
from openapi_server.models.bulk_list_line_item_assigned_targeting_options_response import BulkListLineItemAssignedTargetingOptionsResponse
from openapi_server.models.campaign import Campaign
from openapi_server.models.channel import Channel
from openapi_server.models.create_asset_request import CreateAssetRequest
from openapi_server.models.create_asset_response import CreateAssetResponse
from openapi_server.models.creative import Creative
from openapi_server.models.generate_default_line_item_request import GenerateDefaultLineItemRequest
from openapi_server.models.insertion_order import InsertionOrder
from openapi_server.models.line_item import LineItem
from openapi_server.models.list_advertiser_assigned_targeting_options_response import ListAdvertiserAssignedTargetingOptionsResponse
from openapi_server.models.list_advertisers_response import ListAdvertisersResponse
from openapi_server.models.list_assigned_locations_response import ListAssignedLocationsResponse
from openapi_server.models.list_campaign_assigned_targeting_options_response import ListCampaignAssignedTargetingOptionsResponse
from openapi_server.models.list_campaigns_response import ListCampaignsResponse
from openapi_server.models.list_channels_response import ListChannelsResponse
from openapi_server.models.list_creatives_response import ListCreativesResponse
from openapi_server.models.list_insertion_order_assigned_targeting_options_response import ListInsertionOrderAssignedTargetingOptionsResponse
from openapi_server.models.list_insertion_orders_response import ListInsertionOrdersResponse
from openapi_server.models.list_invoices_response import ListInvoicesResponse
from openapi_server.models.list_line_item_assigned_targeting_options_response import ListLineItemAssignedTargetingOptionsResponse
from openapi_server.models.list_line_items_response import ListLineItemsResponse
from openapi_server.models.list_location_lists_response import ListLocationListsResponse
from openapi_server.models.list_manual_triggers_response import ListManualTriggersResponse
from openapi_server.models.list_negative_keyword_lists_response import ListNegativeKeywordListsResponse
from openapi_server.models.list_negative_keywords_response import ListNegativeKeywordsResponse
from openapi_server.models.list_sites_response import ListSitesResponse
from openapi_server.models.location_list import LocationList
from openapi_server.models.lookup_invoice_currency_response import LookupInvoiceCurrencyResponse
from openapi_server.models.manual_trigger import ManualTrigger
from openapi_server.models.negative_keyword_list import NegativeKeywordList
from openapi_server.models.replace_negative_keywords_request import ReplaceNegativeKeywordsRequest
from openapi_server.models.replace_negative_keywords_response import ReplaceNegativeKeywordsResponse
from openapi_server.models.replace_sites_request import ReplaceSitesRequest
from openapi_server.models.replace_sites_response import ReplaceSitesResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/octet-stream not supported by Connexion")
async def test_displayvideo_advertisers_assets_upload(client):
    """Test case for displayvideo_advertisers_assets_upload

    
    """
    body = openapi_server.CreateAssetRequest()
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
        'Content-Type': 'application/octet-stream',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/advertisers/{advertiser_id}/assets'.format(advertiser_id='advertiser_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_audit(client):
    """Test case for displayvideo_advertisers_audit

    
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
                    ('readMask', 'read_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/advertisers/{advertiser_idaudi}'.format(advertiser_id='advertiser_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_bulk_edit_advertiser_assigned_targeting_options(client):
    """Test case for displayvideo_advertisers_bulk_edit_advertiser_assigned_targeting_options

    
    """
    body = {"createRequests":[{"assignedTargetingOptions":[{"inheritance":"INHERITANCE_UNSPECIFIED","householdIncomeDetails":{"targetingOptionId":"targetingOptionId","householdIncome":"HOUSEHOLD_INCOME_UNSPECIFIED"},"assignedTargetingOptionId":"assignedTargetingOptionId","inventorySourceGroupDetails":{"inventorySourceGroupId":"inventorySourceGroupId"},"channelDetails":{"negative":True,"channelId":"channelId"},"omidDetails":{"targetingOptionId":"targetingOptionId","omid":"OMID_UNSPECIFIED"},"contentInstreamPositionDetails":{"adType":"AD_TYPE_UNSPECIFIED","contentInstreamPosition":"CONTENT_INSTREAM_POSITION_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"browserDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"audienceGroupDetails":{"includedGoogleAudienceGroup":{"settings":[{"googleAudienceId":"googleAudienceId"},{"googleAudienceId":"googleAudienceId"}]},"includedCustomListGroup":{"settings":[{"customListId":"customListId"},{"customListId":"customListId"}]},"includedCombinedAudienceGroup":{"settings":[{"combinedAudienceId":"combinedAudienceId"},{"combinedAudienceId":"combinedAudienceId"}]},"excludedGoogleAudienceGroup":{"settings":[{"googleAudienceId":"googleAudienceId"},{"googleAudienceId":"googleAudienceId"}]},"excludedFirstAndThirdPartyAudienceGroup":{"settings":[{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"},{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"}]},"includedFirstAndThirdPartyAudienceGroups":[{"settings":[{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"},{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"}]},{"settings":[{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"},{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"}]}]},"nativeContentPositionDetails":{"targetingOptionId":"targetingOptionId","contentPosition":"NATIVE_CONTENT_POSITION_UNSPECIFIED"},"dayAndTimeDetails":{"endHour":6,"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startHour":1,"timeZoneResolution":"TIME_ZONE_RESOLUTION_UNSPECIFIED"},"exchangeDetails":{"targetingOptionId":"targetingOptionId"},"keywordDetails":{"negative":True,"keyword":"keyword"},"targetingType":"TARGETING_TYPE_UNSPECIFIED","deviceMakeModelDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"digitalContentLabelExclusionDetails":{"excludedTargetingOptionId":"excludedTargetingOptionId","contentRatingTier":"CONTENT_RATING_TIER_UNSPECIFIED"},"poiDetails":{"proximityRadiusAmount":2.3021358869347655,"proximityRadiusUnit":"DISTANCE_UNIT_UNSPECIFIED","displayName":"displayName","latitude":5.962133916683182,"targetingOptionId":"targetingOptionId","longitude":5.637376656633329},"environmentDetails":{"environment":"ENVIRONMENT_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"subExchangeDetails":{"targetingOptionId":"targetingOptionId"},"appCategoryDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"contentDurationDetails":{"contentDuration":"CONTENT_DURATION_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"deviceTypeDetails":{"deviceType":"DEVICE_TYPE_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"appDetails":{"negative":True,"appPlatform":"APP_PLATFORM_UNSPECIFIED","displayName":"displayName","appId":"appId"},"name":"name","viewabilityDetails":{"viewability":"VIEWABILITY_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"contentGenreDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"authorizedSellerStatusDetails":{"targetingOptionId":"targetingOptionId","authorizedSellerStatus":"AUTHORIZED_SELLER_STATUS_UNSPECIFIED"},"contentStreamTypeDetails":{"contentStreamType":"CONTENT_STREAM_TYPE_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"geoRegionDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId","geoRegionType":"GEO_REGION_TYPE_UNKNOWN"},"businessChainDetails":{"proximityRadiusAmount":0.8008281904610115,"proximityRadiusUnit":"DISTANCE_UNIT_UNSPECIFIED","displayName":"displayName","targetingOptionId":"targetingOptionId"},"parentalStatusDetails":{"targetingOptionId":"targetingOptionId","parentalStatus":"PARENTAL_STATUS_UNSPECIFIED"},"negativeKeywordListDetails":{"negativeKeywordListId":"negativeKeywordListId"},"categoryDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"urlDetails":{"negative":True,"url":"url"},"operatingSystemDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"sensitiveCategoryExclusionDetails":{"sensitiveCategory":"SENSITIVE_CATEGORY_UNSPECIFIED","excludedTargetingOptionId":"excludedTargetingOptionId"},"proximityLocationListDetails":{"proximityLocationListId":"proximityLocationListId","proximityRadiusRange":"PROXIMITY_RADIUS_RANGE_UNSPECIFIED"},"onScreenPositionDetails":{"adType":"AD_TYPE_UNSPECIFIED","targetingOptionId":"targetingOptionId","onScreenPosition":"ON_SCREEN_POSITION_UNSPECIFIED"},"contentOutstreamPositionDetails":{"adType":"AD_TYPE_UNSPECIFIED","contentOutstreamPosition":"CONTENT_OUTSTREAM_POSITION_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"audioContentTypeDetails":{"audioContentType":"AUDIO_CONTENT_TYPE_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"genderDetails":{"gender":"GENDER_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"inventorySourceDetails":{"inventorySourceId":"inventorySourceId"},"languageDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"thirdPartyVerifierDetails":{"doubleVerify":{"appStarRating":{"avoidInsufficientStarRating":True,"avoidedStarRating":"APP_STAR_RATE_UNSPECIFIED"},"customSegmentId":"customSegmentId","brandSafetyCategories":{"avoidUnknownBrandSafetyCategory":True,"avoidedMediumSeverityCategories":["MEDIUM_SEVERITY_UNSPECIFIED","MEDIUM_SEVERITY_UNSPECIFIED"],"avoidedHighSeverityCategories":["HIGHER_SEVERITY_UNSPECIFIED","HIGHER_SEVERITY_UNSPECIFIED"]},"fraudInvalidTraffic":{"avoidInsufficientOption":True,"avoidedFraudOption":"FRAUD_UNSPECIFIED"},"avoidedAgeRatings":["AGE_RATING_UNSPECIFIED","AGE_RATING_UNSPECIFIED"],"videoViewability":{"videoViewableRate":"VIDEO_VIEWABLE_RATE_UNSPECIFIED","playerImpressionRate":"PLAYER_SIZE_400X300_UNSPECIFIED","videoIab":"VIDEO_IAB_UNSPECIFIED"},"displayViewability":{"viewableDuring":"AVERAGE_VIEW_DURATION_UNSPECIFIED","iab":"IAB_VIEWED_RATE_UNSPECIFIED"}},"adloox":{"excludedAdlooxCategories":["ADLOOX_UNSPECIFIED","ADLOOX_UNSPECIFIED"]},"integralAdScience":{"excludeUnrateable":True,"excludedViolenceRisk":"VIOLENCE_UNSPECIFIED","excludedIllegalDownloadsRisk":"ILLEGAL_DOWNLOADS_UNSPECIFIED","excludedOffensiveLanguageRisk":"OFFENSIVE_LANGUAGE_UNSPECIFIED","videoViewability":"VIDEO_VIEWABILITY_UNSPECIFIED","excludedGamblingRisk":"GAMBLING_UNSPECIFIED","displayViewability":"PERFORMANCE_VIEWABILITY_UNSPECIFIED","customSegmentId":["customSegmentId","customSegmentId"],"excludedDrugsRisk":"DRUGS_UNSPECIFIED","excludedAlcoholRisk":"ALCOHOL_UNSPECIFIED","excludedHateSpeechRisk":"HATE_SPEECH_UNSPECIFIED","excludedAdFraudRisk":"SUSPICIOUS_ACTIVITY_UNSPECIFIED","traqScoreOption":"TRAQ_UNSPECIFIED","excludedAdultRisk":"ADULT_UNSPECIFIED"}},"videoPlayerSizeDetails":{"targetingOptionId":"targetingOptionId","videoPlayerSize":"VIDEO_PLAYER_SIZE_UNSPECIFIED"},"carrierAndIspDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"userRewardedContentDetails":{"targetingOptionId":"targetingOptionId","userRewardedContent":"USER_REWARDED_CONTENT_UNSPECIFIED"},"ageRangeDetails":{"ageRange":"AGE_RANGE_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"regionalLocationListDetails":{"negative":True,"regionalLocationListId":"regionalLocationListId"}},{"inheritance":"INHERITANCE_UNSPECIFIED","householdIncomeDetails":{"targetingOptionId":"targetingOptionId","householdIncome":"HOUSEHOLD_INCOME_UNSPECIFIED"},"assignedTargetingOptionId":"assignedTargetingOptionId","inventorySourceGroupDetails":{"inventorySourceGroupId":"inventorySourceGroupId"},"channelDetails":{"negative":True,"channelId":"channelId"},"omidDetails":{"targetingOptionId":"targetingOptionId","omid":"OMID_UNSPECIFIED"},"contentInstreamPositionDetails":{"adType":"AD_TYPE_UNSPECIFIED","contentInstreamPosition":"CONTENT_INSTREAM_POSITION_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"browserDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"audienceGroupDetails":{"includedGoogleAudienceGroup":{"settings":[{"googleAudienceId":"googleAudienceId"},{"googleAudienceId":"googleAudienceId"}]},"includedCustomListGroup":{"settings":[{"customListId":"customListId"},{"customListId":"customListId"}]},"includedCombinedAudienceGroup":{"settings":[{"combinedAudienceId":"combinedAudienceId"},{"combinedAudienceId":"combinedAudienceId"}]},"excludedGoogleAudienceGroup":{"settings":[{"googleAudienceId":"googleAudienceId"},{"googleAudienceId":"googleAudienceId"}]},"excludedFirstAndThirdPartyAudienceGroup":{"settings":[{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"},{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"}]},"includedFirstAndThirdPartyAudienceGroups":[{"settings":[{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"},{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"}]},{"settings":[{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"},{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"}]}]},"nativeContentPositionDetails":{"targetingOptionId":"targetingOptionId","contentPosition":"NATIVE_CONTENT_POSITION_UNSPECIFIED"},"dayAndTimeDetails":{"endHour":6,"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startHour":1,"timeZoneResolution":"TIME_ZONE_RESOLUTION_UNSPECIFIED"},"exchangeDetails":{"targetingOptionId":"targetingOptionId"},"keywordDetails":{"negative":True,"keyword":"keyword"},"targetingType":"TARGETING_TYPE_UNSPECIFIED","deviceMakeModelDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"digitalContentLabelExclusionDetails":{"excludedTargetingOptionId":"excludedTargetingOptionId","contentRatingTier":"CONTENT_RATING_TIER_UNSPECIFIED"},"poiDetails":{"proximityRadiusAmount":2.3021358869347655,"proximityRadiusUnit":"DISTANCE_UNIT_UNSPECIFIED","displayName":"displayName","latitude":5.962133916683182,"targetingOptionId":"targetingOptionId","longitude":5.637376656633329},"environmentDetails":{"environment":"ENVIRONMENT_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"subExchangeDetails":{"targetingOptionId":"targetingOptionId"},"appCategoryDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"contentDurationDetails":{"contentDuration":"CONTENT_DURATION_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"deviceTypeDetails":{"deviceType":"DEVICE_TYPE_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"appDetails":{"negative":True,"appPlatform":"APP_PLATFORM_UNSPECIFIED","displayName":"displayName","appId":"appId"},"name":"name","viewabilityDetails":{"viewability":"VIEWABILITY_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"contentGenreDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"authorizedSellerStatusDetails":{"targetingOptionId":"targetingOptionId","authorizedSellerStatus":"AUTHORIZED_SELLER_STATUS_UNSPECIFIED"},"contentStreamTypeDetails":{"contentStreamType":"CONTENT_STREAM_TYPE_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"geoRegionDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId","geoRegionType":"GEO_REGION_TYPE_UNKNOWN"},"businessChainDetails":{"proximityRadiusAmount":0.8008281904610115,"proximityRadiusUnit":"DISTANCE_UNIT_UNSPECIFIED","displayName":"displayName","targetingOptionId":"targetingOptionId"},"parentalStatusDetails":{"targetingOptionId":"targetingOptionId","parentalStatus":"PARENTAL_STATUS_UNSPECIFIED"},"negativeKeywordListDetails":{"negativeKeywordListId":"negativeKeywordListId"},"categoryDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"urlDetails":{"negative":True,"url":"url"},"operatingSystemDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"sensitiveCategoryExclusionDetails":{"sensitiveCategory":"SENSITIVE_CATEGORY_UNSPECIFIED","excludedTargetingOptionId":"excludedTargetingOptionId"},"proximityLocationListDetails":{"proximityLocationListId":"proximityLocationListId","proximityRadiusRange":"PROXIMITY_RADIUS_RANGE_UNSPECIFIED"},"onScreenPositionDetails":{"adType":"AD_TYPE_UNSPECIFIED","targetingOptionId":"targetingOptionId","onScreenPosition":"ON_SCREEN_POSITION_UNSPECIFIED"},"contentOutstreamPositionDetails":{"adType":"AD_TYPE_UNSPECIFIED","contentOutstreamPosition":"CONTENT_OUTSTREAM_POSITION_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"audioContentTypeDetails":{"audioContentType":"AUDIO_CONTENT_TYPE_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"genderDetails":{"gender":"GENDER_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"inventorySourceDetails":{"inventorySourceId":"inventorySourceId"},"languageDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"thirdPartyVerifierDetails":{"doubleVerify":{"appStarRating":{"avoidInsufficientStarRating":True,"avoidedStarRating":"APP_STAR_RATE_UNSPECIFIED"},"customSegmentId":"customSegmentId","brandSafetyCategories":{"avoidUnknownBrandSafetyCategory":True,"avoidedMediumSeverityCategories":["MEDIUM_SEVERITY_UNSPECIFIED","MEDIUM_SEVERITY_UNSPECIFIED"],"avoidedHighSeverityCategories":["HIGHER_SEVERITY_UNSPECIFIED","HIGHER_SEVERITY_UNSPECIFIED"]},"fraudInvalidTraffic":{"avoidInsufficientOption":True,"avoidedFraudOption":"FRAUD_UNSPECIFIED"},"avoidedAgeRatings":["AGE_RATING_UNSPECIFIED","AGE_RATING_UNSPECIFIED"],"videoViewability":{"videoViewableRate":"VIDEO_VIEWABLE_RATE_UNSPECIFIED","playerImpressionRate":"PLAYER_SIZE_400X300_UNSPECIFIED","videoIab":"VIDEO_IAB_UNSPECIFIED"},"displayViewability":{"viewableDuring":"AVERAGE_VIEW_DURATION_UNSPECIFIED","iab":"IAB_VIEWED_RATE_UNSPECIFIED"}},"adloox":{"excludedAdlooxCategories":["ADLOOX_UNSPECIFIED","ADLOOX_UNSPECIFIED"]},"integralAdScience":{"excludeUnrateable":True,"excludedViolenceRisk":"VIOLENCE_UNSPECIFIED","excludedIllegalDownloadsRisk":"ILLEGAL_DOWNLOADS_UNSPECIFIED","excludedOffensiveLanguageRisk":"OFFENSIVE_LANGUAGE_UNSPECIFIED","videoViewability":"VIDEO_VIEWABILITY_UNSPECIFIED","excludedGamblingRisk":"GAMBLING_UNSPECIFIED","displayViewability":"PERFORMANCE_VIEWABILITY_UNSPECIFIED","customSegmentId":["customSegmentId","customSegmentId"],"excludedDrugsRisk":"DRUGS_UNSPECIFIED","excludedAlcoholRisk":"ALCOHOL_UNSPECIFIED","excludedHateSpeechRisk":"HATE_SPEECH_UNSPECIFIED","excludedAdFraudRisk":"SUSPICIOUS_ACTIVITY_UNSPECIFIED","traqScoreOption":"TRAQ_UNSPECIFIED","excludedAdultRisk":"ADULT_UNSPECIFIED"}},"videoPlayerSizeDetails":{"targetingOptionId":"targetingOptionId","videoPlayerSize":"VIDEO_PLAYER_SIZE_UNSPECIFIED"},"carrierAndIspDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"userRewardedContentDetails":{"targetingOptionId":"targetingOptionId","userRewardedContent":"USER_REWARDED_CONTENT_UNSPECIFIED"},"ageRangeDetails":{"ageRange":"AGE_RANGE_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"regionalLocationListDetails":{"negative":True,"regionalLocationListId":"regionalLocationListId"}}],"targetingType":"TARGETING_TYPE_UNSPECIFIED"},{"assignedTargetingOptions":[{"inheritance":"INHERITANCE_UNSPECIFIED","householdIncomeDetails":{"targetingOptionId":"targetingOptionId","householdIncome":"HOUSEHOLD_INCOME_UNSPECIFIED"},"assignedTargetingOptionId":"assignedTargetingOptionId","inventorySourceGroupDetails":{"inventorySourceGroupId":"inventorySourceGroupId"},"channelDetails":{"negative":True,"channelId":"channelId"},"omidDetails":{"targetingOptionId":"targetingOptionId","omid":"OMID_UNSPECIFIED"},"contentInstreamPositionDetails":{"adType":"AD_TYPE_UNSPECIFIED","contentInstreamPosition":"CONTENT_INSTREAM_POSITION_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"browserDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"audienceGroupDetails":{"includedGoogleAudienceGroup":{"settings":[{"googleAudienceId":"googleAudienceId"},{"googleAudienceId":"googleAudienceId"}]},"includedCustomListGroup":{"settings":[{"customListId":"customListId"},{"customListId":"customListId"}]},"includedCombinedAudienceGroup":{"settings":[{"combinedAudienceId":"combinedAudienceId"},{"combinedAudienceId":"combinedAudienceId"}]},"excludedGoogleAudienceGroup":{"settings":[{"googleAudienceId":"googleAudienceId"},{"googleAudienceId":"googleAudienceId"}]},"excludedFirstAndThirdPartyAudienceGroup":{"settings":[{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"},{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"}]},"includedFirstAndThirdPartyAudienceGroups":[{"settings":[{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"},{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"}]},{"settings":[{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"},{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"}]}]},"nativeContentPositionDetails":{"targetingOptionId":"targetingOptionId","contentPosition":"NATIVE_CONTENT_POSITION_UNSPECIFIED"},"dayAndTimeDetails":{"endHour":6,"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startHour":1,"timeZoneResolution":"TIME_ZONE_RESOLUTION_UNSPECIFIED"},"exchangeDetails":{"targetingOptionId":"targetingOptionId"},"keywordDetails":{"negative":True,"keyword":"keyword"},"targetingType":"TARGETING_TYPE_UNSPECIFIED","deviceMakeModelDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"digitalContentLabelExclusionDetails":{"excludedTargetingOptionId":"excludedTargetingOptionId","contentRatingTier":"CONTENT_RATING_TIER_UNSPECIFIED"},"poiDetails":{"proximityRadiusAmount":2.3021358869347655,"proximityRadiusUnit":"DISTANCE_UNIT_UNSPECIFIED","displayName":"displayName","latitude":5.962133916683182,"targetingOptionId":"targetingOptionId","longitude":5.637376656633329},"environmentDetails":{"environment":"ENVIRONMENT_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"subExchangeDetails":{"targetingOptionId":"targetingOptionId"},"appCategoryDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"contentDurationDetails":{"contentDuration":"CONTENT_DURATION_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"deviceTypeDetails":{"deviceType":"DEVICE_TYPE_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"appDetails":{"negative":True,"appPlatform":"APP_PLATFORM_UNSPECIFIED","displayName":"displayName","appId":"appId"},"name":"name","viewabilityDetails":{"viewability":"VIEWABILITY_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"contentGenreDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"authorizedSellerStatusDetails":{"targetingOptionId":"targetingOptionId","authorizedSellerStatus":"AUTHORIZED_SELLER_STATUS_UNSPECIFIED"},"contentStreamTypeDetails":{"contentStreamType":"CONTENT_STREAM_TYPE_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"geoRegionDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId","geoRegionType":"GEO_REGION_TYPE_UNKNOWN"},"businessChainDetails":{"proximityRadiusAmount":0.8008281904610115,"proximityRadiusUnit":"DISTANCE_UNIT_UNSPECIFIED","displayName":"displayName","targetingOptionId":"targetingOptionId"},"parentalStatusDetails":{"targetingOptionId":"targetingOptionId","parentalStatus":"PARENTAL_STATUS_UNSPECIFIED"},"negativeKeywordListDetails":{"negativeKeywordListId":"negativeKeywordListId"},"categoryDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"urlDetails":{"negative":True,"url":"url"},"operatingSystemDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"sensitiveCategoryExclusionDetails":{"sensitiveCategory":"SENSITIVE_CATEGORY_UNSPECIFIED","excludedTargetingOptionId":"excludedTargetingOptionId"},"proximityLocationListDetails":{"proximityLocationListId":"proximityLocationListId","proximityRadiusRange":"PROXIMITY_RADIUS_RANGE_UNSPECIFIED"},"onScreenPositionDetails":{"adType":"AD_TYPE_UNSPECIFIED","targetingOptionId":"targetingOptionId","onScreenPosition":"ON_SCREEN_POSITION_UNSPECIFIED"},"contentOutstreamPositionDetails":{"adType":"AD_TYPE_UNSPECIFIED","contentOutstreamPosition":"CONTENT_OUTSTREAM_POSITION_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"audioContentTypeDetails":{"audioContentType":"AUDIO_CONTENT_TYPE_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"genderDetails":{"gender":"GENDER_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"inventorySourceDetails":{"inventorySourceId":"inventorySourceId"},"languageDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"thirdPartyVerifierDetails":{"doubleVerify":{"appStarRating":{"avoidInsufficientStarRating":True,"avoidedStarRating":"APP_STAR_RATE_UNSPECIFIED"},"customSegmentId":"customSegmentId","brandSafetyCategories":{"avoidUnknownBrandSafetyCategory":True,"avoidedMediumSeverityCategories":["MEDIUM_SEVERITY_UNSPECIFIED","MEDIUM_SEVERITY_UNSPECIFIED"],"avoidedHighSeverityCategories":["HIGHER_SEVERITY_UNSPECIFIED","HIGHER_SEVERITY_UNSPECIFIED"]},"fraudInvalidTraffic":{"avoidInsufficientOption":True,"avoidedFraudOption":"FRAUD_UNSPECIFIED"},"avoidedAgeRatings":["AGE_RATING_UNSPECIFIED","AGE_RATING_UNSPECIFIED"],"videoViewability":{"videoViewableRate":"VIDEO_VIEWABLE_RATE_UNSPECIFIED","playerImpressionRate":"PLAYER_SIZE_400X300_UNSPECIFIED","videoIab":"VIDEO_IAB_UNSPECIFIED"},"displayViewability":{"viewableDuring":"AVERAGE_VIEW_DURATION_UNSPECIFIED","iab":"IAB_VIEWED_RATE_UNSPECIFIED"}},"adloox":{"excludedAdlooxCategories":["ADLOOX_UNSPECIFIED","ADLOOX_UNSPECIFIED"]},"integralAdScience":{"excludeUnrateable":True,"excludedViolenceRisk":"VIOLENCE_UNSPECIFIED","excludedIllegalDownloadsRisk":"ILLEGAL_DOWNLOADS_UNSPECIFIED","excludedOffensiveLanguageRisk":"OFFENSIVE_LANGUAGE_UNSPECIFIED","videoViewability":"VIDEO_VIEWABILITY_UNSPECIFIED","excludedGamblingRisk":"GAMBLING_UNSPECIFIED","displayViewability":"PERFORMANCE_VIEWABILITY_UNSPECIFIED","customSegmentId":["customSegmentId","customSegmentId"],"excludedDrugsRisk":"DRUGS_UNSPECIFIED","excludedAlcoholRisk":"ALCOHOL_UNSPECIFIED","excludedHateSpeechRisk":"HATE_SPEECH_UNSPECIFIED","excludedAdFraudRisk":"SUSPICIOUS_ACTIVITY_UNSPECIFIED","traqScoreOption":"TRAQ_UNSPECIFIED","excludedAdultRisk":"ADULT_UNSPECIFIED"}},"videoPlayerSizeDetails":{"targetingOptionId":"targetingOptionId","videoPlayerSize":"VIDEO_PLAYER_SIZE_UNSPECIFIED"},"carrierAndIspDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"userRewardedContentDetails":{"targetingOptionId":"targetingOptionId","userRewardedContent":"USER_REWARDED_CONTENT_UNSPECIFIED"},"ageRangeDetails":{"ageRange":"AGE_RANGE_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"regionalLocationListDetails":{"negative":True,"regionalLocationListId":"regionalLocationListId"}},{"inheritance":"INHERITANCE_UNSPECIFIED","householdIncomeDetails":{"targetingOptionId":"targetingOptionId","householdIncome":"HOUSEHOLD_INCOME_UNSPECIFIED"},"assignedTargetingOptionId":"assignedTargetingOptionId","inventorySourceGroupDetails":{"inventorySourceGroupId":"inventorySourceGroupId"},"channelDetails":{"negative":True,"channelId":"channelId"},"omidDetails":{"targetingOptionId":"targetingOptionId","omid":"OMID_UNSPECIFIED"},"contentInstreamPositionDetails":{"adType":"AD_TYPE_UNSPECIFIED","contentInstreamPosition":"CONTENT_INSTREAM_POSITION_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"browserDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"audienceGroupDetails":{"includedGoogleAudienceGroup":{"settings":[{"googleAudienceId":"googleAudienceId"},{"googleAudienceId":"googleAudienceId"}]},"includedCustomListGroup":{"settings":[{"customListId":"customListId"},{"customListId":"customListId"}]},"includedCombinedAudienceGroup":{"settings":[{"combinedAudienceId":"combinedAudienceId"},{"combinedAudienceId":"combinedAudienceId"}]},"excludedGoogleAudienceGroup":{"settings":[{"googleAudienceId":"googleAudienceId"},{"googleAudienceId":"googleAudienceId"}]},"excludedFirstAndThirdPartyAudienceGroup":{"settings":[{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"},{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"}]},"includedFirstAndThirdPartyAudienceGroups":[{"settings":[{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"},{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"}]},{"settings":[{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"},{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"}]}]},"nativeContentPositionDetails":{"targetingOptionId":"targetingOptionId","contentPosition":"NATIVE_CONTENT_POSITION_UNSPECIFIED"},"dayAndTimeDetails":{"endHour":6,"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startHour":1,"timeZoneResolution":"TIME_ZONE_RESOLUTION_UNSPECIFIED"},"exchangeDetails":{"targetingOptionId":"targetingOptionId"},"keywordDetails":{"negative":True,"keyword":"keyword"},"targetingType":"TARGETING_TYPE_UNSPECIFIED","deviceMakeModelDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"digitalContentLabelExclusionDetails":{"excludedTargetingOptionId":"excludedTargetingOptionId","contentRatingTier":"CONTENT_RATING_TIER_UNSPECIFIED"},"poiDetails":{"proximityRadiusAmount":2.3021358869347655,"proximityRadiusUnit":"DISTANCE_UNIT_UNSPECIFIED","displayName":"displayName","latitude":5.962133916683182,"targetingOptionId":"targetingOptionId","longitude":5.637376656633329},"environmentDetails":{"environment":"ENVIRONMENT_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"subExchangeDetails":{"targetingOptionId":"targetingOptionId"},"appCategoryDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"contentDurationDetails":{"contentDuration":"CONTENT_DURATION_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"deviceTypeDetails":{"deviceType":"DEVICE_TYPE_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"appDetails":{"negative":True,"appPlatform":"APP_PLATFORM_UNSPECIFIED","displayName":"displayName","appId":"appId"},"name":"name","viewabilityDetails":{"viewability":"VIEWABILITY_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"contentGenreDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"authorizedSellerStatusDetails":{"targetingOptionId":"targetingOptionId","authorizedSellerStatus":"AUTHORIZED_SELLER_STATUS_UNSPECIFIED"},"contentStreamTypeDetails":{"contentStreamType":"CONTENT_STREAM_TYPE_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"geoRegionDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId","geoRegionType":"GEO_REGION_TYPE_UNKNOWN"},"businessChainDetails":{"proximityRadiusAmount":0.8008281904610115,"proximityRadiusUnit":"DISTANCE_UNIT_UNSPECIFIED","displayName":"displayName","targetingOptionId":"targetingOptionId"},"parentalStatusDetails":{"targetingOptionId":"targetingOptionId","parentalStatus":"PARENTAL_STATUS_UNSPECIFIED"},"negativeKeywordListDetails":{"negativeKeywordListId":"negativeKeywordListId"},"categoryDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"urlDetails":{"negative":True,"url":"url"},"operatingSystemDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"sensitiveCategoryExclusionDetails":{"sensitiveCategory":"SENSITIVE_CATEGORY_UNSPECIFIED","excludedTargetingOptionId":"excludedTargetingOptionId"},"proximityLocationListDetails":{"proximityLocationListId":"proximityLocationListId","proximityRadiusRange":"PROXIMITY_RADIUS_RANGE_UNSPECIFIED"},"onScreenPositionDetails":{"adType":"AD_TYPE_UNSPECIFIED","targetingOptionId":"targetingOptionId","onScreenPosition":"ON_SCREEN_POSITION_UNSPECIFIED"},"contentOutstreamPositionDetails":{"adType":"AD_TYPE_UNSPECIFIED","contentOutstreamPosition":"CONTENT_OUTSTREAM_POSITION_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"audioContentTypeDetails":{"audioContentType":"AUDIO_CONTENT_TYPE_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"genderDetails":{"gender":"GENDER_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"inventorySourceDetails":{"inventorySourceId":"inventorySourceId"},"languageDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"thirdPartyVerifierDetails":{"doubleVerify":{"appStarRating":{"avoidInsufficientStarRating":True,"avoidedStarRating":"APP_STAR_RATE_UNSPECIFIED"},"customSegmentId":"customSegmentId","brandSafetyCategories":{"avoidUnknownBrandSafetyCategory":True,"avoidedMediumSeverityCategories":["MEDIUM_SEVERITY_UNSPECIFIED","MEDIUM_SEVERITY_UNSPECIFIED"],"avoidedHighSeverityCategories":["HIGHER_SEVERITY_UNSPECIFIED","HIGHER_SEVERITY_UNSPECIFIED"]},"fraudInvalidTraffic":{"avoidInsufficientOption":True,"avoidedFraudOption":"FRAUD_UNSPECIFIED"},"avoidedAgeRatings":["AGE_RATING_UNSPECIFIED","AGE_RATING_UNSPECIFIED"],"videoViewability":{"videoViewableRate":"VIDEO_VIEWABLE_RATE_UNSPECIFIED","playerImpressionRate":"PLAYER_SIZE_400X300_UNSPECIFIED","videoIab":"VIDEO_IAB_UNSPECIFIED"},"displayViewability":{"viewableDuring":"AVERAGE_VIEW_DURATION_UNSPECIFIED","iab":"IAB_VIEWED_RATE_UNSPECIFIED"}},"adloox":{"excludedAdlooxCategories":["ADLOOX_UNSPECIFIED","ADLOOX_UNSPECIFIED"]},"integralAdScience":{"excludeUnrateable":True,"excludedViolenceRisk":"VIOLENCE_UNSPECIFIED","excludedIllegalDownloadsRisk":"ILLEGAL_DOWNLOADS_UNSPECIFIED","excludedOffensiveLanguageRisk":"OFFENSIVE_LANGUAGE_UNSPECIFIED","videoViewability":"VIDEO_VIEWABILITY_UNSPECIFIED","excludedGamblingRisk":"GAMBLING_UNSPECIFIED","displayViewability":"PERFORMANCE_VIEWABILITY_UNSPECIFIED","customSegmentId":["customSegmentId","customSegmentId"],"excludedDrugsRisk":"DRUGS_UNSPECIFIED","excludedAlcoholRisk":"ALCOHOL_UNSPECIFIED","excludedHateSpeechRisk":"HATE_SPEECH_UNSPECIFIED","excludedAdFraudRisk":"SUSPICIOUS_ACTIVITY_UNSPECIFIED","traqScoreOption":"TRAQ_UNSPECIFIED","excludedAdultRisk":"ADULT_UNSPECIFIED"}},"videoPlayerSizeDetails":{"targetingOptionId":"targetingOptionId","videoPlayerSize":"VIDEO_PLAYER_SIZE_UNSPECIFIED"},"carrierAndIspDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"userRewardedContentDetails":{"targetingOptionId":"targetingOptionId","userRewardedContent":"USER_REWARDED_CONTENT_UNSPECIFIED"},"ageRangeDetails":{"ageRange":"AGE_RANGE_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"regionalLocationListDetails":{"negative":True,"regionalLocationListId":"regionalLocationListId"}}],"targetingType":"TARGETING_TYPE_UNSPECIFIED"}],"deleteRequests":[{"targetingType":"TARGETING_TYPE_UNSPECIFIED","assignedTargetingOptionIds":["assignedTargetingOptionIds","assignedTargetingOptionIds"]},{"targetingType":"TARGETING_TYPE_UNSPECIFIED","assignedTargetingOptionIds":["assignedTargetingOptionIds","assignedTargetingOptionIds"]}]}
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
        path='/v1/advertisers/{advertiser_idbulk_edit_advertiser_assigned_targeting_option}'.format(advertiser_id='advertiser_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_bulk_list_advertiser_assigned_targeting_options(client):
    """Test case for displayvideo_advertisers_bulk_list_advertiser_assigned_targeting_options

    
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
        path='/v1/advertisers/{advertiser_idbulk_list_advertiser_assigned_targeting_option}'.format(advertiser_id='advertiser_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_campaigns_bulk_list_campaign_assigned_targeting_options(client):
    """Test case for displayvideo_advertisers_campaigns_bulk_list_campaign_assigned_targeting_options

    
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
        path='/v1/advertisers/{advertiser_id}/campaigns/{campaign_idbulk_list_campaign_assigned_targeting_option}'.format(advertiser_id='advertiser_id_example', campaign_id='campaign_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_campaigns_create(client):
    """Test case for displayvideo_advertisers_campaigns_create

    
    """
    body = {"campaignGoal":{"performanceGoal":{"performanceGoalPercentageMicros":"performanceGoalPercentageMicros","performanceGoalType":"PERFORMANCE_GOAL_TYPE_UNSPECIFIED","performanceGoalAmountMicros":"performanceGoalAmountMicros","performanceGoalString":"performanceGoalString"},"campaignGoalType":"CAMPAIGN_GOAL_TYPE_UNSPECIFIED"},"campaignBudgets":[{"invoiceGroupingId":"invoiceGroupingId","dateRange":{"endDate":{"month":6,"year":1,"day":0},"startDate":{"month":6,"year":1,"day":0}},"budgetUnit":"BUDGET_UNIT_UNSPECIFIED","displayName":"displayName","externalBudgetSource":"EXTERNAL_BUDGET_SOURCE_UNSPECIFIED","budgetAmountMicros":"budgetAmountMicros","budgetId":"budgetId","externalBudgetId":"externalBudgetId","prismaConfig":{"supplier":"supplier","prismaType":"PRISMA_TYPE_UNSPECIFIED","prismaCpeCode":{"prismaEstimateCode":"prismaEstimateCode","prismaProductCode":"prismaProductCode","prismaClientCode":"prismaClientCode"}}},{"invoiceGroupingId":"invoiceGroupingId","dateRange":{"endDate":{"month":6,"year":1,"day":0},"startDate":{"month":6,"year":1,"day":0}},"budgetUnit":"BUDGET_UNIT_UNSPECIFIED","displayName":"displayName","externalBudgetSource":"EXTERNAL_BUDGET_SOURCE_UNSPECIFIED","budgetAmountMicros":"budgetAmountMicros","budgetId":"budgetId","externalBudgetId":"externalBudgetId","prismaConfig":{"supplier":"supplier","prismaType":"PRISMA_TYPE_UNSPECIFIED","prismaCpeCode":{"prismaEstimateCode":"prismaEstimateCode","prismaProductCode":"prismaProductCode","prismaClientCode":"prismaClientCode"}}}],"entityStatus":"ENTITY_STATUS_UNSPECIFIED","campaignId":"campaignId","displayName":"displayName","name":"name","updateTime":"updateTime","frequencyCap":{"maxImpressions":5,"unlimited":True,"timeUnitCount":5,"timeUnit":"TIME_UNIT_UNSPECIFIED"},"campaignFlight":{"plannedDates":{"endDate":{"month":6,"year":1,"day":0},"startDate":{"month":6,"year":1,"day":0}},"plannedSpendAmountMicros":"plannedSpendAmountMicros"},"advertiserId":"advertiserId"}
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
        path='/v1/advertisers/{advertiser_id}/campaigns'.format(advertiser_id='advertiser_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_campaigns_delete(client):
    """Test case for displayvideo_advertisers_campaigns_delete

    
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
        path='/v1/advertisers/{advertiser_id}/campaigns/{campaign_id}'.format(advertiser_id='advertiser_id_example', campaign_id='campaign_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_campaigns_get(client):
    """Test case for displayvideo_advertisers_campaigns_get

    
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
        path='/v1/advertisers/{advertiser_id}/campaigns/{campaign_id}'.format(advertiser_id='advertiser_id_example', campaign_id='campaign_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_campaigns_list(client):
    """Test case for displayvideo_advertisers_campaigns_list

    
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
        path='/v1/advertisers/{advertiser_id}/campaigns'.format(advertiser_id='advertiser_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_campaigns_patch(client):
    """Test case for displayvideo_advertisers_campaigns_patch

    
    """
    body = {"campaignGoal":{"performanceGoal":{"performanceGoalPercentageMicros":"performanceGoalPercentageMicros","performanceGoalType":"PERFORMANCE_GOAL_TYPE_UNSPECIFIED","performanceGoalAmountMicros":"performanceGoalAmountMicros","performanceGoalString":"performanceGoalString"},"campaignGoalType":"CAMPAIGN_GOAL_TYPE_UNSPECIFIED"},"campaignBudgets":[{"invoiceGroupingId":"invoiceGroupingId","dateRange":{"endDate":{"month":6,"year":1,"day":0},"startDate":{"month":6,"year":1,"day":0}},"budgetUnit":"BUDGET_UNIT_UNSPECIFIED","displayName":"displayName","externalBudgetSource":"EXTERNAL_BUDGET_SOURCE_UNSPECIFIED","budgetAmountMicros":"budgetAmountMicros","budgetId":"budgetId","externalBudgetId":"externalBudgetId","prismaConfig":{"supplier":"supplier","prismaType":"PRISMA_TYPE_UNSPECIFIED","prismaCpeCode":{"prismaEstimateCode":"prismaEstimateCode","prismaProductCode":"prismaProductCode","prismaClientCode":"prismaClientCode"}}},{"invoiceGroupingId":"invoiceGroupingId","dateRange":{"endDate":{"month":6,"year":1,"day":0},"startDate":{"month":6,"year":1,"day":0}},"budgetUnit":"BUDGET_UNIT_UNSPECIFIED","displayName":"displayName","externalBudgetSource":"EXTERNAL_BUDGET_SOURCE_UNSPECIFIED","budgetAmountMicros":"budgetAmountMicros","budgetId":"budgetId","externalBudgetId":"externalBudgetId","prismaConfig":{"supplier":"supplier","prismaType":"PRISMA_TYPE_UNSPECIFIED","prismaCpeCode":{"prismaEstimateCode":"prismaEstimateCode","prismaProductCode":"prismaProductCode","prismaClientCode":"prismaClientCode"}}}],"entityStatus":"ENTITY_STATUS_UNSPECIFIED","campaignId":"campaignId","displayName":"displayName","name":"name","updateTime":"updateTime","frequencyCap":{"maxImpressions":5,"unlimited":True,"timeUnitCount":5,"timeUnit":"TIME_UNIT_UNSPECIFIED"},"campaignFlight":{"plannedDates":{"endDate":{"month":6,"year":1,"day":0},"startDate":{"month":6,"year":1,"day":0}},"plannedSpendAmountMicros":"plannedSpendAmountMicros"},"advertiserId":"advertiserId"}
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
                    ('updateMask', 'update_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/advertisers/{advertiser_id}/campaigns/{campaign_id}'.format(advertiser_id='advertiser_id_example', campaign_id='campaign_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_campaigns_targeting_types_assigned_targeting_options_get(client):
    """Test case for displayvideo_advertisers_campaigns_targeting_types_assigned_targeting_options_get

    
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
        path='/v1/advertisers/{advertiser_id}/campaigns/{campaign_id}/targetingTypes/{targeting_type}/assignedTargetingOptions/{assigned_targeting_option_id}'.format(advertiser_id='advertiser_id_example', campaign_id='campaign_id_example', targeting_type='targeting_type_example', assigned_targeting_option_id='assigned_targeting_option_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_campaigns_targeting_types_assigned_targeting_options_list(client):
    """Test case for displayvideo_advertisers_campaigns_targeting_types_assigned_targeting_options_list

    
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
        path='/v1/advertisers/{advertiser_id}/campaigns/{campaign_id}/targetingTypes/{targeting_type}/assignedTargetingOptions'.format(advertiser_id='advertiser_id_example', campaign_id='campaign_id_example', targeting_type='targeting_type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_channels_create(client):
    """Test case for displayvideo_advertisers_channels_create

    
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
                    ('partnerId', 'partner_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/advertisers/{advertiser_id}/channels'.format(advertiser_id='advertiser_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_channels_list(client):
    """Test case for displayvideo_advertisers_channels_list

    
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
                    ('pageToken', 'page_token_example'),
                    ('partnerId', 'partner_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/advertisers/{advertiser_id}/channels'.format(advertiser_id='advertiser_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_channels_patch(client):
    """Test case for displayvideo_advertisers_channels_patch

    
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
                    ('partnerId', 'partner_id_example'),
                    ('updateMask', 'update_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/advertisers/{advertiser_id}/channels/{channel_id}'.format(advertiser_id='advertiser_id_example', channel_id='channel_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_channels_sites_bulk_edit(client):
    """Test case for displayvideo_advertisers_channels_sites_bulk_edit

    
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
        path='/v1/advertisers/{advertiser_id}/channels/{channel_id}/sites:bulkEdit'.format(advertiser_id='advertiser_id_example', channel_id='channel_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_channels_sites_delete(client):
    """Test case for displayvideo_advertisers_channels_sites_delete

    
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
                    ('partnerId', 'partner_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/advertisers/{advertiser_id}/channels/{channel_id}/sites/{url_or_app_id}'.format(advertiser_id='advertiser_id_example', channel_id='channel_id_example', url_or_app_id='url_or_app_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_channels_sites_list(client):
    """Test case for displayvideo_advertisers_channels_sites_list

    
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
                    ('pageToken', 'page_token_example'),
                    ('partnerId', 'partner_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/advertisers/{advertiser_id}/channels/{channel_id}/sites'.format(advertiser_id='advertiser_id_example', channel_id='channel_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_channels_sites_replace(client):
    """Test case for displayvideo_advertisers_channels_sites_replace

    
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
        path='/v1/advertisers/{advertiser_id}/channels/{channel_id}/sites:replace'.format(advertiser_id='advertiser_id_example', channel_id='channel_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_create(client):
    """Test case for displayvideo_advertisers_create

    
    """
    body = {"adServerConfig":{"thirdPartyOnlyConfig":{"pixelOrderIdReportingEnabled":True},"cmHybridConfig":{"cmSyncableSiteIds":["cmSyncableSiteIds","cmSyncableSiteIds"],"dv360ToCmDataSharingEnabled":True,"dv360ToCmCostReportingEnabled":True,"cmAdvertiserIds":["cmAdvertiserIds","cmAdvertiserIds"],"cmFloodlightConfigId":"cmFloodlightConfigId","cmFloodlightLinkingAuthorized":True,"cmAccountId":"cmAccountId"}},"displayName":"displayName","creativeConfig":{"dynamicCreativeEnabled":True,"videoCreativeDataSharingAuthorized":True,"obaComplianceDisabled":True,"iasClientId":"iasClientId"},"updateTime":"updateTime","integrationDetails":{"integrationCode":"integrationCode","details":"details"},"advertiserId":"advertiserId","servingConfig":{"exemptTvFromViewabilityTargeting":True},"entityStatus":"ENTITY_STATUS_UNSPECIFIED","prismaEnabled":True,"generalConfig":{"timeZone":"timeZone","currencyCode":"currencyCode","domainUrl":"domainUrl"},"name":"name","partnerId":"partnerId","dataAccessConfig":{"sdfConfig":{"sdfConfig":{"version":"SDF_VERSION_UNSPECIFIED","adminEmail":"adminEmail"},"overridePartnerSdfConfig":True}}}
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
        path='/v1/advertisers',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_creatives_create(client):
    """Test case for displayvideo_advertisers_creatives_create

    
    """
    body = {"appendedTag":"appendedTag","companionCreativeIds":["companionCreativeIds","companionCreativeIds"],"expandOnHover":True,"vastTagUrl":"vastTagUrl","notes":"notes","displayName":"displayName","html5Video":True,"expandingDirection":"EXPANDING_DIRECTION_UNSPECIFIED","iasCampaignMonitoring":True,"cmPlacementId":"cmPlacementId","creativeId":"creativeId","obaIcon":{"clickTrackingUrl":"clickTrackingUrl","resourceUrl":"resourceUrl","viewTrackingUrl":"viewTrackingUrl","resourceMimeType":"resourceMimeType","position":"OBA_ICON_POSITION_UNSPECIFIED","program":"program","landingPageUrl":"landingPageUrl","dimensions":{"heightPixels":0,"widthPixels":6}},"assets":[{"role":"ASSET_ROLE_UNSPECIFIED","asset":{"mediaId":"mediaId","content":"content"}},{"role":"ASSET_ROLE_UNSPECIFIED","asset":{"mediaId":"mediaId","content":"content"}}],"jsTrackerUrl":"jsTrackerUrl","timerEvents":[{"reportingName":"reportingName","name":"name"},{"reportingName":"reportingName","name":"name"}],"integrationCode":"integrationCode","oggAudio":True,"cmTrackingAd":{"cmAdId":"cmAdId","cmPlacementId":"cmPlacementId","cmCreativeId":"cmCreativeId"},"dynamic":True,"transcodes":[{"fileSizeBytes":"fileSizeBytes","frameRate":1.4658129,"bitRateKbps":"bitRateKbps","name":"name","audioSampleRateHz":"audioSampleRateHz","mimeType":"mimeType","transcoded":True,"audioBitRateKbps":"audioBitRateKbps","dimensions":{"heightPixels":0,"widthPixels":6}},{"fileSizeBytes":"fileSizeBytes","frameRate":1.4658129,"bitRateKbps":"bitRateKbps","name":"name","audioSampleRateHz":"audioSampleRateHz","mimeType":"mimeType","transcoded":True,"audioBitRateKbps":"audioBitRateKbps","dimensions":{"heightPixels":0,"widthPixels":6}}],"hostingSource":"HOSTING_SOURCE_UNSPECIFIED","thirdPartyTag":"thirdPartyTag","thirdPartyUrls":[{"type":"THIRD_PARTY_URL_TYPE_UNSPECIFIED","url":"url"},{"type":"THIRD_PARTY_URL_TYPE_UNSPECIFIED","url":"url"}],"lineItemIds":["lineItemIds","lineItemIds"],"trackerUrls":["trackerUrls","trackerUrls"],"counterEvents":[{"reportingName":"reportingName","name":"name"},{"reportingName":"reportingName","name":"name"}],"requireMraid":True,"updateTime":"updateTime","skippable":True,"mp3Audio":True,"universalAdId":{"registry":"UNIVERSAL_AD_REGISTRY_UNSPECIFIED","id":"id"},"advertiserId":"advertiserId","progressOffset":{"seconds":"seconds","percentage":"percentage"},"requirePingForAttribution":True,"vpaid":True,"additionalDimensions":[{"heightPixels":0,"widthPixels":6},{"heightPixels":0,"widthPixels":6}],"createTime":"createTime","creativeType":"CREATIVE_TYPE_UNSPECIFIED","entityStatus":"ENTITY_STATUS_UNSPECIFIED","requireHtml5":True,"name":"name","mediaDuration":"mediaDuration","reviewStatus":{"approvalStatus":"APPROVAL_STATUS_UNSPECIFIED","contentAndPolicyReviewStatus":"REVIEW_STATUS_UNSPECIFIED","creativeAndLandingPageReviewStatus":"REVIEW_STATUS_UNSPECIFIED","publisherReviewStatuses":[{"publisherName":"publisherName","status":"REVIEW_STATUS_UNSPECIFIED"},{"publisherName":"publisherName","status":"REVIEW_STATUS_UNSPECIFIED"}],"exchangeReviewStatuses":[{"exchange":"EXCHANGE_UNSPECIFIED","status":"REVIEW_STATUS_UNSPECIFIED"},{"exchange":"EXCHANGE_UNSPECIFIED","status":"REVIEW_STATUS_UNSPECIFIED"}]},"skipOffset":{"seconds":"seconds","percentage":"percentage"},"creativeAttributes":["CREATIVE_ATTRIBUTE_UNSPECIFIED","CREATIVE_ATTRIBUTE_UNSPECIFIED"],"dimensions":{"heightPixels":0,"widthPixels":6},"exitEvents":[{"reportingName":"reportingName","name":"name","type":"EXIT_EVENT_TYPE_UNSPECIFIED","url":"url"},{"reportingName":"reportingName","name":"name","type":"EXIT_EVENT_TYPE_UNSPECIFIED","url":"url"}]}
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
        path='/v1/advertisers/{advertiser_id}/creatives'.format(advertiser_id='advertiser_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_creatives_delete(client):
    """Test case for displayvideo_advertisers_creatives_delete

    
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
        path='/v1/advertisers/{advertiser_id}/creatives/{creative_id}'.format(advertiser_id='advertiser_id_example', creative_id='creative_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_creatives_get(client):
    """Test case for displayvideo_advertisers_creatives_get

    
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
        path='/v1/advertisers/{advertiser_id}/creatives/{creative_id}'.format(advertiser_id='advertiser_id_example', creative_id='creative_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_creatives_list(client):
    """Test case for displayvideo_advertisers_creatives_list

    
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
        path='/v1/advertisers/{advertiser_id}/creatives'.format(advertiser_id='advertiser_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_creatives_patch(client):
    """Test case for displayvideo_advertisers_creatives_patch

    
    """
    body = {"appendedTag":"appendedTag","companionCreativeIds":["companionCreativeIds","companionCreativeIds"],"expandOnHover":True,"vastTagUrl":"vastTagUrl","notes":"notes","displayName":"displayName","html5Video":True,"expandingDirection":"EXPANDING_DIRECTION_UNSPECIFIED","iasCampaignMonitoring":True,"cmPlacementId":"cmPlacementId","creativeId":"creativeId","obaIcon":{"clickTrackingUrl":"clickTrackingUrl","resourceUrl":"resourceUrl","viewTrackingUrl":"viewTrackingUrl","resourceMimeType":"resourceMimeType","position":"OBA_ICON_POSITION_UNSPECIFIED","program":"program","landingPageUrl":"landingPageUrl","dimensions":{"heightPixels":0,"widthPixels":6}},"assets":[{"role":"ASSET_ROLE_UNSPECIFIED","asset":{"mediaId":"mediaId","content":"content"}},{"role":"ASSET_ROLE_UNSPECIFIED","asset":{"mediaId":"mediaId","content":"content"}}],"jsTrackerUrl":"jsTrackerUrl","timerEvents":[{"reportingName":"reportingName","name":"name"},{"reportingName":"reportingName","name":"name"}],"integrationCode":"integrationCode","oggAudio":True,"cmTrackingAd":{"cmAdId":"cmAdId","cmPlacementId":"cmPlacementId","cmCreativeId":"cmCreativeId"},"dynamic":True,"transcodes":[{"fileSizeBytes":"fileSizeBytes","frameRate":1.4658129,"bitRateKbps":"bitRateKbps","name":"name","audioSampleRateHz":"audioSampleRateHz","mimeType":"mimeType","transcoded":True,"audioBitRateKbps":"audioBitRateKbps","dimensions":{"heightPixels":0,"widthPixels":6}},{"fileSizeBytes":"fileSizeBytes","frameRate":1.4658129,"bitRateKbps":"bitRateKbps","name":"name","audioSampleRateHz":"audioSampleRateHz","mimeType":"mimeType","transcoded":True,"audioBitRateKbps":"audioBitRateKbps","dimensions":{"heightPixels":0,"widthPixels":6}}],"hostingSource":"HOSTING_SOURCE_UNSPECIFIED","thirdPartyTag":"thirdPartyTag","thirdPartyUrls":[{"type":"THIRD_PARTY_URL_TYPE_UNSPECIFIED","url":"url"},{"type":"THIRD_PARTY_URL_TYPE_UNSPECIFIED","url":"url"}],"lineItemIds":["lineItemIds","lineItemIds"],"trackerUrls":["trackerUrls","trackerUrls"],"counterEvents":[{"reportingName":"reportingName","name":"name"},{"reportingName":"reportingName","name":"name"}],"requireMraid":True,"updateTime":"updateTime","skippable":True,"mp3Audio":True,"universalAdId":{"registry":"UNIVERSAL_AD_REGISTRY_UNSPECIFIED","id":"id"},"advertiserId":"advertiserId","progressOffset":{"seconds":"seconds","percentage":"percentage"},"requirePingForAttribution":True,"vpaid":True,"additionalDimensions":[{"heightPixels":0,"widthPixels":6},{"heightPixels":0,"widthPixels":6}],"createTime":"createTime","creativeType":"CREATIVE_TYPE_UNSPECIFIED","entityStatus":"ENTITY_STATUS_UNSPECIFIED","requireHtml5":True,"name":"name","mediaDuration":"mediaDuration","reviewStatus":{"approvalStatus":"APPROVAL_STATUS_UNSPECIFIED","contentAndPolicyReviewStatus":"REVIEW_STATUS_UNSPECIFIED","creativeAndLandingPageReviewStatus":"REVIEW_STATUS_UNSPECIFIED","publisherReviewStatuses":[{"publisherName":"publisherName","status":"REVIEW_STATUS_UNSPECIFIED"},{"publisherName":"publisherName","status":"REVIEW_STATUS_UNSPECIFIED"}],"exchangeReviewStatuses":[{"exchange":"EXCHANGE_UNSPECIFIED","status":"REVIEW_STATUS_UNSPECIFIED"},{"exchange":"EXCHANGE_UNSPECIFIED","status":"REVIEW_STATUS_UNSPECIFIED"}]},"skipOffset":{"seconds":"seconds","percentage":"percentage"},"creativeAttributes":["CREATIVE_ATTRIBUTE_UNSPECIFIED","CREATIVE_ATTRIBUTE_UNSPECIFIED"],"dimensions":{"heightPixels":0,"widthPixels":6},"exitEvents":[{"reportingName":"reportingName","name":"name","type":"EXIT_EVENT_TYPE_UNSPECIFIED","url":"url"},{"reportingName":"reportingName","name":"name","type":"EXIT_EVENT_TYPE_UNSPECIFIED","url":"url"}]}
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
                    ('updateMask', 'update_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/advertisers/{advertiser_id}/creatives/{creative_id}'.format(advertiser_id='advertiser_id_example', creative_id='creative_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_delete(client):
    """Test case for displayvideo_advertisers_delete

    
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
        path='/v1/advertisers/{advertiser_id}'.format(advertiser_id='advertiser_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_get(client):
    """Test case for displayvideo_advertisers_get

    
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
        path='/v1/advertisers/{advertiser_id}'.format(advertiser_id='advertiser_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_insertion_orders_bulk_list_insertion_order_assigned_targeting_options(client):
    """Test case for displayvideo_advertisers_insertion_orders_bulk_list_insertion_order_assigned_targeting_options

    
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
        path='/v1/advertisers/{advertiser_id}/insertionOrders/{insertion_order_idbulk_list_insertion_order_assigned_targeting_option}'.format(advertiser_id='advertiser_id_example', insertion_order_id='insertion_order_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_insertion_orders_create(client):
    """Test case for displayvideo_advertisers_insertion_orders_create

    
    """
    body = {"bidStrategy":{"fixedBid":{"bidAmountMicros":"bidAmountMicros"},"performanceGoalAutoBid":{"performanceGoalType":"BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_UNSPECIFIED","customBiddingAlgorithmId":"customBiddingAlgorithmId","performanceGoalAmountMicros":"performanceGoalAmountMicros","maxAverageCpmBidAmountMicros":"maxAverageCpmBidAmountMicros"},"maximizeSpendAutoBid":{"raiseBidForDeals":True,"performanceGoalType":"BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_UNSPECIFIED","customBiddingAlgorithmId":"customBiddingAlgorithmId","maxAverageCpmBidAmountMicros":"maxAverageCpmBidAmountMicros"}},"performanceGoal":{"performanceGoalPercentageMicros":"performanceGoalPercentageMicros","performanceGoalType":"PERFORMANCE_GOAL_TYPE_UNSPECIFIED","performanceGoalAmountMicros":"performanceGoalAmountMicros","performanceGoalString":"performanceGoalString"},"insertionOrderType":"INSERTION_ORDER_TYPE_UNSPECIFIED","partnerCosts":[{"feeAmount":"feeAmount","costType":"PARTNER_COST_TYPE_UNSPECIFIED","invoiceType":"PARTNER_COST_INVOICE_TYPE_UNSPECIFIED","feeType":"PARTNER_COST_FEE_TYPE_UNSPECIFIED","feePercentageMillis":"feePercentageMillis"},{"feeAmount":"feeAmount","costType":"PARTNER_COST_TYPE_UNSPECIFIED","invoiceType":"PARTNER_COST_INVOICE_TYPE_UNSPECIFIED","feeType":"PARTNER_COST_FEE_TYPE_UNSPECIFIED","feePercentageMillis":"feePercentageMillis"}],"campaignId":"campaignId","displayName":"displayName","insertionOrderId":"insertionOrderId","updateTime":"updateTime","integrationDetails":{"integrationCode":"integrationCode","details":"details"},"advertiserId":"advertiserId","pacing":{"pacingType":"PACING_TYPE_UNSPECIFIED","pacingPeriod":"PACING_PERIOD_UNSPECIFIED","dailyMaxImpressions":"dailyMaxImpressions","dailyMaxMicros":"dailyMaxMicros"},"entityStatus":"ENTITY_STATUS_UNSPECIFIED","name":"name","reservationType":"RESERVATION_TYPE_UNSPECIFIED","frequencyCap":{"maxImpressions":5,"unlimited":True,"timeUnitCount":5,"timeUnit":"TIME_UNIT_UNSPECIFIED"},"billableOutcome":"BILLABLE_OUTCOME_UNSPECIFIED","budget":{"budgetSegments":[{"campaignBudgetId":"campaignBudgetId","dateRange":{"endDate":{"month":6,"year":1,"day":0},"startDate":{"month":6,"year":1,"day":0}},"description":"description","budgetAmountMicros":"budgetAmountMicros"},{"campaignBudgetId":"campaignBudgetId","dateRange":{"endDate":{"month":6,"year":1,"day":0},"startDate":{"month":6,"year":1,"day":0}},"description":"description","budgetAmountMicros":"budgetAmountMicros"}],"budgetUnit":"BUDGET_UNIT_UNSPECIFIED","automationType":"INSERTION_ORDER_AUTOMATION_TYPE_UNSPECIFIED"}}
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
        path='/v1/advertisers/{advertiser_id}/insertionOrders'.format(advertiser_id='advertiser_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_insertion_orders_delete(client):
    """Test case for displayvideo_advertisers_insertion_orders_delete

    
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
        path='/v1/advertisers/{advertiser_id}/insertionOrders/{insertion_order_id}'.format(advertiser_id='advertiser_id_example', insertion_order_id='insertion_order_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_insertion_orders_get(client):
    """Test case for displayvideo_advertisers_insertion_orders_get

    
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
        path='/v1/advertisers/{advertiser_id}/insertionOrders/{insertion_order_id}'.format(advertiser_id='advertiser_id_example', insertion_order_id='insertion_order_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_insertion_orders_list(client):
    """Test case for displayvideo_advertisers_insertion_orders_list

    
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
        path='/v1/advertisers/{advertiser_id}/insertionOrders'.format(advertiser_id='advertiser_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_insertion_orders_patch(client):
    """Test case for displayvideo_advertisers_insertion_orders_patch

    
    """
    body = {"bidStrategy":{"fixedBid":{"bidAmountMicros":"bidAmountMicros"},"performanceGoalAutoBid":{"performanceGoalType":"BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_UNSPECIFIED","customBiddingAlgorithmId":"customBiddingAlgorithmId","performanceGoalAmountMicros":"performanceGoalAmountMicros","maxAverageCpmBidAmountMicros":"maxAverageCpmBidAmountMicros"},"maximizeSpendAutoBid":{"raiseBidForDeals":True,"performanceGoalType":"BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_UNSPECIFIED","customBiddingAlgorithmId":"customBiddingAlgorithmId","maxAverageCpmBidAmountMicros":"maxAverageCpmBidAmountMicros"}},"performanceGoal":{"performanceGoalPercentageMicros":"performanceGoalPercentageMicros","performanceGoalType":"PERFORMANCE_GOAL_TYPE_UNSPECIFIED","performanceGoalAmountMicros":"performanceGoalAmountMicros","performanceGoalString":"performanceGoalString"},"insertionOrderType":"INSERTION_ORDER_TYPE_UNSPECIFIED","partnerCosts":[{"feeAmount":"feeAmount","costType":"PARTNER_COST_TYPE_UNSPECIFIED","invoiceType":"PARTNER_COST_INVOICE_TYPE_UNSPECIFIED","feeType":"PARTNER_COST_FEE_TYPE_UNSPECIFIED","feePercentageMillis":"feePercentageMillis"},{"feeAmount":"feeAmount","costType":"PARTNER_COST_TYPE_UNSPECIFIED","invoiceType":"PARTNER_COST_INVOICE_TYPE_UNSPECIFIED","feeType":"PARTNER_COST_FEE_TYPE_UNSPECIFIED","feePercentageMillis":"feePercentageMillis"}],"campaignId":"campaignId","displayName":"displayName","insertionOrderId":"insertionOrderId","updateTime":"updateTime","integrationDetails":{"integrationCode":"integrationCode","details":"details"},"advertiserId":"advertiserId","pacing":{"pacingType":"PACING_TYPE_UNSPECIFIED","pacingPeriod":"PACING_PERIOD_UNSPECIFIED","dailyMaxImpressions":"dailyMaxImpressions","dailyMaxMicros":"dailyMaxMicros"},"entityStatus":"ENTITY_STATUS_UNSPECIFIED","name":"name","reservationType":"RESERVATION_TYPE_UNSPECIFIED","frequencyCap":{"maxImpressions":5,"unlimited":True,"timeUnitCount":5,"timeUnit":"TIME_UNIT_UNSPECIFIED"},"billableOutcome":"BILLABLE_OUTCOME_UNSPECIFIED","budget":{"budgetSegments":[{"campaignBudgetId":"campaignBudgetId","dateRange":{"endDate":{"month":6,"year":1,"day":0},"startDate":{"month":6,"year":1,"day":0}},"description":"description","budgetAmountMicros":"budgetAmountMicros"},{"campaignBudgetId":"campaignBudgetId","dateRange":{"endDate":{"month":6,"year":1,"day":0},"startDate":{"month":6,"year":1,"day":0}},"description":"description","budgetAmountMicros":"budgetAmountMicros"}],"budgetUnit":"BUDGET_UNIT_UNSPECIFIED","automationType":"INSERTION_ORDER_AUTOMATION_TYPE_UNSPECIFIED"}}
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
                    ('updateMask', 'update_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/advertisers/{advertiser_id}/insertionOrders/{insertion_order_id}'.format(advertiser_id='advertiser_id_example', insertion_order_id='insertion_order_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_insertion_orders_targeting_types_assigned_targeting_options_get(client):
    """Test case for displayvideo_advertisers_insertion_orders_targeting_types_assigned_targeting_options_get

    
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
        path='/v1/advertisers/{advertiser_id}/insertionOrders/{insertion_order_id}/targetingTypes/{targeting_type}/assignedTargetingOptions/{assigned_targeting_option_id}'.format(advertiser_id='advertiser_id_example', insertion_order_id='insertion_order_id_example', targeting_type='targeting_type_example', assigned_targeting_option_id='assigned_targeting_option_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_insertion_orders_targeting_types_assigned_targeting_options_list(client):
    """Test case for displayvideo_advertisers_insertion_orders_targeting_types_assigned_targeting_options_list

    
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
        path='/v1/advertisers/{advertiser_id}/insertionOrders/{insertion_order_id}/targetingTypes/{targeting_type}/assignedTargetingOptions'.format(advertiser_id='advertiser_id_example', insertion_order_id='insertion_order_id_example', targeting_type='targeting_type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_invoices_list(client):
    """Test case for displayvideo_advertisers_invoices_list

    
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
                    ('issueMonth', 'issue_month_example'),
                    ('loiSapinInvoiceType', 'loi_sapin_invoice_type_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/advertisers/{advertiser_id}/invoices'.format(advertiser_id='advertiser_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_invoices_lookup_invoice_currency(client):
    """Test case for displayvideo_advertisers_invoices_lookup_invoice_currency

    
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
                    ('invoiceMonth', 'invoice_month_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/advertisers/{advertiser_id}/invoices:lookupInvoiceCurrency'.format(advertiser_id='advertiser_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_line_items_bulk_edit_line_item_assigned_targeting_options(client):
    """Test case for displayvideo_advertisers_line_items_bulk_edit_line_item_assigned_targeting_options

    
    """
    body = {"createRequests":[{"assignedTargetingOptions":[{"inheritance":"INHERITANCE_UNSPECIFIED","householdIncomeDetails":{"targetingOptionId":"targetingOptionId","householdIncome":"HOUSEHOLD_INCOME_UNSPECIFIED"},"assignedTargetingOptionId":"assignedTargetingOptionId","inventorySourceGroupDetails":{"inventorySourceGroupId":"inventorySourceGroupId"},"channelDetails":{"negative":True,"channelId":"channelId"},"omidDetails":{"targetingOptionId":"targetingOptionId","omid":"OMID_UNSPECIFIED"},"contentInstreamPositionDetails":{"adType":"AD_TYPE_UNSPECIFIED","contentInstreamPosition":"CONTENT_INSTREAM_POSITION_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"browserDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"audienceGroupDetails":{"includedGoogleAudienceGroup":{"settings":[{"googleAudienceId":"googleAudienceId"},{"googleAudienceId":"googleAudienceId"}]},"includedCustomListGroup":{"settings":[{"customListId":"customListId"},{"customListId":"customListId"}]},"includedCombinedAudienceGroup":{"settings":[{"combinedAudienceId":"combinedAudienceId"},{"combinedAudienceId":"combinedAudienceId"}]},"excludedGoogleAudienceGroup":{"settings":[{"googleAudienceId":"googleAudienceId"},{"googleAudienceId":"googleAudienceId"}]},"excludedFirstAndThirdPartyAudienceGroup":{"settings":[{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"},{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"}]},"includedFirstAndThirdPartyAudienceGroups":[{"settings":[{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"},{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"}]},{"settings":[{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"},{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"}]}]},"nativeContentPositionDetails":{"targetingOptionId":"targetingOptionId","contentPosition":"NATIVE_CONTENT_POSITION_UNSPECIFIED"},"dayAndTimeDetails":{"endHour":6,"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startHour":1,"timeZoneResolution":"TIME_ZONE_RESOLUTION_UNSPECIFIED"},"exchangeDetails":{"targetingOptionId":"targetingOptionId"},"keywordDetails":{"negative":True,"keyword":"keyword"},"targetingType":"TARGETING_TYPE_UNSPECIFIED","deviceMakeModelDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"digitalContentLabelExclusionDetails":{"excludedTargetingOptionId":"excludedTargetingOptionId","contentRatingTier":"CONTENT_RATING_TIER_UNSPECIFIED"},"poiDetails":{"proximityRadiusAmount":2.3021358869347655,"proximityRadiusUnit":"DISTANCE_UNIT_UNSPECIFIED","displayName":"displayName","latitude":5.962133916683182,"targetingOptionId":"targetingOptionId","longitude":5.637376656633329},"environmentDetails":{"environment":"ENVIRONMENT_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"subExchangeDetails":{"targetingOptionId":"targetingOptionId"},"appCategoryDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"contentDurationDetails":{"contentDuration":"CONTENT_DURATION_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"deviceTypeDetails":{"deviceType":"DEVICE_TYPE_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"appDetails":{"negative":True,"appPlatform":"APP_PLATFORM_UNSPECIFIED","displayName":"displayName","appId":"appId"},"name":"name","viewabilityDetails":{"viewability":"VIEWABILITY_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"contentGenreDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"authorizedSellerStatusDetails":{"targetingOptionId":"targetingOptionId","authorizedSellerStatus":"AUTHORIZED_SELLER_STATUS_UNSPECIFIED"},"contentStreamTypeDetails":{"contentStreamType":"CONTENT_STREAM_TYPE_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"geoRegionDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId","geoRegionType":"GEO_REGION_TYPE_UNKNOWN"},"businessChainDetails":{"proximityRadiusAmount":0.8008281904610115,"proximityRadiusUnit":"DISTANCE_UNIT_UNSPECIFIED","displayName":"displayName","targetingOptionId":"targetingOptionId"},"parentalStatusDetails":{"targetingOptionId":"targetingOptionId","parentalStatus":"PARENTAL_STATUS_UNSPECIFIED"},"negativeKeywordListDetails":{"negativeKeywordListId":"negativeKeywordListId"},"categoryDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"urlDetails":{"negative":True,"url":"url"},"operatingSystemDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"sensitiveCategoryExclusionDetails":{"sensitiveCategory":"SENSITIVE_CATEGORY_UNSPECIFIED","excludedTargetingOptionId":"excludedTargetingOptionId"},"proximityLocationListDetails":{"proximityLocationListId":"proximityLocationListId","proximityRadiusRange":"PROXIMITY_RADIUS_RANGE_UNSPECIFIED"},"onScreenPositionDetails":{"adType":"AD_TYPE_UNSPECIFIED","targetingOptionId":"targetingOptionId","onScreenPosition":"ON_SCREEN_POSITION_UNSPECIFIED"},"contentOutstreamPositionDetails":{"adType":"AD_TYPE_UNSPECIFIED","contentOutstreamPosition":"CONTENT_OUTSTREAM_POSITION_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"audioContentTypeDetails":{"audioContentType":"AUDIO_CONTENT_TYPE_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"genderDetails":{"gender":"GENDER_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"inventorySourceDetails":{"inventorySourceId":"inventorySourceId"},"languageDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"thirdPartyVerifierDetails":{"doubleVerify":{"appStarRating":{"avoidInsufficientStarRating":True,"avoidedStarRating":"APP_STAR_RATE_UNSPECIFIED"},"customSegmentId":"customSegmentId","brandSafetyCategories":{"avoidUnknownBrandSafetyCategory":True,"avoidedMediumSeverityCategories":["MEDIUM_SEVERITY_UNSPECIFIED","MEDIUM_SEVERITY_UNSPECIFIED"],"avoidedHighSeverityCategories":["HIGHER_SEVERITY_UNSPECIFIED","HIGHER_SEVERITY_UNSPECIFIED"]},"fraudInvalidTraffic":{"avoidInsufficientOption":True,"avoidedFraudOption":"FRAUD_UNSPECIFIED"},"avoidedAgeRatings":["AGE_RATING_UNSPECIFIED","AGE_RATING_UNSPECIFIED"],"videoViewability":{"videoViewableRate":"VIDEO_VIEWABLE_RATE_UNSPECIFIED","playerImpressionRate":"PLAYER_SIZE_400X300_UNSPECIFIED","videoIab":"VIDEO_IAB_UNSPECIFIED"},"displayViewability":{"viewableDuring":"AVERAGE_VIEW_DURATION_UNSPECIFIED","iab":"IAB_VIEWED_RATE_UNSPECIFIED"}},"adloox":{"excludedAdlooxCategories":["ADLOOX_UNSPECIFIED","ADLOOX_UNSPECIFIED"]},"integralAdScience":{"excludeUnrateable":True,"excludedViolenceRisk":"VIOLENCE_UNSPECIFIED","excludedIllegalDownloadsRisk":"ILLEGAL_DOWNLOADS_UNSPECIFIED","excludedOffensiveLanguageRisk":"OFFENSIVE_LANGUAGE_UNSPECIFIED","videoViewability":"VIDEO_VIEWABILITY_UNSPECIFIED","excludedGamblingRisk":"GAMBLING_UNSPECIFIED","displayViewability":"PERFORMANCE_VIEWABILITY_UNSPECIFIED","customSegmentId":["customSegmentId","customSegmentId"],"excludedDrugsRisk":"DRUGS_UNSPECIFIED","excludedAlcoholRisk":"ALCOHOL_UNSPECIFIED","excludedHateSpeechRisk":"HATE_SPEECH_UNSPECIFIED","excludedAdFraudRisk":"SUSPICIOUS_ACTIVITY_UNSPECIFIED","traqScoreOption":"TRAQ_UNSPECIFIED","excludedAdultRisk":"ADULT_UNSPECIFIED"}},"videoPlayerSizeDetails":{"targetingOptionId":"targetingOptionId","videoPlayerSize":"VIDEO_PLAYER_SIZE_UNSPECIFIED"},"carrierAndIspDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"userRewardedContentDetails":{"targetingOptionId":"targetingOptionId","userRewardedContent":"USER_REWARDED_CONTENT_UNSPECIFIED"},"ageRangeDetails":{"ageRange":"AGE_RANGE_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"regionalLocationListDetails":{"negative":True,"regionalLocationListId":"regionalLocationListId"}},{"inheritance":"INHERITANCE_UNSPECIFIED","householdIncomeDetails":{"targetingOptionId":"targetingOptionId","householdIncome":"HOUSEHOLD_INCOME_UNSPECIFIED"},"assignedTargetingOptionId":"assignedTargetingOptionId","inventorySourceGroupDetails":{"inventorySourceGroupId":"inventorySourceGroupId"},"channelDetails":{"negative":True,"channelId":"channelId"},"omidDetails":{"targetingOptionId":"targetingOptionId","omid":"OMID_UNSPECIFIED"},"contentInstreamPositionDetails":{"adType":"AD_TYPE_UNSPECIFIED","contentInstreamPosition":"CONTENT_INSTREAM_POSITION_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"browserDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"audienceGroupDetails":{"includedGoogleAudienceGroup":{"settings":[{"googleAudienceId":"googleAudienceId"},{"googleAudienceId":"googleAudienceId"}]},"includedCustomListGroup":{"settings":[{"customListId":"customListId"},{"customListId":"customListId"}]},"includedCombinedAudienceGroup":{"settings":[{"combinedAudienceId":"combinedAudienceId"},{"combinedAudienceId":"combinedAudienceId"}]},"excludedGoogleAudienceGroup":{"settings":[{"googleAudienceId":"googleAudienceId"},{"googleAudienceId":"googleAudienceId"}]},"excludedFirstAndThirdPartyAudienceGroup":{"settings":[{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"},{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"}]},"includedFirstAndThirdPartyAudienceGroups":[{"settings":[{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"},{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"}]},{"settings":[{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"},{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"}]}]},"nativeContentPositionDetails":{"targetingOptionId":"targetingOptionId","contentPosition":"NATIVE_CONTENT_POSITION_UNSPECIFIED"},"dayAndTimeDetails":{"endHour":6,"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startHour":1,"timeZoneResolution":"TIME_ZONE_RESOLUTION_UNSPECIFIED"},"exchangeDetails":{"targetingOptionId":"targetingOptionId"},"keywordDetails":{"negative":True,"keyword":"keyword"},"targetingType":"TARGETING_TYPE_UNSPECIFIED","deviceMakeModelDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"digitalContentLabelExclusionDetails":{"excludedTargetingOptionId":"excludedTargetingOptionId","contentRatingTier":"CONTENT_RATING_TIER_UNSPECIFIED"},"poiDetails":{"proximityRadiusAmount":2.3021358869347655,"proximityRadiusUnit":"DISTANCE_UNIT_UNSPECIFIED","displayName":"displayName","latitude":5.962133916683182,"targetingOptionId":"targetingOptionId","longitude":5.637376656633329},"environmentDetails":{"environment":"ENVIRONMENT_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"subExchangeDetails":{"targetingOptionId":"targetingOptionId"},"appCategoryDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"contentDurationDetails":{"contentDuration":"CONTENT_DURATION_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"deviceTypeDetails":{"deviceType":"DEVICE_TYPE_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"appDetails":{"negative":True,"appPlatform":"APP_PLATFORM_UNSPECIFIED","displayName":"displayName","appId":"appId"},"name":"name","viewabilityDetails":{"viewability":"VIEWABILITY_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"contentGenreDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"authorizedSellerStatusDetails":{"targetingOptionId":"targetingOptionId","authorizedSellerStatus":"AUTHORIZED_SELLER_STATUS_UNSPECIFIED"},"contentStreamTypeDetails":{"contentStreamType":"CONTENT_STREAM_TYPE_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"geoRegionDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId","geoRegionType":"GEO_REGION_TYPE_UNKNOWN"},"businessChainDetails":{"proximityRadiusAmount":0.8008281904610115,"proximityRadiusUnit":"DISTANCE_UNIT_UNSPECIFIED","displayName":"displayName","targetingOptionId":"targetingOptionId"},"parentalStatusDetails":{"targetingOptionId":"targetingOptionId","parentalStatus":"PARENTAL_STATUS_UNSPECIFIED"},"negativeKeywordListDetails":{"negativeKeywordListId":"negativeKeywordListId"},"categoryDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"urlDetails":{"negative":True,"url":"url"},"operatingSystemDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"sensitiveCategoryExclusionDetails":{"sensitiveCategory":"SENSITIVE_CATEGORY_UNSPECIFIED","excludedTargetingOptionId":"excludedTargetingOptionId"},"proximityLocationListDetails":{"proximityLocationListId":"proximityLocationListId","proximityRadiusRange":"PROXIMITY_RADIUS_RANGE_UNSPECIFIED"},"onScreenPositionDetails":{"adType":"AD_TYPE_UNSPECIFIED","targetingOptionId":"targetingOptionId","onScreenPosition":"ON_SCREEN_POSITION_UNSPECIFIED"},"contentOutstreamPositionDetails":{"adType":"AD_TYPE_UNSPECIFIED","contentOutstreamPosition":"CONTENT_OUTSTREAM_POSITION_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"audioContentTypeDetails":{"audioContentType":"AUDIO_CONTENT_TYPE_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"genderDetails":{"gender":"GENDER_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"inventorySourceDetails":{"inventorySourceId":"inventorySourceId"},"languageDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"thirdPartyVerifierDetails":{"doubleVerify":{"appStarRating":{"avoidInsufficientStarRating":True,"avoidedStarRating":"APP_STAR_RATE_UNSPECIFIED"},"customSegmentId":"customSegmentId","brandSafetyCategories":{"avoidUnknownBrandSafetyCategory":True,"avoidedMediumSeverityCategories":["MEDIUM_SEVERITY_UNSPECIFIED","MEDIUM_SEVERITY_UNSPECIFIED"],"avoidedHighSeverityCategories":["HIGHER_SEVERITY_UNSPECIFIED","HIGHER_SEVERITY_UNSPECIFIED"]},"fraudInvalidTraffic":{"avoidInsufficientOption":True,"avoidedFraudOption":"FRAUD_UNSPECIFIED"},"avoidedAgeRatings":["AGE_RATING_UNSPECIFIED","AGE_RATING_UNSPECIFIED"],"videoViewability":{"videoViewableRate":"VIDEO_VIEWABLE_RATE_UNSPECIFIED","playerImpressionRate":"PLAYER_SIZE_400X300_UNSPECIFIED","videoIab":"VIDEO_IAB_UNSPECIFIED"},"displayViewability":{"viewableDuring":"AVERAGE_VIEW_DURATION_UNSPECIFIED","iab":"IAB_VIEWED_RATE_UNSPECIFIED"}},"adloox":{"excludedAdlooxCategories":["ADLOOX_UNSPECIFIED","ADLOOX_UNSPECIFIED"]},"integralAdScience":{"excludeUnrateable":True,"excludedViolenceRisk":"VIOLENCE_UNSPECIFIED","excludedIllegalDownloadsRisk":"ILLEGAL_DOWNLOADS_UNSPECIFIED","excludedOffensiveLanguageRisk":"OFFENSIVE_LANGUAGE_UNSPECIFIED","videoViewability":"VIDEO_VIEWABILITY_UNSPECIFIED","excludedGamblingRisk":"GAMBLING_UNSPECIFIED","displayViewability":"PERFORMANCE_VIEWABILITY_UNSPECIFIED","customSegmentId":["customSegmentId","customSegmentId"],"excludedDrugsRisk":"DRUGS_UNSPECIFIED","excludedAlcoholRisk":"ALCOHOL_UNSPECIFIED","excludedHateSpeechRisk":"HATE_SPEECH_UNSPECIFIED","excludedAdFraudRisk":"SUSPICIOUS_ACTIVITY_UNSPECIFIED","traqScoreOption":"TRAQ_UNSPECIFIED","excludedAdultRisk":"ADULT_UNSPECIFIED"}},"videoPlayerSizeDetails":{"targetingOptionId":"targetingOptionId","videoPlayerSize":"VIDEO_PLAYER_SIZE_UNSPECIFIED"},"carrierAndIspDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"userRewardedContentDetails":{"targetingOptionId":"targetingOptionId","userRewardedContent":"USER_REWARDED_CONTENT_UNSPECIFIED"},"ageRangeDetails":{"ageRange":"AGE_RANGE_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"regionalLocationListDetails":{"negative":True,"regionalLocationListId":"regionalLocationListId"}}],"targetingType":"TARGETING_TYPE_UNSPECIFIED"},{"assignedTargetingOptions":[{"inheritance":"INHERITANCE_UNSPECIFIED","householdIncomeDetails":{"targetingOptionId":"targetingOptionId","householdIncome":"HOUSEHOLD_INCOME_UNSPECIFIED"},"assignedTargetingOptionId":"assignedTargetingOptionId","inventorySourceGroupDetails":{"inventorySourceGroupId":"inventorySourceGroupId"},"channelDetails":{"negative":True,"channelId":"channelId"},"omidDetails":{"targetingOptionId":"targetingOptionId","omid":"OMID_UNSPECIFIED"},"contentInstreamPositionDetails":{"adType":"AD_TYPE_UNSPECIFIED","contentInstreamPosition":"CONTENT_INSTREAM_POSITION_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"browserDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"audienceGroupDetails":{"includedGoogleAudienceGroup":{"settings":[{"googleAudienceId":"googleAudienceId"},{"googleAudienceId":"googleAudienceId"}]},"includedCustomListGroup":{"settings":[{"customListId":"customListId"},{"customListId":"customListId"}]},"includedCombinedAudienceGroup":{"settings":[{"combinedAudienceId":"combinedAudienceId"},{"combinedAudienceId":"combinedAudienceId"}]},"excludedGoogleAudienceGroup":{"settings":[{"googleAudienceId":"googleAudienceId"},{"googleAudienceId":"googleAudienceId"}]},"excludedFirstAndThirdPartyAudienceGroup":{"settings":[{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"},{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"}]},"includedFirstAndThirdPartyAudienceGroups":[{"settings":[{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"},{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"}]},{"settings":[{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"},{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"}]}]},"nativeContentPositionDetails":{"targetingOptionId":"targetingOptionId","contentPosition":"NATIVE_CONTENT_POSITION_UNSPECIFIED"},"dayAndTimeDetails":{"endHour":6,"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startHour":1,"timeZoneResolution":"TIME_ZONE_RESOLUTION_UNSPECIFIED"},"exchangeDetails":{"targetingOptionId":"targetingOptionId"},"keywordDetails":{"negative":True,"keyword":"keyword"},"targetingType":"TARGETING_TYPE_UNSPECIFIED","deviceMakeModelDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"digitalContentLabelExclusionDetails":{"excludedTargetingOptionId":"excludedTargetingOptionId","contentRatingTier":"CONTENT_RATING_TIER_UNSPECIFIED"},"poiDetails":{"proximityRadiusAmount":2.3021358869347655,"proximityRadiusUnit":"DISTANCE_UNIT_UNSPECIFIED","displayName":"displayName","latitude":5.962133916683182,"targetingOptionId":"targetingOptionId","longitude":5.637376656633329},"environmentDetails":{"environment":"ENVIRONMENT_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"subExchangeDetails":{"targetingOptionId":"targetingOptionId"},"appCategoryDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"contentDurationDetails":{"contentDuration":"CONTENT_DURATION_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"deviceTypeDetails":{"deviceType":"DEVICE_TYPE_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"appDetails":{"negative":True,"appPlatform":"APP_PLATFORM_UNSPECIFIED","displayName":"displayName","appId":"appId"},"name":"name","viewabilityDetails":{"viewability":"VIEWABILITY_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"contentGenreDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"authorizedSellerStatusDetails":{"targetingOptionId":"targetingOptionId","authorizedSellerStatus":"AUTHORIZED_SELLER_STATUS_UNSPECIFIED"},"contentStreamTypeDetails":{"contentStreamType":"CONTENT_STREAM_TYPE_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"geoRegionDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId","geoRegionType":"GEO_REGION_TYPE_UNKNOWN"},"businessChainDetails":{"proximityRadiusAmount":0.8008281904610115,"proximityRadiusUnit":"DISTANCE_UNIT_UNSPECIFIED","displayName":"displayName","targetingOptionId":"targetingOptionId"},"parentalStatusDetails":{"targetingOptionId":"targetingOptionId","parentalStatus":"PARENTAL_STATUS_UNSPECIFIED"},"negativeKeywordListDetails":{"negativeKeywordListId":"negativeKeywordListId"},"categoryDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"urlDetails":{"negative":True,"url":"url"},"operatingSystemDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"sensitiveCategoryExclusionDetails":{"sensitiveCategory":"SENSITIVE_CATEGORY_UNSPECIFIED","excludedTargetingOptionId":"excludedTargetingOptionId"},"proximityLocationListDetails":{"proximityLocationListId":"proximityLocationListId","proximityRadiusRange":"PROXIMITY_RADIUS_RANGE_UNSPECIFIED"},"onScreenPositionDetails":{"adType":"AD_TYPE_UNSPECIFIED","targetingOptionId":"targetingOptionId","onScreenPosition":"ON_SCREEN_POSITION_UNSPECIFIED"},"contentOutstreamPositionDetails":{"adType":"AD_TYPE_UNSPECIFIED","contentOutstreamPosition":"CONTENT_OUTSTREAM_POSITION_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"audioContentTypeDetails":{"audioContentType":"AUDIO_CONTENT_TYPE_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"genderDetails":{"gender":"GENDER_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"inventorySourceDetails":{"inventorySourceId":"inventorySourceId"},"languageDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"thirdPartyVerifierDetails":{"doubleVerify":{"appStarRating":{"avoidInsufficientStarRating":True,"avoidedStarRating":"APP_STAR_RATE_UNSPECIFIED"},"customSegmentId":"customSegmentId","brandSafetyCategories":{"avoidUnknownBrandSafetyCategory":True,"avoidedMediumSeverityCategories":["MEDIUM_SEVERITY_UNSPECIFIED","MEDIUM_SEVERITY_UNSPECIFIED"],"avoidedHighSeverityCategories":["HIGHER_SEVERITY_UNSPECIFIED","HIGHER_SEVERITY_UNSPECIFIED"]},"fraudInvalidTraffic":{"avoidInsufficientOption":True,"avoidedFraudOption":"FRAUD_UNSPECIFIED"},"avoidedAgeRatings":["AGE_RATING_UNSPECIFIED","AGE_RATING_UNSPECIFIED"],"videoViewability":{"videoViewableRate":"VIDEO_VIEWABLE_RATE_UNSPECIFIED","playerImpressionRate":"PLAYER_SIZE_400X300_UNSPECIFIED","videoIab":"VIDEO_IAB_UNSPECIFIED"},"displayViewability":{"viewableDuring":"AVERAGE_VIEW_DURATION_UNSPECIFIED","iab":"IAB_VIEWED_RATE_UNSPECIFIED"}},"adloox":{"excludedAdlooxCategories":["ADLOOX_UNSPECIFIED","ADLOOX_UNSPECIFIED"]},"integralAdScience":{"excludeUnrateable":True,"excludedViolenceRisk":"VIOLENCE_UNSPECIFIED","excludedIllegalDownloadsRisk":"ILLEGAL_DOWNLOADS_UNSPECIFIED","excludedOffensiveLanguageRisk":"OFFENSIVE_LANGUAGE_UNSPECIFIED","videoViewability":"VIDEO_VIEWABILITY_UNSPECIFIED","excludedGamblingRisk":"GAMBLING_UNSPECIFIED","displayViewability":"PERFORMANCE_VIEWABILITY_UNSPECIFIED","customSegmentId":["customSegmentId","customSegmentId"],"excludedDrugsRisk":"DRUGS_UNSPECIFIED","excludedAlcoholRisk":"ALCOHOL_UNSPECIFIED","excludedHateSpeechRisk":"HATE_SPEECH_UNSPECIFIED","excludedAdFraudRisk":"SUSPICIOUS_ACTIVITY_UNSPECIFIED","traqScoreOption":"TRAQ_UNSPECIFIED","excludedAdultRisk":"ADULT_UNSPECIFIED"}},"videoPlayerSizeDetails":{"targetingOptionId":"targetingOptionId","videoPlayerSize":"VIDEO_PLAYER_SIZE_UNSPECIFIED"},"carrierAndIspDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"userRewardedContentDetails":{"targetingOptionId":"targetingOptionId","userRewardedContent":"USER_REWARDED_CONTENT_UNSPECIFIED"},"ageRangeDetails":{"ageRange":"AGE_RANGE_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"regionalLocationListDetails":{"negative":True,"regionalLocationListId":"regionalLocationListId"}},{"inheritance":"INHERITANCE_UNSPECIFIED","householdIncomeDetails":{"targetingOptionId":"targetingOptionId","householdIncome":"HOUSEHOLD_INCOME_UNSPECIFIED"},"assignedTargetingOptionId":"assignedTargetingOptionId","inventorySourceGroupDetails":{"inventorySourceGroupId":"inventorySourceGroupId"},"channelDetails":{"negative":True,"channelId":"channelId"},"omidDetails":{"targetingOptionId":"targetingOptionId","omid":"OMID_UNSPECIFIED"},"contentInstreamPositionDetails":{"adType":"AD_TYPE_UNSPECIFIED","contentInstreamPosition":"CONTENT_INSTREAM_POSITION_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"browserDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"audienceGroupDetails":{"includedGoogleAudienceGroup":{"settings":[{"googleAudienceId":"googleAudienceId"},{"googleAudienceId":"googleAudienceId"}]},"includedCustomListGroup":{"settings":[{"customListId":"customListId"},{"customListId":"customListId"}]},"includedCombinedAudienceGroup":{"settings":[{"combinedAudienceId":"combinedAudienceId"},{"combinedAudienceId":"combinedAudienceId"}]},"excludedGoogleAudienceGroup":{"settings":[{"googleAudienceId":"googleAudienceId"},{"googleAudienceId":"googleAudienceId"}]},"excludedFirstAndThirdPartyAudienceGroup":{"settings":[{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"},{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"}]},"includedFirstAndThirdPartyAudienceGroups":[{"settings":[{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"},{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"}]},{"settings":[{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"},{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"}]}]},"nativeContentPositionDetails":{"targetingOptionId":"targetingOptionId","contentPosition":"NATIVE_CONTENT_POSITION_UNSPECIFIED"},"dayAndTimeDetails":{"endHour":6,"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startHour":1,"timeZoneResolution":"TIME_ZONE_RESOLUTION_UNSPECIFIED"},"exchangeDetails":{"targetingOptionId":"targetingOptionId"},"keywordDetails":{"negative":True,"keyword":"keyword"},"targetingType":"TARGETING_TYPE_UNSPECIFIED","deviceMakeModelDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"digitalContentLabelExclusionDetails":{"excludedTargetingOptionId":"excludedTargetingOptionId","contentRatingTier":"CONTENT_RATING_TIER_UNSPECIFIED"},"poiDetails":{"proximityRadiusAmount":2.3021358869347655,"proximityRadiusUnit":"DISTANCE_UNIT_UNSPECIFIED","displayName":"displayName","latitude":5.962133916683182,"targetingOptionId":"targetingOptionId","longitude":5.637376656633329},"environmentDetails":{"environment":"ENVIRONMENT_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"subExchangeDetails":{"targetingOptionId":"targetingOptionId"},"appCategoryDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"contentDurationDetails":{"contentDuration":"CONTENT_DURATION_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"deviceTypeDetails":{"deviceType":"DEVICE_TYPE_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"appDetails":{"negative":True,"appPlatform":"APP_PLATFORM_UNSPECIFIED","displayName":"displayName","appId":"appId"},"name":"name","viewabilityDetails":{"viewability":"VIEWABILITY_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"contentGenreDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"authorizedSellerStatusDetails":{"targetingOptionId":"targetingOptionId","authorizedSellerStatus":"AUTHORIZED_SELLER_STATUS_UNSPECIFIED"},"contentStreamTypeDetails":{"contentStreamType":"CONTENT_STREAM_TYPE_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"geoRegionDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId","geoRegionType":"GEO_REGION_TYPE_UNKNOWN"},"businessChainDetails":{"proximityRadiusAmount":0.8008281904610115,"proximityRadiusUnit":"DISTANCE_UNIT_UNSPECIFIED","displayName":"displayName","targetingOptionId":"targetingOptionId"},"parentalStatusDetails":{"targetingOptionId":"targetingOptionId","parentalStatus":"PARENTAL_STATUS_UNSPECIFIED"},"negativeKeywordListDetails":{"negativeKeywordListId":"negativeKeywordListId"},"categoryDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"urlDetails":{"negative":True,"url":"url"},"operatingSystemDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"sensitiveCategoryExclusionDetails":{"sensitiveCategory":"SENSITIVE_CATEGORY_UNSPECIFIED","excludedTargetingOptionId":"excludedTargetingOptionId"},"proximityLocationListDetails":{"proximityLocationListId":"proximityLocationListId","proximityRadiusRange":"PROXIMITY_RADIUS_RANGE_UNSPECIFIED"},"onScreenPositionDetails":{"adType":"AD_TYPE_UNSPECIFIED","targetingOptionId":"targetingOptionId","onScreenPosition":"ON_SCREEN_POSITION_UNSPECIFIED"},"contentOutstreamPositionDetails":{"adType":"AD_TYPE_UNSPECIFIED","contentOutstreamPosition":"CONTENT_OUTSTREAM_POSITION_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"audioContentTypeDetails":{"audioContentType":"AUDIO_CONTENT_TYPE_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"genderDetails":{"gender":"GENDER_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"inventorySourceDetails":{"inventorySourceId":"inventorySourceId"},"languageDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"thirdPartyVerifierDetails":{"doubleVerify":{"appStarRating":{"avoidInsufficientStarRating":True,"avoidedStarRating":"APP_STAR_RATE_UNSPECIFIED"},"customSegmentId":"customSegmentId","brandSafetyCategories":{"avoidUnknownBrandSafetyCategory":True,"avoidedMediumSeverityCategories":["MEDIUM_SEVERITY_UNSPECIFIED","MEDIUM_SEVERITY_UNSPECIFIED"],"avoidedHighSeverityCategories":["HIGHER_SEVERITY_UNSPECIFIED","HIGHER_SEVERITY_UNSPECIFIED"]},"fraudInvalidTraffic":{"avoidInsufficientOption":True,"avoidedFraudOption":"FRAUD_UNSPECIFIED"},"avoidedAgeRatings":["AGE_RATING_UNSPECIFIED","AGE_RATING_UNSPECIFIED"],"videoViewability":{"videoViewableRate":"VIDEO_VIEWABLE_RATE_UNSPECIFIED","playerImpressionRate":"PLAYER_SIZE_400X300_UNSPECIFIED","videoIab":"VIDEO_IAB_UNSPECIFIED"},"displayViewability":{"viewableDuring":"AVERAGE_VIEW_DURATION_UNSPECIFIED","iab":"IAB_VIEWED_RATE_UNSPECIFIED"}},"adloox":{"excludedAdlooxCategories":["ADLOOX_UNSPECIFIED","ADLOOX_UNSPECIFIED"]},"integralAdScience":{"excludeUnrateable":True,"excludedViolenceRisk":"VIOLENCE_UNSPECIFIED","excludedIllegalDownloadsRisk":"ILLEGAL_DOWNLOADS_UNSPECIFIED","excludedOffensiveLanguageRisk":"OFFENSIVE_LANGUAGE_UNSPECIFIED","videoViewability":"VIDEO_VIEWABILITY_UNSPECIFIED","excludedGamblingRisk":"GAMBLING_UNSPECIFIED","displayViewability":"PERFORMANCE_VIEWABILITY_UNSPECIFIED","customSegmentId":["customSegmentId","customSegmentId"],"excludedDrugsRisk":"DRUGS_UNSPECIFIED","excludedAlcoholRisk":"ALCOHOL_UNSPECIFIED","excludedHateSpeechRisk":"HATE_SPEECH_UNSPECIFIED","excludedAdFraudRisk":"SUSPICIOUS_ACTIVITY_UNSPECIFIED","traqScoreOption":"TRAQ_UNSPECIFIED","excludedAdultRisk":"ADULT_UNSPECIFIED"}},"videoPlayerSizeDetails":{"targetingOptionId":"targetingOptionId","videoPlayerSize":"VIDEO_PLAYER_SIZE_UNSPECIFIED"},"carrierAndIspDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"userRewardedContentDetails":{"targetingOptionId":"targetingOptionId","userRewardedContent":"USER_REWARDED_CONTENT_UNSPECIFIED"},"ageRangeDetails":{"ageRange":"AGE_RANGE_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"regionalLocationListDetails":{"negative":True,"regionalLocationListId":"regionalLocationListId"}}],"targetingType":"TARGETING_TYPE_UNSPECIFIED"}],"deleteRequests":[{"targetingType":"TARGETING_TYPE_UNSPECIFIED","assignedTargetingOptionIds":["assignedTargetingOptionIds","assignedTargetingOptionIds"]},{"targetingType":"TARGETING_TYPE_UNSPECIFIED","assignedTargetingOptionIds":["assignedTargetingOptionIds","assignedTargetingOptionIds"]}]}
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
        path='/v1/advertisers/{advertiser_id}/lineItems/{line_item_idbulk_edit_line_item_assigned_targeting_option}'.format(advertiser_id='advertiser_id_example', line_item_id='line_item_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_line_items_bulk_list_line_item_assigned_targeting_options(client):
    """Test case for displayvideo_advertisers_line_items_bulk_list_line_item_assigned_targeting_options

    
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
        path='/v1/advertisers/{advertiser_id}/lineItems/{line_item_idbulk_list_line_item_assigned_targeting_option}'.format(advertiser_id='advertiser_id_example', line_item_id='line_item_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_line_items_create(client):
    """Test case for displayvideo_advertisers_line_items_create

    
    """
    body = {"bidStrategy":{"fixedBid":{"bidAmountMicros":"bidAmountMicros"},"performanceGoalAutoBid":{"performanceGoalType":"BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_UNSPECIFIED","customBiddingAlgorithmId":"customBiddingAlgorithmId","performanceGoalAmountMicros":"performanceGoalAmountMicros","maxAverageCpmBidAmountMicros":"maxAverageCpmBidAmountMicros"},"maximizeSpendAutoBid":{"raiseBidForDeals":True,"performanceGoalType":"BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_UNSPECIFIED","customBiddingAlgorithmId":"customBiddingAlgorithmId","maxAverageCpmBidAmountMicros":"maxAverageCpmBidAmountMicros"}},"flight":{"dateRange":{"endDate":{"month":6,"year":1,"day":0},"startDate":{"month":6,"year":1,"day":0}},"triggerId":"triggerId","flightDateType":"LINE_ITEM_FLIGHT_DATE_TYPE_UNSPECIFIED"},"partnerCosts":[{"feeAmount":"feeAmount","costType":"PARTNER_COST_TYPE_UNSPECIFIED","invoiceType":"PARTNER_COST_INVOICE_TYPE_UNSPECIFIED","feeType":"PARTNER_COST_FEE_TYPE_UNSPECIFIED","feePercentageMillis":"feePercentageMillis"},{"feeAmount":"feeAmount","costType":"PARTNER_COST_TYPE_UNSPECIFIED","invoiceType":"PARTNER_COST_INVOICE_TYPE_UNSPECIFIED","feeType":"PARTNER_COST_FEE_TYPE_UNSPECIFIED","feePercentageMillis":"feePercentageMillis"}],"displayName":"displayName","targetingExpansion":{"targetingExpansionLevel":"TARGETING_EXPANSION_LEVEL_UNSPECIFIED","excludeFirstPartyAudience":True},"excludeNewExchanges":True,"lineItemType":"LINE_ITEM_TYPE_UNSPECIFIED","budget":{"budgetAllocationType":"LINE_ITEM_BUDGET_ALLOCATION_TYPE_UNSPECIFIED","budgetUnit":"BUDGET_UNIT_UNSPECIFIED","maxAmount":"maxAmount"},"warningMessages":["LINE_ITEM_WARNING_MESSAGE_UNSPECIFIED","LINE_ITEM_WARNING_MESSAGE_UNSPECIFIED"],"lineItemId":"lineItemId","partnerRevenueModel":{"markupAmount":"markupAmount","markupType":"PARTNER_REVENUE_MODEL_MARKUP_TYPE_UNSPECIFIED"},"campaignId":"campaignId","insertionOrderId":"insertionOrderId","mobileApp":{"displayName":"displayName","appId":"appId","publisher":"publisher","platform":"PLATFORM_UNSPECIFIED"},"conversionCounting":{"floodlightActivityConfigs":[{"postViewLookbackWindowDays":6,"floodlightActivityId":"floodlightActivityId","postClickLookbackWindowDays":0},{"postViewLookbackWindowDays":6,"floodlightActivityId":"floodlightActivityId","postClickLookbackWindowDays":0}],"postViewCountPercentageMillis":"postViewCountPercentageMillis"},"updateTime":"updateTime","creativeIds":["creativeIds","creativeIds"],"integrationDetails":{"integrationCode":"integrationCode","details":"details"},"advertiserId":"advertiserId","pacing":{"pacingType":"PACING_TYPE_UNSPECIFIED","pacingPeriod":"PACING_PERIOD_UNSPECIFIED","dailyMaxImpressions":"dailyMaxImpressions","dailyMaxMicros":"dailyMaxMicros"},"entityStatus":"ENTITY_STATUS_UNSPECIFIED","inventorySourceIds":["inventorySourceIds","inventorySourceIds"],"name":"name","reservationType":"RESERVATION_TYPE_UNSPECIFIED","frequencyCap":{"maxImpressions":5,"unlimited":True,"timeUnitCount":5,"timeUnit":"TIME_UNIT_UNSPECIFIED"}}
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
        path='/v1/advertisers/{advertiser_id}/lineItems'.format(advertiser_id='advertiser_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_line_items_delete(client):
    """Test case for displayvideo_advertisers_line_items_delete

    
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
        path='/v1/advertisers/{advertiser_id}/lineItems/{line_item_id}'.format(advertiser_id='advertiser_id_example', line_item_id='line_item_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_line_items_generate_default(client):
    """Test case for displayvideo_advertisers_line_items_generate_default

    
    """
    body = {"displayName":"displayName","lineItemType":"LINE_ITEM_TYPE_UNSPECIFIED","insertionOrderId":"insertionOrderId","mobileApp":{"displayName":"displayName","appId":"appId","publisher":"publisher","platform":"PLATFORM_UNSPECIFIED"}}
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
        path='/v1/advertisers/{advertiser_id}/lineItems:generateDefault'.format(advertiser_id='advertiser_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_line_items_get(client):
    """Test case for displayvideo_advertisers_line_items_get

    
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
        path='/v1/advertisers/{advertiser_id}/lineItems/{line_item_id}'.format(advertiser_id='advertiser_id_example', line_item_id='line_item_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_line_items_list(client):
    """Test case for displayvideo_advertisers_line_items_list

    
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
        path='/v1/advertisers/{advertiser_id}/lineItems'.format(advertiser_id='advertiser_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_line_items_patch(client):
    """Test case for displayvideo_advertisers_line_items_patch

    
    """
    body = {"bidStrategy":{"fixedBid":{"bidAmountMicros":"bidAmountMicros"},"performanceGoalAutoBid":{"performanceGoalType":"BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_UNSPECIFIED","customBiddingAlgorithmId":"customBiddingAlgorithmId","performanceGoalAmountMicros":"performanceGoalAmountMicros","maxAverageCpmBidAmountMicros":"maxAverageCpmBidAmountMicros"},"maximizeSpendAutoBid":{"raiseBidForDeals":True,"performanceGoalType":"BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_UNSPECIFIED","customBiddingAlgorithmId":"customBiddingAlgorithmId","maxAverageCpmBidAmountMicros":"maxAverageCpmBidAmountMicros"}},"flight":{"dateRange":{"endDate":{"month":6,"year":1,"day":0},"startDate":{"month":6,"year":1,"day":0}},"triggerId":"triggerId","flightDateType":"LINE_ITEM_FLIGHT_DATE_TYPE_UNSPECIFIED"},"partnerCosts":[{"feeAmount":"feeAmount","costType":"PARTNER_COST_TYPE_UNSPECIFIED","invoiceType":"PARTNER_COST_INVOICE_TYPE_UNSPECIFIED","feeType":"PARTNER_COST_FEE_TYPE_UNSPECIFIED","feePercentageMillis":"feePercentageMillis"},{"feeAmount":"feeAmount","costType":"PARTNER_COST_TYPE_UNSPECIFIED","invoiceType":"PARTNER_COST_INVOICE_TYPE_UNSPECIFIED","feeType":"PARTNER_COST_FEE_TYPE_UNSPECIFIED","feePercentageMillis":"feePercentageMillis"}],"displayName":"displayName","targetingExpansion":{"targetingExpansionLevel":"TARGETING_EXPANSION_LEVEL_UNSPECIFIED","excludeFirstPartyAudience":True},"excludeNewExchanges":True,"lineItemType":"LINE_ITEM_TYPE_UNSPECIFIED","budget":{"budgetAllocationType":"LINE_ITEM_BUDGET_ALLOCATION_TYPE_UNSPECIFIED","budgetUnit":"BUDGET_UNIT_UNSPECIFIED","maxAmount":"maxAmount"},"warningMessages":["LINE_ITEM_WARNING_MESSAGE_UNSPECIFIED","LINE_ITEM_WARNING_MESSAGE_UNSPECIFIED"],"lineItemId":"lineItemId","partnerRevenueModel":{"markupAmount":"markupAmount","markupType":"PARTNER_REVENUE_MODEL_MARKUP_TYPE_UNSPECIFIED"},"campaignId":"campaignId","insertionOrderId":"insertionOrderId","mobileApp":{"displayName":"displayName","appId":"appId","publisher":"publisher","platform":"PLATFORM_UNSPECIFIED"},"conversionCounting":{"floodlightActivityConfigs":[{"postViewLookbackWindowDays":6,"floodlightActivityId":"floodlightActivityId","postClickLookbackWindowDays":0},{"postViewLookbackWindowDays":6,"floodlightActivityId":"floodlightActivityId","postClickLookbackWindowDays":0}],"postViewCountPercentageMillis":"postViewCountPercentageMillis"},"updateTime":"updateTime","creativeIds":["creativeIds","creativeIds"],"integrationDetails":{"integrationCode":"integrationCode","details":"details"},"advertiserId":"advertiserId","pacing":{"pacingType":"PACING_TYPE_UNSPECIFIED","pacingPeriod":"PACING_PERIOD_UNSPECIFIED","dailyMaxImpressions":"dailyMaxImpressions","dailyMaxMicros":"dailyMaxMicros"},"entityStatus":"ENTITY_STATUS_UNSPECIFIED","inventorySourceIds":["inventorySourceIds","inventorySourceIds"],"name":"name","reservationType":"RESERVATION_TYPE_UNSPECIFIED","frequencyCap":{"maxImpressions":5,"unlimited":True,"timeUnitCount":5,"timeUnit":"TIME_UNIT_UNSPECIFIED"}}
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
                    ('updateMask', 'update_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/advertisers/{advertiser_id}/lineItems/{line_item_id}'.format(advertiser_id='advertiser_id_example', line_item_id='line_item_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_line_items_targeting_types_assigned_targeting_options_create(client):
    """Test case for displayvideo_advertisers_line_items_targeting_types_assigned_targeting_options_create

    
    """
    body = {"inheritance":"INHERITANCE_UNSPECIFIED","householdIncomeDetails":{"targetingOptionId":"targetingOptionId","householdIncome":"HOUSEHOLD_INCOME_UNSPECIFIED"},"assignedTargetingOptionId":"assignedTargetingOptionId","inventorySourceGroupDetails":{"inventorySourceGroupId":"inventorySourceGroupId"},"channelDetails":{"negative":True,"channelId":"channelId"},"omidDetails":{"targetingOptionId":"targetingOptionId","omid":"OMID_UNSPECIFIED"},"contentInstreamPositionDetails":{"adType":"AD_TYPE_UNSPECIFIED","contentInstreamPosition":"CONTENT_INSTREAM_POSITION_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"browserDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"audienceGroupDetails":{"includedGoogleAudienceGroup":{"settings":[{"googleAudienceId":"googleAudienceId"},{"googleAudienceId":"googleAudienceId"}]},"includedCustomListGroup":{"settings":[{"customListId":"customListId"},{"customListId":"customListId"}]},"includedCombinedAudienceGroup":{"settings":[{"combinedAudienceId":"combinedAudienceId"},{"combinedAudienceId":"combinedAudienceId"}]},"excludedGoogleAudienceGroup":{"settings":[{"googleAudienceId":"googleAudienceId"},{"googleAudienceId":"googleAudienceId"}]},"excludedFirstAndThirdPartyAudienceGroup":{"settings":[{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"},{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"}]},"includedFirstAndThirdPartyAudienceGroups":[{"settings":[{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"},{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"}]},{"settings":[{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"},{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"}]}]},"nativeContentPositionDetails":{"targetingOptionId":"targetingOptionId","contentPosition":"NATIVE_CONTENT_POSITION_UNSPECIFIED"},"dayAndTimeDetails":{"endHour":6,"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startHour":1,"timeZoneResolution":"TIME_ZONE_RESOLUTION_UNSPECIFIED"},"exchangeDetails":{"targetingOptionId":"targetingOptionId"},"keywordDetails":{"negative":True,"keyword":"keyword"},"targetingType":"TARGETING_TYPE_UNSPECIFIED","deviceMakeModelDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"digitalContentLabelExclusionDetails":{"excludedTargetingOptionId":"excludedTargetingOptionId","contentRatingTier":"CONTENT_RATING_TIER_UNSPECIFIED"},"poiDetails":{"proximityRadiusAmount":2.3021358869347655,"proximityRadiusUnit":"DISTANCE_UNIT_UNSPECIFIED","displayName":"displayName","latitude":5.962133916683182,"targetingOptionId":"targetingOptionId","longitude":5.637376656633329},"environmentDetails":{"environment":"ENVIRONMENT_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"subExchangeDetails":{"targetingOptionId":"targetingOptionId"},"appCategoryDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"contentDurationDetails":{"contentDuration":"CONTENT_DURATION_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"deviceTypeDetails":{"deviceType":"DEVICE_TYPE_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"appDetails":{"negative":True,"appPlatform":"APP_PLATFORM_UNSPECIFIED","displayName":"displayName","appId":"appId"},"name":"name","viewabilityDetails":{"viewability":"VIEWABILITY_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"contentGenreDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"authorizedSellerStatusDetails":{"targetingOptionId":"targetingOptionId","authorizedSellerStatus":"AUTHORIZED_SELLER_STATUS_UNSPECIFIED"},"contentStreamTypeDetails":{"contentStreamType":"CONTENT_STREAM_TYPE_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"geoRegionDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId","geoRegionType":"GEO_REGION_TYPE_UNKNOWN"},"businessChainDetails":{"proximityRadiusAmount":0.8008281904610115,"proximityRadiusUnit":"DISTANCE_UNIT_UNSPECIFIED","displayName":"displayName","targetingOptionId":"targetingOptionId"},"parentalStatusDetails":{"targetingOptionId":"targetingOptionId","parentalStatus":"PARENTAL_STATUS_UNSPECIFIED"},"negativeKeywordListDetails":{"negativeKeywordListId":"negativeKeywordListId"},"categoryDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"urlDetails":{"negative":True,"url":"url"},"operatingSystemDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"sensitiveCategoryExclusionDetails":{"sensitiveCategory":"SENSITIVE_CATEGORY_UNSPECIFIED","excludedTargetingOptionId":"excludedTargetingOptionId"},"proximityLocationListDetails":{"proximityLocationListId":"proximityLocationListId","proximityRadiusRange":"PROXIMITY_RADIUS_RANGE_UNSPECIFIED"},"onScreenPositionDetails":{"adType":"AD_TYPE_UNSPECIFIED","targetingOptionId":"targetingOptionId","onScreenPosition":"ON_SCREEN_POSITION_UNSPECIFIED"},"contentOutstreamPositionDetails":{"adType":"AD_TYPE_UNSPECIFIED","contentOutstreamPosition":"CONTENT_OUTSTREAM_POSITION_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"audioContentTypeDetails":{"audioContentType":"AUDIO_CONTENT_TYPE_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"genderDetails":{"gender":"GENDER_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"inventorySourceDetails":{"inventorySourceId":"inventorySourceId"},"languageDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"thirdPartyVerifierDetails":{"doubleVerify":{"appStarRating":{"avoidInsufficientStarRating":True,"avoidedStarRating":"APP_STAR_RATE_UNSPECIFIED"},"customSegmentId":"customSegmentId","brandSafetyCategories":{"avoidUnknownBrandSafetyCategory":True,"avoidedMediumSeverityCategories":["MEDIUM_SEVERITY_UNSPECIFIED","MEDIUM_SEVERITY_UNSPECIFIED"],"avoidedHighSeverityCategories":["HIGHER_SEVERITY_UNSPECIFIED","HIGHER_SEVERITY_UNSPECIFIED"]},"fraudInvalidTraffic":{"avoidInsufficientOption":True,"avoidedFraudOption":"FRAUD_UNSPECIFIED"},"avoidedAgeRatings":["AGE_RATING_UNSPECIFIED","AGE_RATING_UNSPECIFIED"],"videoViewability":{"videoViewableRate":"VIDEO_VIEWABLE_RATE_UNSPECIFIED","playerImpressionRate":"PLAYER_SIZE_400X300_UNSPECIFIED","videoIab":"VIDEO_IAB_UNSPECIFIED"},"displayViewability":{"viewableDuring":"AVERAGE_VIEW_DURATION_UNSPECIFIED","iab":"IAB_VIEWED_RATE_UNSPECIFIED"}},"adloox":{"excludedAdlooxCategories":["ADLOOX_UNSPECIFIED","ADLOOX_UNSPECIFIED"]},"integralAdScience":{"excludeUnrateable":True,"excludedViolenceRisk":"VIOLENCE_UNSPECIFIED","excludedIllegalDownloadsRisk":"ILLEGAL_DOWNLOADS_UNSPECIFIED","excludedOffensiveLanguageRisk":"OFFENSIVE_LANGUAGE_UNSPECIFIED","videoViewability":"VIDEO_VIEWABILITY_UNSPECIFIED","excludedGamblingRisk":"GAMBLING_UNSPECIFIED","displayViewability":"PERFORMANCE_VIEWABILITY_UNSPECIFIED","customSegmentId":["customSegmentId","customSegmentId"],"excludedDrugsRisk":"DRUGS_UNSPECIFIED","excludedAlcoholRisk":"ALCOHOL_UNSPECIFIED","excludedHateSpeechRisk":"HATE_SPEECH_UNSPECIFIED","excludedAdFraudRisk":"SUSPICIOUS_ACTIVITY_UNSPECIFIED","traqScoreOption":"TRAQ_UNSPECIFIED","excludedAdultRisk":"ADULT_UNSPECIFIED"}},"videoPlayerSizeDetails":{"targetingOptionId":"targetingOptionId","videoPlayerSize":"VIDEO_PLAYER_SIZE_UNSPECIFIED"},"carrierAndIspDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"userRewardedContentDetails":{"targetingOptionId":"targetingOptionId","userRewardedContent":"USER_REWARDED_CONTENT_UNSPECIFIED"},"ageRangeDetails":{"ageRange":"AGE_RANGE_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"regionalLocationListDetails":{"negative":True,"regionalLocationListId":"regionalLocationListId"}}
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
        path='/v1/advertisers/{advertiser_id}/lineItems/{line_item_id}/targetingTypes/{targeting_type}/assignedTargetingOptions'.format(advertiser_id='advertiser_id_example', line_item_id='line_item_id_example', targeting_type='targeting_type_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_line_items_targeting_types_assigned_targeting_options_delete(client):
    """Test case for displayvideo_advertisers_line_items_targeting_types_assigned_targeting_options_delete

    
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
        path='/v1/advertisers/{advertiser_id}/lineItems/{line_item_id}/targetingTypes/{targeting_type}/assignedTargetingOptions/{assigned_targeting_option_id}'.format(advertiser_id='advertiser_id_example', line_item_id='line_item_id_example', targeting_type='targeting_type_example', assigned_targeting_option_id='assigned_targeting_option_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_line_items_targeting_types_assigned_targeting_options_get(client):
    """Test case for displayvideo_advertisers_line_items_targeting_types_assigned_targeting_options_get

    
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
        path='/v1/advertisers/{advertiser_id}/lineItems/{line_item_id}/targetingTypes/{targeting_type}/assignedTargetingOptions/{assigned_targeting_option_id}'.format(advertiser_id='advertiser_id_example', line_item_id='line_item_id_example', targeting_type='targeting_type_example', assigned_targeting_option_id='assigned_targeting_option_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_line_items_targeting_types_assigned_targeting_options_list(client):
    """Test case for displayvideo_advertisers_line_items_targeting_types_assigned_targeting_options_list

    
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
        path='/v1/advertisers/{advertiser_id}/lineItems/{line_item_id}/targetingTypes/{targeting_type}/assignedTargetingOptions'.format(advertiser_id='advertiser_id_example', line_item_id='line_item_id_example', targeting_type='targeting_type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_list(client):
    """Test case for displayvideo_advertisers_list

    
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
                    ('pageToken', 'page_token_example'),
                    ('partnerId', 'partner_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/advertisers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_location_lists_assigned_locations_bulk_edit(client):
    """Test case for displayvideo_advertisers_location_lists_assigned_locations_bulk_edit

    
    """
    body = {"createdAssignedLocations":[{"assignedLocationId":"assignedLocationId","name":"name","targetingOptionId":"targetingOptionId"},{"assignedLocationId":"assignedLocationId","name":"name","targetingOptionId":"targetingOptionId"}],"deletedAssignedLocations":["deletedAssignedLocations","deletedAssignedLocations"]}
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
        path='/v1/advertisers/{advertiser_id}/locationLists/{location_list_id}/assignedLocations:bulkEdit'.format(advertiser_id='advertiser_id_example', location_list_id='location_list_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_location_lists_assigned_locations_create(client):
    """Test case for displayvideo_advertisers_location_lists_assigned_locations_create

    
    """
    body = {"assignedLocationId":"assignedLocationId","name":"name","targetingOptionId":"targetingOptionId"}
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
        path='/v1/advertisers/{advertiser_id}/locationLists/{location_list_id}/assignedLocations'.format(advertiser_id='advertiser_id_example', location_list_id='location_list_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_location_lists_assigned_locations_delete(client):
    """Test case for displayvideo_advertisers_location_lists_assigned_locations_delete

    
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
        path='/v1/advertisers/{advertiser_id}/locationLists/{location_list_id}/assignedLocations/{assigned_location_id}'.format(advertiser_id='advertiser_id_example', location_list_id='location_list_id_example', assigned_location_id='assigned_location_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_location_lists_assigned_locations_list(client):
    """Test case for displayvideo_advertisers_location_lists_assigned_locations_list

    
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
        path='/v1/advertisers/{advertiser_id}/locationLists/{location_list_id}/assignedLocations'.format(advertiser_id='advertiser_id_example', location_list_id='location_list_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_location_lists_create(client):
    """Test case for displayvideo_advertisers_location_lists_create

    
    """
    body = {"displayName":"displayName","name":"name","locationType":"TARGETING_LOCATION_TYPE_UNSPECIFIED","locationListId":"locationListId","advertiserId":"advertiserId"}
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
        path='/v1/advertisers/{advertiser_id}/locationLists'.format(advertiser_id='advertiser_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_location_lists_list(client):
    """Test case for displayvideo_advertisers_location_lists_list

    
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
        path='/v1/advertisers/{advertiser_id}/locationLists'.format(advertiser_id='advertiser_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_location_lists_patch(client):
    """Test case for displayvideo_advertisers_location_lists_patch

    
    """
    body = {"displayName":"displayName","name":"name","locationType":"TARGETING_LOCATION_TYPE_UNSPECIFIED","locationListId":"locationListId","advertiserId":"advertiserId"}
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
                    ('updateMask', 'update_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/advertisers/{advertiser_id}/locationLists/{location_list_id}'.format(advertiser_id='advertiser_id_example', location_list_id='location_list_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_manual_triggers_activate(client):
    """Test case for displayvideo_advertisers_manual_triggers_activate

    
    """
    body = None
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
        path='/v1/advertisers/{advertiser_id}/manualTriggers/{trigger_idactivat}'.format(advertiser_id='advertiser_id_example', trigger_id='trigger_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_manual_triggers_create(client):
    """Test case for displayvideo_advertisers_manual_triggers_create

    
    """
    body = {"displayName":"displayName","latestActivationTime":"latestActivationTime","triggerId":"triggerId","name":"name","state":"STATE_UNSPECIFIED","activationDurationMinutes":"activationDurationMinutes","advertiserId":"advertiserId"}
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
        path='/v1/advertisers/{advertiser_id}/manualTriggers'.format(advertiser_id='advertiser_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_manual_triggers_deactivate(client):
    """Test case for displayvideo_advertisers_manual_triggers_deactivate

    
    """
    body = None
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
        path='/v1/advertisers/{advertiser_id}/manualTriggers/{trigger_iddeactivat}'.format(advertiser_id='advertiser_id_example', trigger_id='trigger_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_manual_triggers_get(client):
    """Test case for displayvideo_advertisers_manual_triggers_get

    
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
        path='/v1/advertisers/{advertiser_id}/manualTriggers/{trigger_id}'.format(advertiser_id='advertiser_id_example', trigger_id='trigger_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_manual_triggers_list(client):
    """Test case for displayvideo_advertisers_manual_triggers_list

    
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
        path='/v1/advertisers/{advertiser_id}/manualTriggers'.format(advertiser_id='advertiser_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_manual_triggers_patch(client):
    """Test case for displayvideo_advertisers_manual_triggers_patch

    
    """
    body = {"displayName":"displayName","latestActivationTime":"latestActivationTime","triggerId":"triggerId","name":"name","state":"STATE_UNSPECIFIED","activationDurationMinutes":"activationDurationMinutes","advertiserId":"advertiserId"}
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
                    ('updateMask', 'update_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/advertisers/{advertiser_id}/manualTriggers/{trigger_id}'.format(advertiser_id='advertiser_id_example', trigger_id='trigger_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_negative_keyword_lists_create(client):
    """Test case for displayvideo_advertisers_negative_keyword_lists_create

    
    """
    body = {"targetedLineItemCount":"targetedLineItemCount","displayName":"displayName","negativeKeywordListId":"negativeKeywordListId","name":"name","advertiserId":"advertiserId"}
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
        path='/v1/advertisers/{advertiser_id}/negativeKeywordLists'.format(advertiser_id='advertiser_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_negative_keyword_lists_list(client):
    """Test case for displayvideo_advertisers_negative_keyword_lists_list

    
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
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/advertisers/{advertiser_id}/negativeKeywordLists'.format(advertiser_id='advertiser_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_negative_keyword_lists_negative_keywords_bulk_edit(client):
    """Test case for displayvideo_advertisers_negative_keyword_lists_negative_keywords_bulk_edit

    
    """
    body = {"createdNegativeKeywords":[{"name":"name","keywordValue":"keywordValue"},{"name":"name","keywordValue":"keywordValue"}],"deletedNegativeKeywords":["deletedNegativeKeywords","deletedNegativeKeywords"]}
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
        path='/v1/advertisers/{advertiser_id}/negativeKeywordLists/{negative_keyword_list_id}/negativeKeywords:bulkEdit'.format(advertiser_id='advertiser_id_example', negative_keyword_list_id='negative_keyword_list_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_negative_keyword_lists_negative_keywords_delete(client):
    """Test case for displayvideo_advertisers_negative_keyword_lists_negative_keywords_delete

    
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
        path='/v1/advertisers/{advertiser_id}/negativeKeywordLists/{negative_keyword_list_id}/negativeKeywords/{keyword_value}'.format(advertiser_id='advertiser_id_example', negative_keyword_list_id='negative_keyword_list_id_example', keyword_value='keyword_value_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_negative_keyword_lists_negative_keywords_list(client):
    """Test case for displayvideo_advertisers_negative_keyword_lists_negative_keywords_list

    
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
        path='/v1/advertisers/{advertiser_id}/negativeKeywordLists/{negative_keyword_list_id}/negativeKeywords'.format(advertiser_id='advertiser_id_example', negative_keyword_list_id='negative_keyword_list_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_negative_keyword_lists_negative_keywords_replace(client):
    """Test case for displayvideo_advertisers_negative_keyword_lists_negative_keywords_replace

    
    """
    body = {"newNegativeKeywords":[{"name":"name","keywordValue":"keywordValue"},{"name":"name","keywordValue":"keywordValue"}]}
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
        path='/v1/advertisers/{advertiser_id}/negativeKeywordLists/{negative_keyword_list_id}/negativeKeywords:replace'.format(advertiser_id='advertiser_id_example', negative_keyword_list_id='negative_keyword_list_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_negative_keyword_lists_patch(client):
    """Test case for displayvideo_advertisers_negative_keyword_lists_patch

    
    """
    body = {"targetedLineItemCount":"targetedLineItemCount","displayName":"displayName","negativeKeywordListId":"negativeKeywordListId","name":"name","advertiserId":"advertiserId"}
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
                    ('updateMask', 'update_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/advertisers/{advertiser_id}/negativeKeywordLists/{negative_keyword_list_id}'.format(advertiser_id='advertiser_id_example', negative_keyword_list_id='negative_keyword_list_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_patch(client):
    """Test case for displayvideo_advertisers_patch

    
    """
    body = {"adServerConfig":{"thirdPartyOnlyConfig":{"pixelOrderIdReportingEnabled":True},"cmHybridConfig":{"cmSyncableSiteIds":["cmSyncableSiteIds","cmSyncableSiteIds"],"dv360ToCmDataSharingEnabled":True,"dv360ToCmCostReportingEnabled":True,"cmAdvertiserIds":["cmAdvertiserIds","cmAdvertiserIds"],"cmFloodlightConfigId":"cmFloodlightConfigId","cmFloodlightLinkingAuthorized":True,"cmAccountId":"cmAccountId"}},"displayName":"displayName","creativeConfig":{"dynamicCreativeEnabled":True,"videoCreativeDataSharingAuthorized":True,"obaComplianceDisabled":True,"iasClientId":"iasClientId"},"updateTime":"updateTime","integrationDetails":{"integrationCode":"integrationCode","details":"details"},"advertiserId":"advertiserId","servingConfig":{"exemptTvFromViewabilityTargeting":True},"entityStatus":"ENTITY_STATUS_UNSPECIFIED","prismaEnabled":True,"generalConfig":{"timeZone":"timeZone","currencyCode":"currencyCode","domainUrl":"domainUrl"},"name":"name","partnerId":"partnerId","dataAccessConfig":{"sdfConfig":{"sdfConfig":{"version":"SDF_VERSION_UNSPECIFIED","adminEmail":"adminEmail"},"overridePartnerSdfConfig":True}}}
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
                    ('updateMask', 'update_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/advertisers/{advertiser_id}'.format(advertiser_id='advertiser_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_targeting_types_assigned_targeting_options_create(client):
    """Test case for displayvideo_advertisers_targeting_types_assigned_targeting_options_create

    
    """
    body = {"inheritance":"INHERITANCE_UNSPECIFIED","householdIncomeDetails":{"targetingOptionId":"targetingOptionId","householdIncome":"HOUSEHOLD_INCOME_UNSPECIFIED"},"assignedTargetingOptionId":"assignedTargetingOptionId","inventorySourceGroupDetails":{"inventorySourceGroupId":"inventorySourceGroupId"},"channelDetails":{"negative":True,"channelId":"channelId"},"omidDetails":{"targetingOptionId":"targetingOptionId","omid":"OMID_UNSPECIFIED"},"contentInstreamPositionDetails":{"adType":"AD_TYPE_UNSPECIFIED","contentInstreamPosition":"CONTENT_INSTREAM_POSITION_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"browserDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"audienceGroupDetails":{"includedGoogleAudienceGroup":{"settings":[{"googleAudienceId":"googleAudienceId"},{"googleAudienceId":"googleAudienceId"}]},"includedCustomListGroup":{"settings":[{"customListId":"customListId"},{"customListId":"customListId"}]},"includedCombinedAudienceGroup":{"settings":[{"combinedAudienceId":"combinedAudienceId"},{"combinedAudienceId":"combinedAudienceId"}]},"excludedGoogleAudienceGroup":{"settings":[{"googleAudienceId":"googleAudienceId"},{"googleAudienceId":"googleAudienceId"}]},"excludedFirstAndThirdPartyAudienceGroup":{"settings":[{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"},{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"}]},"includedFirstAndThirdPartyAudienceGroups":[{"settings":[{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"},{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"}]},{"settings":[{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"},{"firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","recency":"RECENCY_NO_LIMIT"}]}]},"nativeContentPositionDetails":{"targetingOptionId":"targetingOptionId","contentPosition":"NATIVE_CONTENT_POSITION_UNSPECIFIED"},"dayAndTimeDetails":{"endHour":6,"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startHour":1,"timeZoneResolution":"TIME_ZONE_RESOLUTION_UNSPECIFIED"},"exchangeDetails":{"targetingOptionId":"targetingOptionId"},"keywordDetails":{"negative":True,"keyword":"keyword"},"targetingType":"TARGETING_TYPE_UNSPECIFIED","deviceMakeModelDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"digitalContentLabelExclusionDetails":{"excludedTargetingOptionId":"excludedTargetingOptionId","contentRatingTier":"CONTENT_RATING_TIER_UNSPECIFIED"},"poiDetails":{"proximityRadiusAmount":2.3021358869347655,"proximityRadiusUnit":"DISTANCE_UNIT_UNSPECIFIED","displayName":"displayName","latitude":5.962133916683182,"targetingOptionId":"targetingOptionId","longitude":5.637376656633329},"environmentDetails":{"environment":"ENVIRONMENT_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"subExchangeDetails":{"targetingOptionId":"targetingOptionId"},"appCategoryDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"contentDurationDetails":{"contentDuration":"CONTENT_DURATION_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"deviceTypeDetails":{"deviceType":"DEVICE_TYPE_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"appDetails":{"negative":True,"appPlatform":"APP_PLATFORM_UNSPECIFIED","displayName":"displayName","appId":"appId"},"name":"name","viewabilityDetails":{"viewability":"VIEWABILITY_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"contentGenreDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"authorizedSellerStatusDetails":{"targetingOptionId":"targetingOptionId","authorizedSellerStatus":"AUTHORIZED_SELLER_STATUS_UNSPECIFIED"},"contentStreamTypeDetails":{"contentStreamType":"CONTENT_STREAM_TYPE_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"geoRegionDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId","geoRegionType":"GEO_REGION_TYPE_UNKNOWN"},"businessChainDetails":{"proximityRadiusAmount":0.8008281904610115,"proximityRadiusUnit":"DISTANCE_UNIT_UNSPECIFIED","displayName":"displayName","targetingOptionId":"targetingOptionId"},"parentalStatusDetails":{"targetingOptionId":"targetingOptionId","parentalStatus":"PARENTAL_STATUS_UNSPECIFIED"},"negativeKeywordListDetails":{"negativeKeywordListId":"negativeKeywordListId"},"categoryDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"urlDetails":{"negative":True,"url":"url"},"operatingSystemDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"sensitiveCategoryExclusionDetails":{"sensitiveCategory":"SENSITIVE_CATEGORY_UNSPECIFIED","excludedTargetingOptionId":"excludedTargetingOptionId"},"proximityLocationListDetails":{"proximityLocationListId":"proximityLocationListId","proximityRadiusRange":"PROXIMITY_RADIUS_RANGE_UNSPECIFIED"},"onScreenPositionDetails":{"adType":"AD_TYPE_UNSPECIFIED","targetingOptionId":"targetingOptionId","onScreenPosition":"ON_SCREEN_POSITION_UNSPECIFIED"},"contentOutstreamPositionDetails":{"adType":"AD_TYPE_UNSPECIFIED","contentOutstreamPosition":"CONTENT_OUTSTREAM_POSITION_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"audioContentTypeDetails":{"audioContentType":"AUDIO_CONTENT_TYPE_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"genderDetails":{"gender":"GENDER_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"inventorySourceDetails":{"inventorySourceId":"inventorySourceId"},"languageDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"thirdPartyVerifierDetails":{"doubleVerify":{"appStarRating":{"avoidInsufficientStarRating":True,"avoidedStarRating":"APP_STAR_RATE_UNSPECIFIED"},"customSegmentId":"customSegmentId","brandSafetyCategories":{"avoidUnknownBrandSafetyCategory":True,"avoidedMediumSeverityCategories":["MEDIUM_SEVERITY_UNSPECIFIED","MEDIUM_SEVERITY_UNSPECIFIED"],"avoidedHighSeverityCategories":["HIGHER_SEVERITY_UNSPECIFIED","HIGHER_SEVERITY_UNSPECIFIED"]},"fraudInvalidTraffic":{"avoidInsufficientOption":True,"avoidedFraudOption":"FRAUD_UNSPECIFIED"},"avoidedAgeRatings":["AGE_RATING_UNSPECIFIED","AGE_RATING_UNSPECIFIED"],"videoViewability":{"videoViewableRate":"VIDEO_VIEWABLE_RATE_UNSPECIFIED","playerImpressionRate":"PLAYER_SIZE_400X300_UNSPECIFIED","videoIab":"VIDEO_IAB_UNSPECIFIED"},"displayViewability":{"viewableDuring":"AVERAGE_VIEW_DURATION_UNSPECIFIED","iab":"IAB_VIEWED_RATE_UNSPECIFIED"}},"adloox":{"excludedAdlooxCategories":["ADLOOX_UNSPECIFIED","ADLOOX_UNSPECIFIED"]},"integralAdScience":{"excludeUnrateable":True,"excludedViolenceRisk":"VIOLENCE_UNSPECIFIED","excludedIllegalDownloadsRisk":"ILLEGAL_DOWNLOADS_UNSPECIFIED","excludedOffensiveLanguageRisk":"OFFENSIVE_LANGUAGE_UNSPECIFIED","videoViewability":"VIDEO_VIEWABILITY_UNSPECIFIED","excludedGamblingRisk":"GAMBLING_UNSPECIFIED","displayViewability":"PERFORMANCE_VIEWABILITY_UNSPECIFIED","customSegmentId":["customSegmentId","customSegmentId"],"excludedDrugsRisk":"DRUGS_UNSPECIFIED","excludedAlcoholRisk":"ALCOHOL_UNSPECIFIED","excludedHateSpeechRisk":"HATE_SPEECH_UNSPECIFIED","excludedAdFraudRisk":"SUSPICIOUS_ACTIVITY_UNSPECIFIED","traqScoreOption":"TRAQ_UNSPECIFIED","excludedAdultRisk":"ADULT_UNSPECIFIED"}},"videoPlayerSizeDetails":{"targetingOptionId":"targetingOptionId","videoPlayerSize":"VIDEO_PLAYER_SIZE_UNSPECIFIED"},"carrierAndIspDetails":{"negative":True,"displayName":"displayName","targetingOptionId":"targetingOptionId"},"userRewardedContentDetails":{"targetingOptionId":"targetingOptionId","userRewardedContent":"USER_REWARDED_CONTENT_UNSPECIFIED"},"ageRangeDetails":{"ageRange":"AGE_RANGE_UNSPECIFIED","targetingOptionId":"targetingOptionId"},"regionalLocationListDetails":{"negative":True,"regionalLocationListId":"regionalLocationListId"}}
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
        path='/v1/advertisers/{advertiser_id}/targetingTypes/{targeting_type}/assignedTargetingOptions'.format(advertiser_id='advertiser_id_example', targeting_type='targeting_type_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_targeting_types_assigned_targeting_options_delete(client):
    """Test case for displayvideo_advertisers_targeting_types_assigned_targeting_options_delete

    
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
        path='/v1/advertisers/{advertiser_id}/targetingTypes/{targeting_type}/assignedTargetingOptions/{assigned_targeting_option_id}'.format(advertiser_id='advertiser_id_example', targeting_type='targeting_type_example', assigned_targeting_option_id='assigned_targeting_option_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_targeting_types_assigned_targeting_options_get(client):
    """Test case for displayvideo_advertisers_targeting_types_assigned_targeting_options_get

    
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
        path='/v1/advertisers/{advertiser_id}/targetingTypes/{targeting_type}/assignedTargetingOptions/{assigned_targeting_option_id}'.format(advertiser_id='advertiser_id_example', targeting_type='targeting_type_example', assigned_targeting_option_id='assigned_targeting_option_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_advertisers_targeting_types_assigned_targeting_options_list(client):
    """Test case for displayvideo_advertisers_targeting_types_assigned_targeting_options_list

    
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
        path='/v1/advertisers/{advertiser_id}/targetingTypes/{targeting_type}/assignedTargetingOptions'.format(advertiser_id='advertiser_id_example', targeting_type='targeting_type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

