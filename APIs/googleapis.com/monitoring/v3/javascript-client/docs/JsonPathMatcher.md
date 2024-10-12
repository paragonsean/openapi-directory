# CloudMonitoringApi.JsonPathMatcher

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jsonMatcher** | **String** | The type of JSONPath match that will be applied to the JSON output (ContentMatcher.content) | [optional] 
**jsonPath** | **String** | JSONPath within the response output pointing to the expected ContentMatcher::content to match against. | [optional] 



## Enum: JsonMatcherEnum


* `JSON_PATH_MATCHER_OPTION_UNSPECIFIED` (value: `"JSON_PATH_MATCHER_OPTION_UNSPECIFIED"`)

* `EXACT_MATCH` (value: `"EXACT_MATCH"`)

* `REGEX_MATCH` (value: `"REGEX_MATCH"`)




