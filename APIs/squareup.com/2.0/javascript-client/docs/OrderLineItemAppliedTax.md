# SquareConnectApi.OrderLineItemAppliedTax

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appliedMoney** | [**Money**](Money.md) |  | [optional] 
**taxUid** | **String** | The &#x60;uid&#x60; of the tax for which this applied tax represents. It must reference a tax present in the &#x60;order.taxes&#x60; field.  This field is immutable. To change which taxes apply to a line item, delete and add a new &#x60;OrderLineItemAppliedTax&#x60;. | 
**uid** | **String** | A unique ID that identifies the applied tax only within this order. | [optional] 


