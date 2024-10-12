

# NewMessageResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**body** | **String** | HTTP response body. If the response body contains binary data that cannot be included directly in the JSON, you should encode the content with Base64.  |  [optional] |
|**bodyEncoding** | **String** | If the request body was encoded with Base64, this field should be present and set to  \&quot;base64\&quot;. If not specified, defaults to \&quot;plaintext\&quot;  |  [optional] |
|**headers** | **String** | JSON object of header keys and values -- with values as a string or an array of strings. |  [optional] |
|**reason** | **String** | Textual description of HTTP status code. This will be set automatically if not  provided in the API call. For example, if the status code is 404, this will be  set to \&quot;Not Found\&quot; unless you explicitly specify a different reason.  |  [optional] |
|**responseTime** | **Float** | Length of time it took to receive the response, in seconds. |  [optional] |
|**status** | **Integer** | HTTP status code returned in the response. |  [optional] |
|**timestamp** | **Float** | Unix timestamp indicating when the request was made. |  [optional] |



