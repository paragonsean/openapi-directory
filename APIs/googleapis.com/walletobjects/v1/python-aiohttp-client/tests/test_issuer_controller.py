# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.issuer import Issuer
from openapi_server.models.issuer_list_response import IssuerListResponse


pytestmark = pytest.mark.asyncio

async def test_walletobjects_issuer_get(client):
    """Test case for walletobjects_issuer_get

    
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
        path='/walletobjects/v1/issuer/{resource_id}'.format(resource_id='resource_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_walletobjects_issuer_insert(client):
    """Test case for walletobjects_issuer_insert

    
    """
    body = {"issuerId":"issuerId","contactInfo":{"alertsEmails":["alertsEmails","alertsEmails"],"phone":"phone","name":"name","email":"email"},"homepageUrl":"homepageUrl","name":"name","callbackOptions":{"updateRequestUrl":"updateRequestUrl","url":"url"},"smartTapMerchantData":{"smartTapMerchantId":"smartTapMerchantId","authenticationKeys":[{"publicKeyPem":"publicKeyPem","id":0},{"publicKeyPem":"publicKeyPem","id":0}]}}
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
        path='/walletobjects/v1/issuer',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_walletobjects_issuer_list(client):
    """Test case for walletobjects_issuer_list

    
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
        path='/walletobjects/v1/issuer',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_walletobjects_issuer_patch(client):
    """Test case for walletobjects_issuer_patch

    
    """
    body = {"issuerId":"issuerId","contactInfo":{"alertsEmails":["alertsEmails","alertsEmails"],"phone":"phone","name":"name","email":"email"},"homepageUrl":"homepageUrl","name":"name","callbackOptions":{"updateRequestUrl":"updateRequestUrl","url":"url"},"smartTapMerchantData":{"smartTapMerchantId":"smartTapMerchantId","authenticationKeys":[{"publicKeyPem":"publicKeyPem","id":0},{"publicKeyPem":"publicKeyPem","id":0}]}}
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
        path='/walletobjects/v1/issuer/{resource_id}'.format(resource_id='resource_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_walletobjects_issuer_update(client):
    """Test case for walletobjects_issuer_update

    
    """
    body = {"issuerId":"issuerId","contactInfo":{"alertsEmails":["alertsEmails","alertsEmails"],"phone":"phone","name":"name","email":"email"},"homepageUrl":"homepageUrl","name":"name","callbackOptions":{"updateRequestUrl":"updateRequestUrl","url":"url"},"smartTapMerchantData":{"smartTapMerchantId":"smartTapMerchantId","authenticationKeys":[{"publicKeyPem":"publicKeyPem","id":0},{"publicKeyPem":"publicKeyPem","id":0}]}}
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
        path='/walletobjects/v1/issuer/{resource_id}'.format(resource_id='resource_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

