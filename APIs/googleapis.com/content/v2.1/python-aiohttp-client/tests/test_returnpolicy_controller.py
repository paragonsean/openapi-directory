# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.return_policy import ReturnPolicy
from openapi_server.models.returnpolicy_custom_batch_request import ReturnpolicyCustomBatchRequest
from openapi_server.models.returnpolicy_custom_batch_response import ReturnpolicyCustomBatchResponse
from openapi_server.models.returnpolicy_list_response import ReturnpolicyListResponse


pytestmark = pytest.mark.asyncio

async def test_content_returnpolicy_custombatch(client):
    """Test case for content_returnpolicy_custombatch

    
    """
    body = {"entries":[{"method":"method","returnPolicyId":"returnPolicyId","merchantId":"merchantId","returnPolicy":{"country":"country","nonFreeReturnReasons":["nonFreeReturnReasons","nonFreeReturnReasons"],"returnPolicyId":"returnPolicyId","kind":"kind","returnShippingFee":{"currency":"currency","value":"value"},"name":"name","label":"label","policy":{"lastReturnDate":"lastReturnDate","numberOfDays":"numberOfDays","type":"type"},"seasonalOverrides":[{"endDate":"endDate","name":"name","startDate":"startDate","policy":{"lastReturnDate":"lastReturnDate","numberOfDays":"numberOfDays","type":"type"}},{"endDate":"endDate","name":"name","startDate":"startDate","policy":{"lastReturnDate":"lastReturnDate","numberOfDays":"numberOfDays","type":"type"}}]},"batchId":0},{"method":"method","returnPolicyId":"returnPolicyId","merchantId":"merchantId","returnPolicy":{"country":"country","nonFreeReturnReasons":["nonFreeReturnReasons","nonFreeReturnReasons"],"returnPolicyId":"returnPolicyId","kind":"kind","returnShippingFee":{"currency":"currency","value":"value"},"name":"name","label":"label","policy":{"lastReturnDate":"lastReturnDate","numberOfDays":"numberOfDays","type":"type"},"seasonalOverrides":[{"endDate":"endDate","name":"name","startDate":"startDate","policy":{"lastReturnDate":"lastReturnDate","numberOfDays":"numberOfDays","type":"type"}},{"endDate":"endDate","name":"name","startDate":"startDate","policy":{"lastReturnDate":"lastReturnDate","numberOfDays":"numberOfDays","type":"type"}}]},"batchId":0}]}
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
        path='/content/v2.1/returnpolicy/batch',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_returnpolicy_delete(client):
    """Test case for content_returnpolicy_delete

    
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
        path='/content/v2.1/{merchant_id}/returnpolicy/{return_policy_id}'.format(merchant_id='merchant_id_example', return_policy_id='return_policy_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_returnpolicy_get(client):
    """Test case for content_returnpolicy_get

    
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
        path='/content/v2.1/{merchant_id}/returnpolicy/{return_policy_id}'.format(merchant_id='merchant_id_example', return_policy_id='return_policy_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_returnpolicy_insert(client):
    """Test case for content_returnpolicy_insert

    
    """
    body = {"country":"country","nonFreeReturnReasons":["nonFreeReturnReasons","nonFreeReturnReasons"],"returnPolicyId":"returnPolicyId","kind":"kind","returnShippingFee":{"currency":"currency","value":"value"},"name":"name","label":"label","policy":{"lastReturnDate":"lastReturnDate","numberOfDays":"numberOfDays","type":"type"},"seasonalOverrides":[{"endDate":"endDate","name":"name","startDate":"startDate","policy":{"lastReturnDate":"lastReturnDate","numberOfDays":"numberOfDays","type":"type"}},{"endDate":"endDate","name":"name","startDate":"startDate","policy":{"lastReturnDate":"lastReturnDate","numberOfDays":"numberOfDays","type":"type"}}]}
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
        path='/content/v2.1/{merchant_id}/returnpolicy'.format(merchant_id='merchant_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_returnpolicy_list(client):
    """Test case for content_returnpolicy_list

    
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
        path='/content/v2.1/{merchant_id}/returnpolicy'.format(merchant_id='merchant_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

