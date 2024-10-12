

# TimeOffRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **BigDecimal** | The amount of time off requested. |  [optional] |
|**approvalDate** | **String** | The date the request was approved |  [optional] |
|**createdAt** | **OffsetDateTime** | The date and time when the object was created. |  [optional] [readonly] |
|**createdBy** | **String** | The user who created the object. |  [optional] [readonly] |
|**customMappings** | **Object** | When custom mappings are configured on the resource, the result is included here. |  [optional] |
|**description** | **String** | Description of the time off request. |  [optional] |
|**employeeId** | **String** | ID of the employee |  [optional] |
|**endDate** | **String** | The end date of the time off request. |  [optional] |
|**id** | **String** | A unique identifier for an object. |  [optional] [readonly] |
|**notes** | [**TimeOffRequestNotes**](TimeOffRequestNotes.md) |  |  [optional] |
|**policyId** | **String** | ID of the policy |  [optional] |
|**requestDate** | **String** | The date the request was made. |  [optional] |
|**requestType** | [**RequestTypeEnum**](#RequestTypeEnum) | The type of request |  [optional] |
|**startDate** | **String** | The start date of the time off request. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the time off request. |  [optional] |
|**units** | [**UnitsEnum**](#UnitsEnum) | The unit of time off requested. Possible values include: &#x60;hours&#x60;, &#x60;days&#x60;, or &#x60;other&#x60;. |  [optional] |
|**updatedAt** | **OffsetDateTime** | The date and time when the object was last updated. |  [optional] [readonly] |
|**updatedBy** | **String** | The user who last updated the object. |  [optional] [readonly] |



## Enum: RequestTypeEnum

| Name | Value |
|---- | -----|
| VACATION | &quot;vacation&quot; |
| SICK | &quot;sick&quot; |
| PERSONAL | &quot;personal&quot; |
| JURY_DUTY | &quot;jury_duty&quot; |
| VOLUNTEER | &quot;volunteer&quot; |
| BEREAVEMENT | &quot;bereavement&quot; |
| OTHER | &quot;other&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| REQUESTED | &quot;requested&quot; |
| APPROVED | &quot;approved&quot; |
| DECLINED | &quot;declined&quot; |
| CANCELLED | &quot;cancelled&quot; |
| DELETED | &quot;deleted&quot; |
| OTHER | &quot;other&quot; |



## Enum: UnitsEnum

| Name | Value |
|---- | -----|
| DAYS | &quot;days&quot; |
| HOURS | &quot;hours&quot; |
| OTHER | &quot;other&quot; |



