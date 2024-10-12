

# CloudErrorBody

Describes a particular API error with an error code and a message.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **String** | An error code that describes the error condition more precisely than an HTTP status code. Can be used to programmatically handle specific error cases. |  [optional] |
|**details** | [**List&lt;CloudErrorBody&gt;**](CloudErrorBody.md) | Contains nested errors that are related to this error. |  [optional] |
|**message** | **String** | A message that describes the error in detail and provides debugging information. |  [optional] |
|**target** | **String** | The target of the particular error (for example, the name of the property in error). |  [optional] |



