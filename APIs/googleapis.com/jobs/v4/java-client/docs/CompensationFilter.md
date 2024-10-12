

# CompensationFilter

Filter on job compensation type and amount.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**includeJobsWithUnspecifiedCompensationRange** | **Boolean** | If set to true, jobs with unspecified compensation range fields are included. |  [optional] |
|**range** | [**CompensationRange**](CompensationRange.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Required. Type of filter. |  [optional] |
|**units** | [**List&lt;UnitsEnum&gt;**](#List&lt;UnitsEnum&gt;) | Required. Specify desired &#x60;base compensation entry&#39;s&#x60; CompensationInfo.CompensationUnit. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| FILTER_TYPE_UNSPECIFIED | &quot;FILTER_TYPE_UNSPECIFIED&quot; |
| UNIT_ONLY | &quot;UNIT_ONLY&quot; |
| UNIT_AND_AMOUNT | &quot;UNIT_AND_AMOUNT&quot; |
| ANNUALIZED_BASE_AMOUNT | &quot;ANNUALIZED_BASE_AMOUNT&quot; |
| ANNUALIZED_TOTAL_AMOUNT | &quot;ANNUALIZED_TOTAL_AMOUNT&quot; |



## Enum: List&lt;UnitsEnum&gt;

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



