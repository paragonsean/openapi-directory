# SquareConnectApi.OrderLineItemAppliedDiscount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appliedMoney** | [**Money**](Money.md) |  | [optional] 
**discountUid** | **String** | The &#x60;uid&#x60; of the discount that the applied discount represents. It must reference a discount present in the &#x60;order.discounts&#x60; field.  This field is immutable. To change which discounts apply to a line item, you must delete the discount and re-add it as a new &#x60;OrderLineItemAppliedDiscount&#x60;. | 
**uid** | **String** | A unique ID that identifies the applied discount only within this order. | [optional] 


