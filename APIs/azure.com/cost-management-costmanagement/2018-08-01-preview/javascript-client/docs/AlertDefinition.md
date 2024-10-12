# CostManagementClient.AlertDefinition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **String** | Category of the alert. | [optional] [readonly] 
**criteria** | **String** | Criteria (condition) of the alert. | [optional] [readonly] 
**type** | **String** | The type of cost-entity the alert is defined on. | [optional] [readonly] 



## Enum: CategoryEnum


* `Cost` (value: `"Cost"`)

* `Usage` (value: `"Usage"`)

* `Billing` (value: `"Billing"`)





## Enum: CriteriaEnum


* `CostThresholdExceeded` (value: `"CostThresholdExceeded"`)

* `UsageThresholdExceeded` (value: `"UsageThresholdExceeded"`)

* `CreditThresholdReached` (value: `"CreditThresholdReached"`)





## Enum: TypeEnum


* `Budget` (value: `"Budget"`)

* `Invoice` (value: `"Invoice"`)

* `Credit` (value: `"Credit"`)




