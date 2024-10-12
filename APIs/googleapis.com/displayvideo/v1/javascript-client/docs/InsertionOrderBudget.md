# DisplayVideo360Api.InsertionOrderBudget

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**automationType** | **String** | The type of automation used to manage bid and budget for the insertion order. If this field is unspecified in creation, the value defaults to &#x60;INSERTION_ORDER_AUTOMATION_TYPE_NONE&#x60;. | [optional] 
**budgetSegments** | [**[InsertionOrderBudgetSegment]**](InsertionOrderBudgetSegment.md) | Required. The list of budget segments. Use a budget segment to specify a specific budget for a given period of time an insertion order is running. | [optional] 
**budgetUnit** | **String** | Required. Immutable. The budget unit specifies whether the budget is currency based or impression based. | [optional] 



## Enum: AutomationTypeEnum


* `UNSPECIFIED` (value: `"INSERTION_ORDER_AUTOMATION_TYPE_UNSPECIFIED"`)

* `BUDGET` (value: `"INSERTION_ORDER_AUTOMATION_TYPE_BUDGET"`)

* `NONE` (value: `"INSERTION_ORDER_AUTOMATION_TYPE_NONE"`)

* `BID_BUDGET` (value: `"INSERTION_ORDER_AUTOMATION_TYPE_BID_BUDGET"`)





## Enum: BudgetUnitEnum


* `UNSPECIFIED` (value: `"BUDGET_UNIT_UNSPECIFIED"`)

* `CURRENCY` (value: `"BUDGET_UNIT_CURRENCY"`)

* `IMPRESSIONS` (value: `"BUDGET_UNIT_IMPRESSIONS"`)




