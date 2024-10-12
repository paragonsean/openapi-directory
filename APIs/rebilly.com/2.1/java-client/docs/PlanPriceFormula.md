

# PlanPriceFormula


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**formula** | [**FormulaEnum**](#FormulaEnum) | The price formula determines what algorithm is used to calculate the invoice price based on a few factors, - the quantity in the order (which may be variable if usage pricing, otherwise determined when creating the order) - the price brackets data  To determine which formula is correct, please see the price formula documentation.  |  |



## Enum: FormulaEnum

| Name | Value |
|---- | -----|
| FIXED_FEE | &quot;fixed-fee&quot; |
| FLAT_RATE | &quot;flat-rate&quot; |
| STAIRSTEP | &quot;stairstep&quot; |
| TIERED | &quot;tiered&quot; |
| VOLUME | &quot;volume&quot; |



