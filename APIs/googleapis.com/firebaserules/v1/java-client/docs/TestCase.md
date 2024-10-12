

# TestCase

`TestCase` messages provide the request context and an expectation as to whether the given context will be allowed or denied. Test cases may specify the `request`, `resource`, and `function_mocks` to mock a function call to a service-provided function. The `request` object represents context present at request-time. The `resource` is the value of the target resource as it appears in persistent storage before the request is executed.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**expectation** | [**ExpectationEnum**](#ExpectationEnum) | Test expectation. |  [optional] |
|**expressionReportLevel** | [**ExpressionReportLevelEnum**](#ExpressionReportLevelEnum) | Specifies what should be included in the response. |  [optional] |
|**functionMocks** | [**List&lt;FunctionMock&gt;**](FunctionMock.md) | Optional function mocks for service-defined functions. If not set, any service defined function is expected to return an error, which may or may not influence the test outcome. |  [optional] |
|**pathEncoding** | [**PathEncodingEnum**](#PathEncodingEnum) | Specifies whether paths (such as request.path) are encoded and how. |  [optional] |
|**request** | **Object** | Request context. The exact format of the request context is service-dependent. See the appropriate service documentation for information about the supported fields and types on the request. Minimally, all services support the following fields and types: Request field | Type ---------------|----------------- auth.uid | &#x60;string&#x60; auth.token | &#x60;map&#x60; headers | &#x60;map&#x60; method | &#x60;string&#x60; params | &#x60;map&#x60; path | &#x60;string&#x60; time | &#x60;google.protobuf.Timestamp&#x60; If the request value is not well-formed for the service, the request will be rejected as an invalid argument. |  [optional] |
|**resource** | **Object** | Optional resource value as it appears in persistent storage before the request is fulfilled. The resource type depends on the &#x60;request.path&#x60; value. |  [optional] |



## Enum: ExpectationEnum

| Name | Value |
|---- | -----|
| EXPECTATION_UNSPECIFIED | &quot;EXPECTATION_UNSPECIFIED&quot; |
| ALLOW | &quot;ALLOW&quot; |
| DENY | &quot;DENY&quot; |



## Enum: ExpressionReportLevelEnum

| Name | Value |
|---- | -----|
| LEVEL_UNSPECIFIED | &quot;LEVEL_UNSPECIFIED&quot; |
| NONE | &quot;NONE&quot; |
| FULL | &quot;FULL&quot; |
| VISITED | &quot;VISITED&quot; |



## Enum: PathEncodingEnum

| Name | Value |
|---- | -----|
| ENCODING_UNSPECIFIED | &quot;ENCODING_UNSPECIFIED&quot; |
| URL_ENCODED | &quot;URL_ENCODED&quot; |
| PLAIN | &quot;PLAIN&quot; |



