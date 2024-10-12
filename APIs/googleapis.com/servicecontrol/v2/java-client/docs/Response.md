

# Response

This message defines attributes for a typical network response. It generally models semantics of an HTTP response.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backendLatency** | **String** | The amount of time it takes the backend service to fully respond to a request. Measured from when the destination service starts to send the request to the backend until when the destination service receives the complete response from the backend. |  [optional] |
|**code** | **String** | The HTTP response status code, such as &#x60;200&#x60; and &#x60;404&#x60;. |  [optional] |
|**headers** | **Map&lt;String, String&gt;** | The HTTP response headers. If multiple headers share the same key, they must be merged according to HTTP spec. All header keys must be lowercased, because HTTP header keys are case-insensitive. |  [optional] |
|**size** | **String** | The HTTP response size in bytes. If unknown, it must be -1. |  [optional] |
|**time** | **String** | The timestamp when the &#x60;destination&#x60; service sends the last byte of the response. |  [optional] |



