# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_promotion_response import ListPromotionResponse
from openapi_server.models.promotion import Promotion


pytestmark = pytest.mark.asyncio

async def test_content_promotions_create(client):
    """Test case for content_promotions_create

    
    """
    body = {"limitValue":{"currency":"currency","value":"value"},"redemptionChannel":["REDEMPTION_CHANNEL_UNSPECIFIED","REDEMPTION_CHANNEL_UNSPECIFIED"],"productTypeExclusion":["productTypeExclusion","productTypeExclusion"],"orderLimit":5,"promotionEffectiveTimePeriod":{"startTime":"startTime","endTime":"endTime"},"freeGiftItemId":"freeGiftItemId","getThisQuantityDiscounted":0,"itemGroupId":["itemGroupId","itemGroupId"],"limitQuantity":6,"promotionId":"promotionId","shippingServiceNames":["shippingServiceNames","shippingServiceNames"],"promotionStatus":{"lastUpdateDate":"lastUpdateDate","promotionIssue":[{"code":"code","detail":"detail"},{"code":"code","detail":"detail"}],"destinationStatuses":[{"destination":"destination","status":"STATE_UNSPECIFIED"},{"destination":"destination","status":"STATE_UNSPECIFIED"}],"creationDate":"creationDate"},"storeCodeExclusion":["storeCodeExclusion","storeCodeExclusion"],"offerType":"OFFER_TYPE_UNSPECIFIED","itemIdExclusion":["itemIdExclusion","itemIdExclusion"],"promotionDestinationIds":["promotionDestinationIds","promotionDestinationIds"],"id":"id","promotionDisplayDates":"promotionDisplayDates","brand":["brand","brand"],"productType":["productType","productType"],"couponValueType":"COUPON_VALUE_TYPE_UNSPECIFIED","itemGroupIdExclusion":["itemGroupIdExclusion","itemGroupIdExclusion"],"freeGiftValue":{"currency":"currency","value":"value"},"minimumPurchaseQuantity":1,"percentOff":5,"moneyBudget":{"currency":"currency","value":"value"},"promotionDisplayTimePeriod":{"startTime":"startTime","endTime":"endTime"},"freeGiftDescription":"freeGiftDescription","targetCountry":"targetCountry","promotionUrl":"promotionUrl","storeApplicability":"STORE_APPLICABILITY_UNSPECIFIED","itemId":["itemId","itemId"],"promotionEffectiveDates":"promotionEffectiveDates","moneyOffAmount":{"currency":"currency","value":"value"},"minimumPurchaseAmount":{"currency":"currency","value":"value"},"genericRedemptionCode":"genericRedemptionCode","brandExclusion":["brandExclusion","brandExclusion"],"contentLanguage":"contentLanguage","productApplicability":"PRODUCT_APPLICABILITY_UNSPECIFIED","longTitle":"longTitle","storeCode":["storeCode","storeCode"]}
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
        path='/content/v2.1/{merchant_id}/promotions'.format(merchant_id='merchant_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_promotions_get(client):
    """Test case for content_promotions_get

    
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
        path='/content/v2.1/{merchant_id}/promotions/{id}'.format(merchant_id='merchant_id_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_promotions_list(client):
    """Test case for content_promotions_list

    
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
                    ('countryCode', 'country_code_example'),
                    ('languageCode', 'language_code_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/content/v2.1/{merchant_id}/promotions'.format(merchant_id='merchant_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

