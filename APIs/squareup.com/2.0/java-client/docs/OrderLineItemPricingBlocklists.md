

# OrderLineItemPricingBlocklists

Describes pricing adjustments that are blocked from manual and  automatic application to a line item. For more information, see  [Apply Taxes and Discounts](https://developer.squareup.com/docs/orders-api/apply-taxes-and-discounts).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**blockedDiscounts** | [**List&lt;OrderLineItemPricingBlocklistsBlockedDiscount&gt;**](OrderLineItemPricingBlocklistsBlockedDiscount.md) | A list of discounts blocked from applying to the line item.  Discounts can be blocked by the &#x60;discount_uid&#x60; (for ad hoc discounts) or  the &#x60;discount_catalog_object_id&#x60; (for catalog discounts). |  [optional] |
|**blockedTaxes** | [**List&lt;OrderLineItemPricingBlocklistsBlockedTax&gt;**](OrderLineItemPricingBlocklistsBlockedTax.md) | A list of taxes blocked from applying to the line item.  Taxes can be blocked by the &#x60;tax_uid&#x60; (for ad hoc taxes) or  the &#x60;tax_catalog_object_id&#x60; (for catalog taxes). |  [optional] |



