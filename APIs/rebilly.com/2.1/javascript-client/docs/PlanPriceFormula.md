# RebillyRestApi.PlanPriceFormula

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**formula** | **String** | The price formula determines what algorithm is used to calculate the invoice price based on a few factors, - the quantity in the order (which may be variable if usage pricing, otherwise determined when creating the order) - the price brackets data  To determine which formula is correct, please see the price formula documentation.  | 



## Enum: FormulaEnum


* `fixed-fee` (value: `"fixed-fee"`)

* `flat-rate` (value: `"flat-rate"`)

* `stairstep` (value: `"stairstep"`)

* `tiered` (value: `"tiered"`)

* `volume` (value: `"volume"`)




