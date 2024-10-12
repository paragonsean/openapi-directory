

# NewMessageRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**body** | **String** | HTTP request body (most commonly used for POST and PUT requests). If the request body contains binary data that cannot be included directly in the  JSON, encode the content with Base64 and include the body_encoding attribute accordingly.  |  [optional] |
|**bodyEncoding** | **String** | If the request body was encoded with Base64, this field should be present and set to  \&quot;base64\&quot;. If not specified, defaults to \&quot;plaintext\&quot;  |  [optional] |
|**form** | **String** | JSON object of set of form fields included in a POST request.  Values can either be represented as a string or as an array of strings.  |  [optional] |
|**headers** | **String** | JSON object of header keys and values -- with values as a string or an array of strings. |  [optional] |
|**method** | **String** | HTTP method name (GET, POST, PUT, HEAD, OPTIONS, PATCH, DELETE, etc.) |  [optional] |
|**timestamp** | **Float** | Unix timestamp indicating when the request was made. |  [optional] |
|**url** | **String** | Full URL of the request, including URL querystring parameters. |  [optional] |



