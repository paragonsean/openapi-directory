# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.base_response import BaseResponse
from openapi_server.models.item_promotion import ItemPromotion
from openapi_server.models.item_promotion_response import ItemPromotionResponse


pytestmark = pytest.mark.asyncio

async def test_create_item_promotion(client):
    """Test case for create_item_promotion

    
    """
    body = {"promotionType":"promotionType","endDate":"endDate","promotionImageUrl":"promotionImageUrl","discountRules":[{"discountSpecification":{"minAmount":{"currency":"currency","value":"value"},"minQuantity":1,"numberOfDiscountedItems":5,"forEachAmount":{"currency":"currency","value":"value"},"forEachQuantity":6},"maxDiscountAmount":{"currency":"currency","value":"value"},"ruleOrder":5,"discountBenefit":{"amountOffOrder":{"currency":"currency","value":"value"},"amountOffItem":{"currency":"currency","value":"value"},"percentageOffItem":"percentageOffItem","percentageOffOrder":"percentageOffOrder"}},{"discountSpecification":{"minAmount":{"currency":"currency","value":"value"},"minQuantity":1,"numberOfDiscountedItems":5,"forEachAmount":{"currency":"currency","value":"value"},"forEachQuantity":6},"maxDiscountAmount":{"currency":"currency","value":"value"},"ruleOrder":5,"discountBenefit":{"amountOffOrder":{"currency":"currency","value":"value"},"amountOffItem":{"currency":"currency","value":"value"},"percentageOffItem":"percentageOffItem","percentageOffOrder":"percentageOffOrder"}}],"description":"description","couponConfiguration":{"maxCouponRedemptionPerUser":0,"couponType":"couponType","couponCode":"couponCode"},"priority":"priority","promotionStatus":"promotionStatus","marketplaceId":"marketplaceId","inventoryCriterion":{"inventoryItems":[{"inventoryReferenceId":"inventoryReferenceId"},{"inventoryReferenceId":"inventoryReferenceId"}],"listingIds":["listingIds","listingIds"],"ruleCriteria":{"markupInventoryItems":[{"inventoryReferenceId":"inventoryReferenceId"},{"inventoryReferenceId":"inventoryReferenceId"}],"markupListingIds":["markupListingIds","markupListingIds"],"excludeInventoryItems":[{"inventoryReferenceId":"inventoryReferenceId"},{"inventoryReferenceId":"inventoryReferenceId"}],"excludeListingIds":["excludeListingIds","excludeListingIds"],"selectionRules":[{"categoryIds":["categoryIds","categoryIds"],"brands":["brands","brands"],"categoryScope":"categoryScope","minPrice":{"currency":"currency","value":"value"},"maxPrice":{"currency":"currency","value":"value"},"listingConditionIds":["listingConditionIds","listingConditionIds"]},{"categoryIds":["categoryIds","categoryIds"],"brands":["brands","brands"],"categoryScope":"categoryScope","minPrice":{"currency":"currency","value":"value"},"maxPrice":{"currency":"currency","value":"value"},"listingConditionIds":["listingConditionIds","listingConditionIds"]}]},"inventoryCriterionType":"inventoryCriterionType"},"applyDiscountToSingleItemOnly":True,"name":"name","startDate":"startDate","budget":{"currency":"currency","value":"value"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/marketing/v1/item_promotion',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_item_promotion(client):
    """Test case for delete_item_promotion

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/sell/marketing/v1/item_promotion/{promotion_id}'.format(promotion_id='promotion_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_item_promotion(client):
    """Test case for get_item_promotion

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/marketing/v1/item_promotion/{promotion_id}'.format(promotion_id='promotion_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_item_promotion(client):
    """Test case for update_item_promotion

    
    """
    body = {"promotionType":"promotionType","endDate":"endDate","promotionImageUrl":"promotionImageUrl","discountRules":[{"discountSpecification":{"minAmount":{"currency":"currency","value":"value"},"minQuantity":1,"numberOfDiscountedItems":5,"forEachAmount":{"currency":"currency","value":"value"},"forEachQuantity":6},"maxDiscountAmount":{"currency":"currency","value":"value"},"ruleOrder":5,"discountBenefit":{"amountOffOrder":{"currency":"currency","value":"value"},"amountOffItem":{"currency":"currency","value":"value"},"percentageOffItem":"percentageOffItem","percentageOffOrder":"percentageOffOrder"}},{"discountSpecification":{"minAmount":{"currency":"currency","value":"value"},"minQuantity":1,"numberOfDiscountedItems":5,"forEachAmount":{"currency":"currency","value":"value"},"forEachQuantity":6},"maxDiscountAmount":{"currency":"currency","value":"value"},"ruleOrder":5,"discountBenefit":{"amountOffOrder":{"currency":"currency","value":"value"},"amountOffItem":{"currency":"currency","value":"value"},"percentageOffItem":"percentageOffItem","percentageOffOrder":"percentageOffOrder"}}],"description":"description","couponConfiguration":{"maxCouponRedemptionPerUser":0,"couponType":"couponType","couponCode":"couponCode"},"priority":"priority","promotionStatus":"promotionStatus","marketplaceId":"marketplaceId","inventoryCriterion":{"inventoryItems":[{"inventoryReferenceId":"inventoryReferenceId"},{"inventoryReferenceId":"inventoryReferenceId"}],"listingIds":["listingIds","listingIds"],"ruleCriteria":{"markupInventoryItems":[{"inventoryReferenceId":"inventoryReferenceId"},{"inventoryReferenceId":"inventoryReferenceId"}],"markupListingIds":["markupListingIds","markupListingIds"],"excludeInventoryItems":[{"inventoryReferenceId":"inventoryReferenceId"},{"inventoryReferenceId":"inventoryReferenceId"}],"excludeListingIds":["excludeListingIds","excludeListingIds"],"selectionRules":[{"categoryIds":["categoryIds","categoryIds"],"brands":["brands","brands"],"categoryScope":"categoryScope","minPrice":{"currency":"currency","value":"value"},"maxPrice":{"currency":"currency","value":"value"},"listingConditionIds":["listingConditionIds","listingConditionIds"]},{"categoryIds":["categoryIds","categoryIds"],"brands":["brands","brands"],"categoryScope":"categoryScope","minPrice":{"currency":"currency","value":"value"},"maxPrice":{"currency":"currency","value":"value"},"listingConditionIds":["listingConditionIds","listingConditionIds"]}]},"inventoryCriterionType":"inventoryCriterionType"},"applyDiscountToSingleItemOnly":True,"name":"name","startDate":"startDate","budget":{"currency":"currency","value":"value"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/sell/marketing/v1/item_promotion/{promotion_id}'.format(promotion_id='promotion_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

