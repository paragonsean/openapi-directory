# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.product import Product
from openapi_server.models.products_custom_batch_request import ProductsCustomBatchRequest
from openapi_server.models.products_custom_batch_response import ProductsCustomBatchResponse
from openapi_server.models.products_list_response import ProductsListResponse


pytestmark = pytest.mark.asyncio

async def test_content_products_custombatch(client):
    """Test case for content_products_custombatch

    
    """
    body = {"entries":[{"product":{"additionalImageLinks":["additionalImageLinks","additionalImageLinks"],"customLabel4":"customLabel4","customLabel3":"customLabel3","channel":"channel","availabilityDate":"availabilityDate","onlineOnly":True,"taxes":[{"country":"country","rate":2.3021358869347655,"locationId":"locationId","postalCode":"postalCode","region":"region","taxShip":True},{"country":"country","rate":2.3021358869347655,"locationId":"locationId","postalCode":"postalCode","region":"region","taxShip":True}],"adwordsGrouping":"adwordsGrouping","source":"source","loyaltyPoints":{"name":"name","pointsValue":"pointsValue","ratio":1.4658129805029452},"canonicalLink":"canonicalLink","displayAdsLink":"displayAdsLink","shippingHeight":{"unit":"unit","value":5.962133916683182},"sellOnGoogleQuantity":"sellOnGoogleQuantity","shipping":[{"country":"country","locationId":"locationId","price":{"currency":"currency","value":"value"},"service":"service","postalCode":"postalCode","region":"region","locationGroupName":"locationGroupName"},{"country":"country","locationId":"locationId","price":{"currency":"currency","value":"value"},"service":"service","postalCode":"postalCode","region":"region","locationGroupName":"locationGroupName"}],"sizes":["sizes","sizes"],"price":{"currency":"currency","value":"value"},"customLabel2":"customLabel2","customLabel1":"customLabel1","customLabel0":"customLabel0","displayAdsSimilarIds":["displayAdsSimilarIds","displayAdsSimilarIds"],"id":"id","brand":"brand","customGroups":[{"name":"name","attributes":[{"unit":"unit","name":"name","type":"type","value":"value"},{"unit":"unit","name":"name","type":"type","value":"value"}]},{"name":"name","attributes":[{"unit":"unit","name":"name","type":"type","value":"value"},{"unit":"unit","name":"name","type":"type","value":"value"}]}],"sizeType":"sizeType","sizeSystem":"sizeSystem","kind":"kind","destinations":[{"destinationName":"destinationName","intention":"intention"},{"destinationName":"destinationName","intention":"intention"}],"displayAdsValue":6.027456183070403,"shippingLabel":"shippingLabel","mpn":"mpn","ageGroup":"ageGroup","mobileLink":"mobileLink","targetCountry":"targetCountry","condition":"condition","minEnergyEfficiencyClass":"minEnergyEfficiencyClass","installment":{"amount":{"currency":"currency","value":"value"},"months":"months"},"contentLanguage":"contentLanguage","offerId":"offerId","identifierExists":True,"adult":True,"customAttributes":[{"unit":"unit","name":"name","type":"type","value":"value"},{"unit":"unit","name":"name","type":"type","value":"value"}],"energyEfficiencyClass":"energyEfficiencyClass","googleProductCategory":"googleProductCategory","isBundle":True,"validatedDestinations":["validatedDestinations","validatedDestinations"],"color":"color","gender":"gender","adwordsLabels":["adwordsLabels","adwordsLabels"],"aspects":[{"aspectName":"aspectName","destinationName":"destinationName","intention":"intention"},{"aspectName":"aspectName","destinationName":"destinationName","intention":"intention"}],"link":"link","pattern":"pattern","salePriceEffectiveDate":"salePriceEffectiveDate","description":"description","multipack":"multipack","minHandlingTime":"minHandlingTime","availability":"availability","title":"title","itemGroupId":"itemGroupId","maxEnergyEfficiencyClass":"maxEnergyEfficiencyClass","displayAdsId":"displayAdsId","imageLink":"imageLink","unitPricingBaseMeasure":{"unit":"unit","value":"value"},"shippingWeight":{"unit":"unit","value":5.637376656633329},"shippingWidth":{"unit":"unit","value":5.962133916683182},"productType":"productType","additionalProductTypes":["additionalProductTypes","additionalProductTypes"],"expirationDate":"expirationDate","costOfGoodsSold":{"currency":"currency","value":"value"},"gtin":"gtin","shippingLength":{"unit":"unit","value":5.962133916683182},"salePrice":{"currency":"currency","value":"value"},"warnings":[{"reason":"reason","domain":"domain","message":"message"},{"reason":"reason","domain":"domain","message":"message"}],"maxHandlingTime":"maxHandlingTime","promotionIds":["promotionIds","promotionIds"],"adwordsRedirect":"adwordsRedirect","material":"material","displayAdsTitle":"displayAdsTitle","unitPricingMeasure":{"unit":"unit","value":7.061401241503109}},"method":"method","productId":"productId","merchantId":"merchantId","batchId":0},{"product":{"additionalImageLinks":["additionalImageLinks","additionalImageLinks"],"customLabel4":"customLabel4","customLabel3":"customLabel3","channel":"channel","availabilityDate":"availabilityDate","onlineOnly":True,"taxes":[{"country":"country","rate":2.3021358869347655,"locationId":"locationId","postalCode":"postalCode","region":"region","taxShip":True},{"country":"country","rate":2.3021358869347655,"locationId":"locationId","postalCode":"postalCode","region":"region","taxShip":True}],"adwordsGrouping":"adwordsGrouping","source":"source","loyaltyPoints":{"name":"name","pointsValue":"pointsValue","ratio":1.4658129805029452},"canonicalLink":"canonicalLink","displayAdsLink":"displayAdsLink","shippingHeight":{"unit":"unit","value":5.962133916683182},"sellOnGoogleQuantity":"sellOnGoogleQuantity","shipping":[{"country":"country","locationId":"locationId","price":{"currency":"currency","value":"value"},"service":"service","postalCode":"postalCode","region":"region","locationGroupName":"locationGroupName"},{"country":"country","locationId":"locationId","price":{"currency":"currency","value":"value"},"service":"service","postalCode":"postalCode","region":"region","locationGroupName":"locationGroupName"}],"sizes":["sizes","sizes"],"price":{"currency":"currency","value":"value"},"customLabel2":"customLabel2","customLabel1":"customLabel1","customLabel0":"customLabel0","displayAdsSimilarIds":["displayAdsSimilarIds","displayAdsSimilarIds"],"id":"id","brand":"brand","customGroups":[{"name":"name","attributes":[{"unit":"unit","name":"name","type":"type","value":"value"},{"unit":"unit","name":"name","type":"type","value":"value"}]},{"name":"name","attributes":[{"unit":"unit","name":"name","type":"type","value":"value"},{"unit":"unit","name":"name","type":"type","value":"value"}]}],"sizeType":"sizeType","sizeSystem":"sizeSystem","kind":"kind","destinations":[{"destinationName":"destinationName","intention":"intention"},{"destinationName":"destinationName","intention":"intention"}],"displayAdsValue":6.027456183070403,"shippingLabel":"shippingLabel","mpn":"mpn","ageGroup":"ageGroup","mobileLink":"mobileLink","targetCountry":"targetCountry","condition":"condition","minEnergyEfficiencyClass":"minEnergyEfficiencyClass","installment":{"amount":{"currency":"currency","value":"value"},"months":"months"},"contentLanguage":"contentLanguage","offerId":"offerId","identifierExists":True,"adult":True,"customAttributes":[{"unit":"unit","name":"name","type":"type","value":"value"},{"unit":"unit","name":"name","type":"type","value":"value"}],"energyEfficiencyClass":"energyEfficiencyClass","googleProductCategory":"googleProductCategory","isBundle":True,"validatedDestinations":["validatedDestinations","validatedDestinations"],"color":"color","gender":"gender","adwordsLabels":["adwordsLabels","adwordsLabels"],"aspects":[{"aspectName":"aspectName","destinationName":"destinationName","intention":"intention"},{"aspectName":"aspectName","destinationName":"destinationName","intention":"intention"}],"link":"link","pattern":"pattern","salePriceEffectiveDate":"salePriceEffectiveDate","description":"description","multipack":"multipack","minHandlingTime":"minHandlingTime","availability":"availability","title":"title","itemGroupId":"itemGroupId","maxEnergyEfficiencyClass":"maxEnergyEfficiencyClass","displayAdsId":"displayAdsId","imageLink":"imageLink","unitPricingBaseMeasure":{"unit":"unit","value":"value"},"shippingWeight":{"unit":"unit","value":5.637376656633329},"shippingWidth":{"unit":"unit","value":5.962133916683182},"productType":"productType","additionalProductTypes":["additionalProductTypes","additionalProductTypes"],"expirationDate":"expirationDate","costOfGoodsSold":{"currency":"currency","value":"value"},"gtin":"gtin","shippingLength":{"unit":"unit","value":5.962133916683182},"salePrice":{"currency":"currency","value":"value"},"warnings":[{"reason":"reason","domain":"domain","message":"message"},{"reason":"reason","domain":"domain","message":"message"}],"maxHandlingTime":"maxHandlingTime","promotionIds":["promotionIds","promotionIds"],"adwordsRedirect":"adwordsRedirect","material":"material","displayAdsTitle":"displayAdsTitle","unitPricingMeasure":{"unit":"unit","value":7.061401241503109}},"method":"method","productId":"productId","merchantId":"merchantId","batchId":0}]}
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
        path='/content/v2/products/batch',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_products_delete(client):
    """Test case for content_products_delete

    
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
                    ('dryRun', True)]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/content/v2/{merchant_id}/products/{product_id}'.format(merchant_id='merchant_id_example', product_id='product_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_products_get(client):
    """Test case for content_products_get

    
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
        path='/content/v2/{merchant_id}/products/{product_id}'.format(merchant_id='merchant_id_example', product_id='product_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_products_insert(client):
    """Test case for content_products_insert

    
    """
    body = {"additionalImageLinks":["additionalImageLinks","additionalImageLinks"],"customLabel4":"customLabel4","customLabel3":"customLabel3","channel":"channel","availabilityDate":"availabilityDate","onlineOnly":True,"taxes":[{"country":"country","rate":2.3021358869347655,"locationId":"locationId","postalCode":"postalCode","region":"region","taxShip":True},{"country":"country","rate":2.3021358869347655,"locationId":"locationId","postalCode":"postalCode","region":"region","taxShip":True}],"adwordsGrouping":"adwordsGrouping","source":"source","loyaltyPoints":{"name":"name","pointsValue":"pointsValue","ratio":1.4658129805029452},"canonicalLink":"canonicalLink","displayAdsLink":"displayAdsLink","shippingHeight":{"unit":"unit","value":5.962133916683182},"sellOnGoogleQuantity":"sellOnGoogleQuantity","shipping":[{"country":"country","locationId":"locationId","price":{"currency":"currency","value":"value"},"service":"service","postalCode":"postalCode","region":"region","locationGroupName":"locationGroupName"},{"country":"country","locationId":"locationId","price":{"currency":"currency","value":"value"},"service":"service","postalCode":"postalCode","region":"region","locationGroupName":"locationGroupName"}],"sizes":["sizes","sizes"],"price":{"currency":"currency","value":"value"},"customLabel2":"customLabel2","customLabel1":"customLabel1","customLabel0":"customLabel0","displayAdsSimilarIds":["displayAdsSimilarIds","displayAdsSimilarIds"],"id":"id","brand":"brand","customGroups":[{"name":"name","attributes":[{"unit":"unit","name":"name","type":"type","value":"value"},{"unit":"unit","name":"name","type":"type","value":"value"}]},{"name":"name","attributes":[{"unit":"unit","name":"name","type":"type","value":"value"},{"unit":"unit","name":"name","type":"type","value":"value"}]}],"sizeType":"sizeType","sizeSystem":"sizeSystem","kind":"kind","destinations":[{"destinationName":"destinationName","intention":"intention"},{"destinationName":"destinationName","intention":"intention"}],"displayAdsValue":6.027456183070403,"shippingLabel":"shippingLabel","mpn":"mpn","ageGroup":"ageGroup","mobileLink":"mobileLink","targetCountry":"targetCountry","condition":"condition","minEnergyEfficiencyClass":"minEnergyEfficiencyClass","installment":{"amount":{"currency":"currency","value":"value"},"months":"months"},"contentLanguage":"contentLanguage","offerId":"offerId","identifierExists":True,"adult":True,"customAttributes":[{"unit":"unit","name":"name","type":"type","value":"value"},{"unit":"unit","name":"name","type":"type","value":"value"}],"energyEfficiencyClass":"energyEfficiencyClass","googleProductCategory":"googleProductCategory","isBundle":True,"validatedDestinations":["validatedDestinations","validatedDestinations"],"color":"color","gender":"gender","adwordsLabels":["adwordsLabels","adwordsLabels"],"aspects":[{"aspectName":"aspectName","destinationName":"destinationName","intention":"intention"},{"aspectName":"aspectName","destinationName":"destinationName","intention":"intention"}],"link":"link","pattern":"pattern","salePriceEffectiveDate":"salePriceEffectiveDate","description":"description","multipack":"multipack","minHandlingTime":"minHandlingTime","availability":"availability","title":"title","itemGroupId":"itemGroupId","maxEnergyEfficiencyClass":"maxEnergyEfficiencyClass","displayAdsId":"displayAdsId","imageLink":"imageLink","unitPricingBaseMeasure":{"unit":"unit","value":"value"},"shippingWeight":{"unit":"unit","value":5.637376656633329},"shippingWidth":{"unit":"unit","value":5.962133916683182},"productType":"productType","additionalProductTypes":["additionalProductTypes","additionalProductTypes"],"expirationDate":"expirationDate","costOfGoodsSold":{"currency":"currency","value":"value"},"gtin":"gtin","shippingLength":{"unit":"unit","value":5.962133916683182},"salePrice":{"currency":"currency","value":"value"},"warnings":[{"reason":"reason","domain":"domain","message":"message"},{"reason":"reason","domain":"domain","message":"message"}],"maxHandlingTime":"maxHandlingTime","promotionIds":["promotionIds","promotionIds"],"adwordsRedirect":"adwordsRedirect","material":"material","displayAdsTitle":"displayAdsTitle","unitPricingMeasure":{"unit":"unit","value":7.061401241503109}}
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
        path='/content/v2/{merchant_id}/products'.format(merchant_id='merchant_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_products_list(client):
    """Test case for content_products_list

    
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
                    ('includeInvalidInsertedItems', True),
                    ('maxResults', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/content/v2/{merchant_id}/products'.format(merchant_id='merchant_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

