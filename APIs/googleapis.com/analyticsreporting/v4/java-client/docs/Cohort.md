

# Cohort

Defines a cohort. A cohort is a group of users who share a common characteristic. For example, all users with the same acquisition date belong to the same cohort.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dateRange** | [**DateRange**](DateRange.md) |  |  [optional] |
|**name** | **String** | A unique name for the cohort. If not defined name will be auto-generated with values cohort_[1234...]. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of the cohort. The only supported type as of now is &#x60;FIRST_VISIT_DATE&#x60;. If this field is unspecified the cohort is treated as &#x60;FIRST_VISIT_DATE&#x60; type cohort. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED_COHORT_TYPE | &quot;UNSPECIFIED_COHORT_TYPE&quot; |
| FIRST_VISIT_DATE | &quot;FIRST_VISIT_DATE&quot; |



