

# BudgetProperties

The properties of the budget.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **BigDecimal** | The total amount of cost to track with the budget |  |
|**category** | [**CategoryEnum**](#CategoryEnum) | The category of the budget, whether the budget tracks cost or something else. |  |
|**currentSpend** | [**CurrentSpend**](CurrentSpend.md) |  |  [optional] |
|**notifications** | [**Map&lt;String, Notification&gt;**](Notification.md) | Dictionary of notifications associated with the budget. Budget can have up to five notifications. |  [optional] |
|**timeGrain** | [**TimeGrainEnum**](#TimeGrainEnum) | The time covered by a budget. Tracking of the amount will be reset based on the time grain. |  |
|**timePeriod** | [**BudgetTimePeriod**](BudgetTimePeriod.md) |  |  |



## Enum: CategoryEnum

| Name | Value |
|---- | -----|
| COST | &quot;Cost&quot; |



## Enum: TimeGrainEnum

| Name | Value |
|---- | -----|
| MONTHLY | &quot;Monthly&quot; |
| QUARTERLY | &quot;Quarterly&quot; |
| ANNUALLY | &quot;Annually&quot; |



