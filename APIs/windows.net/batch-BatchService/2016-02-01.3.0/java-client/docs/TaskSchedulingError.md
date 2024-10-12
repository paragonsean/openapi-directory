

# TaskSchedulingError

Information about an error when scheduling a task.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**category** | [**CategoryEnum**](#CategoryEnum) | The category of the task scheduling error. |  |
|**code** | **String** | An identifier for the task scheduling error. Codes are invariant and are intended to be consumed programmatically. |  [optional] |
|**details** | [**List&lt;NameValuePair&gt;**](NameValuePair.md) | The list of additional error details related to the scheduling error. |  [optional] |
|**message** | **String** | A message describing the task scheduling error, intended to be suitable for display in a user interface. |  [optional] |



## Enum: CategoryEnum

| Name | Value |
|---- | -----|
| USERERROR | &quot;usererror&quot; |
| SERVERERROR | &quot;servererror&quot; |
| UNMAPPED | &quot;unmapped&quot; |



