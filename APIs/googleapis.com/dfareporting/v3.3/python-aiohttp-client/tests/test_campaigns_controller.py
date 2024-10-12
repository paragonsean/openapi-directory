# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.campaign import Campaign
from openapi_server.models.campaigns_list_response import CampaignsListResponse


pytestmark = pytest.mark.asyncio

async def test_dfareporting_campaigns_get(client):
    """Test case for dfareporting_campaigns_get

    
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
        path='/dfareporting/v3.3/userprofiles/{profile_id}/campaigns/{id}'.format(profile_id='profile_id_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfareporting_campaigns_insert(client):
    """Test case for dfareporting_campaigns_insert

    
    """
    body = {"defaultClickThroughEventTagProperties":{"defaultClickThroughEventTagId":"defaultClickThroughEventTagId","overrideInheritedEventTag":True},"nielsenOcrEnabled":True,"endDate":"2000-01-23","idDimensionValue":{"kind":"kind","matchType":"EXACT","etag":"etag","id":"id","value":"value","dimensionName":"dimensionName"},"archived":True,"defaultLandingPageId":"defaultLandingPageId","advertiserGroupId":"advertiserGroupId","advertiserIdDimensionValue":{"kind":"kind","matchType":"EXACT","etag":"etag","id":"id","value":"value","dimensionName":"dimensionName"},"traffickerEmails":["traffickerEmails","traffickerEmails"],"id":"id","createInfo":{"time":"time"},"eventTagOverrides":[{"id":"id","enabled":True},{"id":"id","enabled":True}],"billingInvoiceCode":"billingInvoiceCode","subaccountId":"subaccountId","kind":"kind","lastModifiedInfo":{"time":"time"},"additionalCreativeOptimizationConfigurations":[{"optimizationActivitys":[{"floodlightActivityIdDimensionValue":{"kind":"kind","matchType":"EXACT","etag":"etag","id":"id","value":"value","dimensionName":"dimensionName"},"weight":0,"floodlightActivityId":"floodlightActivityId"},{"floodlightActivityIdDimensionValue":{"kind":"kind","matchType":"EXACT","etag":"etag","id":"id","value":"value","dimensionName":"dimensionName"},"weight":0,"floodlightActivityId":"floodlightActivityId"}],"optimizationModel":"CLICK","name":"name","id":"id"},{"optimizationActivitys":[{"floodlightActivityIdDimensionValue":{"kind":"kind","matchType":"EXACT","etag":"etag","id":"id","value":"value","dimensionName":"dimensionName"},"weight":0,"floodlightActivityId":"floodlightActivityId"},{"floodlightActivityIdDimensionValue":{"kind":"kind","matchType":"EXACT","etag":"etag","id":"id","value":"value","dimensionName":"dimensionName"},"weight":0,"floodlightActivityId":"floodlightActivityId"}],"optimizationModel":"CLICK","name":"name","id":"id"}],"externalId":"externalId","adBlockingConfiguration":{"overrideClickThroughUrl":True,"creativeBundleId":"creativeBundleId","clickThroughUrl":"clickThroughUrl","enabled":True},"audienceSegmentGroups":[{"name":"name","id":"id","audienceSegments":[{"allocation":6,"name":"name","id":"id"},{"allocation":6,"name":"name","id":"id"}]},{"name":"name","id":"id","audienceSegments":[{"allocation":6,"name":"name","id":"id"},{"allocation":6,"name":"name","id":"id"}]}],"advertiserId":"advertiserId","accountId":"accountId","creativeOptimizationConfiguration":{"optimizationActivitys":[{"floodlightActivityIdDimensionValue":{"kind":"kind","matchType":"EXACT","etag":"etag","id":"id","value":"value","dimensionName":"dimensionName"},"weight":0,"floodlightActivityId":"floodlightActivityId"},{"floodlightActivityIdDimensionValue":{"kind":"kind","matchType":"EXACT","etag":"etag","id":"id","value":"value","dimensionName":"dimensionName"},"weight":0,"floodlightActivityId":"floodlightActivityId"}],"optimizationModel":"CLICK","name":"name","id":"id"},"name":"name","clickThroughUrlSuffixProperties":{"overrideInheritedSuffix":True,"clickThroughUrlSuffix":"clickThroughUrlSuffix"},"comment":"comment","creativeGroupIds":["creativeGroupIds","creativeGroupIds"],"startDate":"2000-01-23"}
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
        path='/dfareporting/v3.3/userprofiles/{profile_id}/campaigns'.format(profile_id='profile_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfareporting_campaigns_list(client):
    """Test case for dfareporting_campaigns_list

    
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
                    ('advertiserGroupIds', ['advertiser_group_ids_example']),
                    ('advertiserIds', ['advertiser_ids_example']),
                    ('archived', True),
                    ('atLeastOneOptimizationActivity', True),
                    ('excludedIds', ['excluded_ids_example']),
                    ('ids', ['ids_example']),
                    ('maxResults', 56),
                    ('overriddenEventTagId', 'overridden_event_tag_id_example'),
                    ('pageToken', 'page_token_example'),
                    ('searchString', 'search_string_example'),
                    ('sortField', 'sort_field_example'),
                    ('sortOrder', 'sort_order_example'),
                    ('subaccountId', 'subaccount_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/dfareporting/v3.3/userprofiles/{profile_id}/campaigns'.format(profile_id='profile_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfareporting_campaigns_patch(client):
    """Test case for dfareporting_campaigns_patch

    
    """
    body = {"defaultClickThroughEventTagProperties":{"defaultClickThroughEventTagId":"defaultClickThroughEventTagId","overrideInheritedEventTag":True},"nielsenOcrEnabled":True,"endDate":"2000-01-23","idDimensionValue":{"kind":"kind","matchType":"EXACT","etag":"etag","id":"id","value":"value","dimensionName":"dimensionName"},"archived":True,"defaultLandingPageId":"defaultLandingPageId","advertiserGroupId":"advertiserGroupId","advertiserIdDimensionValue":{"kind":"kind","matchType":"EXACT","etag":"etag","id":"id","value":"value","dimensionName":"dimensionName"},"traffickerEmails":["traffickerEmails","traffickerEmails"],"id":"id","createInfo":{"time":"time"},"eventTagOverrides":[{"id":"id","enabled":True},{"id":"id","enabled":True}],"billingInvoiceCode":"billingInvoiceCode","subaccountId":"subaccountId","kind":"kind","lastModifiedInfo":{"time":"time"},"additionalCreativeOptimizationConfigurations":[{"optimizationActivitys":[{"floodlightActivityIdDimensionValue":{"kind":"kind","matchType":"EXACT","etag":"etag","id":"id","value":"value","dimensionName":"dimensionName"},"weight":0,"floodlightActivityId":"floodlightActivityId"},{"floodlightActivityIdDimensionValue":{"kind":"kind","matchType":"EXACT","etag":"etag","id":"id","value":"value","dimensionName":"dimensionName"},"weight":0,"floodlightActivityId":"floodlightActivityId"}],"optimizationModel":"CLICK","name":"name","id":"id"},{"optimizationActivitys":[{"floodlightActivityIdDimensionValue":{"kind":"kind","matchType":"EXACT","etag":"etag","id":"id","value":"value","dimensionName":"dimensionName"},"weight":0,"floodlightActivityId":"floodlightActivityId"},{"floodlightActivityIdDimensionValue":{"kind":"kind","matchType":"EXACT","etag":"etag","id":"id","value":"value","dimensionName":"dimensionName"},"weight":0,"floodlightActivityId":"floodlightActivityId"}],"optimizationModel":"CLICK","name":"name","id":"id"}],"externalId":"externalId","adBlockingConfiguration":{"overrideClickThroughUrl":True,"creativeBundleId":"creativeBundleId","clickThroughUrl":"clickThroughUrl","enabled":True},"audienceSegmentGroups":[{"name":"name","id":"id","audienceSegments":[{"allocation":6,"name":"name","id":"id"},{"allocation":6,"name":"name","id":"id"}]},{"name":"name","id":"id","audienceSegments":[{"allocation":6,"name":"name","id":"id"},{"allocation":6,"name":"name","id":"id"}]}],"advertiserId":"advertiserId","accountId":"accountId","creativeOptimizationConfiguration":{"optimizationActivitys":[{"floodlightActivityIdDimensionValue":{"kind":"kind","matchType":"EXACT","etag":"etag","id":"id","value":"value","dimensionName":"dimensionName"},"weight":0,"floodlightActivityId":"floodlightActivityId"},{"floodlightActivityIdDimensionValue":{"kind":"kind","matchType":"EXACT","etag":"etag","id":"id","value":"value","dimensionName":"dimensionName"},"weight":0,"floodlightActivityId":"floodlightActivityId"}],"optimizationModel":"CLICK","name":"name","id":"id"},"name":"name","clickThroughUrlSuffixProperties":{"overrideInheritedSuffix":True,"clickThroughUrlSuffix":"clickThroughUrlSuffix"},"comment":"comment","creativeGroupIds":["creativeGroupIds","creativeGroupIds"],"startDate":"2000-01-23"}
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
        path='/dfareporting/v3.3/userprofiles/{profile_id}/campaigns'.format(profile_id='profile_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfareporting_campaigns_update(client):
    """Test case for dfareporting_campaigns_update

    
    """
    body = {"defaultClickThroughEventTagProperties":{"defaultClickThroughEventTagId":"defaultClickThroughEventTagId","overrideInheritedEventTag":True},"nielsenOcrEnabled":True,"endDate":"2000-01-23","idDimensionValue":{"kind":"kind","matchType":"EXACT","etag":"etag","id":"id","value":"value","dimensionName":"dimensionName"},"archived":True,"defaultLandingPageId":"defaultLandingPageId","advertiserGroupId":"advertiserGroupId","advertiserIdDimensionValue":{"kind":"kind","matchType":"EXACT","etag":"etag","id":"id","value":"value","dimensionName":"dimensionName"},"traffickerEmails":["traffickerEmails","traffickerEmails"],"id":"id","createInfo":{"time":"time"},"eventTagOverrides":[{"id":"id","enabled":True},{"id":"id","enabled":True}],"billingInvoiceCode":"billingInvoiceCode","subaccountId":"subaccountId","kind":"kind","lastModifiedInfo":{"time":"time"},"additionalCreativeOptimizationConfigurations":[{"optimizationActivitys":[{"floodlightActivityIdDimensionValue":{"kind":"kind","matchType":"EXACT","etag":"etag","id":"id","value":"value","dimensionName":"dimensionName"},"weight":0,"floodlightActivityId":"floodlightActivityId"},{"floodlightActivityIdDimensionValue":{"kind":"kind","matchType":"EXACT","etag":"etag","id":"id","value":"value","dimensionName":"dimensionName"},"weight":0,"floodlightActivityId":"floodlightActivityId"}],"optimizationModel":"CLICK","name":"name","id":"id"},{"optimizationActivitys":[{"floodlightActivityIdDimensionValue":{"kind":"kind","matchType":"EXACT","etag":"etag","id":"id","value":"value","dimensionName":"dimensionName"},"weight":0,"floodlightActivityId":"floodlightActivityId"},{"floodlightActivityIdDimensionValue":{"kind":"kind","matchType":"EXACT","etag":"etag","id":"id","value":"value","dimensionName":"dimensionName"},"weight":0,"floodlightActivityId":"floodlightActivityId"}],"optimizationModel":"CLICK","name":"name","id":"id"}],"externalId":"externalId","adBlockingConfiguration":{"overrideClickThroughUrl":True,"creativeBundleId":"creativeBundleId","clickThroughUrl":"clickThroughUrl","enabled":True},"audienceSegmentGroups":[{"name":"name","id":"id","audienceSegments":[{"allocation":6,"name":"name","id":"id"},{"allocation":6,"name":"name","id":"id"}]},{"name":"name","id":"id","audienceSegments":[{"allocation":6,"name":"name","id":"id"},{"allocation":6,"name":"name","id":"id"}]}],"advertiserId":"advertiserId","accountId":"accountId","creativeOptimizationConfiguration":{"optimizationActivitys":[{"floodlightActivityIdDimensionValue":{"kind":"kind","matchType":"EXACT","etag":"etag","id":"id","value":"value","dimensionName":"dimensionName"},"weight":0,"floodlightActivityId":"floodlightActivityId"},{"floodlightActivityIdDimensionValue":{"kind":"kind","matchType":"EXACT","etag":"etag","id":"id","value":"value","dimensionName":"dimensionName"},"weight":0,"floodlightActivityId":"floodlightActivityId"}],"optimizationModel":"CLICK","name":"name","id":"id"},"name":"name","clickThroughUrlSuffixProperties":{"overrideInheritedSuffix":True,"clickThroughUrlSuffix":"clickThroughUrlSuffix"},"comment":"comment","creativeGroupIds":["creativeGroupIds","creativeGroupIds"],"startDate":"2000-01-23"}
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
        path='/dfareporting/v3.3/userprofiles/{profile_id}/campaigns'.format(profile_id='profile_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

