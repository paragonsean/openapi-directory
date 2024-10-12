

# AlertDefinition

The definition (rule) of an Alert

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**category** | [**CategoryEnum**](#CategoryEnum) | Category of the alert. |  [optional] [readonly] |
|**criteria** | [**CriteriaEnum**](#CriteriaEnum) | Criteria (condition) of the alert. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of cost-entity the alert is defined on. |  [optional] [readonly] |



## Enum: CategoryEnum

| Name | Value |
|---- | -----|
| COST | &quot;Cost&quot; |
| USAGE | &quot;Usage&quot; |
| BILLING | &quot;Billing&quot; |



## Enum: CriteriaEnum

| Name | Value |
|---- | -----|
| COST_THRESHOLD_EXCEEDED | &quot;CostThresholdExceeded&quot; |
| USAGE_THRESHOLD_EXCEEDED | &quot;UsageThresholdExceeded&quot; |
| CREDIT_THRESHOLD_REACHED | &quot;CreditThresholdReached&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| BUDGET | &quot;Budget&quot; |
| INVOICE | &quot;Invoice&quot; |
| CREDIT | &quot;Credit&quot; |



