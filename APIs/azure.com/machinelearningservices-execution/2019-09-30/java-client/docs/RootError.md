

# RootError

The root error.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **String** | The service-defined error code. Supported error codes: ServiceError, UserError, ValidationError, AzureStorageError, TransientError, RequestThrottled. |  [optional] |
|**details** | [**List&lt;ErrorDetails&gt;**](ErrorDetails.md) | The related errors that occurred during the request. |  [optional] |
|**innerError** | [**InnerErrorResponse**](InnerErrorResponse.md) |  |  [optional] |
|**message** | **String** | A human-readable representation of the error. |  [optional] |
|**target** | **String** | The target of the error (e.g., the name of the property in error). |  [optional] |



