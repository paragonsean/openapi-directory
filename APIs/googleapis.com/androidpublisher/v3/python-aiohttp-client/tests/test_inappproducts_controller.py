# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.in_app_product import InAppProduct
from openapi_server.models.inappproducts_batch_delete_request import InappproductsBatchDeleteRequest
from openapi_server.models.inappproducts_batch_get_response import InappproductsBatchGetResponse
from openapi_server.models.inappproducts_batch_update_request import InappproductsBatchUpdateRequest
from openapi_server.models.inappproducts_batch_update_response import InappproductsBatchUpdateResponse
from openapi_server.models.inappproducts_list_response import InappproductsListResponse


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_inappproducts_batch_delete(client):
    """Test case for androidpublisher_inappproducts_batch_delete

    
    """
    body = {"requests":[{"packageName":"packageName","sku":"sku","latencyTolerance":"PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED"},{"packageName":"packageName","sku":"sku","latencyTolerance":"PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED"}]}
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
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/androidpublisher/v3/applications/{package_name}/inappproducts:batchDelete'.format(package_name='package_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_inappproducts_batch_get(client):
    """Test case for androidpublisher_inappproducts_batch_get

    
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
                    ('sku', ['sku_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/androidpublisher/v3/applications/{package_name}/inappproducts:batchGet'.format(package_name='package_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_inappproducts_batch_update(client):
    """Test case for androidpublisher_inappproducts_batch_update

    
    """
    body = {"requests":[{"inappproduct":{"defaultPrice":{"priceMicros":"priceMicros","currency":"currency"},"gracePeriod":"gracePeriod","subscriptionTaxesAndComplianceSettings":{"taxRateInfoByRegionCode":{"key":{"eligibleForStreamingServiceTaxRate":True,"taxTier":"TAX_TIER_UNSPECIFIED","streamingTaxType":"STREAMING_TAX_TYPE_UNSPECIFIED"}},"isTokenizedDigitalAsset":True,"eeaWithdrawalRightType":"WITHDRAWAL_RIGHT_TYPE_UNSPECIFIED"},"managedProductTaxesAndComplianceSettings":{"taxRateInfoByRegionCode":{"key":{"eligibleForStreamingServiceTaxRate":True,"taxTier":"TAX_TIER_UNSPECIFIED","streamingTaxType":"STREAMING_TAX_TYPE_UNSPECIFIED"}},"isTokenizedDigitalAsset":True,"eeaWithdrawalRightType":"WITHDRAWAL_RIGHT_TYPE_UNSPECIFIED"},"purchaseType":"purchaseTypeUnspecified","listings":{"key":{"benefits":["benefits","benefits"],"description":"description","title":"title"}},"subscriptionPeriod":"subscriptionPeriod","defaultLanguage":"defaultLanguage","trialPeriod":"trialPeriod","packageName":"packageName","prices":{"key":{"priceMicros":"priceMicros","currency":"currency"}},"sku":"sku","status":"statusUnspecified"},"allowMissing":True,"autoConvertMissingPrices":True,"packageName":"packageName","sku":"sku","latencyTolerance":"PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED"},{"inappproduct":{"defaultPrice":{"priceMicros":"priceMicros","currency":"currency"},"gracePeriod":"gracePeriod","subscriptionTaxesAndComplianceSettings":{"taxRateInfoByRegionCode":{"key":{"eligibleForStreamingServiceTaxRate":True,"taxTier":"TAX_TIER_UNSPECIFIED","streamingTaxType":"STREAMING_TAX_TYPE_UNSPECIFIED"}},"isTokenizedDigitalAsset":True,"eeaWithdrawalRightType":"WITHDRAWAL_RIGHT_TYPE_UNSPECIFIED"},"managedProductTaxesAndComplianceSettings":{"taxRateInfoByRegionCode":{"key":{"eligibleForStreamingServiceTaxRate":True,"taxTier":"TAX_TIER_UNSPECIFIED","streamingTaxType":"STREAMING_TAX_TYPE_UNSPECIFIED"}},"isTokenizedDigitalAsset":True,"eeaWithdrawalRightType":"WITHDRAWAL_RIGHT_TYPE_UNSPECIFIED"},"purchaseType":"purchaseTypeUnspecified","listings":{"key":{"benefits":["benefits","benefits"],"description":"description","title":"title"}},"subscriptionPeriod":"subscriptionPeriod","defaultLanguage":"defaultLanguage","trialPeriod":"trialPeriod","packageName":"packageName","prices":{"key":{"priceMicros":"priceMicros","currency":"currency"}},"sku":"sku","status":"statusUnspecified"},"allowMissing":True,"autoConvertMissingPrices":True,"packageName":"packageName","sku":"sku","latencyTolerance":"PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED"}]}
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
        path='/androidpublisher/v3/applications/{package_name}/inappproducts:batchUpdate'.format(package_name='package_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_inappproducts_delete(client):
    """Test case for androidpublisher_inappproducts_delete

    
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
                    ('latencyTolerance', 'latency_tolerance_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/androidpublisher/v3/applications/{package_name}/inappproducts/{sku}'.format(package_name='package_name_example', sku='sku_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_inappproducts_get(client):
    """Test case for androidpublisher_inappproducts_get

    
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
        path='/androidpublisher/v3/applications/{package_name}/inappproducts/{sku}'.format(package_name='package_name_example', sku='sku_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_inappproducts_insert(client):
    """Test case for androidpublisher_inappproducts_insert

    
    """
    body = {"defaultPrice":{"priceMicros":"priceMicros","currency":"currency"},"gracePeriod":"gracePeriod","subscriptionTaxesAndComplianceSettings":{"taxRateInfoByRegionCode":{"key":{"eligibleForStreamingServiceTaxRate":True,"taxTier":"TAX_TIER_UNSPECIFIED","streamingTaxType":"STREAMING_TAX_TYPE_UNSPECIFIED"}},"isTokenizedDigitalAsset":True,"eeaWithdrawalRightType":"WITHDRAWAL_RIGHT_TYPE_UNSPECIFIED"},"managedProductTaxesAndComplianceSettings":{"taxRateInfoByRegionCode":{"key":{"eligibleForStreamingServiceTaxRate":True,"taxTier":"TAX_TIER_UNSPECIFIED","streamingTaxType":"STREAMING_TAX_TYPE_UNSPECIFIED"}},"isTokenizedDigitalAsset":True,"eeaWithdrawalRightType":"WITHDRAWAL_RIGHT_TYPE_UNSPECIFIED"},"purchaseType":"purchaseTypeUnspecified","listings":{"key":{"benefits":["benefits","benefits"],"description":"description","title":"title"}},"subscriptionPeriod":"subscriptionPeriod","defaultLanguage":"defaultLanguage","trialPeriod":"trialPeriod","packageName":"packageName","prices":{"key":{"priceMicros":"priceMicros","currency":"currency"}},"sku":"sku","status":"statusUnspecified"}
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
                    ('autoConvertMissingPrices', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/androidpublisher/v3/applications/{package_name}/inappproducts'.format(package_name='package_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_inappproducts_list(client):
    """Test case for androidpublisher_inappproducts_list

    
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
                    ('startIndex', 56),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/androidpublisher/v3/applications/{package_name}/inappproducts'.format(package_name='package_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_inappproducts_patch(client):
    """Test case for androidpublisher_inappproducts_patch

    
    """
    body = {"defaultPrice":{"priceMicros":"priceMicros","currency":"currency"},"gracePeriod":"gracePeriod","subscriptionTaxesAndComplianceSettings":{"taxRateInfoByRegionCode":{"key":{"eligibleForStreamingServiceTaxRate":True,"taxTier":"TAX_TIER_UNSPECIFIED","streamingTaxType":"STREAMING_TAX_TYPE_UNSPECIFIED"}},"isTokenizedDigitalAsset":True,"eeaWithdrawalRightType":"WITHDRAWAL_RIGHT_TYPE_UNSPECIFIED"},"managedProductTaxesAndComplianceSettings":{"taxRateInfoByRegionCode":{"key":{"eligibleForStreamingServiceTaxRate":True,"taxTier":"TAX_TIER_UNSPECIFIED","streamingTaxType":"STREAMING_TAX_TYPE_UNSPECIFIED"}},"isTokenizedDigitalAsset":True,"eeaWithdrawalRightType":"WITHDRAWAL_RIGHT_TYPE_UNSPECIFIED"},"purchaseType":"purchaseTypeUnspecified","listings":{"key":{"benefits":["benefits","benefits"],"description":"description","title":"title"}},"subscriptionPeriod":"subscriptionPeriod","defaultLanguage":"defaultLanguage","trialPeriod":"trialPeriod","packageName":"packageName","prices":{"key":{"priceMicros":"priceMicros","currency":"currency"}},"sku":"sku","status":"statusUnspecified"}
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
                    ('autoConvertMissingPrices', True),
                    ('latencyTolerance', 'latency_tolerance_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/androidpublisher/v3/applications/{package_name}/inappproducts/{sku}'.format(package_name='package_name_example', sku='sku_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_inappproducts_update(client):
    """Test case for androidpublisher_inappproducts_update

    
    """
    body = {"defaultPrice":{"priceMicros":"priceMicros","currency":"currency"},"gracePeriod":"gracePeriod","subscriptionTaxesAndComplianceSettings":{"taxRateInfoByRegionCode":{"key":{"eligibleForStreamingServiceTaxRate":True,"taxTier":"TAX_TIER_UNSPECIFIED","streamingTaxType":"STREAMING_TAX_TYPE_UNSPECIFIED"}},"isTokenizedDigitalAsset":True,"eeaWithdrawalRightType":"WITHDRAWAL_RIGHT_TYPE_UNSPECIFIED"},"managedProductTaxesAndComplianceSettings":{"taxRateInfoByRegionCode":{"key":{"eligibleForStreamingServiceTaxRate":True,"taxTier":"TAX_TIER_UNSPECIFIED","streamingTaxType":"STREAMING_TAX_TYPE_UNSPECIFIED"}},"isTokenizedDigitalAsset":True,"eeaWithdrawalRightType":"WITHDRAWAL_RIGHT_TYPE_UNSPECIFIED"},"purchaseType":"purchaseTypeUnspecified","listings":{"key":{"benefits":["benefits","benefits"],"description":"description","title":"title"}},"subscriptionPeriod":"subscriptionPeriod","defaultLanguage":"defaultLanguage","trialPeriod":"trialPeriod","packageName":"packageName","prices":{"key":{"priceMicros":"priceMicros","currency":"currency"}},"sku":"sku","status":"statusUnspecified"}
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
                    ('allowMissing', True),
                    ('autoConvertMissingPrices', True),
                    ('latencyTolerance', 'latency_tolerance_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/androidpublisher/v3/applications/{package_name}/inappproducts/{sku}'.format(package_name='package_name_example', sku='sku_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

