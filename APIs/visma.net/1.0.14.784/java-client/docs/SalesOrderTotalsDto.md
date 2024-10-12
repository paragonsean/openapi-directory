

# SalesOrderTotalsDto


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**costTotal** | **Double** | The total of the costs on the lines of the sales order. How the &#x60;costTotal&#x60; is calculated is dependent on the option &#x60;useReplacementCostForMarginAndProfit&#x60;.  If this option is &#x60;true&#x60; the &#x60;costTotal&#x60; will be calculated based on the &#x60;replacementUnitCost&#x60;.  If this option is &#x60;false&#x60;, the &#x60;costTotal&#x60; will be calculate based on &#x60;unitCost&#x60; |  [optional] |
|**costTotalInBaseCurrency** | **Double** | The total of the costs on the lines of the sales order in base currency. |  [optional] |
|**discountTotal** | **Double** | The discount total |  [optional] |
|**discountTotalInBaseCurrency** | **Double** | The discount total in base currency |  [optional] |
|**freightCost** | **Double** | The freight cost calculated for the sales order. Not applicable for transfer order types. |  [optional] |
|**freightCostInBaseCurrency** | **Double** | The freight cost calculated for the sales order in base currency. Not applicable for transfer order types. |  [optional] [readonly] |
|**freightTotal** | **Double** | The freight amount calculated in accordance with the shipping terms. Not applicable for transfer order types. |  [optional] |
|**freightTotalInBaseCurrency** | **Double** | The freight amount calculated in accordance with the shipping terms in base currency. Not applicable for transfer order types. |  [optional] |
|**orderTotal** | **Double** | The order total |  [optional] |
|**orderTotalInBaseCurrency** | **Double** | The order total in base currency |  [optional] |
|**taxExemptTotal** | **Double** | The VAT exempt total |  [optional] |
|**taxExemptTotalInBaseCurrency** | **Double** | The VAT exempt total in base currency |  [optional] |
|**taxTotal** | **Double** | The tax total |  [optional] |
|**taxTotalInBaseCurrency** | **Double** | The tax total in base currency |  [optional] |
|**taxableTotal** | **Double** | The VAT taxable total |  [optional] |
|**taxableTotalInBaseCurrency** | **Double** | The VAT taxable in base currency |  [optional] |
|**unbilledAmount** | **Double** | The sum of unbilled amounts for the lines |  [optional] |
|**unbilledAmountInBaseCurrency** | **Double** | The sum of unbilled amounts for the lines in base currency |  [optional] |
|**unshippedAmount** | **Double** | The sum of unshipped amounts for the lines |  [optional] |
|**unshippedAmountInBaseCurrency** | **Double** | The sum of unshipped amounts for the lines in base currency |  [optional] |



