

# OrderLineItemAppliedDiscount

Represents an applied portion of a discount to a line item in an order.  Order scoped discounts have automatically applied discounts present for each line item. Line-item scoped discounts must have applied discounts added manually for any applicable line items. The corresponding applied money is automatically computed based on participating line items.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appliedMoney** | [**Money**](Money.md) |  |  [optional] |
|**discountUid** | **String** | The &#x60;uid&#x60; of the discount that the applied discount represents. It must reference a discount present in the &#x60;order.discounts&#x60; field.  This field is immutable. To change which discounts apply to a line item, you must delete the discount and re-add it as a new &#x60;OrderLineItemAppliedDiscount&#x60;. |  |
|**uid** | **String** | A unique ID that identifies the applied discount only within this order. |  [optional] |



