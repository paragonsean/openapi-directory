# ConsumptionManagementClient.BudgetProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **Number** | The total amount of cost to track with the budget | 
**category** | **String** | The category of the budget, whether the budget tracks cost or usage. | 
**currentSpend** | [**CurrentSpend**](CurrentSpend.md) |  | [optional] 
**filters** | [**Filters**](Filters.md) |  | [optional] 
**notifications** | [**{String: Notification}**](Notification.md) | Dictionary of notifications associated with the budget. Budget can have up to five notifications. | [optional] 
**timeGrain** | **String** | The time covered by a budget. Tracking of the amount will be reset based on the time grain. | 
**timePeriod** | [**BudgetTimePeriod**](BudgetTimePeriod.md) |  | 



## Enum: CategoryEnum


* `Cost` (value: `"Cost"`)

* `Usage` (value: `"Usage"`)





## Enum: TimeGrainEnum


* `Monthly` (value: `"Monthly"`)

* `Quarterly` (value: `"Quarterly"`)

* `Annually` (value: `"Annually"`)

* `BillingMonth` (value: `"BillingMonth"`)

* `BillingQuarter` (value: `"BillingQuarter"`)

* `BillingAnnual` (value: `"BillingAnnual"`)




