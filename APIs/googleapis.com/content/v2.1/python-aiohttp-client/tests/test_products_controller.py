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
    body = {"entries":[{"product":{"additionalImageLinks":["additionalImageLinks","additionalImageLinks"],"adsRedirect":"adsRedirect","transitTimeLabel":"transitTimeLabel","feedLabel":"feedLabel","channel":"channel","taxes":[{"country":"country","rate":4.145608029883936,"locationId":"locationId","postalCode":"postalCode","region":"region","taxShip":True},{"country":"country","rate":4.145608029883936,"locationId":"locationId","postalCode":"postalCode","region":"region","taxShip":True}],"externalSellerId":"externalSellerId","loyaltyPoints":{"name":"name","pointsValue":"pointsValue","ratio":2.3021358869347655},"additionalSizeType":"additionalSizeType","sellOnGoogleQuantity":"sellOnGoogleQuantity","productWidth":{"unit":"unit","value":7.061401241503109},"sizes":["sizes","sizes"],"price":{"currency":"currency","value":"value"},"displayAdsSimilarIds":["displayAdsSimilarIds","displayAdsSimilarIds"],"id":"id","brand":"brand","sizeSystem":"sizeSystem","pickupMethod":"pickupMethod","mpn":"mpn","productTypes":["productTypes","productTypes"],"mobileLink":"mobileLink","virtualModelLink":"virtualModelLink","offerId":"offerId","adult":True,"energyEfficiencyClass":"energyEfficiencyClass","googleProductCategory":"googleProductCategory","isBundle":True,"gender":"gender","pattern":"pattern","adsLabels":["adsLabels","adsLabels"],"minHandlingTime":"minHandlingTime","availability":"availability","maxEnergyEfficiencyClass":"maxEnergyEfficiencyClass","imageLink":"imageLink","shippingWeight":{"unit":"unit","value":2.027123023002322},"shippingWidth":{"unit":"unit","value":3.616076749251911},"productHeight":{"unit":"unit","value":7.061401241503109},"salePrice":{"currency":"currency","value":"value"},"maxHandlingTime":"maxHandlingTime","linkTemplate":"linkTemplate","productWeight":{"unit":"unit","value":9.301444243932576},"displayAdsTitle":"displayAdsTitle","unitPricingMeasure":{"unit":"unit","value":7.386281948385884},"customLabel4":"customLabel4","includedDestinations":["includedDestinations","includedDestinations"],"customLabel3":"customLabel3","availabilityDate":"availabilityDate","source":"source","productDetails":[{"sectionName":"sectionName","attributeValue":"attributeValue","attributeName":"attributeName"},{"sectionName":"sectionName","attributeValue":"attributeValue","attributeName":"attributeName"}],"canonicalLink":"canonicalLink","displayAdsLink":"displayAdsLink","shippingHeight":{"unit":"unit","value":3.616076749251911},"shipping":[{"maxTransitTime":"maxTransitTime","country":"country","locationId":"locationId","price":{"currency":"currency","value":"value"},"service":"service","postalCode":"postalCode","maxHandlingTime":"maxHandlingTime","minHandlingTime":"minHandlingTime","region":"region","minTransitTime":"minTransitTime","locationGroupName":"locationGroupName"},{"maxTransitTime":"maxTransitTime","country":"country","locationId":"locationId","price":{"currency":"currency","value":"value"},"service":"service","postalCode":"postalCode","maxHandlingTime":"maxHandlingTime","minHandlingTime":"minHandlingTime","region":"region","minTransitTime":"minTransitTime","locationGroupName":"locationGroupName"}],"customLabel2":"customLabel2","customLabel1":"customLabel1","customLabel0":"customLabel0","cloudExportAdditionalProperties":[{"minValue":5.962134,"textValue":["textValue","textValue"],"propertyName":"propertyName","intValue":["intValue","intValue"],"maxValue":1.4658129,"unitCode":"unitCode","floatValue":[6.0274563,6.0274563],"boolValue":True},{"minValue":5.962134,"textValue":["textValue","textValue"],"propertyName":"propertyName","intValue":["intValue","intValue"],"maxValue":1.4658129,"unitCode":"unitCode","floatValue":[6.0274563,6.0274563],"boolValue":True}],"pickupSla":"pickupSla","sizeType":"sizeType","kind":"kind","excludedDestinations":["excludedDestinations","excludedDestinations"],"displayAdsValue":5.637376656633329,"shippingLabel":"shippingLabel","ageGroup":"ageGroup","pause":"pause","targetCountry":"targetCountry","taxCategory":"taxCategory","subscriptionCost":{"amount":{"currency":"currency","value":"value"},"period":"period","periodLength":"periodLength"},"condition":"condition","minEnergyEfficiencyClass":"minEnergyEfficiencyClass","installment":{"amount":{"currency":"currency","value":"value"},"months":"months"},"contentLanguage":"contentLanguage","identifierExists":True,"customAttributes":[{"groupValues":[null,null],"name":"name","value":"value"},{"groupValues":[null,null],"name":"name","value":"value"}],"color":"color","link":"link","salePriceEffectiveDate":"salePriceEffectiveDate","description":"description","multipack":"multipack","title":"title","adsGrouping":"adsGrouping","itemGroupId":"itemGroupId","displayAdsId":"displayAdsId","productHighlights":["productHighlights","productHighlights"],"unitPricingBaseMeasure":{"unit":"unit","value":"value"},"productLength":{"unit":"unit","value":7.061401241503109},"expirationDate":"expirationDate","costOfGoodsSold":{"currency":"currency","value":"value"},"gtin":"gtin","disclosureDate":"disclosureDate","shippingLength":{"unit":"unit","value":3.616076749251911},"promotionIds":["promotionIds","promotionIds"],"certifications":[{"certificationAuthority":"certificationAuthority","certificationName":"certificationName","certificationCode":"certificationCode"},{"certificationAuthority":"certificationAuthority","certificationName":"certificationName","certificationCode":"certificationCode"}],"lifestyleImageLinks":["lifestyleImageLinks","lifestyleImageLinks"],"mobileLinkTemplate":"mobileLinkTemplate","material":"material","shoppingAdsExcludedCountries":["shoppingAdsExcludedCountries","shoppingAdsExcludedCountries"]},"method":"method","productId":"productId","feedId":"feedId","merchantId":"merchantId","batchId":0,"updateMask":"updateMask"},{"product":{"additionalImageLinks":["additionalImageLinks","additionalImageLinks"],"adsRedirect":"adsRedirect","transitTimeLabel":"transitTimeLabel","feedLabel":"feedLabel","channel":"channel","taxes":[{"country":"country","rate":4.145608029883936,"locationId":"locationId","postalCode":"postalCode","region":"region","taxShip":True},{"country":"country","rate":4.145608029883936,"locationId":"locationId","postalCode":"postalCode","region":"region","taxShip":True}],"externalSellerId":"externalSellerId","loyaltyPoints":{"name":"name","pointsValue":"pointsValue","ratio":2.3021358869347655},"additionalSizeType":"additionalSizeType","sellOnGoogleQuantity":"sellOnGoogleQuantity","productWidth":{"unit":"unit","value":7.061401241503109},"sizes":["sizes","sizes"],"price":{"currency":"currency","value":"value"},"displayAdsSimilarIds":["displayAdsSimilarIds","displayAdsSimilarIds"],"id":"id","brand":"brand","sizeSystem":"sizeSystem","pickupMethod":"pickupMethod","mpn":"mpn","productTypes":["productTypes","productTypes"],"mobileLink":"mobileLink","virtualModelLink":"virtualModelLink","offerId":"offerId","adult":True,"energyEfficiencyClass":"energyEfficiencyClass","googleProductCategory":"googleProductCategory","isBundle":True,"gender":"gender","pattern":"pattern","adsLabels":["adsLabels","adsLabels"],"minHandlingTime":"minHandlingTime","availability":"availability","maxEnergyEfficiencyClass":"maxEnergyEfficiencyClass","imageLink":"imageLink","shippingWeight":{"unit":"unit","value":2.027123023002322},"shippingWidth":{"unit":"unit","value":3.616076749251911},"productHeight":{"unit":"unit","value":7.061401241503109},"salePrice":{"currency":"currency","value":"value"},"maxHandlingTime":"maxHandlingTime","linkTemplate":"linkTemplate","productWeight":{"unit":"unit","value":9.301444243932576},"displayAdsTitle":"displayAdsTitle","unitPricingMeasure":{"unit":"unit","value":7.386281948385884},"customLabel4":"customLabel4","includedDestinations":["includedDestinations","includedDestinations"],"customLabel3":"customLabel3","availabilityDate":"availabilityDate","source":"source","productDetails":[{"sectionName":"sectionName","attributeValue":"attributeValue","attributeName":"attributeName"},{"sectionName":"sectionName","attributeValue":"attributeValue","attributeName":"attributeName"}],"canonicalLink":"canonicalLink","displayAdsLink":"displayAdsLink","shippingHeight":{"unit":"unit","value":3.616076749251911},"shipping":[{"maxTransitTime":"maxTransitTime","country":"country","locationId":"locationId","price":{"currency":"currency","value":"value"},"service":"service","postalCode":"postalCode","maxHandlingTime":"maxHandlingTime","minHandlingTime":"minHandlingTime","region":"region","minTransitTime":"minTransitTime","locationGroupName":"locationGroupName"},{"maxTransitTime":"maxTransitTime","country":"country","locationId":"locationId","price":{"currency":"currency","value":"value"},"service":"service","postalCode":"postalCode","maxHandlingTime":"maxHandlingTime","minHandlingTime":"minHandlingTime","region":"region","minTransitTime":"minTransitTime","locationGroupName":"locationGroupName"}],"customLabel2":"customLabel2","customLabel1":"customLabel1","customLabel0":"customLabel0","cloudExportAdditionalProperties":[{"minValue":5.962134,"textValue":["textValue","textValue"],"propertyName":"propertyName","intValue":["intValue","intValue"],"maxValue":1.4658129,"unitCode":"unitCode","floatValue":[6.0274563,6.0274563],"boolValue":True},{"minValue":5.962134,"textValue":["textValue","textValue"],"propertyName":"propertyName","intValue":["intValue","intValue"],"maxValue":1.4658129,"unitCode":"unitCode","floatValue":[6.0274563,6.0274563],"boolValue":True}],"pickupSla":"pickupSla","sizeType":"sizeType","kind":"kind","excludedDestinations":["excludedDestinations","excludedDestinations"],"displayAdsValue":5.637376656633329,"shippingLabel":"shippingLabel","ageGroup":"ageGroup","pause":"pause","targetCountry":"targetCountry","taxCategory":"taxCategory","subscriptionCost":{"amount":{"currency":"currency","value":"value"},"period":"period","periodLength":"periodLength"},"condition":"condition","minEnergyEfficiencyClass":"minEnergyEfficiencyClass","installment":{"amount":{"currency":"currency","value":"value"},"months":"months"},"contentLanguage":"contentLanguage","identifierExists":True,"customAttributes":[{"groupValues":[null,null],"name":"name","value":"value"},{"groupValues":[null,null],"name":"name","value":"value"}],"color":"color","link":"link","salePriceEffectiveDate":"salePriceEffectiveDate","description":"description","multipack":"multipack","title":"title","adsGrouping":"adsGrouping","itemGroupId":"itemGroupId","displayAdsId":"displayAdsId","productHighlights":["productHighlights","productHighlights"],"unitPricingBaseMeasure":{"unit":"unit","value":"value"},"productLength":{"unit":"unit","value":7.061401241503109},"expirationDate":"expirationDate","costOfGoodsSold":{"currency":"currency","value":"value"},"gtin":"gtin","disclosureDate":"disclosureDate","shippingLength":{"unit":"unit","value":3.616076749251911},"promotionIds":["promotionIds","promotionIds"],"certifications":[{"certificationAuthority":"certificationAuthority","certificationName":"certificationName","certificationCode":"certificationCode"},{"certificationAuthority":"certificationAuthority","certificationName":"certificationName","certificationCode":"certificationCode"}],"lifestyleImageLinks":["lifestyleImageLinks","lifestyleImageLinks"],"mobileLinkTemplate":"mobileLinkTemplate","material":"material","shoppingAdsExcludedCountries":["shoppingAdsExcludedCountries","shoppingAdsExcludedCountries"]},"method":"method","productId":"productId","feedId":"feedId","merchantId":"merchantId","batchId":0,"updateMask":"updateMask"}]}
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
        path='/content/v2.1/products/batch',
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
                    ('feedId', 'feed_id_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/content/v2.1/{merchant_id}/products/{product_id}'.format(merchant_id='merchant_id_example', product_id='product_id_example'),
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
        path='/content/v2.1/{merchant_id}/products/{product_id}'.format(merchant_id='merchant_id_example', product_id='product_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_products_insert(client):
    """Test case for content_products_insert

    
    """
    body = {"additionalImageLinks":["additionalImageLinks","additionalImageLinks"],"adsRedirect":"adsRedirect","transitTimeLabel":"transitTimeLabel","feedLabel":"feedLabel","channel":"channel","taxes":[{"country":"country","rate":4.145608029883936,"locationId":"locationId","postalCode":"postalCode","region":"region","taxShip":True},{"country":"country","rate":4.145608029883936,"locationId":"locationId","postalCode":"postalCode","region":"region","taxShip":True}],"externalSellerId":"externalSellerId","loyaltyPoints":{"name":"name","pointsValue":"pointsValue","ratio":2.3021358869347655},"additionalSizeType":"additionalSizeType","sellOnGoogleQuantity":"sellOnGoogleQuantity","productWidth":{"unit":"unit","value":7.061401241503109},"sizes":["sizes","sizes"],"price":{"currency":"currency","value":"value"},"displayAdsSimilarIds":["displayAdsSimilarIds","displayAdsSimilarIds"],"id":"id","brand":"brand","sizeSystem":"sizeSystem","pickupMethod":"pickupMethod","mpn":"mpn","productTypes":["productTypes","productTypes"],"mobileLink":"mobileLink","virtualModelLink":"virtualModelLink","offerId":"offerId","adult":True,"energyEfficiencyClass":"energyEfficiencyClass","googleProductCategory":"googleProductCategory","isBundle":True,"gender":"gender","pattern":"pattern","adsLabels":["adsLabels","adsLabels"],"minHandlingTime":"minHandlingTime","availability":"availability","maxEnergyEfficiencyClass":"maxEnergyEfficiencyClass","imageLink":"imageLink","shippingWeight":{"unit":"unit","value":2.027123023002322},"shippingWidth":{"unit":"unit","value":3.616076749251911},"productHeight":{"unit":"unit","value":7.061401241503109},"salePrice":{"currency":"currency","value":"value"},"maxHandlingTime":"maxHandlingTime","linkTemplate":"linkTemplate","productWeight":{"unit":"unit","value":9.301444243932576},"displayAdsTitle":"displayAdsTitle","unitPricingMeasure":{"unit":"unit","value":7.386281948385884},"customLabel4":"customLabel4","includedDestinations":["includedDestinations","includedDestinations"],"customLabel3":"customLabel3","availabilityDate":"availabilityDate","source":"source","productDetails":[{"sectionName":"sectionName","attributeValue":"attributeValue","attributeName":"attributeName"},{"sectionName":"sectionName","attributeValue":"attributeValue","attributeName":"attributeName"}],"canonicalLink":"canonicalLink","displayAdsLink":"displayAdsLink","shippingHeight":{"unit":"unit","value":3.616076749251911},"shipping":[{"maxTransitTime":"maxTransitTime","country":"country","locationId":"locationId","price":{"currency":"currency","value":"value"},"service":"service","postalCode":"postalCode","maxHandlingTime":"maxHandlingTime","minHandlingTime":"minHandlingTime","region":"region","minTransitTime":"minTransitTime","locationGroupName":"locationGroupName"},{"maxTransitTime":"maxTransitTime","country":"country","locationId":"locationId","price":{"currency":"currency","value":"value"},"service":"service","postalCode":"postalCode","maxHandlingTime":"maxHandlingTime","minHandlingTime":"minHandlingTime","region":"region","minTransitTime":"minTransitTime","locationGroupName":"locationGroupName"}],"customLabel2":"customLabel2","customLabel1":"customLabel1","customLabel0":"customLabel0","cloudExportAdditionalProperties":[{"minValue":5.962134,"textValue":["textValue","textValue"],"propertyName":"propertyName","intValue":["intValue","intValue"],"maxValue":1.4658129,"unitCode":"unitCode","floatValue":[6.0274563,6.0274563],"boolValue":True},{"minValue":5.962134,"textValue":["textValue","textValue"],"propertyName":"propertyName","intValue":["intValue","intValue"],"maxValue":1.4658129,"unitCode":"unitCode","floatValue":[6.0274563,6.0274563],"boolValue":True}],"pickupSla":"pickupSla","sizeType":"sizeType","kind":"kind","excludedDestinations":["excludedDestinations","excludedDestinations"],"displayAdsValue":5.637376656633329,"shippingLabel":"shippingLabel","ageGroup":"ageGroup","pause":"pause","targetCountry":"targetCountry","taxCategory":"taxCategory","subscriptionCost":{"amount":{"currency":"currency","value":"value"},"period":"period","periodLength":"periodLength"},"condition":"condition","minEnergyEfficiencyClass":"minEnergyEfficiencyClass","installment":{"amount":{"currency":"currency","value":"value"},"months":"months"},"contentLanguage":"contentLanguage","identifierExists":True,"customAttributes":[{"groupValues":[null,null],"name":"name","value":"value"},{"groupValues":[null,null],"name":"name","value":"value"}],"color":"color","link":"link","salePriceEffectiveDate":"salePriceEffectiveDate","description":"description","multipack":"multipack","title":"title","adsGrouping":"adsGrouping","itemGroupId":"itemGroupId","displayAdsId":"displayAdsId","productHighlights":["productHighlights","productHighlights"],"unitPricingBaseMeasure":{"unit":"unit","value":"value"},"productLength":{"unit":"unit","value":7.061401241503109},"expirationDate":"expirationDate","costOfGoodsSold":{"currency":"currency","value":"value"},"gtin":"gtin","disclosureDate":"disclosureDate","shippingLength":{"unit":"unit","value":3.616076749251911},"promotionIds":["promotionIds","promotionIds"],"certifications":[{"certificationAuthority":"certificationAuthority","certificationName":"certificationName","certificationCode":"certificationCode"},{"certificationAuthority":"certificationAuthority","certificationName":"certificationName","certificationCode":"certificationCode"}],"lifestyleImageLinks":["lifestyleImageLinks","lifestyleImageLinks"],"mobileLinkTemplate":"mobileLinkTemplate","material":"material","shoppingAdsExcludedCountries":["shoppingAdsExcludedCountries","shoppingAdsExcludedCountries"]}
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
                    ('feedId', 'feed_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/content/v2.1/{merchant_id}/products'.format(merchant_id='merchant_id_example'),
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
                    ('maxResults', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/content/v2.1/{merchant_id}/products'.format(merchant_id='merchant_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_products_update(client):
    """Test case for content_products_update

    
    """
    body = {"additionalImageLinks":["additionalImageLinks","additionalImageLinks"],"adsRedirect":"adsRedirect","transitTimeLabel":"transitTimeLabel","feedLabel":"feedLabel","channel":"channel","taxes":[{"country":"country","rate":4.145608029883936,"locationId":"locationId","postalCode":"postalCode","region":"region","taxShip":True},{"country":"country","rate":4.145608029883936,"locationId":"locationId","postalCode":"postalCode","region":"region","taxShip":True}],"externalSellerId":"externalSellerId","loyaltyPoints":{"name":"name","pointsValue":"pointsValue","ratio":2.3021358869347655},"additionalSizeType":"additionalSizeType","sellOnGoogleQuantity":"sellOnGoogleQuantity","productWidth":{"unit":"unit","value":7.061401241503109},"sizes":["sizes","sizes"],"price":{"currency":"currency","value":"value"},"displayAdsSimilarIds":["displayAdsSimilarIds","displayAdsSimilarIds"],"id":"id","brand":"brand","sizeSystem":"sizeSystem","pickupMethod":"pickupMethod","mpn":"mpn","productTypes":["productTypes","productTypes"],"mobileLink":"mobileLink","virtualModelLink":"virtualModelLink","offerId":"offerId","adult":True,"energyEfficiencyClass":"energyEfficiencyClass","googleProductCategory":"googleProductCategory","isBundle":True,"gender":"gender","pattern":"pattern","adsLabels":["adsLabels","adsLabels"],"minHandlingTime":"minHandlingTime","availability":"availability","maxEnergyEfficiencyClass":"maxEnergyEfficiencyClass","imageLink":"imageLink","shippingWeight":{"unit":"unit","value":2.027123023002322},"shippingWidth":{"unit":"unit","value":3.616076749251911},"productHeight":{"unit":"unit","value":7.061401241503109},"salePrice":{"currency":"currency","value":"value"},"maxHandlingTime":"maxHandlingTime","linkTemplate":"linkTemplate","productWeight":{"unit":"unit","value":9.301444243932576},"displayAdsTitle":"displayAdsTitle","unitPricingMeasure":{"unit":"unit","value":7.386281948385884},"customLabel4":"customLabel4","includedDestinations":["includedDestinations","includedDestinations"],"customLabel3":"customLabel3","availabilityDate":"availabilityDate","source":"source","productDetails":[{"sectionName":"sectionName","attributeValue":"attributeValue","attributeName":"attributeName"},{"sectionName":"sectionName","attributeValue":"attributeValue","attributeName":"attributeName"}],"canonicalLink":"canonicalLink","displayAdsLink":"displayAdsLink","shippingHeight":{"unit":"unit","value":3.616076749251911},"shipping":[{"maxTransitTime":"maxTransitTime","country":"country","locationId":"locationId","price":{"currency":"currency","value":"value"},"service":"service","postalCode":"postalCode","maxHandlingTime":"maxHandlingTime","minHandlingTime":"minHandlingTime","region":"region","minTransitTime":"minTransitTime","locationGroupName":"locationGroupName"},{"maxTransitTime":"maxTransitTime","country":"country","locationId":"locationId","price":{"currency":"currency","value":"value"},"service":"service","postalCode":"postalCode","maxHandlingTime":"maxHandlingTime","minHandlingTime":"minHandlingTime","region":"region","minTransitTime":"minTransitTime","locationGroupName":"locationGroupName"}],"customLabel2":"customLabel2","customLabel1":"customLabel1","customLabel0":"customLabel0","cloudExportAdditionalProperties":[{"minValue":5.962134,"textValue":["textValue","textValue"],"propertyName":"propertyName","intValue":["intValue","intValue"],"maxValue":1.4658129,"unitCode":"unitCode","floatValue":[6.0274563,6.0274563],"boolValue":True},{"minValue":5.962134,"textValue":["textValue","textValue"],"propertyName":"propertyName","intValue":["intValue","intValue"],"maxValue":1.4658129,"unitCode":"unitCode","floatValue":[6.0274563,6.0274563],"boolValue":True}],"pickupSla":"pickupSla","sizeType":"sizeType","kind":"kind","excludedDestinations":["excludedDestinations","excludedDestinations"],"displayAdsValue":5.637376656633329,"shippingLabel":"shippingLabel","ageGroup":"ageGroup","pause":"pause","targetCountry":"targetCountry","taxCategory":"taxCategory","subscriptionCost":{"amount":{"currency":"currency","value":"value"},"period":"period","periodLength":"periodLength"},"condition":"condition","minEnergyEfficiencyClass":"minEnergyEfficiencyClass","installment":{"amount":{"currency":"currency","value":"value"},"months":"months"},"contentLanguage":"contentLanguage","identifierExists":True,"customAttributes":[{"groupValues":[null,null],"name":"name","value":"value"},{"groupValues":[null,null],"name":"name","value":"value"}],"color":"color","link":"link","salePriceEffectiveDate":"salePriceEffectiveDate","description":"description","multipack":"multipack","title":"title","adsGrouping":"adsGrouping","itemGroupId":"itemGroupId","displayAdsId":"displayAdsId","productHighlights":["productHighlights","productHighlights"],"unitPricingBaseMeasure":{"unit":"unit","value":"value"},"productLength":{"unit":"unit","value":7.061401241503109},"expirationDate":"expirationDate","costOfGoodsSold":{"currency":"currency","value":"value"},"gtin":"gtin","disclosureDate":"disclosureDate","shippingLength":{"unit":"unit","value":3.616076749251911},"promotionIds":["promotionIds","promotionIds"],"certifications":[{"certificationAuthority":"certificationAuthority","certificationName":"certificationName","certificationCode":"certificationCode"},{"certificationAuthority":"certificationAuthority","certificationName":"certificationName","certificationCode":"certificationCode"}],"lifestyleImageLinks":["lifestyleImageLinks","lifestyleImageLinks"],"mobileLinkTemplate":"mobileLinkTemplate","material":"material","shoppingAdsExcludedCountries":["shoppingAdsExcludedCountries","shoppingAdsExcludedCountries"]}
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
                    ('updateMask', 'update_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/content/v2.1/{merchant_id}/products/{product_id}'.format(merchant_id='merchant_id_example', product_id='product_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

