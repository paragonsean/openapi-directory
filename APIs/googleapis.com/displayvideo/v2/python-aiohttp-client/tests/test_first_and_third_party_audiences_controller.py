# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.edit_customer_match_members_request import EditCustomerMatchMembersRequest
from openapi_server.models.edit_customer_match_members_response import EditCustomerMatchMembersResponse
from openapi_server.models.first_and_third_party_audience import FirstAndThirdPartyAudience
from openapi_server.models.list_first_and_third_party_audiences_response import ListFirstAndThirdPartyAudiencesResponse


pytestmark = pytest.mark.asyncio

async def test_displayvideo_first_and_third_party_audiences_create(client):
    """Test case for displayvideo_first_and_third_party_audiences_create

    
    """
    body = {"activeDisplayAudienceSize":"activeDisplayAudienceSize","displayMobileAppAudienceSize":"displayMobileAppAudienceSize","firstAndThirdPartyAudienceType":"FIRST_AND_THIRD_PARTY_AUDIENCE_TYPE_UNSPECIFIED","gmailAudienceSize":"gmailAudienceSize","audienceSource":"AUDIENCE_SOURCE_UNSPECIFIED","mobileDeviceIdList":{"mobileDeviceIds":["mobileDeviceIds","mobileDeviceIds"],"consent":{"adUserData":"CONSENT_STATUS_UNSPECIFIED","adPersonalization":"CONSENT_STATUS_UNSPECIFIED"}},"displayName":"displayName","description":"description","appId":"appId","firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","membershipDurationDays":"membershipDurationDays","name":"name","youtubeAudienceSize":"youtubeAudienceSize","displayDesktopAudienceSize":"displayDesktopAudienceSize","audienceType":"AUDIENCE_TYPE_UNSPECIFIED","contactInfoList":{"contactInfos":[{"hashedFirstName":"hashedFirstName","zipCodes":["zipCodes","zipCodes"],"countryCode":"countryCode","hashedLastName":"hashedLastName","hashedEmails":["hashedEmails","hashedEmails"],"hashedPhoneNumbers":["hashedPhoneNumbers","hashedPhoneNumbers"]},{"hashedFirstName":"hashedFirstName","zipCodes":["zipCodes","zipCodes"],"countryCode":"countryCode","hashedLastName":"hashedLastName","hashedEmails":["hashedEmails","hashedEmails"],"hashedPhoneNumbers":["hashedPhoneNumbers","hashedPhoneNumbers"]}],"consent":{"adUserData":"CONSENT_STATUS_UNSPECIFIED","adPersonalization":"CONSENT_STATUS_UNSPECIFIED"}},"displayMobileWebAudienceSize":"displayMobileWebAudienceSize","displayAudienceSize":"displayAudienceSize"}
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
        path='/v2/firstAndThirdPartyAudiences',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_first_and_third_party_audiences_edit_customer_match_members(client):
    """Test case for displayvideo_first_and_third_party_audiences_edit_customer_match_members

    
    """
    body = {"addedMobileDeviceIdList":{"mobileDeviceIds":["mobileDeviceIds","mobileDeviceIds"],"consent":{"adUserData":"CONSENT_STATUS_UNSPECIFIED","adPersonalization":"CONSENT_STATUS_UNSPECIFIED"}},"removedMobileDeviceIdList":{"mobileDeviceIds":["mobileDeviceIds","mobileDeviceIds"],"consent":{"adUserData":"CONSENT_STATUS_UNSPECIFIED","adPersonalization":"CONSENT_STATUS_UNSPECIFIED"}},"addedContactInfoList":{"contactInfos":[{"hashedFirstName":"hashedFirstName","zipCodes":["zipCodes","zipCodes"],"countryCode":"countryCode","hashedLastName":"hashedLastName","hashedEmails":["hashedEmails","hashedEmails"],"hashedPhoneNumbers":["hashedPhoneNumbers","hashedPhoneNumbers"]},{"hashedFirstName":"hashedFirstName","zipCodes":["zipCodes","zipCodes"],"countryCode":"countryCode","hashedLastName":"hashedLastName","hashedEmails":["hashedEmails","hashedEmails"],"hashedPhoneNumbers":["hashedPhoneNumbers","hashedPhoneNumbers"]}],"consent":{"adUserData":"CONSENT_STATUS_UNSPECIFIED","adPersonalization":"CONSENT_STATUS_UNSPECIFIED"}},"removedContactInfoList":{"contactInfos":[{"hashedFirstName":"hashedFirstName","zipCodes":["zipCodes","zipCodes"],"countryCode":"countryCode","hashedLastName":"hashedLastName","hashedEmails":["hashedEmails","hashedEmails"],"hashedPhoneNumbers":["hashedPhoneNumbers","hashedPhoneNumbers"]},{"hashedFirstName":"hashedFirstName","zipCodes":["zipCodes","zipCodes"],"countryCode":"countryCode","hashedLastName":"hashedLastName","hashedEmails":["hashedEmails","hashedEmails"],"hashedPhoneNumbers":["hashedPhoneNumbers","hashedPhoneNumbers"]}],"consent":{"adUserData":"CONSENT_STATUS_UNSPECIFIED","adPersonalization":"CONSENT_STATUS_UNSPECIFIED"}},"advertiserId":"advertiserId"}
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
        path='/v2/firstAndThirdPartyAudiences/{first_and_third_party_audience_idedit_customer_match_member}'.format(first_and_third_party_audience_id='first_and_third_party_audience_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_first_and_third_party_audiences_get(client):
    """Test case for displayvideo_first_and_third_party_audiences_get

    
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
                    ('partnerId', 'partner_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/firstAndThirdPartyAudiences/{first_and_third_party_audience_id}'.format(first_and_third_party_audience_id='first_and_third_party_audience_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_first_and_third_party_audiences_list(client):
    """Test case for displayvideo_first_and_third_party_audiences_list

    
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
                    ('pageToken', 'page_token_example'),
                    ('partnerId', 'partner_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/firstAndThirdPartyAudiences',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_first_and_third_party_audiences_patch(client):
    """Test case for displayvideo_first_and_third_party_audiences_patch

    
    """
    body = {"activeDisplayAudienceSize":"activeDisplayAudienceSize","displayMobileAppAudienceSize":"displayMobileAppAudienceSize","firstAndThirdPartyAudienceType":"FIRST_AND_THIRD_PARTY_AUDIENCE_TYPE_UNSPECIFIED","gmailAudienceSize":"gmailAudienceSize","audienceSource":"AUDIENCE_SOURCE_UNSPECIFIED","mobileDeviceIdList":{"mobileDeviceIds":["mobileDeviceIds","mobileDeviceIds"],"consent":{"adUserData":"CONSENT_STATUS_UNSPECIFIED","adPersonalization":"CONSENT_STATUS_UNSPECIFIED"}},"displayName":"displayName","description":"description","appId":"appId","firstAndThirdPartyAudienceId":"firstAndThirdPartyAudienceId","membershipDurationDays":"membershipDurationDays","name":"name","youtubeAudienceSize":"youtubeAudienceSize","displayDesktopAudienceSize":"displayDesktopAudienceSize","audienceType":"AUDIENCE_TYPE_UNSPECIFIED","contactInfoList":{"contactInfos":[{"hashedFirstName":"hashedFirstName","zipCodes":["zipCodes","zipCodes"],"countryCode":"countryCode","hashedLastName":"hashedLastName","hashedEmails":["hashedEmails","hashedEmails"],"hashedPhoneNumbers":["hashedPhoneNumbers","hashedPhoneNumbers"]},{"hashedFirstName":"hashedFirstName","zipCodes":["zipCodes","zipCodes"],"countryCode":"countryCode","hashedLastName":"hashedLastName","hashedEmails":["hashedEmails","hashedEmails"],"hashedPhoneNumbers":["hashedPhoneNumbers","hashedPhoneNumbers"]}],"consent":{"adUserData":"CONSENT_STATUS_UNSPECIFIED","adPersonalization":"CONSENT_STATUS_UNSPECIFIED"}},"displayMobileWebAudienceSize":"displayMobileWebAudienceSize","displayAudienceSize":"displayAudienceSize"}
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
        path='/v2/firstAndThirdPartyAudiences/{first_and_third_party_audience_id}'.format(first_and_third_party_audience_id='first_and_third_party_audience_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

