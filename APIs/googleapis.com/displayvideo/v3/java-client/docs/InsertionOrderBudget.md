

# InsertionOrderBudget

Settings that control how insertion order budget is allocated.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**automationType** | [**AutomationTypeEnum**](#AutomationTypeEnum) | The type of automation used to manage bid and budget for the insertion order. If this field is unspecified in creation, the value defaults to &#x60;INSERTION_ORDER_AUTOMATION_TYPE_NONE&#x60;. |  [optional] |
|**budgetSegments** | [**List&lt;InsertionOrderBudgetSegment&gt;**](InsertionOrderBudgetSegment.md) | Required. The list of budget segments. Use a budget segment to specify a specific budget for a given period of time an insertion order is running. |  [optional] |
|**budgetUnit** | [**BudgetUnitEnum**](#BudgetUnitEnum) | Required. Immutable. The budget unit specifies whether the budget is currency based or impression based. |  [optional] |



## Enum: AutomationTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;INSERTION_ORDER_AUTOMATION_TYPE_UNSPECIFIED&quot; |
| BUDGET | &quot;INSERTION_ORDER_AUTOMATION_TYPE_BUDGET&quot; |
| NONE | &quot;INSERTION_ORDER_AUTOMATION_TYPE_NONE&quot; |
| BID_BUDGET | &quot;INSERTION_ORDER_AUTOMATION_TYPE_BID_BUDGET&quot; |



## Enum: BudgetUnitEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;BUDGET_UNIT_UNSPECIFIED&quot; |
| CURRENCY | &quot;BUDGET_UNIT_CURRENCY&quot; |
| IMPRESSIONS | &quot;BUDGET_UNIT_IMPRESSIONS&quot; |



