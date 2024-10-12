# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_tax import AccountTax
from openapi_server.models.accounttax_custom_batch_request import AccounttaxCustomBatchRequest
from openapi_server.models.accounttax_custom_batch_response import AccounttaxCustomBatchResponse
from openapi_server.models.accounttax_list_response import AccounttaxListResponse


pytestmark = pytest.mark.asyncio

async def test_content_accounttax_custombatch(client):
    """Test case for content_accounttax_custombatch

    
    """
    body = {"entries":[{"accountId":"accountId","accountTax":{"accountId":"accountId","kind":"kind","rules":[{"ratePercent":"ratePercent","useGlobalRate":True,"country":"country","locationId":"locationId","shippingTaxed":True},{"ratePercent":"ratePercent","useGlobalRate":True,"country":"country","locationId":"locationId","shippingTaxed":True}]},"method":"method","merchantId":"merchantId","batchId":0},{"accountId":"accountId","accountTax":{"accountId":"accountId","kind":"kind","rules":[{"ratePercent":"ratePercent","useGlobalRate":True,"country":"country","locationId":"locationId","shippingTaxed":True},{"ratePercent":"ratePercent","useGlobalRate":True,"country":"country","locationId":"locationId","shippingTaxed":True}]},"method":"method","merchantId":"merchantId","batchId":0}]}
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
        path='/content/v2.1/accounttax/batch',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_accounttax_get(client):
    """Test case for content_accounttax_get

    
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
        path='/content/v2.1/{merchant_id}/accounttax/{account_id}'.format(merchant_id='merchant_id_example', account_id='account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_accounttax_list(client):
    """Test case for content_accounttax_list

    
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
        path='/content/v2.1/{merchant_id}/accounttax'.format(merchant_id='merchant_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_accounttax_update(client):
    """Test case for content_accounttax_update

    
    """
    body = {"accountId":"accountId","kind":"kind","rules":[{"ratePercent":"ratePercent","useGlobalRate":True,"country":"country","locationId":"locationId","shippingTaxed":True},{"ratePercent":"ratePercent","useGlobalRate":True,"country":"country","locationId":"locationId","shippingTaxed":True}]}
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
        path='/content/v2.1/{merchant_id}/accounttax/{account_id}'.format(merchant_id='merchant_id_example', account_id='account_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

