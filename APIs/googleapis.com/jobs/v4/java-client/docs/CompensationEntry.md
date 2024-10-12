

# CompensationEntry

A compensation entry that represents one component of compensation, such as base pay, bonus, or other compensation type. Annualization: One compensation entry can be annualized if - it contains valid amount or range. - and its expected_units_per_year is set or can be derived. Its annualized range is determined as (amount or range) times expected_units_per_year.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | [**Money**](Money.md) |  |  [optional] |
|**description** | **String** | Compensation description. For example, could indicate equity terms or provide additional context to an estimated bonus. |  [optional] |
|**expectedUnitsPerYear** | **Double** | Expected number of units paid each year. If not specified, when Job.employment_types is FULLTIME, a default value is inferred based on unit. Default values: - HOURLY: 2080 - DAILY: 260 - WEEKLY: 52 - MONTHLY: 12 - ANNUAL: 1 |  [optional] |
|**range** | [**CompensationRange**](CompensationRange.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Compensation type. Default is CompensationType.COMPENSATION_TYPE_UNSPECIFIED. |  [optional] |
|**unit** | [**UnitEnum**](#UnitEnum) | Frequency of the specified amount. Default is CompensationUnit.COMPENSATION_UNIT_UNSPECIFIED. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| COMPENSATION_TYPE_UNSPECIFIED | &quot;COMPENSATION_TYPE_UNSPECIFIED&quot; |
| BASE | &quot;BASE&quot; |
| BONUS | &quot;BONUS&quot; |
| SIGNING_BONUS | &quot;SIGNING_BONUS&quot; |
| EQUITY | &quot;EQUITY&quot; |
| PROFIT_SHARING | &quot;PROFIT_SHARING&quot; |
| COMMISSIONS | &quot;COMMISSIONS&quot; |
| TIPS | &quot;TIPS&quot; |
| OTHER_COMPENSATION_TYPE | &quot;OTHER_COMPENSATION_TYPE&quot; |



## Enum: UnitEnum

| Name | Value |
|---- | -----|
| COMPENSATION_UNIT_UNSPECIFIED | &quot;COMPENSATION_UNIT_UNSPECIFIED&quot; |
| HOURLY | &quot;HOURLY&quot; |
| DAILY | &quot;DAILY&quot; |
| WEEKLY | &quot;WEEKLY&quot; |
| MONTHLY | &quot;MONTHLY&quot; |
| YEARLY | &quot;YEARLY&quot; |
| ONE_TIME | &quot;ONE_TIME&quot; |
| OTHER_COMPENSATION_UNIT | &quot;OTHER_COMPENSATION_UNIT&quot; |



