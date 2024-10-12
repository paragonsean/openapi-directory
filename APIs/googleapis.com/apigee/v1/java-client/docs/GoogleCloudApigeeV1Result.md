

# GoogleCloudApigeeV1Result

Result is short for \"action result\", could be different types identified by \"action_result\" field. Supported types: 1. DebugInfo : generic debug info collected by runtime recorded as a list of properties. For example, the contents could be virtual host info, state change result, or execution metadata. Required fields : properties, timestamp 2. RequestMessage: information of a http request. Contains headers, request URI and http methods type.Required fields : headers, uri, verb 3. ResponseMessage: information of a http response. Contains headers, reason phrase and http status code. Required fields : headers, reasonPhrase, statusCode 4. ErrorMessage: information of a http error message. Contains detail error message, reason phrase and status code. Required fields : content, headers, reasonPhrase, statusCode 5. VariableAccess: a list of variable access actions, can be Get, Set and Remove. Required fields : accessList

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actionResult** | **String** | Type of the action result. Can be one of the five: DebugInfo, RequestMessage, ResponseMessage, ErrorMessage, VariableAccess |  [optional] |
|**accessList** | [**List&lt;GoogleCloudApigeeV1Access&gt;**](GoogleCloudApigeeV1Access.md) | A list of variable access actions agaist the api proxy. Supported values: Get, Set, Remove. |  [optional] |
|**content** | **String** | Error message content. for example, \&quot;content\&quot; : \&quot;{\\\&quot;fault\\\&quot;:{\\\&quot;faultstring\\\&quot;:\\\&quot;API timed out\\\&quot;,\\\&quot;detail\\\&quot;:{\\\&quot;errorcode\\\&quot;:\\\&quot;flow.APITimedOut\\\&quot;}}}\&quot; |  [optional] |
|**headers** | [**List&lt;GoogleCloudApigeeV1Property&gt;**](GoogleCloudApigeeV1Property.md) | A list of HTTP headers. for example, &#39;\&quot;headers\&quot; : [ { \&quot;name\&quot; : \&quot;Content-Length\&quot;, \&quot;value\&quot; : \&quot;83\&quot; }, { \&quot;name\&quot; : \&quot;Content-Type\&quot;, \&quot;value\&quot; : \&quot;application/json\&quot; } ]&#39; |  [optional] |
|**properties** | [**GoogleCloudApigeeV1Properties**](GoogleCloudApigeeV1Properties.md) |  |  [optional] |
|**reasonPhrase** | **String** | HTTP response phrase |  [optional] |
|**statusCode** | **String** | HTTP response code |  [optional] |
|**timestamp** | **String** | Timestamp of when the result is recorded. Its format is dd-mm-yy hh:mm:ss:xxx. For example, &#x60;\&quot;timestamp\&quot; : \&quot;12-08-19 00:31:59:960\&quot;&#x60; |  [optional] |
|**uRI** | **String** | The relative path of the api proxy. for example, &#x60;\&quot;uRI\&quot; : \&quot;/iloveapis\&quot;&#x60; |  [optional] |
|**verb** | **String** | HTTP method verb |  [optional] |



