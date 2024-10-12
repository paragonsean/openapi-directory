# CloudMonitoringApi.ContentMatcher

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **String** | String, regex or JSON content to match. Maximum 1024 bytes. An empty content string indicates no content matching is to be performed. | [optional] 
**jsonPathMatcher** | [**JsonPathMatcher**](JsonPathMatcher.md) |  | [optional] 
**matcher** | **String** | The type of content matcher that will be applied to the server output, compared to the content string when the check is run. | [optional] 



## Enum: MatcherEnum


* `CONTENT_MATCHER_OPTION_UNSPECIFIED` (value: `"CONTENT_MATCHER_OPTION_UNSPECIFIED"`)

* `CONTAINS_STRING` (value: `"CONTAINS_STRING"`)

* `NOT_CONTAINS_STRING` (value: `"NOT_CONTAINS_STRING"`)

* `MATCHES_REGEX` (value: `"MATCHES_REGEX"`)

* `NOT_MATCHES_REGEX` (value: `"NOT_MATCHES_REGEX"`)

* `MATCHES_JSON_PATH` (value: `"MATCHES_JSON_PATH"`)

* `NOT_MATCHES_JSON_PATH` (value: `"NOT_MATCHES_JSON_PATH"`)




