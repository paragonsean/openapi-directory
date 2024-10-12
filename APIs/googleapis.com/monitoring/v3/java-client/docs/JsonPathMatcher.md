

# JsonPathMatcher

Information needed to perform a JSONPath content match. Used for ContentMatcherOption::MATCHES_JSON_PATH and ContentMatcherOption::NOT_MATCHES_JSON_PATH.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**jsonMatcher** | [**JsonMatcherEnum**](#JsonMatcherEnum) | The type of JSONPath match that will be applied to the JSON output (ContentMatcher.content) |  [optional] |
|**jsonPath** | **String** | JSONPath within the response output pointing to the expected ContentMatcher::content to match against. |  [optional] |



## Enum: JsonMatcherEnum

| Name | Value |
|---- | -----|
| JSON_PATH_MATCHER_OPTION_UNSPECIFIED | &quot;JSON_PATH_MATCHER_OPTION_UNSPECIFIED&quot; |
| EXACT_MATCH | &quot;EXACT_MATCH&quot; |
| REGEX_MATCH | &quot;REGEX_MATCH&quot; |



