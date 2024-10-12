# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account import Account
from openapi_server.models.accounts_auth_info_response import AccountsAuthInfoResponse
from openapi_server.models.accounts_claim_website_response import AccountsClaimWebsiteResponse
from openapi_server.models.accounts_custom_batch_request import AccountsCustomBatchRequest
from openapi_server.models.accounts_custom_batch_response import AccountsCustomBatchResponse
from openapi_server.models.accounts_link_request import AccountsLinkRequest
from openapi_server.models.accounts_link_response import AccountsLinkResponse
from openapi_server.models.accounts_list_response import AccountsListResponse


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
        path='/content/v2/accounts/authinfo',
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
        path='/content/v2/{merchant_id}/accounts/{account_id}/claimwebsite'.format(merchant_id='merchant_id_example', account_id='account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_accounts_custombatch(client):
    """Test case for content_accounts_custombatch

    
    """
    body = {"entries":[{"accountId":"accountId","linkRequest":{"linkedAccountId":"linkedAccountId","action":"action","linkType":"linkType"},"labelIds":["labelIds","labelIds"],"method":"method","merchantId":"merchantId","force":True,"batchId":0,"overwrite":True,"account":{"youtubeChannelLinks":[{"channelId":"channelId","status":"status"},{"channelId":"channelId","status":"status"}],"adultContent":True,"sellerId":"sellerId","websiteUrl":"websiteUrl","businessInformation":{"koreanBusinessRegistrationNumber":"koreanBusinessRegistrationNumber","address":{"country":"country","streetAddress":"streetAddress","postalCode":"postalCode","locality":"locality","region":"region"},"phoneNumber":"phoneNumber","customerService":{"phoneNumber":"phoneNumber","email":"email","url":"url"}},"kind":"kind","name":"name","adwordsLinks":[{"adwordsId":"adwordsId","status":"status"},{"adwordsId":"adwordsId","status":"status"}],"id":"id","googleMyBusinessLink":{"gmbEmail":"gmbEmail","status":"status"},"reviewsUrl":"reviewsUrl","users":[{"emailAddress":"emailAddress","admin":True,"orderManager":True,"paymentsAnalyst":True,"paymentsManager":True},{"emailAddress":"emailAddress","admin":True,"orderManager":True,"paymentsAnalyst":True,"paymentsManager":True}]}},{"accountId":"accountId","linkRequest":{"linkedAccountId":"linkedAccountId","action":"action","linkType":"linkType"},"labelIds":["labelIds","labelIds"],"method":"method","merchantId":"merchantId","force":True,"batchId":0,"overwrite":True,"account":{"youtubeChannelLinks":[{"channelId":"channelId","status":"status"},{"channelId":"channelId","status":"status"}],"adultContent":True,"sellerId":"sellerId","websiteUrl":"websiteUrl","businessInformation":{"koreanBusinessRegistrationNumber":"koreanBusinessRegistrationNumber","address":{"country":"country","streetAddress":"streetAddress","postalCode":"postalCode","locality":"locality","region":"region"},"phoneNumber":"phoneNumber","customerService":{"phoneNumber":"phoneNumber","email":"email","url":"url"}},"kind":"kind","name":"name","adwordsLinks":[{"adwordsId":"adwordsId","status":"status"},{"adwordsId":"adwordsId","status":"status"}],"id":"id","googleMyBusinessLink":{"gmbEmail":"gmbEmail","status":"status"},"reviewsUrl":"reviewsUrl","users":[{"emailAddress":"emailAddress","admin":True,"orderManager":True,"paymentsAnalyst":True,"paymentsManager":True},{"emailAddress":"emailAddress","admin":True,"orderManager":True,"paymentsAnalyst":True,"paymentsManager":True}]}}]}
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
                    ('dryRun', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/content/v2/accounts/batch',
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
                    ('dryRun', True),
                    ('force', True)]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/content/v2/{merchant_id}/accounts/{account_id}'.format(merchant_id='merchant_id_example', account_id='account_id_example'),
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
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/content/v2/{merchant_id}/accounts/{account_id}'.format(merchant_id='merchant_id_example', account_id='account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_accounts_insert(client):
    """Test case for content_accounts_insert

    
    """
    body = {"youtubeChannelLinks":[{"channelId":"channelId","status":"status"},{"channelId":"channelId","status":"status"}],"adultContent":True,"sellerId":"sellerId","websiteUrl":"websiteUrl","businessInformation":{"koreanBusinessRegistrationNumber":"koreanBusinessRegistrationNumber","address":{"country":"country","streetAddress":"streetAddress","postalCode":"postalCode","locality":"locality","region":"region"},"phoneNumber":"phoneNumber","customerService":{"phoneNumber":"phoneNumber","email":"email","url":"url"}},"kind":"kind","name":"name","adwordsLinks":[{"adwordsId":"adwordsId","status":"status"},{"adwordsId":"adwordsId","status":"status"}],"id":"id","googleMyBusinessLink":{"gmbEmail":"gmbEmail","status":"status"},"reviewsUrl":"reviewsUrl","users":[{"emailAddress":"emailAddress","admin":True,"orderManager":True,"paymentsAnalyst":True,"paymentsManager":True},{"emailAddress":"emailAddress","admin":True,"orderManager":True,"paymentsAnalyst":True,"paymentsManager":True}]}
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
                    ('dryRun', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/content/v2/{merchant_id}/accounts'.format(merchant_id='merchant_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_accounts_link(client):
    """Test case for content_accounts_link

    
    """
    body = {"linkedAccountId":"linkedAccountId","action":"action","linkType":"linkType"}
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
        path='/content/v2/{merchant_id}/accounts/{account_id}/link'.format(merchant_id='merchant_id_example', account_id='account_id_example'),
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
                    ('maxResults', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/content/v2/{merchant_id}/accounts'.format(merchant_id='merchant_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_accounts_update(client):
    """Test case for content_accounts_update

    
    """
    body = {"youtubeChannelLinks":[{"channelId":"channelId","status":"status"},{"channelId":"channelId","status":"status"}],"adultContent":True,"sellerId":"sellerId","websiteUrl":"websiteUrl","businessInformation":{"koreanBusinessRegistrationNumber":"koreanBusinessRegistrationNumber","address":{"country":"country","streetAddress":"streetAddress","postalCode":"postalCode","locality":"locality","region":"region"},"phoneNumber":"phoneNumber","customerService":{"phoneNumber":"phoneNumber","email":"email","url":"url"}},"kind":"kind","name":"name","adwordsLinks":[{"adwordsId":"adwordsId","status":"status"},{"adwordsId":"adwordsId","status":"status"}],"id":"id","googleMyBusinessLink":{"gmbEmail":"gmbEmail","status":"status"},"reviewsUrl":"reviewsUrl","users":[{"emailAddress":"emailAddress","admin":True,"orderManager":True,"paymentsAnalyst":True,"paymentsManager":True},{"emailAddress":"emailAddress","admin":True,"orderManager":True,"paymentsAnalyst":True,"paymentsManager":True}]}
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
                    ('dryRun', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/content/v2/{merchant_id}/accounts/{account_id}'.format(merchant_id='merchant_id_example', account_id='account_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

