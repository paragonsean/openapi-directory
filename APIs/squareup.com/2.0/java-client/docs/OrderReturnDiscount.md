

# OrderReturnDiscount

Represents a discount being returned that applies to one or more return line items in an order.  Fixed-amount, order-scoped discounts are distributed across all non-zero return line item totals. The amount distributed to each return line item is relative to that item’s contribution to the order subtotal.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amountMoney** | [**Money**](Money.md) |  |  [optional] |
|**appliedMoney** | [**Money**](Money.md) |  |  [optional] |
|**catalogObjectId** | **String** | The catalog object ID referencing [CatalogDiscount](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogDiscount). |  [optional] |
|**catalogVersion** | **Long** | The version of the catalog object that this discount references. |  [optional] |
|**name** | **String** | The discount&#39;s name. |  [optional] |
|**percentage** | **String** | The percentage of the tax, as a string representation of a decimal number. A value of &#x60;\&quot;7.25\&quot;&#x60; corresponds to a percentage of 7.25%.  &#x60;percentage&#x60; is not set for amount-based discounts. |  [optional] |
|**scope** | **String** | Indicates the level at which the &#x60;OrderReturnDiscount&#x60; applies. For &#x60;ORDER&#x60; scoped discounts, the server generates references in &#x60;applied_discounts&#x60; on all &#x60;OrderReturnLineItem&#x60;s. For &#x60;LINE_ITEM&#x60; scoped discounts, the discount is only applied to &#x60;OrderReturnLineItem&#x60;s with references in their &#x60;applied_discounts&#x60; field. |  [optional] |
|**sourceDiscountUid** | **String** | The discount &#x60;uid&#x60; from the order that contains the original application of this discount. |  [optional] |
|**type** | **String** | The type of the discount. If it is created by the API, it is &#x60;FIXED_PERCENTAGE&#x60; or &#x60;FIXED_AMOUNT&#x60;.  Discounts that do not reference a catalog object ID must have a type of &#x60;FIXED_PERCENTAGE&#x60; or &#x60;FIXED_AMOUNT&#x60;. |  [optional] |
|**uid** | **String** | A unique ID that identifies the returned discount only within this order. |  [optional] |



