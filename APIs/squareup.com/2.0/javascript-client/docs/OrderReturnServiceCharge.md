# SquareConnectApi.OrderReturnServiceCharge

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amountMoney** | [**Money**](Money.md) |  | [optional] 
**appliedMoney** | [**Money**](Money.md) |  | [optional] 
**appliedTaxes** | [**[OrderLineItemAppliedTax]**](OrderLineItemAppliedTax.md) | The list of references to &#x60;OrderReturnTax&#x60; entities applied to the &#x60;OrderReturnServiceCharge&#x60;. Each &#x60;OrderLineItemAppliedTax&#x60; has a &#x60;tax_uid&#x60; that references the &#x60;uid&#x60; of a top-level &#x60;OrderReturnTax&#x60; that is being applied to the &#x60;OrderReturnServiceCharge&#x60;. On reads, the applied amount is populated. | [optional] 
**calculationPhase** | **String** | The calculation phase after which to apply the service charge. | [optional] 
**catalogObjectId** | **String** | The catalog object ID of the associated [OrderServiceCharge](https://developer.squareup.com/reference/square_2021-08-18/objects/OrderServiceCharge). | [optional] 
**catalogVersion** | **Number** | The version of the catalog object that this service charge references. | [optional] 
**name** | **String** | The name of the service charge. | [optional] 
**percentage** | **String** | The percentage of the service charge, as a string representation of a decimal number. For example, a value of &#x60;\&quot;7.25\&quot;&#x60; corresponds to a percentage of 7.25%.  Either &#x60;percentage&#x60; or &#x60;amount_money&#x60; should be set, but not both. | [optional] 
**sourceServiceChargeUid** | **String** | The service charge &#x60;uid&#x60; from the order containing the original service charge. &#x60;source_service_charge_uid&#x60; is &#x60;null&#x60; for unlinked returns. | [optional] 
**taxable** | **Boolean** | Indicates whether the surcharge can be taxed. Service charges calculated in the &#x60;TOTAL_PHASE&#x60; cannot be marked as taxable. | [optional] 
**totalMoney** | [**Money**](Money.md) |  | [optional] 
**totalTaxMoney** | [**Money**](Money.md) |  | [optional] 
**uid** | **String** | A unique ID that identifies the return service charge only within this order. | [optional] 


