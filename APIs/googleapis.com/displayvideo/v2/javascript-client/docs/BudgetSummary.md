# DisplayVideo360Api.BudgetSummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**externalBudgetId** | **String** | Corresponds to the external_budget_id of a campaign budget. If the value is not set in the campaign budget, this field will be empty. | [optional] 
**preTaxAmountMicros** | **String** | The sum of charges made under this budget before taxes, in micros of the invoice&#39;s currency. For example, if currency_code is &#x60;USD&#x60;, then 1000000 represents one US dollar. | [optional] 
**prismaCpeCode** | [**PrismaCpeCode**](PrismaCpeCode.md) |  | [optional] 
**taxAmountMicros** | **String** | The amount of tax applied to charges under this budget, in micros of the invoice&#39;s currency. For example, if currency_code is &#x60;USD&#x60;, then 1000000 represents one US dollar. | [optional] 
**totalAmountMicros** | **String** | The total sum of charges made under this budget, including tax, in micros of the invoice&#39;s currency. For example, if currency_code is &#x60;USD&#x60;, then 1000000 represents one US dollar. | [optional] 


