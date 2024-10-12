

# TCPHealthCheck


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**receive** | **List&lt;String&gt;** | An array of base64 encoded strings, each representing array of bytes that is expected in health check responses. When checking the response, \&quot;fuzzy\&quot; matching is performed such that each binary block must be found, and in the order specified, but not necessarily contiguously.  |  [optional] |
|**send** | **String** | Base64 encoded string representing an array of bytes to be sent in health check requests. Leaving this field empty implies a connect-only health check.  |  [optional] |



