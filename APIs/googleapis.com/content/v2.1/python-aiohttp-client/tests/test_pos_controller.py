# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.pos_custom_batch_request import PosCustomBatchRequest
from openapi_server.models.pos_custom_batch_response import PosCustomBatchResponse
from openapi_server.models.pos_inventory_request import PosInventoryRequest
from openapi_server.models.pos_inventory_response import PosInventoryResponse
from openapi_server.models.pos_list_response import PosListResponse
from openapi_server.models.pos_sale_request import PosSaleRequest
from openapi_server.models.pos_sale_response import PosSaleResponse
from openapi_server.models.pos_store import PosStore


pytestmark = pytest.mark.asyncio

async def test_content_pos_custombatch(client):
    """Test case for content_pos_custombatch

    
    """
    body = {"entries":[{"sale":{"itemId":"itemId","gtin":"gtin","quantity":"quantity","saleId":"saleId","kind":"kind","price":{"currency":"currency","value":"value"},"contentLanguage":"contentLanguage","storeCode":"storeCode","targetCountry":"targetCountry","timestamp":"timestamp"},"targetMerchantId":"targetMerchantId","method":"method","merchantId":"merchantId","store":{"phoneNumber":"phoneNumber","matchingStatusHint":"matchingStatusHint","storeAddress":"storeAddress","websiteUrl":"websiteUrl","kind":"kind","gcidCategory":["gcidCategory","gcidCategory"],"placeId":"placeId","storeName":"storeName","matchingStatus":"matchingStatus","storeCode":"storeCode"},"batchId":0,"inventory":{"itemId":"itemId","gtin":"gtin","quantity":"quantity","kind":"kind","price":{"currency":"currency","value":"value"},"contentLanguage":"contentLanguage","pickupMethod":"pickupMethod","pickupSla":"pickupSla","storeCode":"storeCode","targetCountry":"targetCountry","timestamp":"timestamp"},"storeCode":"storeCode"},{"sale":{"itemId":"itemId","gtin":"gtin","quantity":"quantity","saleId":"saleId","kind":"kind","price":{"currency":"currency","value":"value"},"contentLanguage":"contentLanguage","storeCode":"storeCode","targetCountry":"targetCountry","timestamp":"timestamp"},"targetMerchantId":"targetMerchantId","method":"method","merchantId":"merchantId","store":{"phoneNumber":"phoneNumber","matchingStatusHint":"matchingStatusHint","storeAddress":"storeAddress","websiteUrl":"websiteUrl","kind":"kind","gcidCategory":["gcidCategory","gcidCategory"],"placeId":"placeId","storeName":"storeName","matchingStatus":"matchingStatus","storeCode":"storeCode"},"batchId":0,"inventory":{"itemId":"itemId","gtin":"gtin","quantity":"quantity","kind":"kind","price":{"currency":"currency","value":"value"},"contentLanguage":"contentLanguage","pickupMethod":"pickupMethod","pickupSla":"pickupSla","storeCode":"storeCode","targetCountry":"targetCountry","timestamp":"timestamp"},"storeCode":"storeCode"}]}
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
        path='/content/v2.1/pos/batch',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_pos_delete(client):
    """Test case for content_pos_delete

    
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
        path='/content/v2.1/{merchant_id}/pos/{target_merchant_id}/store/{store_code}'.format(merchant_id='merchant_id_example', target_merchant_id='target_merchant_id_example', store_code='store_code_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_pos_get(client):
    """Test case for content_pos_get

    
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
        path='/content/v2.1/{merchant_id}/pos/{target_merchant_id}/store/{store_code}'.format(merchant_id='merchant_id_example', target_merchant_id='target_merchant_id_example', store_code='store_code_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_pos_insert(client):
    """Test case for content_pos_insert

    
    """
    body = {"phoneNumber":"phoneNumber","matchingStatusHint":"matchingStatusHint","storeAddress":"storeAddress","websiteUrl":"websiteUrl","kind":"kind","gcidCategory":["gcidCategory","gcidCategory"],"placeId":"placeId","storeName":"storeName","matchingStatus":"matchingStatus","storeCode":"storeCode"}
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
        path='/content/v2.1/{merchant_id}/pos/{target_merchant_id}/store'.format(merchant_id='merchant_id_example', target_merchant_id='target_merchant_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_pos_inventory(client):
    """Test case for content_pos_inventory

    
    """
    body = {"itemId":"itemId","gtin":"gtin","quantity":"quantity","price":{"currency":"currency","value":"value"},"contentLanguage":"contentLanguage","pickupMethod":"pickupMethod","pickupSla":"pickupSla","storeCode":"storeCode","targetCountry":"targetCountry","timestamp":"timestamp"}
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
        path='/content/v2.1/{merchant_id}/pos/{target_merchant_id}/inventory'.format(merchant_id='merchant_id_example', target_merchant_id='target_merchant_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_pos_list(client):
    """Test case for content_pos_list

    
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
        path='/content/v2.1/{merchant_id}/pos/{target_merchant_id}/store'.format(merchant_id='merchant_id_example', target_merchant_id='target_merchant_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_pos_sale(client):
    """Test case for content_pos_sale

    
    """
    body = {"itemId":"itemId","gtin":"gtin","quantity":"quantity","saleId":"saleId","price":{"currency":"currency","value":"value"},"contentLanguage":"contentLanguage","storeCode":"storeCode","targetCountry":"targetCountry","timestamp":"timestamp"}
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
        path='/content/v2.1/{merchant_id}/pos/{target_merchant_id}/sale'.format(merchant_id='merchant_id_example', target_merchant_id='target_merchant_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

