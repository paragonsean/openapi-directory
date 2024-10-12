

# BatchResponse

A response object returned from a batch request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**body** | **Object** | The JSON body that the invoked endpoint returned. |  [optional] |
|**headers** | **Object** | A map of HTTP headers specific to this result. This is primarily used for returning a &#x60;Location&#x60; header to accompany a &#x60;201 Created&#x60; result.  The parent HTTP response will contain all common headers. |  [optional] |
|**statusCode** | **Integer** | The HTTP status code that the invoked endpoint returned. |  [optional] |



