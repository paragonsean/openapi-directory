# AppServiceEnvironmentsApiClient.AppServiceEnvironmentsListOperations200ResponseInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdTime** | **Date** | Time when operation has started. | [optional] 
**errors** | [**[AppServiceEnvironmentsListOperations200ResponseInnerErrorsInner]**](AppServiceEnvironmentsListOperations200ResponseInnerErrorsInner.md) | Any errors associate with the operation. | [optional] 
**expirationTime** | **Date** | Time when operation will expire. | [optional] 
**geoMasterOperationId** | **String** | Applicable only for stamp operation ids. | [optional] 
**id** | **String** | Operation ID. | [optional] 
**modifiedTime** | **Date** | Time when operation has been updated. | [optional] 
**name** | **String** | Operation name. | [optional] 
**status** | **String** | The current status of the operation. | [optional] 



## Enum: StatusEnum


* `InProgress` (value: `"InProgress"`)

* `Failed` (value: `"Failed"`)

* `Succeeded` (value: `"Succeeded"`)

* `TimedOut` (value: `"TimedOut"`)

* `Created` (value: `"Created"`)




