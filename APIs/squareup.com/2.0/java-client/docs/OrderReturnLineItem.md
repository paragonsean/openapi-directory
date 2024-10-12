

# OrderReturnLineItem

The line item being returned in an order.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appliedDiscounts** | [**List&lt;OrderLineItemAppliedDiscount&gt;**](OrderLineItemAppliedDiscount.md) | The list of references to &#x60;OrderReturnDiscount&#x60; entities applied to the return line item. Each &#x60;OrderLineItemAppliedDiscount&#x60; has a &#x60;discount_uid&#x60; that references the &#x60;uid&#x60; of a top-level &#x60;OrderReturnDiscount&#x60; applied to the return line item. On reads, the applied amount is populated. |  [optional] |
|**appliedTaxes** | [**List&lt;OrderLineItemAppliedTax&gt;**](OrderLineItemAppliedTax.md) | The list of references to &#x60;OrderReturnTax&#x60; entities applied to the return line item. Each &#x60;OrderLineItemAppliedTax&#x60; has a &#x60;tax_uid&#x60; that references the &#x60;uid&#x60; of a top-level &#x60;OrderReturnTax&#x60; applied to the return line item. On reads, the applied amount is populated. |  [optional] |
|**basePriceMoney** | [**Money**](Money.md) |  |  [optional] |
|**catalogObjectId** | **String** | The [CatalogItemVariation](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItemVariation) ID applied to this return line item. |  [optional] |
|**catalogVersion** | **Long** | The version of the catalog object that this line item references. |  [optional] |
|**grossReturnMoney** | [**Money**](Money.md) |  |  [optional] |
|**itemType** | **String** | The type of line item: an itemized return, a non-itemized return (custom amount), or the return of an unactivated gift card sale. |  [optional] |
|**name** | **String** | The name of the line item. |  [optional] |
|**note** | **String** | The note of the return line item. |  [optional] |
|**quantity** | **String** | The quantity returned, formatted as a decimal number. For example, &#x60;\&quot;3\&quot;&#x60;.  Line items with a &#x60;quantity_unit&#x60; can have non-integer quantities. For example, &#x60;\&quot;1.70000\&quot;&#x60;. |  |
|**quantityUnit** | [**OrderQuantityUnit**](OrderQuantityUnit.md) |  |  [optional] |
|**returnModifiers** | [**List&lt;OrderReturnLineItemModifier&gt;**](OrderReturnLineItemModifier.md) | The [CatalogModifier](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogModifier)s applied to this line item. |  [optional] |
|**sourceLineItemUid** | **String** | The &#x60;uid&#x60; of the line item in the original sale order. |  [optional] |
|**totalDiscountMoney** | [**Money**](Money.md) |  |  [optional] |
|**totalMoney** | [**Money**](Money.md) |  |  [optional] |
|**totalTaxMoney** | [**Money**](Money.md) |  |  [optional] |
|**uid** | **String** | A unique ID for this return line-item entry. |  [optional] |
|**variationName** | **String** | The name of the variation applied to this return line item. |  [optional] |
|**variationTotalPriceMoney** | [**Money**](Money.md) |  |  [optional] |



