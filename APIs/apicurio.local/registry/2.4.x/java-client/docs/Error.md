

# Error

All error responses, whether `4xx` or `5xx` will include one of these as the response body.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**detail** | **String** | Full details about the error.  This might contain a server stack trace, for example. |  [optional] |
|**errorCode** | **Integer** | The server-side error code. |  [optional] |
|**message** | **String** | The short error message. |  [optional] |
|**name** | **String** | The error name - typically the classname of the exception thrown by the server. |  [optional] |



