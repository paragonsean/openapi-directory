

# TestReturn

TestReturn is used for wrapping the return code of a test step execution

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **Integer** | Return code for test (0 means Success, 1 means Failure) |  |
|**elapsedTime** | **Long** | Elapsed time in milliseconds |  |
|**eventMessage** | [**EventMessage**](EventMessage.md) |  |  [optional] |
|**message** | **String** | Error message if any |  [optional] |
|**request** | [**Request**](Request.md) |  |  [optional] |
|**response** | [**Response**](Response.md) |  |  [optional] |



