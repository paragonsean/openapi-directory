

# InnerErrorModel

An object containing more specific information about the error. As per Microsoft One API guidelines - https://github.com/Microsoft/api-guidelines/blob/vNext/Guidelines.md#7102-error-condition-responses.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **String** | A more specific error code than was provided by the containing error. |  [optional] |
|**innerError** | [**InnerErrorModel**](InnerErrorModel.md) |  |  [optional] |



