# FirebaseRulesApi.TestCase

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expectation** | **String** | Test expectation. | [optional] 
**expressionReportLevel** | **String** | Specifies what should be included in the response. | [optional] 
**functionMocks** | [**[FunctionMock]**](FunctionMock.md) | Optional function mocks for service-defined functions. If not set, any service defined function is expected to return an error, which may or may not influence the test outcome. | [optional] 
**pathEncoding** | **String** | Specifies whether paths (such as request.path) are encoded and how. | [optional] 
**request** | **Object** | Request context. The exact format of the request context is service-dependent. See the appropriate service documentation for information about the supported fields and types on the request. Minimally, all services support the following fields and types: Request field | Type ---------------|----------------- auth.uid | &#x60;string&#x60; auth.token | &#x60;map&#x60; headers | &#x60;map&#x60; method | &#x60;string&#x60; params | &#x60;map&#x60; path | &#x60;string&#x60; time | &#x60;google.protobuf.Timestamp&#x60; If the request value is not well-formed for the service, the request will be rejected as an invalid argument. | [optional] 
**resource** | **Object** | Optional resource value as it appears in persistent storage before the request is fulfilled. The resource type depends on the &#x60;request.path&#x60; value. | [optional] 



## Enum: ExpectationEnum


* `EXPECTATION_UNSPECIFIED` (value: `"EXPECTATION_UNSPECIFIED"`)

* `ALLOW` (value: `"ALLOW"`)

* `DENY` (value: `"DENY"`)





## Enum: ExpressionReportLevelEnum


* `LEVEL_UNSPECIFIED` (value: `"LEVEL_UNSPECIFIED"`)

* `NONE` (value: `"NONE"`)

* `FULL` (value: `"FULL"`)

* `VISITED` (value: `"VISITED"`)





## Enum: PathEncodingEnum


* `ENCODING_UNSPECIFIED` (value: `"ENCODING_UNSPECIFIED"`)

* `URL_ENCODED` (value: `"URL_ENCODED"`)

* `PLAIN` (value: `"PLAIN"`)




