# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_or_update_calculator_configuration200_response import CreateOrUpdateCalculatorConfiguration200Response
from openapi_server.models.create_or_update_calculator_configuration_request import CreateOrUpdateCalculatorConfigurationRequest
from openapi_server.models.get_all_benefits200_response import GetAllBenefits200Response
from openapi_server.models.get_all_taxes200_response import GetAllTaxes200Response
from openapi_server.models.get_archived_promotions200_response import GetArchivedPromotions200Response
from openapi_server.models.get_archived_taxes200_response import GetArchivedTaxes200Response
from openapi_server.models.get_calculator_configuration_by_id200_response import GetCalculatorConfigurationById200Response
from openapi_server.models.get_calculator_configuration_by_id200_response1 import GetCalculatorConfigurationById200Response1


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/csv not supported by Connexion")
async def test_api_rnb_pvt_import_calculator_configuration_post(client):
    """Test case for api_rnb_pvt_import_calculator_configuration_post

    Create Multiple SKU Promotion
    """
    body = '/path/to/file'
    headers = { 
        'Content-Type': 'text/csv',
        'content_type': 'text/csv',
        'accept': 'application/json',
        'x_vtex_calculator_name': 'Test',
        'x_vtex_cumulative': false,
        'x_vtex_cluster_operator': 'any',
        'x_vtex_cluster_expression': 'cluster_name=true',
        'x_vtex_start_date': '2020-08-18T16:00:00+3:00',
        'x_vtex_end_date': '2020-08-18T16:30:00+3:00',
        'x_vtex_accumulate_with_manual_prices': false,
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/rnb/pvt/import/calculatorConfiguration',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/csv not supported by Connexion")
async def test_api_rnb_pvt_import_calculator_configuration_promotion_id_put(client):
    """Test case for api_rnb_pvt_import_calculator_configuration_promotion_id_put

    Update Multiple SKU Promotion
    """
    body = '/path/to/file'
    headers = { 
        'Content-Type': 'text/csv',
        'content_type': 'text/csv',
        'accept': 'application/json',
        'x_vtex_calculator_name': 'Test',
        'x_vtex_cumulative': false,
        'x_vtex_cluster_operator': 'any',
        'x_vtex_cluster_expression': 'cluster_name=true',
        'x_vtex_start_date': '2020-08-18T16:00:00+3:00',
        'x_vtex_end_date': '2020-08-18T16:30:00+3:00',
        'x_vtex_accumulate_with_manual_prices': false,
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/rnb/pvt/import/calculatorConfiguration/{promotion_id}'.format(promotion_id='dc6b6f59-ec2b-4a13-8490-0d1e0c53ddf9'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_archive_promotion(client):
    """Test case for archive_promotion

    Archive Promotion or Tax
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/rnb/pvt/archive/calculatorConfiguration/{id_calculator_configuration}'.format(id_calculator_configuration='d8a1cd2e-b667-4054-b3ae-b79124c7218e'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_or_update_calculator_configuration(client):
    """Test case for create_or_update_calculator_configuration

    Create or Update Promotion or Tax
    """
    body = {"absoluteShippingDiscountValue":0,"accumulateWithManualPrice":false,"activateGiftsMultiplier":false,"activeDaysOfWeek":[],"affiliates":[],"applyToAllShippings":false,"areSalesChannelIdsExclusive":false,"beginDateUtc":"2020-05-01T18:47:15.89Z","brands":[],"brandsAreInclusive":false,"campaigns":[],"cardIssuers":[],"categories":[],"categoriesAreInclusive":false,"clusterExpressions":[],"collections":[],"collections1BuyTogether":[],"collections2BuyTogether":[],"collectionsIsInclusive":false,"compareListPriceAndPrice":false,"conditionsIds":["372e1868-2c0e-4437-be45-1ef8c9cab735"],"coupon":[],"cumulative":false,"daysAgoOfPurchases":0,"description":"Promotion for Social Seller","disableDeal":false,"discountType":"percentual","enableBuyTogetherPerSku":false,"firstBuyIsProfileOptimistic":false,"giftListTypes":[],"idCalculatorConfiguration":"d8a1cd2e-b667-4054-b3ae-b79124c7218e","idSellerIsInclusive":false,"idsSalesChannel":[],"installment":0,"isActive":true,"isArchived":false,"isDifferentListPriceAndPrice":false,"isFeatured":false,"isFirstBuy":false,"isMinMaxInstallments":false,"isSlaSelected":false,"itemMaxPrice":0,"itemMinPrice":0,"lastModified":"2021-09-17T18:13:16.2896414Z","listSku1BuyTogether":[],"listSku2BuyTogether":[],"marketingTags":[],"marketingTagsAreNotInclusive":false,"maxInstallment":0,"maxNumberOfAffectedItems":0,"maxNumberOfAffectedItemsGroupKey":"perCart","maxPricesPerItems":[],"maxUsage":0,"maxUsagePerClient":0,"maximumUnitPriceDiscount":0,"merchants":[],"minInstallment":0,"minimumQuantityBuyTogether":0,"multipleUsePerClient":false,"name":"Promoção Social Seller","newOffset":-3,"nominalDiscountValue":0,"nominalRewardValue":0,"nominalShippingDiscountValue":0,"nominalTax":0,"offset":-3,"orderStatusRewardValue":"invoiced","origin":"marketplace","paymentsMethods":[],"paymentsRules":[],"percentualDiscountValue":10,"percentualDiscountValueList":[],"percentualDiscountValueList1":0,"percentualDiscountValueList2":0,"percentualRewardValue":0,"percentualShippingDiscountValue":0,"percentualTax":0,"products":[],"productsAreInclusive":false,"productsSpecifications":[],"quantityToAffectBuyTogether":0,"rebatePercentualDiscountValue":0,"restrictionsBins":[],"shippingPercentualTax":0,"shouldDistributeDiscountAmongMatchedItems":false,"skus":[],"skusAreInclusive":true,"skusGift":{"quantitySelectable":0},"slasIds":[],"stores":[],"storesAreInclusive":false,"totalValueCeling":0,"totalValueFloor":0,"totalValueIncludeAllItems":false,"totalValueMode":"IncludeMatchedItems","totalValuePurchase":0,"type":"regular","useNewProgressiveAlgorithm":false,"utmCampaign":"georgeTest","utmSource":"georgeSource","zipCodeRanges":[]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/rnb/pvt/calculatorconfiguration',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_benefits(client):
    """Test case for get_all_benefits

    Get All Promotions
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/rnb/pvt/benefits/calculatorconfiguration',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_taxes(client):
    """Test case for get_all_taxes

    Get All Taxes
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/rnb/pvt/taxes/calculatorconfiguration',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_archived_promotions(client):
    """Test case for get_archived_promotions

    List Archived Promotions
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/rnb/pvt/archive/benefits/calculatorConfiguration',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_archived_taxes(client):
    """Test case for get_archived_taxes

    List Archived Taxes
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/rnb/pvt/archive/taxes/calculatorConfiguration',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_calculator_configuration_by_id(client):
    """Test case for get_calculator_configuration_by_id

    Get Promotion or Tax by ID
    """
    headers = { 
        'Accept': 'Tax',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/rnb/pvt/calculatorconfiguration/{id_calculator_configuration}'.format(id_calculator_configuration='d8a1cd2e-b667-4054-b3ae-b79124c7218e'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unarchive_promotion(client):
    """Test case for unarchive_promotion

    Unarchive Promotion or Tax
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/rnb/pvt/unarchive/calculatorConfiguration/{id_calculator_configuration}'.format(id_calculator_configuration='d8a1cd2e-b667-4054-b3ae-b79124c7218e'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

