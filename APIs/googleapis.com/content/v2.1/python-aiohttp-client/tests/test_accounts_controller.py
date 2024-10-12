# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account import Account
from openapi_server.models.account_credentials import AccountCredentials
from openapi_server.models.account_label import AccountLabel
from openapi_server.models.account_return_carrier import AccountReturnCarrier
from openapi_server.models.accounts_auth_info_response import AccountsAuthInfoResponse
from openapi_server.models.accounts_claim_website_response import AccountsClaimWebsiteResponse
from openapi_server.models.accounts_custom_batch_request import AccountsCustomBatchRequest
from openapi_server.models.accounts_custom_batch_response import AccountsCustomBatchResponse
from openapi_server.models.accounts_link_request import AccountsLinkRequest
from openapi_server.models.accounts_link_response import AccountsLinkResponse
from openapi_server.models.accounts_list_links_response import AccountsListLinksResponse
from openapi_server.models.accounts_list_response import AccountsListResponse
from openapi_server.models.accounts_update_labels_request import AccountsUpdateLabelsRequest
from openapi_server.models.accounts_update_labels_response import AccountsUpdateLabelsResponse
from openapi_server.models.list_account_labels_response import ListAccountLabelsResponse
from openapi_server.models.list_account_return_carrier_response import ListAccountReturnCarrierResponse
from openapi_server.models.request_phone_verification_request import RequestPhoneVerificationRequest
from openapi_server.models.request_phone_verification_response import RequestPhoneVerificationResponse
from openapi_server.models.verify_phone_number_request import VerifyPhoneNumberRequest
from openapi_server.models.verify_phone_number_response import VerifyPhoneNumberResponse


pytestmark = pytest.mark.asyncio

async def test_content_accounts_authinfo(client):
    """Test case for content_accounts_authinfo

    
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
        path='/content/v2.1/accounts/authinfo',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_accounts_claimwebsite(client):
    """Test case for content_accounts_claimwebsite

    
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
                    ('overwrite', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/content/v2.1/{merchant_id}/accounts/{account_id}/claimwebsite'.format(merchant_id='merchant_id_example', account_id='account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_accounts_credentials_create(client):
    """Test case for content_accounts_credentials_create

    
    """
    body = {"expiresIn":"expiresIn","purpose":"ACCOUNT_CREDENTIALS_PURPOSE_UNSPECIFIED","accessToken":"accessToken"}
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
        path='/content/v2.1/accounts/{account_id}/credentials'.format(account_id='account_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_accounts_custombatch(client):
    """Test case for content_accounts_custombatch

    
    """
    body = {"entries":[{"accountId":"accountId","linkRequest":{"linkedAccountId":"linkedAccountId","action":"action","linkType":"linkType","services":["services","services"]},"view":"view","labelIds":["labelIds","labelIds"],"method":"method","merchantId":"merchantId","force":True,"batchId":0,"overwrite":True,"account":{"kind":"kind","conversionSettings":{"freeListingsAutoTaggingEnabled":True},"automaticLabelIds":["automaticLabelIds","automaticLabelIds"],"users":[{"emailAddress":"emailAddress","reportingManager":True,"admin":True,"orderManager":True,"paymentsAnalyst":True,"paymentsManager":True},{"emailAddress":"emailAddress","reportingManager":True,"admin":True,"orderManager":True,"paymentsAnalyst":True,"paymentsManager":True}],"youtubeChannelLinks":[{"channelId":"channelId","status":"status"},{"channelId":"channelId","status":"status"}],"adultContent":True,"labelIds":["labelIds","labelIds"],"sellerId":"sellerId","businessIdentity":{"includeForPromotions":True,"smallBusiness":{"selfIdentified":True},"blackOwned":{"selfIdentified":True},"veteranOwned":{"selfIdentified":True},"womenOwned":{"selfIdentified":True},"latinoOwned":{"selfIdentified":True}},"websiteUrl":"websiteUrl","businessInformation":{"koreanBusinessRegistrationNumber":"koreanBusinessRegistrationNumber","address":{"country":"country","streetAddress":"streetAddress","postalCode":"postalCode","locality":"locality","region":"region"},"phoneNumber":"phoneNumber","phoneVerificationStatus":"phoneVerificationStatus","customerService":{"phoneNumber":"phoneNumber","email":"email","url":"url"}},"adsLinks":[{"adsId":"adsId","status":"status"},{"adsId":"adsId","status":"status"}],"cssId":"cssId","name":"name","accountManagement":"accountManagement","id":"id","googleMyBusinessLink":{"gmbEmail":"gmbEmail","gmbAccountId":"gmbAccountId","status":"status"},"automaticImprovements":{"itemUpdates":{"effectiveAllowPriceUpdates":True,"effectiveAllowStrictAvailabilityUpdates":True,"effectiveAllowConditionUpdates":True,"accountItemUpdatesSettings":{"allowConditionUpdates":True,"allowPriceUpdates":True,"allowAvailabilityUpdates":True,"allowStrictAvailabilityUpdates":True},"effectiveAllowAvailabilityUpdates":True},"shippingImprovements":{"allowShippingImprovements":True},"imageImprovements":{"accountImageImprovementsSettings":{"allowAutomaticImageImprovements":True},"effectiveAllowAutomaticImageImprovements":True}}}},{"accountId":"accountId","linkRequest":{"linkedAccountId":"linkedAccountId","action":"action","linkType":"linkType","services":["services","services"]},"view":"view","labelIds":["labelIds","labelIds"],"method":"method","merchantId":"merchantId","force":True,"batchId":0,"overwrite":True,"account":{"kind":"kind","conversionSettings":{"freeListingsAutoTaggingEnabled":True},"automaticLabelIds":["automaticLabelIds","automaticLabelIds"],"users":[{"emailAddress":"emailAddress","reportingManager":True,"admin":True,"orderManager":True,"paymentsAnalyst":True,"paymentsManager":True},{"emailAddress":"emailAddress","reportingManager":True,"admin":True,"orderManager":True,"paymentsAnalyst":True,"paymentsManager":True}],"youtubeChannelLinks":[{"channelId":"channelId","status":"status"},{"channelId":"channelId","status":"status"}],"adultContent":True,"labelIds":["labelIds","labelIds"],"sellerId":"sellerId","businessIdentity":{"includeForPromotions":True,"smallBusiness":{"selfIdentified":True},"blackOwned":{"selfIdentified":True},"veteranOwned":{"selfIdentified":True},"womenOwned":{"selfIdentified":True},"latinoOwned":{"selfIdentified":True}},"websiteUrl":"websiteUrl","businessInformation":{"koreanBusinessRegistrationNumber":"koreanBusinessRegistrationNumber","address":{"country":"country","streetAddress":"streetAddress","postalCode":"postalCode","locality":"locality","region":"region"},"phoneNumber":"phoneNumber","phoneVerificationStatus":"phoneVerificationStatus","customerService":{"phoneNumber":"phoneNumber","email":"email","url":"url"}},"adsLinks":[{"adsId":"adsId","status":"status"},{"adsId":"adsId","status":"status"}],"cssId":"cssId","name":"name","accountManagement":"accountManagement","id":"id","googleMyBusinessLink":{"gmbEmail":"gmbEmail","gmbAccountId":"gmbAccountId","status":"status"},"automaticImprovements":{"itemUpdates":{"effectiveAllowPriceUpdates":True,"effectiveAllowStrictAvailabilityUpdates":True,"effectiveAllowConditionUpdates":True,"accountItemUpdatesSettings":{"allowConditionUpdates":True,"allowPriceUpdates":True,"allowAvailabilityUpdates":True,"allowStrictAvailabilityUpdates":True},"effectiveAllowAvailabilityUpdates":True},"shippingImprovements":{"allowShippingImprovements":True},"imageImprovements":{"accountImageImprovementsSettings":{"allowAutomaticImageImprovements":True},"effectiveAllowAutomaticImageImprovements":True}}}}]}
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
        path='/content/v2.1/accounts/batch',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_accounts_delete(client):
    """Test case for content_accounts_delete

    
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
                    ('force', True)]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/content/v2.1/{merchant_id}/accounts/{account_id}'.format(merchant_id='merchant_id_example', account_id='account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_accounts_get(client):
    """Test case for content_accounts_get

    
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
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/content/v2.1/{merchant_id}/accounts/{account_id}'.format(merchant_id='merchant_id_example', account_id='account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_accounts_insert(client):
    """Test case for content_accounts_insert

    
    """
    body = {"kind":"kind","conversionSettings":{"freeListingsAutoTaggingEnabled":True},"automaticLabelIds":["automaticLabelIds","automaticLabelIds"],"users":[{"emailAddress":"emailAddress","reportingManager":True,"admin":True,"orderManager":True,"paymentsAnalyst":True,"paymentsManager":True},{"emailAddress":"emailAddress","reportingManager":True,"admin":True,"orderManager":True,"paymentsAnalyst":True,"paymentsManager":True}],"youtubeChannelLinks":[{"channelId":"channelId","status":"status"},{"channelId":"channelId","status":"status"}],"adultContent":True,"labelIds":["labelIds","labelIds"],"sellerId":"sellerId","businessIdentity":{"includeForPromotions":True,"smallBusiness":{"selfIdentified":True},"blackOwned":{"selfIdentified":True},"veteranOwned":{"selfIdentified":True},"womenOwned":{"selfIdentified":True},"latinoOwned":{"selfIdentified":True}},"websiteUrl":"websiteUrl","businessInformation":{"koreanBusinessRegistrationNumber":"koreanBusinessRegistrationNumber","address":{"country":"country","streetAddress":"streetAddress","postalCode":"postalCode","locality":"locality","region":"region"},"phoneNumber":"phoneNumber","phoneVerificationStatus":"phoneVerificationStatus","customerService":{"phoneNumber":"phoneNumber","email":"email","url":"url"}},"adsLinks":[{"adsId":"adsId","status":"status"},{"adsId":"adsId","status":"status"}],"cssId":"cssId","name":"name","accountManagement":"accountManagement","id":"id","googleMyBusinessLink":{"gmbEmail":"gmbEmail","gmbAccountId":"gmbAccountId","status":"status"},"automaticImprovements":{"itemUpdates":{"effectiveAllowPriceUpdates":True,"effectiveAllowStrictAvailabilityUpdates":True,"effectiveAllowConditionUpdates":True,"accountItemUpdatesSettings":{"allowConditionUpdates":True,"allowPriceUpdates":True,"allowAvailabilityUpdates":True,"allowStrictAvailabilityUpdates":True},"effectiveAllowAvailabilityUpdates":True},"shippingImprovements":{"allowShippingImprovements":True},"imageImprovements":{"accountImageImprovementsSettings":{"allowAutomaticImageImprovements":True},"effectiveAllowAutomaticImageImprovements":True}}}
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
        path='/content/v2.1/{merchant_id}/accounts'.format(merchant_id='merchant_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_accounts_labels_create(client):
    """Test case for content_accounts_labels_create

    
    """
    body = {"accountId":"accountId","labelId":"labelId","labelType":"LABEL_TYPE_UNSPECIFIED","name":"name","description":"description"}
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
        path='/content/v2.1/accounts/{account_id}/labels'.format(account_id='account_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_accounts_labels_delete(client):
    """Test case for content_accounts_labels_delete

    
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
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/content/v2.1/accounts/{account_id}/labels/{label_id}'.format(account_id='account_id_example', label_id='label_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_accounts_labels_list(client):
    """Test case for content_accounts_labels_list

    
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
        path='/content/v2.1/accounts/{account_id}/labels'.format(account_id='account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_accounts_labels_patch(client):
    """Test case for content_accounts_labels_patch

    
    """
    body = {"accountId":"accountId","labelId":"labelId","labelType":"LABEL_TYPE_UNSPECIFIED","name":"name","description":"description"}
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
        method='PATCH',
        path='/content/v2.1/accounts/{account_id}/labels/{label_id}'.format(account_id='account_id_example', label_id='label_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_accounts_link(client):
    """Test case for content_accounts_link

    
    """
    body = {"linkedAccountId":"linkedAccountId","eCommercePlatformLinkInfo":{"externalAccountId":"externalAccountId"},"action":"action","linkType":"linkType","services":["services","services"],"paymentServiceProviderLinkInfo":{"externalAccountId":"externalAccountId","externalAccountBusinessCountry":"externalAccountBusinessCountry"}}
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
        path='/content/v2.1/{merchant_id}/accounts/{account_id}/link'.format(merchant_id='merchant_id_example', account_id='account_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_accounts_list(client):
    """Test case for content_accounts_list

    
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
                    ('label', 'label_example'),
                    ('maxResults', 56),
                    ('name', 'name_example'),
                    ('pageToken', 'page_token_example'),
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/content/v2.1/{merchant_id}/accounts'.format(merchant_id='merchant_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_accounts_listlinks(client):
    """Test case for content_accounts_listlinks

    
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
                    ('maxResults', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/content/v2.1/{merchant_id}/accounts/{account_id}/listlinks'.format(merchant_id='merchant_id_example', account_id='account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_accounts_requestphoneverification(client):
    """Test case for content_accounts_requestphoneverification

    
    """
    body = {"phoneRegionCode":"phoneRegionCode","phoneNumber":"phoneNumber","phoneVerificationMethod":"PHONE_VERIFICATION_METHOD_UNSPECIFIED","languageCode":"languageCode"}
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
        path='/content/v2.1/{merchant_id}/accounts/{account_id}/requestphoneverification'.format(merchant_id='merchant_id_example', account_id='account_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_accounts_returncarrier_create(client):
    """Test case for content_accounts_returncarrier_create

    
    """
    body = {"carrierAccountId":"carrierAccountId","carrierCode":"CARRIER_CODE_UNSPECIFIED","carrierAccountNumber":"carrierAccountNumber","carrierAccountName":"carrierAccountName"}
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
        path='/content/v2.1/accounts/{account_id}/returncarrier'.format(account_id='account_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_accounts_returncarrier_delete(client):
    """Test case for content_accounts_returncarrier_delete

    
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
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/content/v2.1/accounts/{account_id}/returncarrier/{carrier_account_id}'.format(account_id='account_id_example', carrier_account_id='carrier_account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_accounts_returncarrier_list(client):
    """Test case for content_accounts_returncarrier_list

    
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
        path='/content/v2.1/accounts/{account_id}/returncarrier'.format(account_id='account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_accounts_returncarrier_patch(client):
    """Test case for content_accounts_returncarrier_patch

    
    """
    body = {"carrierAccountId":"carrierAccountId","carrierCode":"CARRIER_CODE_UNSPECIFIED","carrierAccountNumber":"carrierAccountNumber","carrierAccountName":"carrierAccountName"}
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
        method='PATCH',
        path='/content/v2.1/accounts/{account_id}/returncarrier/{carrier_account_id}'.format(account_id='account_id_example', carrier_account_id='carrier_account_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_accounts_update(client):
    """Test case for content_accounts_update

    
    """
    body = {"kind":"kind","conversionSettings":{"freeListingsAutoTaggingEnabled":True},"automaticLabelIds":["automaticLabelIds","automaticLabelIds"],"users":[{"emailAddress":"emailAddress","reportingManager":True,"admin":True,"orderManager":True,"paymentsAnalyst":True,"paymentsManager":True},{"emailAddress":"emailAddress","reportingManager":True,"admin":True,"orderManager":True,"paymentsAnalyst":True,"paymentsManager":True}],"youtubeChannelLinks":[{"channelId":"channelId","status":"status"},{"channelId":"channelId","status":"status"}],"adultContent":True,"labelIds":["labelIds","labelIds"],"sellerId":"sellerId","businessIdentity":{"includeForPromotions":True,"smallBusiness":{"selfIdentified":True},"blackOwned":{"selfIdentified":True},"veteranOwned":{"selfIdentified":True},"womenOwned":{"selfIdentified":True},"latinoOwned":{"selfIdentified":True}},"websiteUrl":"websiteUrl","businessInformation":{"koreanBusinessRegistrationNumber":"koreanBusinessRegistrationNumber","address":{"country":"country","streetAddress":"streetAddress","postalCode":"postalCode","locality":"locality","region":"region"},"phoneNumber":"phoneNumber","phoneVerificationStatus":"phoneVerificationStatus","customerService":{"phoneNumber":"phoneNumber","email":"email","url":"url"}},"adsLinks":[{"adsId":"adsId","status":"status"},{"adsId":"adsId","status":"status"}],"cssId":"cssId","name":"name","accountManagement":"accountManagement","id":"id","googleMyBusinessLink":{"gmbEmail":"gmbEmail","gmbAccountId":"gmbAccountId","status":"status"},"automaticImprovements":{"itemUpdates":{"effectiveAllowPriceUpdates":True,"effectiveAllowStrictAvailabilityUpdates":True,"effectiveAllowConditionUpdates":True,"accountItemUpdatesSettings":{"allowConditionUpdates":True,"allowPriceUpdates":True,"allowAvailabilityUpdates":True,"allowStrictAvailabilityUpdates":True},"effectiveAllowAvailabilityUpdates":True},"shippingImprovements":{"allowShippingImprovements":True},"imageImprovements":{"accountImageImprovementsSettings":{"allowAutomaticImageImprovements":True},"effectiveAllowAutomaticImageImprovements":True}}}
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
        path='/content/v2.1/{merchant_id}/accounts/{account_id}'.format(merchant_id='merchant_id_example', account_id='account_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_accounts_updatelabels(client):
    """Test case for content_accounts_updatelabels

    
    """
    body = {"labelIds":["labelIds","labelIds"]}
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
        path='/content/v2.1/{merchant_id}/accounts/{account_id}/updatelabels'.format(merchant_id='merchant_id_example', account_id='account_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_accounts_verifyphonenumber(client):
    """Test case for content_accounts_verifyphonenumber

    
    """
    body = {"phoneVerificationMethod":"PHONE_VERIFICATION_METHOD_UNSPECIFIED","verificationId":"verificationId","verificationCode":"verificationCode"}
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
        path='/content/v2.1/{merchant_id}/accounts/{account_id}/verifyphonenumber'.format(merchant_id='merchant_id_example', account_id='account_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

