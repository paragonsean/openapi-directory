

# Error

The error object. As per Microsoft One API guidelines - https://github.com/Microsoft/api-guidelines/blob/vNext/Guidelines.md#7102-error-condition-responses.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **ErrorCode** |  |  |
|**details** | [**List&lt;Error&gt;**](Error.md) | An array of details about specific errors that led to this reported error. |  [optional] |
|**innerError** | [**InnerErrorModel**](InnerErrorModel.md) |  |  [optional] |
|**message** | **String** | A human-readable representation of the error. |  [optional] |
|**target** | **String** | The target of the error. |  [optional] |



