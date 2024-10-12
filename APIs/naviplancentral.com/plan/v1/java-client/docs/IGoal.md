

# IGoal


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assetsRemainingAfterFundingGoal** | [**IOptionalFieldCurrency**](IOptionalFieldCurrency.md) |  |  [optional] |
|**coverage** | [**IOptionalFieldGoalCoveragePercent**](IOptionalFieldGoalCoveragePercent.md) |  |  [optional] |
|**description** | **String** |  |  [optional] [readonly] |
|**endDate** | [**Date**](Date.md) |  |  [optional] |
|**identifier** | [**GoalId**](GoalId.md) |  |  [optional] |
|**startDate** | [**Date**](Date.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] [readonly] |
|**yearAssetsDepleted** | [**IOptionalFieldYear**](IOptionalFieldYear.md) |  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| RETIREMENT | &quot;Retirement&quot; |
| SURVIVOR_INCOME | &quot;SurvivorIncome&quot; |
| CRITICAL_ILLNESS | &quot;CriticalIllness&quot; |
| LONG_TERM_CARE_INSURANCE | &quot;LongTermCareInsurance&quot; |
| CASHFLOW | &quot;Cashflow&quot; |
| DISABILITY_INCOME | &quot;DisabilityIncome&quot; |
| EDUCATION | &quot;Education&quot; |
| MAJOR_PURCHASE | &quot;MajorPurchase&quot; |
| EMERGENCY_FUND | &quot;EmergencyFund&quot; |
| UNDEFINED | &quot;Undefined&quot; |
| NOT_SUPPORTED | &quot;NotSupported&quot; |



