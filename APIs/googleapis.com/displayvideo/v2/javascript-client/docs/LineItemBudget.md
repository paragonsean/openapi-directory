# DisplayVideo360Api.LineItemBudget

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**budgetAllocationType** | **String** | Required. The type of the budget allocation. &#x60;LINE_ITEM_BUDGET_ALLOCATION_TYPE_AUTOMATIC&#x60; is only applicable when automatic budget allocation is enabled for the parent insertion order. | [optional] 
**budgetUnit** | **String** | Output only. The budget unit specifies whether the budget is currency based or impression based. This value is inherited from the parent insertion order. | [optional] [readonly] 
**maxAmount** | **String** | The maximum budget amount the line item will spend. Must be greater than 0. When budget_allocation_type is: * &#x60;LINE_ITEM_BUDGET_ALLOCATION_TYPE_AUTOMATIC&#x60;, this field is immutable and is set by the system. * &#x60;LINE_ITEM_BUDGET_ALLOCATION_TYPE_FIXED&#x60;, if budget_unit is: - &#x60;BUDGET_UNIT_CURRENCY&#x60;, this field represents maximum budget amount to spend, in micros of the advertiser&#39;s currency. For example, 1500000 represents 1.5 standard units of the currency. - &#x60;BUDGET_UNIT_IMPRESSIONS&#x60;, this field represents the maximum number of impressions to serve. * &#x60;LINE_ITEM_BUDGET_ALLOCATION_TYPE_UNLIMITED&#x60;, this field is not applicable and will be ignored by the system. | [optional] 



## Enum: BudgetAllocationTypeEnum


* `UNSPECIFIED` (value: `"LINE_ITEM_BUDGET_ALLOCATION_TYPE_UNSPECIFIED"`)

* `AUTOMATIC` (value: `"LINE_ITEM_BUDGET_ALLOCATION_TYPE_AUTOMATIC"`)

* `FIXED` (value: `"LINE_ITEM_BUDGET_ALLOCATION_TYPE_FIXED"`)

* `UNLIMITED` (value: `"LINE_ITEM_BUDGET_ALLOCATION_TYPE_UNLIMITED"`)





## Enum: BudgetUnitEnum


* `UNSPECIFIED` (value: `"BUDGET_UNIT_UNSPECIFIED"`)

* `CURRENCY` (value: `"BUDGET_UNIT_CURRENCY"`)

* `IMPRESSIONS` (value: `"BUDGET_UNIT_IMPRESSIONS"`)




