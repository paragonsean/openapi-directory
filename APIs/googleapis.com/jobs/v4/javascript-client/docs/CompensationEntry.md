# CloudTalentSolutionApi.CompensationEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**Money**](Money.md) |  | [optional] 
**description** | **String** | Compensation description. For example, could indicate equity terms or provide additional context to an estimated bonus. | [optional] 
**expectedUnitsPerYear** | **Number** | Expected number of units paid each year. If not specified, when Job.employment_types is FULLTIME, a default value is inferred based on unit. Default values: - HOURLY: 2080 - DAILY: 260 - WEEKLY: 52 - MONTHLY: 12 - ANNUAL: 1 | [optional] 
**range** | [**CompensationRange**](CompensationRange.md) |  | [optional] 
**type** | **String** | Compensation type. Default is CompensationType.COMPENSATION_TYPE_UNSPECIFIED. | [optional] 
**unit** | **String** | Frequency of the specified amount. Default is CompensationUnit.COMPENSATION_UNIT_UNSPECIFIED. | [optional] 



## Enum: TypeEnum


* `COMPENSATION_TYPE_UNSPECIFIED` (value: `"COMPENSATION_TYPE_UNSPECIFIED"`)

* `BASE` (value: `"BASE"`)

* `BONUS` (value: `"BONUS"`)

* `SIGNING_BONUS` (value: `"SIGNING_BONUS"`)

* `EQUITY` (value: `"EQUITY"`)

* `PROFIT_SHARING` (value: `"PROFIT_SHARING"`)

* `COMMISSIONS` (value: `"COMMISSIONS"`)

* `TIPS` (value: `"TIPS"`)

* `OTHER_COMPENSATION_TYPE` (value: `"OTHER_COMPENSATION_TYPE"`)





## Enum: UnitEnum


* `COMPENSATION_UNIT_UNSPECIFIED` (value: `"COMPENSATION_UNIT_UNSPECIFIED"`)

* `HOURLY` (value: `"HOURLY"`)

* `DAILY` (value: `"DAILY"`)

* `WEEKLY` (value: `"WEEKLY"`)

* `MONTHLY` (value: `"MONTHLY"`)

* `YEARLY` (value: `"YEARLY"`)

* `ONE_TIME` (value: `"ONE_TIME"`)

* `OTHER_COMPENSATION_UNIT` (value: `"OTHER_COMPENSATION_UNIT"`)




