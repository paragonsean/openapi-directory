# BatchService.TaskSchedulingError

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **String** | The category of the task scheduling error. | 
**code** | **String** | An identifier for the task scheduling error. Codes are invariant and are intended to be consumed programmatically. | [optional] 
**details** | [**[NameValuePair]**](NameValuePair.md) | The list of additional error details related to the scheduling error. | [optional] 
**message** | **String** | A message describing the task scheduling error, intended to be suitable for display in a user interface. | [optional] 



## Enum: CategoryEnum


* `usererror` (value: `"usererror"`)

* `servererror` (value: `"servererror"`)

* `unmapped` (value: `"unmapped"`)




