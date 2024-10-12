# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_return_policy_online_response import ListReturnPolicyOnlineResponse
from openapi_server.models.return_policy_online import ReturnPolicyOnline


pytestmark = pytest.mark.asyncio

async def test_content_returnpolicyonline_create(client):
    """Test case for content_returnpolicyonline_create

    
    """
    body = {"returnPolicyUri":"returnPolicyUri","returnPolicyId":"returnPolicyId","returnReasonCategoryInfo":[{"returnShippingFee":{"fixedFee":{"currency":"currency","value":"value"},"type":"TYPE_UNSPECIFIED"},"returnReasonCategory":"RETURN_REASON_CATEGORY_UNSPECIFIED","returnLabelSource":"RETURN_LABEL_SOURCE_UNSPECIFIED"},{"returnShippingFee":{"fixedFee":{"currency":"currency","value":"value"},"type":"TYPE_UNSPECIFIED"},"returnReasonCategory":"RETURN_REASON_CATEGORY_UNSPECIFIED","returnLabelSource":"RETURN_LABEL_SOURCE_UNSPECIFIED"}],"itemConditions":["ITEM_CONDITION_UNSPECIFIED","ITEM_CONDITION_UNSPECIFIED"],"name":"name","returnMethods":["RETURN_METHOD_UNSPECIFIED","RETURN_METHOD_UNSPECIFIED"],"countries":["countries","countries"],"label":"label","policy":{"days":"days","type":"TYPE_UNSPECIFIED"},"restockingFee":{"microPercent":0,"fixedFee":{"currency":"currency","value":"value"}}}
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
        path='/content/v2.1/{merchant_id}/returnpolicyonline'.format(merchant_id='merchant_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_returnpolicyonline_delete(client):
    """Test case for content_returnpolicyonline_delete

    
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
        path='/content/v2.1/{merchant_id}/returnpolicyonline/{return_policy_id}'.format(merchant_id='merchant_id_example', return_policy_id='return_policy_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_returnpolicyonline_get(client):
    """Test case for content_returnpolicyonline_get

    
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
        path='/content/v2.1/{merchant_id}/returnpolicyonline/{return_policy_id}'.format(merchant_id='merchant_id_example', return_policy_id='return_policy_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_returnpolicyonline_list(client):
    """Test case for content_returnpolicyonline_list

    
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
        path='/content/v2.1/{merchant_id}/returnpolicyonline'.format(merchant_id='merchant_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_returnpolicyonline_patch(client):
    """Test case for content_returnpolicyonline_patch

    
    """
    body = {"returnPolicyUri":"returnPolicyUri","returnPolicyId":"returnPolicyId","returnReasonCategoryInfo":[{"returnShippingFee":{"fixedFee":{"currency":"currency","value":"value"},"type":"TYPE_UNSPECIFIED"},"returnReasonCategory":"RETURN_REASON_CATEGORY_UNSPECIFIED","returnLabelSource":"RETURN_LABEL_SOURCE_UNSPECIFIED"},{"returnShippingFee":{"fixedFee":{"currency":"currency","value":"value"},"type":"TYPE_UNSPECIFIED"},"returnReasonCategory":"RETURN_REASON_CATEGORY_UNSPECIFIED","returnLabelSource":"RETURN_LABEL_SOURCE_UNSPECIFIED"}],"itemConditions":["ITEM_CONDITION_UNSPECIFIED","ITEM_CONDITION_UNSPECIFIED"],"name":"name","returnMethods":["RETURN_METHOD_UNSPECIFIED","RETURN_METHOD_UNSPECIFIED"],"countries":["countries","countries"],"label":"label","policy":{"days":"days","type":"TYPE_UNSPECIFIED"},"restockingFee":{"microPercent":0,"fixedFee":{"currency":"currency","value":"value"}}}
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
        path='/content/v2.1/{merchant_id}/returnpolicyonline/{return_policy_id}'.format(merchant_id='merchant_id_example', return_policy_id='return_policy_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

