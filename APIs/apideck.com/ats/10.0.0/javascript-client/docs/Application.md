# AtsApi.Application

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicantId** | **String** |  | 
**createdAt** | **Date** | The date and time when the object was created. | [optional] [readonly] 
**createdBy** | **String** | The user who created the object. | [optional] [readonly] 
**customMappings** | **Object** | When custom mappings are configured on the resource, the result is included here. | [optional] 
**id** | **String** | A unique identifier for an object. | [optional] [readonly] 
**jobId** | **String** |  | 
**stage** | [**ApplicationStage**](ApplicationStage.md) |  | [optional] 
**status** | **String** |  | [optional] 
**updatedAt** | **Date** | The date and time when the object was last updated. | [optional] [readonly] 
**updatedBy** | **String** | The user who last updated the object. | [optional] [readonly] 



## Enum: StatusEnum


* `open` (value: `"open"`)

* `rejected` (value: `"rejected"`)

* `hired` (value: `"hired"`)

* `converted` (value: `"converted"`)

* `other` (value: `"other"`)




