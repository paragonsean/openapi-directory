# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.ad import Ad
from openapi_server.models.ads_list_response import AdsListResponse


pytestmark = pytest.mark.asyncio

async def test_dfareporting_ads_get(client):
    """Test case for dfareporting_ads_get

    
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
        path='/dfareporting/v3.3/userprofiles/{profile_id}/ads/{id}'.format(profile_id='profile_id_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfareporting_ads_insert(client):
    """Test case for dfareporting_ads_insert

    
    """
    body = {"geoTargeting":{"postalCodes":[{"code":"code","countryCode":"countryCode","countryDartId":"countryDartId","kind":"kind","id":"id"},{"code":"code","countryCode":"countryCode","countryDartId":"countryDartId","kind":"kind","id":"id"}],"regions":[{"regionCode":"regionCode","countryCode":"countryCode","countryDartId":"countryDartId","kind":"kind","name":"name","dartId":"dartId"},{"regionCode":"regionCode","countryCode":"countryCode","countryDartId":"countryDartId","kind":"kind","name":"name","dartId":"dartId"}],"cities":[{"regionCode":"regionCode","metroDmaId":"metroDmaId","regionDartId":"regionDartId","countryCode":"countryCode","countryDartId":"countryDartId","kind":"kind","metroCode":"metroCode","name":"name","dartId":"dartId"},{"regionCode":"regionCode","metroDmaId":"metroDmaId","regionDartId":"regionDartId","countryCode":"countryCode","countryDartId":"countryDartId","kind":"kind","metroCode":"metroCode","name":"name","dartId":"dartId"}],"excludeCountries":True,"countries":[{"countryCode":"countryCode","kind":"kind","sslEnabled":True,"name":"name","dartId":"dartId"},{"countryCode":"countryCode","kind":"kind","sslEnabled":True,"name":"name","dartId":"dartId"}],"metros":[{"countryCode":"countryCode","countryDartId":"countryDartId","kind":"kind","dmaId":"dmaId","metroCode":"metroCode","name":"name","dartId":"dartId"},{"countryCode":"countryCode","countryDartId":"countryDartId","kind":"kind","dmaId":"dmaId","metroCode":"metroCode","name":"name","dartId":"dartId"}]},"technologyTargeting":{"operatingSystems":[{"desktop":True,"kind":"kind","mobile":True,"name":"name","dartId":"dartId"},{"desktop":True,"kind":"kind","mobile":True,"name":"name","dartId":"dartId"}],"mobileCarriers":[{"countryCode":"countryCode","countryDartId":"countryDartId","kind":"kind","name":"name","id":"id"},{"countryCode":"countryCode","countryDartId":"countryDartId","kind":"kind","name":"name","id":"id"}],"operatingSystemVersions":[{"kind":"kind","name":"name","id":"id","majorVersion":"majorVersion","minorVersion":"minorVersion","operatingSystem":{"desktop":True,"kind":"kind","mobile":True,"name":"name","dartId":"dartId"}},{"kind":"kind","name":"name","id":"id","majorVersion":"majorVersion","minorVersion":"minorVersion","operatingSystem":{"desktop":True,"kind":"kind","mobile":True,"name":"name","dartId":"dartId"}}],"browsers":[{"browserVersionId":"browserVersionId","kind":"kind","name":"name","dartId":"dartId","majorVersion":"majorVersion","minorVersion":"minorVersion"},{"browserVersionId":"browserVersionId","kind":"kind","name":"name","dartId":"dartId","majorVersion":"majorVersion","minorVersion":"minorVersion"}],"connectionTypes":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"platformTypes":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}]},"defaultClickThroughEventTagProperties":{"defaultClickThroughEventTagId":"defaultClickThroughEventTagId","overrideInheritedEventTag":True},"campaignIdDimensionValue":{"kind":"kind","matchType":"EXACT","etag":"etag","id":"id","value":"value","dimensionName":"dimensionName"},"targetingTemplateId":"targetingTemplateId","type":"AD_SERVING_STANDARD_AD","idDimensionValue":{"kind":"kind","matchType":"EXACT","etag":"etag","id":"id","value":"value","dimensionName":"dimensionName"},"languageTargeting":{"languages":[{"kind":"kind","name":"name","id":"id","languageCode":"languageCode"},{"kind":"kind","name":"name","id":"id","languageCode":"languageCode"}]},"sslRequired":True,"creativeRotation":{"weightCalculationStrategy":"WEIGHT_STRATEGY_EQUAL","creativeAssignments":[{"clickThroughUrl":{"defaultLandingPage":True,"landingPageId":"landingPageId","computedClickThroughUrl":"computedClickThroughUrl","customClickThroughUrl":"customClickThroughUrl"},"active":True,"creativeGroupAssignments":[{"creativeGroupNumber":"CREATIVE_GROUP_ONE","creativeGroupId":"creativeGroupId"},{"creativeGroupNumber":"CREATIVE_GROUP_ONE","creativeGroupId":"creativeGroupId"}],"richMediaExitOverrides":[{"clickThroughUrl":{"defaultLandingPage":True,"landingPageId":"landingPageId","computedClickThroughUrl":"computedClickThroughUrl","customClickThroughUrl":"customClickThroughUrl"},"exitId":"exitId","enabled":True},{"clickThroughUrl":{"defaultLandingPage":True,"landingPageId":"landingPageId","computedClickThroughUrl":"computedClickThroughUrl","customClickThroughUrl":"customClickThroughUrl"},"exitId":"exitId","enabled":True}],"weight":6,"creativeId":"creativeId","sequence":0,"applyEventTags":True,"sslCompliant":True,"creativeIdDimensionValue":{"kind":"kind","matchType":"EXACT","etag":"etag","id":"id","value":"value","dimensionName":"dimensionName"},"startTime":"2000-01-23T04:56:07.000+00:00","endTime":"2000-01-23T04:56:07.000+00:00","companionCreativeOverrides":[{"clickThroughUrl":{"defaultLandingPage":True,"landingPageId":"landingPageId","computedClickThroughUrl":"computedClickThroughUrl","customClickThroughUrl":"customClickThroughUrl"},"creativeId":"creativeId"},{"clickThroughUrl":{"defaultLandingPage":True,"landingPageId":"landingPageId","computedClickThroughUrl":"computedClickThroughUrl","customClickThroughUrl":"customClickThroughUrl"},"creativeId":"creativeId"}]},{"clickThroughUrl":{"defaultLandingPage":True,"landingPageId":"landingPageId","computedClickThroughUrl":"computedClickThroughUrl","customClickThroughUrl":"customClickThroughUrl"},"active":True,"creativeGroupAssignments":[{"creativeGroupNumber":"CREATIVE_GROUP_ONE","creativeGroupId":"creativeGroupId"},{"creativeGroupNumber":"CREATIVE_GROUP_ONE","creativeGroupId":"creativeGroupId"}],"richMediaExitOverrides":[{"clickThroughUrl":{"defaultLandingPage":True,"landingPageId":"landingPageId","computedClickThroughUrl":"computedClickThroughUrl","customClickThroughUrl":"customClickThroughUrl"},"exitId":"exitId","enabled":True},{"clickThroughUrl":{"defaultLandingPage":True,"landingPageId":"landingPageId","computedClickThroughUrl":"computedClickThroughUrl","customClickThroughUrl":"customClickThroughUrl"},"exitId":"exitId","enabled":True}],"weight":6,"creativeId":"creativeId","sequence":0,"applyEventTags":True,"sslCompliant":True,"creativeIdDimensionValue":{"kind":"kind","matchType":"EXACT","etag":"etag","id":"id","value":"value","dimensionName":"dimensionName"},"startTime":"2000-01-23T04:56:07.000+00:00","endTime":"2000-01-23T04:56:07.000+00:00","companionCreativeOverrides":[{"clickThroughUrl":{"defaultLandingPage":True,"landingPageId":"landingPageId","computedClickThroughUrl":"computedClickThroughUrl","customClickThroughUrl":"customClickThroughUrl"},"creativeId":"creativeId"},{"clickThroughUrl":{"defaultLandingPage":True,"landingPageId":"landingPageId","computedClickThroughUrl":"computedClickThroughUrl","customClickThroughUrl":"customClickThroughUrl"},"creativeId":"creativeId"}]}],"creativeOptimizationConfigurationId":"creativeOptimizationConfigurationId","type":"CREATIVE_ROTATION_TYPE_SEQUENTIAL"},"archived":True,"advertiserIdDimensionValue":{"kind":"kind","matchType":"EXACT","etag":"etag","id":"id","value":"value","dimensionName":"dimensionName"},"startTime":"2000-01-23T04:56:07.000+00:00","audienceSegmentId":"audienceSegmentId","id":"id","createInfo":{"time":"time"},"eventTagOverrides":[{"id":"id","enabled":True},{"id":"id","enabled":True}],"keyValueTargetingExpression":{"expression":"expression"},"subaccountId":"subaccountId","comments":"comments","campaignId":"campaignId","kind":"kind","lastModifiedInfo":{"time":"time"},"clickThroughUrl":{"defaultLandingPage":True,"landingPageId":"landingPageId","computedClickThroughUrl":"computedClickThroughUrl","customClickThroughUrl":"customClickThroughUrl"},"active":True,"creativeGroupAssignments":[{"creativeGroupNumber":"CREATIVE_GROUP_ONE","creativeGroupId":"creativeGroupId"},{"creativeGroupNumber":"CREATIVE_GROUP_ONE","creativeGroupId":"creativeGroupId"}],"dayPartTargeting":{"hoursOfDay":[1,1],"userLocalTime":True,"daysOfWeek":["MONDAY","MONDAY"]},"advertiserId":"advertiserId","deliverySchedule":{"impressionRatio":"impressionRatio","frequencyCap":{"duration":"duration","impressions":"impressions"},"hardCutoff":True,"priority":"AD_PRIORITY_01"},"accountId":"accountId","dynamicClickTracker":True,"size":{"kind":"kind","width":5,"iab":True,"id":"id","height":5},"sslCompliant":True,"name":"name","remarketingListExpression":{"expression":"expression"},"clickThroughUrlSuffixProperties":{"overrideInheritedSuffix":True,"clickThroughUrlSuffix":"clickThroughUrlSuffix"},"endTime":"2000-01-23T04:56:07.000+00:00","placementAssignments":[{"placementIdDimensionValue":{"kind":"kind","matchType":"EXACT","etag":"etag","id":"id","value":"value","dimensionName":"dimensionName"},"placementId":"placementId","active":True,"sslRequired":True},{"placementIdDimensionValue":{"kind":"kind","matchType":"EXACT","etag":"etag","id":"id","value":"value","dimensionName":"dimensionName"},"placementId":"placementId","active":True,"sslRequired":True}],"compatibility":"DISPLAY"}
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
        path='/dfareporting/v3.3/userprofiles/{profile_id}/ads'.format(profile_id='profile_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfareporting_ads_list(client):
    """Test case for dfareporting_ads_list

    
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
                    ('active', True),
                    ('advertiserId', 'advertiser_id_example'),
                    ('archived', True),
                    ('audienceSegmentIds', ['audience_segment_ids_example']),
                    ('campaignIds', ['campaign_ids_example']),
                    ('compatibility', 'compatibility_example'),
                    ('creativeIds', ['creative_ids_example']),
                    ('creativeOptimizationConfigurationIds', ['creative_optimization_configuration_ids_example']),
                    ('dynamicClickTracker', True),
                    ('ids', ['ids_example']),
                    ('landingPageIds', ['landing_page_ids_example']),
                    ('maxResults', 56),
                    ('overriddenEventTagId', 'overridden_event_tag_id_example'),
                    ('pageToken', 'page_token_example'),
                    ('placementIds', ['placement_ids_example']),
                    ('remarketingListIds', ['remarketing_list_ids_example']),
                    ('searchString', 'search_string_example'),
                    ('sizeIds', ['size_ids_example']),
                    ('sortField', 'sort_field_example'),
                    ('sortOrder', 'sort_order_example'),
                    ('sslCompliant', True),
                    ('sslRequired', True),
                    ('type', ['type_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/dfareporting/v3.3/userprofiles/{profile_id}/ads'.format(profile_id='profile_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfareporting_ads_patch(client):
    """Test case for dfareporting_ads_patch

    
    """
    body = {"geoTargeting":{"postalCodes":[{"code":"code","countryCode":"countryCode","countryDartId":"countryDartId","kind":"kind","id":"id"},{"code":"code","countryCode":"countryCode","countryDartId":"countryDartId","kind":"kind","id":"id"}],"regions":[{"regionCode":"regionCode","countryCode":"countryCode","countryDartId":"countryDartId","kind":"kind","name":"name","dartId":"dartId"},{"regionCode":"regionCode","countryCode":"countryCode","countryDartId":"countryDartId","kind":"kind","name":"name","dartId":"dartId"}],"cities":[{"regionCode":"regionCode","metroDmaId":"metroDmaId","regionDartId":"regionDartId","countryCode":"countryCode","countryDartId":"countryDartId","kind":"kind","metroCode":"metroCode","name":"name","dartId":"dartId"},{"regionCode":"regionCode","metroDmaId":"metroDmaId","regionDartId":"regionDartId","countryCode":"countryCode","countryDartId":"countryDartId","kind":"kind","metroCode":"metroCode","name":"name","dartId":"dartId"}],"excludeCountries":True,"countries":[{"countryCode":"countryCode","kind":"kind","sslEnabled":True,"name":"name","dartId":"dartId"},{"countryCode":"countryCode","kind":"kind","sslEnabled":True,"name":"name","dartId":"dartId"}],"metros":[{"countryCode":"countryCode","countryDartId":"countryDartId","kind":"kind","dmaId":"dmaId","metroCode":"metroCode","name":"name","dartId":"dartId"},{"countryCode":"countryCode","countryDartId":"countryDartId","kind":"kind","dmaId":"dmaId","metroCode":"metroCode","name":"name","dartId":"dartId"}]},"technologyTargeting":{"operatingSystems":[{"desktop":True,"kind":"kind","mobile":True,"name":"name","dartId":"dartId"},{"desktop":True,"kind":"kind","mobile":True,"name":"name","dartId":"dartId"}],"mobileCarriers":[{"countryCode":"countryCode","countryDartId":"countryDartId","kind":"kind","name":"name","id":"id"},{"countryCode":"countryCode","countryDartId":"countryDartId","kind":"kind","name":"name","id":"id"}],"operatingSystemVersions":[{"kind":"kind","name":"name","id":"id","majorVersion":"majorVersion","minorVersion":"minorVersion","operatingSystem":{"desktop":True,"kind":"kind","mobile":True,"name":"name","dartId":"dartId"}},{"kind":"kind","name":"name","id":"id","majorVersion":"majorVersion","minorVersion":"minorVersion","operatingSystem":{"desktop":True,"kind":"kind","mobile":True,"name":"name","dartId":"dartId"}}],"browsers":[{"browserVersionId":"browserVersionId","kind":"kind","name":"name","dartId":"dartId","majorVersion":"majorVersion","minorVersion":"minorVersion"},{"browserVersionId":"browserVersionId","kind":"kind","name":"name","dartId":"dartId","majorVersion":"majorVersion","minorVersion":"minorVersion"}],"connectionTypes":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"platformTypes":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}]},"defaultClickThroughEventTagProperties":{"defaultClickThroughEventTagId":"defaultClickThroughEventTagId","overrideInheritedEventTag":True},"campaignIdDimensionValue":{"kind":"kind","matchType":"EXACT","etag":"etag","id":"id","value":"value","dimensionName":"dimensionName"},"targetingTemplateId":"targetingTemplateId","type":"AD_SERVING_STANDARD_AD","idDimensionValue":{"kind":"kind","matchType":"EXACT","etag":"etag","id":"id","value":"value","dimensionName":"dimensionName"},"languageTargeting":{"languages":[{"kind":"kind","name":"name","id":"id","languageCode":"languageCode"},{"kind":"kind","name":"name","id":"id","languageCode":"languageCode"}]},"sslRequired":True,"creativeRotation":{"weightCalculationStrategy":"WEIGHT_STRATEGY_EQUAL","creativeAssignments":[{"clickThroughUrl":{"defaultLandingPage":True,"landingPageId":"landingPageId","computedClickThroughUrl":"computedClickThroughUrl","customClickThroughUrl":"customClickThroughUrl"},"active":True,"creativeGroupAssignments":[{"creativeGroupNumber":"CREATIVE_GROUP_ONE","creativeGroupId":"creativeGroupId"},{"creativeGroupNumber":"CREATIVE_GROUP_ONE","creativeGroupId":"creativeGroupId"}],"richMediaExitOverrides":[{"clickThroughUrl":{"defaultLandingPage":True,"landingPageId":"landingPageId","computedClickThroughUrl":"computedClickThroughUrl","customClickThroughUrl":"customClickThroughUrl"},"exitId":"exitId","enabled":True},{"clickThroughUrl":{"defaultLandingPage":True,"landingPageId":"landingPageId","computedClickThroughUrl":"computedClickThroughUrl","customClickThroughUrl":"customClickThroughUrl"},"exitId":"exitId","enabled":True}],"weight":6,"creativeId":"creativeId","sequence":0,"applyEventTags":True,"sslCompliant":True,"creativeIdDimensionValue":{"kind":"kind","matchType":"EXACT","etag":"etag","id":"id","value":"value","dimensionName":"dimensionName"},"startTime":"2000-01-23T04:56:07.000+00:00","endTime":"2000-01-23T04:56:07.000+00:00","companionCreativeOverrides":[{"clickThroughUrl":{"defaultLandingPage":True,"landingPageId":"landingPageId","computedClickThroughUrl":"computedClickThroughUrl","customClickThroughUrl":"customClickThroughUrl"},"creativeId":"creativeId"},{"clickThroughUrl":{"defaultLandingPage":True,"landingPageId":"landingPageId","computedClickThroughUrl":"computedClickThroughUrl","customClickThroughUrl":"customClickThroughUrl"},"creativeId":"creativeId"}]},{"clickThroughUrl":{"defaultLandingPage":True,"landingPageId":"landingPageId","computedClickThroughUrl":"computedClickThroughUrl","customClickThroughUrl":"customClickThroughUrl"},"active":True,"creativeGroupAssignments":[{"creativeGroupNumber":"CREATIVE_GROUP_ONE","creativeGroupId":"creativeGroupId"},{"creativeGroupNumber":"CREATIVE_GROUP_ONE","creativeGroupId":"creativeGroupId"}],"richMediaExitOverrides":[{"clickThroughUrl":{"defaultLandingPage":True,"landingPageId":"landingPageId","computedClickThroughUrl":"computedClickThroughUrl","customClickThroughUrl":"customClickThroughUrl"},"exitId":"exitId","enabled":True},{"clickThroughUrl":{"defaultLandingPage":True,"landingPageId":"landingPageId","computedClickThroughUrl":"computedClickThroughUrl","customClickThroughUrl":"customClickThroughUrl"},"exitId":"exitId","enabled":True}],"weight":6,"creativeId":"creativeId","sequence":0,"applyEventTags":True,"sslCompliant":True,"creativeIdDimensionValue":{"kind":"kind","matchType":"EXACT","etag":"etag","id":"id","value":"value","dimensionName":"dimensionName"},"startTime":"2000-01-23T04:56:07.000+00:00","endTime":"2000-01-23T04:56:07.000+00:00","companionCreativeOverrides":[{"clickThroughUrl":{"defaultLandingPage":True,"landingPageId":"landingPageId","computedClickThroughUrl":"computedClickThroughUrl","customClickThroughUrl":"customClickThroughUrl"},"creativeId":"creativeId"},{"clickThroughUrl":{"defaultLandingPage":True,"landingPageId":"landingPageId","computedClickThroughUrl":"computedClickThroughUrl","customClickThroughUrl":"customClickThroughUrl"},"creativeId":"creativeId"}]}],"creativeOptimizationConfigurationId":"creativeOptimizationConfigurationId","type":"CREATIVE_ROTATION_TYPE_SEQUENTIAL"},"archived":True,"advertiserIdDimensionValue":{"kind":"kind","matchType":"EXACT","etag":"etag","id":"id","value":"value","dimensionName":"dimensionName"},"startTime":"2000-01-23T04:56:07.000+00:00","audienceSegmentId":"audienceSegmentId","id":"id","createInfo":{"time":"time"},"eventTagOverrides":[{"id":"id","enabled":True},{"id":"id","enabled":True}],"keyValueTargetingExpression":{"expression":"expression"},"subaccountId":"subaccountId","comments":"comments","campaignId":"campaignId","kind":"kind","lastModifiedInfo":{"time":"time"},"clickThroughUrl":{"defaultLandingPage":True,"landingPageId":"landingPageId","computedClickThroughUrl":"computedClickThroughUrl","customClickThroughUrl":"customClickThroughUrl"},"active":True,"creativeGroupAssignments":[{"creativeGroupNumber":"CREATIVE_GROUP_ONE","creativeGroupId":"creativeGroupId"},{"creativeGroupNumber":"CREATIVE_GROUP_ONE","creativeGroupId":"creativeGroupId"}],"dayPartTargeting":{"hoursOfDay":[1,1],"userLocalTime":True,"daysOfWeek":["MONDAY","MONDAY"]},"advertiserId":"advertiserId","deliverySchedule":{"impressionRatio":"impressionRatio","frequencyCap":{"duration":"duration","impressions":"impressions"},"hardCutoff":True,"priority":"AD_PRIORITY_01"},"accountId":"accountId","dynamicClickTracker":True,"size":{"kind":"kind","width":5,"iab":True,"id":"id","height":5},"sslCompliant":True,"name":"name","remarketingListExpression":{"expression":"expression"},"clickThroughUrlSuffixProperties":{"overrideInheritedSuffix":True,"clickThroughUrlSuffix":"clickThroughUrlSuffix"},"endTime":"2000-01-23T04:56:07.000+00:00","placementAssignments":[{"placementIdDimensionValue":{"kind":"kind","matchType":"EXACT","etag":"etag","id":"id","value":"value","dimensionName":"dimensionName"},"placementId":"placementId","active":True,"sslRequired":True},{"placementIdDimensionValue":{"kind":"kind","matchType":"EXACT","etag":"etag","id":"id","value":"value","dimensionName":"dimensionName"},"placementId":"placementId","active":True,"sslRequired":True}],"compatibility":"DISPLAY"}
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
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/dfareporting/v3.3/userprofiles/{profile_id}/ads'.format(profile_id='profile_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfareporting_ads_update(client):
    """Test case for dfareporting_ads_update

    
    """
    body = {"geoTargeting":{"postalCodes":[{"code":"code","countryCode":"countryCode","countryDartId":"countryDartId","kind":"kind","id":"id"},{"code":"code","countryCode":"countryCode","countryDartId":"countryDartId","kind":"kind","id":"id"}],"regions":[{"regionCode":"regionCode","countryCode":"countryCode","countryDartId":"countryDartId","kind":"kind","name":"name","dartId":"dartId"},{"regionCode":"regionCode","countryCode":"countryCode","countryDartId":"countryDartId","kind":"kind","name":"name","dartId":"dartId"}],"cities":[{"regionCode":"regionCode","metroDmaId":"metroDmaId","regionDartId":"regionDartId","countryCode":"countryCode","countryDartId":"countryDartId","kind":"kind","metroCode":"metroCode","name":"name","dartId":"dartId"},{"regionCode":"regionCode","metroDmaId":"metroDmaId","regionDartId":"regionDartId","countryCode":"countryCode","countryDartId":"countryDartId","kind":"kind","metroCode":"metroCode","name":"name","dartId":"dartId"}],"excludeCountries":True,"countries":[{"countryCode":"countryCode","kind":"kind","sslEnabled":True,"name":"name","dartId":"dartId"},{"countryCode":"countryCode","kind":"kind","sslEnabled":True,"name":"name","dartId":"dartId"}],"metros":[{"countryCode":"countryCode","countryDartId":"countryDartId","kind":"kind","dmaId":"dmaId","metroCode":"metroCode","name":"name","dartId":"dartId"},{"countryCode":"countryCode","countryDartId":"countryDartId","kind":"kind","dmaId":"dmaId","metroCode":"metroCode","name":"name","dartId":"dartId"}]},"technologyTargeting":{"operatingSystems":[{"desktop":True,"kind":"kind","mobile":True,"name":"name","dartId":"dartId"},{"desktop":True,"kind":"kind","mobile":True,"name":"name","dartId":"dartId"}],"mobileCarriers":[{"countryCode":"countryCode","countryDartId":"countryDartId","kind":"kind","name":"name","id":"id"},{"countryCode":"countryCode","countryDartId":"countryDartId","kind":"kind","name":"name","id":"id"}],"operatingSystemVersions":[{"kind":"kind","name":"name","id":"id","majorVersion":"majorVersion","minorVersion":"minorVersion","operatingSystem":{"desktop":True,"kind":"kind","mobile":True,"name":"name","dartId":"dartId"}},{"kind":"kind","name":"name","id":"id","majorVersion":"majorVersion","minorVersion":"minorVersion","operatingSystem":{"desktop":True,"kind":"kind","mobile":True,"name":"name","dartId":"dartId"}}],"browsers":[{"browserVersionId":"browserVersionId","kind":"kind","name":"name","dartId":"dartId","majorVersion":"majorVersion","minorVersion":"minorVersion"},{"browserVersionId":"browserVersionId","kind":"kind","name":"name","dartId":"dartId","majorVersion":"majorVersion","minorVersion":"minorVersion"}],"connectionTypes":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"platformTypes":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}]},"defaultClickThroughEventTagProperties":{"defaultClickThroughEventTagId":"defaultClickThroughEventTagId","overrideInheritedEventTag":True},"campaignIdDimensionValue":{"kind":"kind","matchType":"EXACT","etag":"etag","id":"id","value":"value","dimensionName":"dimensionName"},"targetingTemplateId":"targetingTemplateId","type":"AD_SERVING_STANDARD_AD","idDimensionValue":{"kind":"kind","matchType":"EXACT","etag":"etag","id":"id","value":"value","dimensionName":"dimensionName"},"languageTargeting":{"languages":[{"kind":"kind","name":"name","id":"id","languageCode":"languageCode"},{"kind":"kind","name":"name","id":"id","languageCode":"languageCode"}]},"sslRequired":True,"creativeRotation":{"weightCalculationStrategy":"WEIGHT_STRATEGY_EQUAL","creativeAssignments":[{"clickThroughUrl":{"defaultLandingPage":True,"landingPageId":"landingPageId","computedClickThroughUrl":"computedClickThroughUrl","customClickThroughUrl":"customClickThroughUrl"},"active":True,"creativeGroupAssignments":[{"creativeGroupNumber":"CREATIVE_GROUP_ONE","creativeGroupId":"creativeGroupId"},{"creativeGroupNumber":"CREATIVE_GROUP_ONE","creativeGroupId":"creativeGroupId"}],"richMediaExitOverrides":[{"clickThroughUrl":{"defaultLandingPage":True,"landingPageId":"landingPageId","computedClickThroughUrl":"computedClickThroughUrl","customClickThroughUrl":"customClickThroughUrl"},"exitId":"exitId","enabled":True},{"clickThroughUrl":{"defaultLandingPage":True,"landingPageId":"landingPageId","computedClickThroughUrl":"computedClickThroughUrl","customClickThroughUrl":"customClickThroughUrl"},"exitId":"exitId","enabled":True}],"weight":6,"creativeId":"creativeId","sequence":0,"applyEventTags":True,"sslCompliant":True,"creativeIdDimensionValue":{"kind":"kind","matchType":"EXACT","etag":"etag","id":"id","value":"value","dimensionName":"dimensionName"},"startTime":"2000-01-23T04:56:07.000+00:00","endTime":"2000-01-23T04:56:07.000+00:00","companionCreativeOverrides":[{"clickThroughUrl":{"defaultLandingPage":True,"landingPageId":"landingPageId","computedClickThroughUrl":"computedClickThroughUrl","customClickThroughUrl":"customClickThroughUrl"},"creativeId":"creativeId"},{"clickThroughUrl":{"defaultLandingPage":True,"landingPageId":"landingPageId","computedClickThroughUrl":"computedClickThroughUrl","customClickThroughUrl":"customClickThroughUrl"},"creativeId":"creativeId"}]},{"clickThroughUrl":{"defaultLandingPage":True,"landingPageId":"landingPageId","computedClickThroughUrl":"computedClickThroughUrl","customClickThroughUrl":"customClickThroughUrl"},"active":True,"creativeGroupAssignments":[{"creativeGroupNumber":"CREATIVE_GROUP_ONE","creativeGroupId":"creativeGroupId"},{"creativeGroupNumber":"CREATIVE_GROUP_ONE","creativeGroupId":"creativeGroupId"}],"richMediaExitOverrides":[{"clickThroughUrl":{"defaultLandingPage":True,"landingPageId":"landingPageId","computedClickThroughUrl":"computedClickThroughUrl","customClickThroughUrl":"customClickThroughUrl"},"exitId":"exitId","enabled":True},{"clickThroughUrl":{"defaultLandingPage":True,"landingPageId":"landingPageId","computedClickThroughUrl":"computedClickThroughUrl","customClickThroughUrl":"customClickThroughUrl"},"exitId":"exitId","enabled":True}],"weight":6,"creativeId":"creativeId","sequence":0,"applyEventTags":True,"sslCompliant":True,"creativeIdDimensionValue":{"kind":"kind","matchType":"EXACT","etag":"etag","id":"id","value":"value","dimensionName":"dimensionName"},"startTime":"2000-01-23T04:56:07.000+00:00","endTime":"2000-01-23T04:56:07.000+00:00","companionCreativeOverrides":[{"clickThroughUrl":{"defaultLandingPage":True,"landingPageId":"landingPageId","computedClickThroughUrl":"computedClickThroughUrl","customClickThroughUrl":"customClickThroughUrl"},"creativeId":"creativeId"},{"clickThroughUrl":{"defaultLandingPage":True,"landingPageId":"landingPageId","computedClickThroughUrl":"computedClickThroughUrl","customClickThroughUrl":"customClickThroughUrl"},"creativeId":"creativeId"}]}],"creativeOptimizationConfigurationId":"creativeOptimizationConfigurationId","type":"CREATIVE_ROTATION_TYPE_SEQUENTIAL"},"archived":True,"advertiserIdDimensionValue":{"kind":"kind","matchType":"EXACT","etag":"etag","id":"id","value":"value","dimensionName":"dimensionName"},"startTime":"2000-01-23T04:56:07.000+00:00","audienceSegmentId":"audienceSegmentId","id":"id","createInfo":{"time":"time"},"eventTagOverrides":[{"id":"id","enabled":True},{"id":"id","enabled":True}],"keyValueTargetingExpression":{"expression":"expression"},"subaccountId":"subaccountId","comments":"comments","campaignId":"campaignId","kind":"kind","lastModifiedInfo":{"time":"time"},"clickThroughUrl":{"defaultLandingPage":True,"landingPageId":"landingPageId","computedClickThroughUrl":"computedClickThroughUrl","customClickThroughUrl":"customClickThroughUrl"},"active":True,"creativeGroupAssignments":[{"creativeGroupNumber":"CREATIVE_GROUP_ONE","creativeGroupId":"creativeGroupId"},{"creativeGroupNumber":"CREATIVE_GROUP_ONE","creativeGroupId":"creativeGroupId"}],"dayPartTargeting":{"hoursOfDay":[1,1],"userLocalTime":True,"daysOfWeek":["MONDAY","MONDAY"]},"advertiserId":"advertiserId","deliverySchedule":{"impressionRatio":"impressionRatio","frequencyCap":{"duration":"duration","impressions":"impressions"},"hardCutoff":True,"priority":"AD_PRIORITY_01"},"accountId":"accountId","dynamicClickTracker":True,"size":{"kind":"kind","width":5,"iab":True,"id":"id","height":5},"sslCompliant":True,"name":"name","remarketingListExpression":{"expression":"expression"},"clickThroughUrlSuffixProperties":{"overrideInheritedSuffix":True,"clickThroughUrlSuffix":"clickThroughUrlSuffix"},"endTime":"2000-01-23T04:56:07.000+00:00","placementAssignments":[{"placementIdDimensionValue":{"kind":"kind","matchType":"EXACT","etag":"etag","id":"id","value":"value","dimensionName":"dimensionName"},"placementId":"placementId","active":True,"sslRequired":True},{"placementIdDimensionValue":{"kind":"kind","matchType":"EXACT","etag":"etag","id":"id","value":"value","dimensionName":"dimensionName"},"placementId":"placementId","active":True,"sslRequired":True}],"compatibility":"DISPLAY"}
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
        method='PUT',
        path='/dfareporting/v3.3/userprofiles/{profile_id}/ads'.format(profile_id='profile_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

