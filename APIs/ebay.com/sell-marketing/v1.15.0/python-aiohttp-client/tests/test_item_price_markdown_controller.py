# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.item_price_markdown import ItemPriceMarkdown


pytestmark = pytest.mark.asyncio

async def test_create_item_price_markdown_promotion(client):
    """Test case for create_item_price_markdown_promotion

    
    """
    body = {"marketplaceId":"marketplaceId","selectedInventoryDiscounts":[{"inventoryCriterion":{"inventoryItems":[{"inventoryReferenceId":"inventoryReferenceId"},{"inventoryReferenceId":"inventoryReferenceId"}],"listingIds":["listingIds","listingIds"],"ruleCriteria":{"markupInventoryItems":[{"inventoryReferenceId":"inventoryReferenceId"},{"inventoryReferenceId":"inventoryReferenceId"}],"markupListingIds":["markupListingIds","markupListingIds"],"excludeInventoryItems":[{"inventoryReferenceId":"inventoryReferenceId"},{"inventoryReferenceId":"inventoryReferenceId"}],"excludeListingIds":["excludeListingIds","excludeListingIds"],"selectionRules":[{"categoryIds":["categoryIds","categoryIds"],"brands":["brands","brands"],"categoryScope":"categoryScope","minPrice":{"currency":"currency","value":"value"},"maxPrice":{"currency":"currency","value":"value"},"listingConditionIds":["listingConditionIds","listingConditionIds"]},{"categoryIds":["categoryIds","categoryIds"],"brands":["brands","brands"],"categoryScope":"categoryScope","minPrice":{"currency":"currency","value":"value"},"maxPrice":{"currency":"currency","value":"value"},"listingConditionIds":["listingConditionIds","listingConditionIds"]}]},"inventoryCriterionType":"inventoryCriterionType"},"ruleOrder":0,"discountId":"discountId","discountBenefit":{"amountOffOrder":{"currency":"currency","value":"value"},"amountOffItem":{"currency":"currency","value":"value"},"percentageOffItem":"percentageOffItem","percentageOffOrder":"percentageOffOrder"}},{"inventoryCriterion":{"inventoryItems":[{"inventoryReferenceId":"inventoryReferenceId"},{"inventoryReferenceId":"inventoryReferenceId"}],"listingIds":["listingIds","listingIds"],"ruleCriteria":{"markupInventoryItems":[{"inventoryReferenceId":"inventoryReferenceId"},{"inventoryReferenceId":"inventoryReferenceId"}],"markupListingIds":["markupListingIds","markupListingIds"],"excludeInventoryItems":[{"inventoryReferenceId":"inventoryReferenceId"},{"inventoryReferenceId":"inventoryReferenceId"}],"excludeListingIds":["excludeListingIds","excludeListingIds"],"selectionRules":[{"categoryIds":["categoryIds","categoryIds"],"brands":["brands","brands"],"categoryScope":"categoryScope","minPrice":{"currency":"currency","value":"value"},"maxPrice":{"currency":"currency","value":"value"},"listingConditionIds":["listingConditionIds","listingConditionIds"]},{"categoryIds":["categoryIds","categoryIds"],"brands":["brands","brands"],"categoryScope":"categoryScope","minPrice":{"currency":"currency","value":"value"},"maxPrice":{"currency":"currency","value":"value"},"listingConditionIds":["listingConditionIds","listingConditionIds"]}]},"inventoryCriterionType":"inventoryCriterionType"},"ruleOrder":0,"discountId":"discountId","discountBenefit":{"amountOffOrder":{"currency":"currency","value":"value"},"amountOffItem":{"currency":"currency","value":"value"},"percentageOffItem":"percentageOffItem","percentageOffOrder":"percentageOffOrder"}}],"endDate":"endDate","promotionImageUrl":"promotionImageUrl","name":"name","description":"description","blockPriceIncreaseInItemRevision":True,"autoSelectFutureInventory":True,"priority":"priority","applyFreeShipping":True,"startDate":"startDate","promotionStatus":"promotionStatus"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/marketing/v1/item_price_markdown',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_item_price_markdown_promotion(client):
    """Test case for delete_item_price_markdown_promotion

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/sell/marketing/v1/item_price_markdown/{promotion_id}'.format(promotion_id='promotion_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_item_price_markdown_promotion(client):
    """Test case for get_item_price_markdown_promotion

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/marketing/v1/item_price_markdown/{promotion_id}'.format(promotion_id='promotion_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_item_price_markdown_promotion(client):
    """Test case for update_item_price_markdown_promotion

    
    """
    body = {"marketplaceId":"marketplaceId","selectedInventoryDiscounts":[{"inventoryCriterion":{"inventoryItems":[{"inventoryReferenceId":"inventoryReferenceId"},{"inventoryReferenceId":"inventoryReferenceId"}],"listingIds":["listingIds","listingIds"],"ruleCriteria":{"markupInventoryItems":[{"inventoryReferenceId":"inventoryReferenceId"},{"inventoryReferenceId":"inventoryReferenceId"}],"markupListingIds":["markupListingIds","markupListingIds"],"excludeInventoryItems":[{"inventoryReferenceId":"inventoryReferenceId"},{"inventoryReferenceId":"inventoryReferenceId"}],"excludeListingIds":["excludeListingIds","excludeListingIds"],"selectionRules":[{"categoryIds":["categoryIds","categoryIds"],"brands":["brands","brands"],"categoryScope":"categoryScope","minPrice":{"currency":"currency","value":"value"},"maxPrice":{"currency":"currency","value":"value"},"listingConditionIds":["listingConditionIds","listingConditionIds"]},{"categoryIds":["categoryIds","categoryIds"],"brands":["brands","brands"],"categoryScope":"categoryScope","minPrice":{"currency":"currency","value":"value"},"maxPrice":{"currency":"currency","value":"value"},"listingConditionIds":["listingConditionIds","listingConditionIds"]}]},"inventoryCriterionType":"inventoryCriterionType"},"ruleOrder":0,"discountId":"discountId","discountBenefit":{"amountOffOrder":{"currency":"currency","value":"value"},"amountOffItem":{"currency":"currency","value":"value"},"percentageOffItem":"percentageOffItem","percentageOffOrder":"percentageOffOrder"}},{"inventoryCriterion":{"inventoryItems":[{"inventoryReferenceId":"inventoryReferenceId"},{"inventoryReferenceId":"inventoryReferenceId"}],"listingIds":["listingIds","listingIds"],"ruleCriteria":{"markupInventoryItems":[{"inventoryReferenceId":"inventoryReferenceId"},{"inventoryReferenceId":"inventoryReferenceId"}],"markupListingIds":["markupListingIds","markupListingIds"],"excludeInventoryItems":[{"inventoryReferenceId":"inventoryReferenceId"},{"inventoryReferenceId":"inventoryReferenceId"}],"excludeListingIds":["excludeListingIds","excludeListingIds"],"selectionRules":[{"categoryIds":["categoryIds","categoryIds"],"brands":["brands","brands"],"categoryScope":"categoryScope","minPrice":{"currency":"currency","value":"value"},"maxPrice":{"currency":"currency","value":"value"},"listingConditionIds":["listingConditionIds","listingConditionIds"]},{"categoryIds":["categoryIds","categoryIds"],"brands":["brands","brands"],"categoryScope":"categoryScope","minPrice":{"currency":"currency","value":"value"},"maxPrice":{"currency":"currency","value":"value"},"listingConditionIds":["listingConditionIds","listingConditionIds"]}]},"inventoryCriterionType":"inventoryCriterionType"},"ruleOrder":0,"discountId":"discountId","discountBenefit":{"amountOffOrder":{"currency":"currency","value":"value"},"amountOffItem":{"currency":"currency","value":"value"},"percentageOffItem":"percentageOffItem","percentageOffOrder":"percentageOffOrder"}}],"endDate":"endDate","promotionImageUrl":"promotionImageUrl","name":"name","description":"description","blockPriceIncreaseInItemRevision":True,"autoSelectFutureInventory":True,"priority":"priority","applyFreeShipping":True,"startDate":"startDate","promotionStatus":"promotionStatus"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/sell/marketing/v1/item_price_markdown/{promotion_id}'.format(promotion_id='promotion_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

