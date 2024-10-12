# CloudTalentSolutionApi.CompensationFilter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**includeJobsWithUnspecifiedCompensationRange** | **Boolean** | Optional. If set to true, jobs with unspecified compensation range fields are included. | [optional] 
**range** | [**CompensationRange**](CompensationRange.md) |  | [optional] 
**type** | **String** | Required. Type of filter. | [optional] 
**units** | **[String]** | Required. Specify desired &#x60;base compensation entry&#39;s&#x60; CompensationInfo.CompensationUnit. | [optional] 



## Enum: TypeEnum


* `FILTER_TYPE_UNSPECIFIED` (value: `"FILTER_TYPE_UNSPECIFIED"`)

* `UNIT_ONLY` (value: `"UNIT_ONLY"`)

* `UNIT_AND_AMOUNT` (value: `"UNIT_AND_AMOUNT"`)

* `ANNUALIZED_BASE_AMOUNT` (value: `"ANNUALIZED_BASE_AMOUNT"`)

* `ANNUALIZED_TOTAL_AMOUNT` (value: `"ANNUALIZED_TOTAL_AMOUNT"`)





## Enum: [UnitsEnum]


* `COMPENSATION_UNIT_UNSPECIFIED` (value: `"COMPENSATION_UNIT_UNSPECIFIED"`)

* `HOURLY` (value: `"HOURLY"`)

* `DAILY` (value: `"DAILY"`)

* `WEEKLY` (value: `"WEEKLY"`)

* `MONTHLY` (value: `"MONTHLY"`)

* `YEARLY` (value: `"YEARLY"`)

* `ONE_TIME` (value: `"ONE_TIME"`)

* `OTHER_COMPENSATION_UNIT` (value: `"OTHER_COMPENSATION_UNIT"`)




