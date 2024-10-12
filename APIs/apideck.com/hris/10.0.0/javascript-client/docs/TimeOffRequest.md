# HrisApi.TimeOffRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **Number** | The amount of time off requested. | [optional] 
**approvalDate** | **String** | The date the request was approved | [optional] 
**createdAt** | **Date** | The date and time when the object was created. | [optional] [readonly] 
**createdBy** | **String** | The user who created the object. | [optional] [readonly] 
**customMappings** | **Object** | When custom mappings are configured on the resource, the result is included here. | [optional] 
**description** | **String** | Description of the time off request. | [optional] 
**employeeId** | **String** | ID of the employee | [optional] 
**endDate** | **String** | The end date of the time off request. | [optional] 
**id** | **String** | A unique identifier for an object. | [optional] [readonly] 
**notes** | [**TimeOffRequestNotes**](TimeOffRequestNotes.md) |  | [optional] 
**policyId** | **String** | ID of the policy | [optional] 
**requestDate** | **String** | The date the request was made. | [optional] 
**requestType** | **String** | The type of request | [optional] 
**startDate** | **String** | The start date of the time off request. | [optional] 
**status** | **String** | The status of the time off request. | [optional] 
**units** | **String** | The unit of time off requested. Possible values include: &#x60;hours&#x60;, &#x60;days&#x60;, or &#x60;other&#x60;. | [optional] 
**updatedAt** | **Date** | The date and time when the object was last updated. | [optional] [readonly] 
**updatedBy** | **String** | The user who last updated the object. | [optional] [readonly] 



## Enum: RequestTypeEnum


* `vacation` (value: `"vacation"`)

* `sick` (value: `"sick"`)

* `personal` (value: `"personal"`)

* `jury_duty` (value: `"jury_duty"`)

* `volunteer` (value: `"volunteer"`)

* `bereavement` (value: `"bereavement"`)

* `other` (value: `"other"`)





## Enum: StatusEnum


* `requested` (value: `"requested"`)

* `approved` (value: `"approved"`)

* `declined` (value: `"declined"`)

* `cancelled` (value: `"cancelled"`)

* `deleted` (value: `"deleted"`)

* `other` (value: `"other"`)





## Enum: UnitsEnum


* `days` (value: `"days"`)

* `hours` (value: `"hours"`)

* `other` (value: `"other"`)




