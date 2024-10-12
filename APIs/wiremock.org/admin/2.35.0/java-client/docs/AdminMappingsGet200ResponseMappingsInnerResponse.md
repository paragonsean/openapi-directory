

# AdminMappingsGet200ResponseMappingsInnerResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalProxyRequestHeaders** | **Object** | Extra request headers to send when proxying to another host. |  [optional] |
|**base64Body** | **String** | The response body as a base64 encoded string (useful for binary content). Only one of body, base64Body, jsonBody or bodyFileName may be specified. |  [optional] |
|**body** | **String** | The response body as a string. Only one of body, base64Body, jsonBody or bodyFileName may be specified. |  [optional] |
|**bodyFileName** | **String** | The path to the file containing the response body, relative to the configured file root. Only one of body, base64Body, jsonBody or bodyFileName may be specified. |  [optional] |
|**delayDistribution** | [**AdminMappingsGet200ResponseMappingsInnerResponseAllOfDelayDistribution**](AdminMappingsGet200ResponseMappingsInnerResponseAllOfDelayDistribution.md) |  |  [optional] |
|**fault** | [**FaultEnum**](#FaultEnum) | The fault to apply (instead of a full, valid response). |  [optional] |
|**fixedDelayMilliseconds** | **Integer** | Number of milliseconds to delay be before sending the response. |  [optional] |
|**fromConfiguredStub** | **Boolean** | Read-only flag indicating false if this was the default, unmatched response. Not present otherwise. |  [optional] |
|**headers** | **Object** | Map of response headers to send |  [optional] |
|**jsonBody** | **Object** | The response body as a JSON object. Only one of body, base64Body, jsonBody or bodyFileName may be specified. |  [optional] |
|**proxyBaseUrl** | **String** | The base URL of the target to proxy matching requests to. |  [optional] |
|**status** | **Integer** | The HTTP status code to be returned |  [optional] |
|**statusMessage** | **String** | The HTTP status message to be returned |  [optional] |
|**transformerParameters** | **Object** | Parameters to apply to response transformers. |  [optional] |
|**transformers** | **List&lt;String&gt;** | List of names of transformers to apply to this response. |  [optional] |



## Enum: FaultEnum

| Name | Value |
|---- | -----|
| CONNECTION_RESET_BY_PEER | &quot;CONNECTION_RESET_BY_PEER&quot; |
| EMPTY_RESPONSE | &quot;EMPTY_RESPONSE&quot; |
| MALFORMED_RESPONSE_CHUNK | &quot;MALFORMED_RESPONSE_CHUNK&quot; |
| RANDOM_DATA_THEN_CLOSE | &quot;RANDOM_DATA_THEN_CLOSE&quot; |



