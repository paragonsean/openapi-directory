

# OperatingStatus

Current status of facility operations. The overall status of the facility, which can be: Normal Hours and Services, Facility Notice, Limited Hours and/or Services, or Closed. This field replaces active_status.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalInfo** | **String** | Details of facility notices for visitors, such as messages about parking lot closures or floor visitation information. |  [optional] |
|**code** | [**CodeEnum**](#CodeEnum) | Status codes indicate normal hours/services, limited hours/services, closed operations, or published facility notices for visitors. |  |
|**supplementalStatus** | [**List&lt;SupplementalStatus&gt;**](SupplementalStatus.md) | List of supplemental statuses for VA facility. |  [optional] |



## Enum: CodeEnum

| Name | Value |
|---- | -----|
| NORMAL | &quot;NORMAL&quot; |
| NOTICE | &quot;NOTICE&quot; |
| LIMITED | &quot;LIMITED&quot; |
| CLOSED | &quot;CLOSED&quot; |



