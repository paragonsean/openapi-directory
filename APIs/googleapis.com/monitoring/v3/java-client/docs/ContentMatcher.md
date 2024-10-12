

# ContentMatcher

Optional. Used to perform content matching. This allows matching based on substrings and regular expressions, together with their negations. Only the first 4 MB of an HTTP or HTTPS check's response (and the first 1 MB of a TCP check's response) are examined for purposes of content matching.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**content** | **String** | String, regex or JSON content to match. Maximum 1024 bytes. An empty content string indicates no content matching is to be performed. |  [optional] |
|**jsonPathMatcher** | [**JsonPathMatcher**](JsonPathMatcher.md) |  |  [optional] |
|**matcher** | [**MatcherEnum**](#MatcherEnum) | The type of content matcher that will be applied to the server output, compared to the content string when the check is run. |  [optional] |



## Enum: MatcherEnum

| Name | Value |
|---- | -----|
| CONTENT_MATCHER_OPTION_UNSPECIFIED | &quot;CONTENT_MATCHER_OPTION_UNSPECIFIED&quot; |
| CONTAINS_STRING | &quot;CONTAINS_STRING&quot; |
| NOT_CONTAINS_STRING | &quot;NOT_CONTAINS_STRING&quot; |
| MATCHES_REGEX | &quot;MATCHES_REGEX&quot; |
| NOT_MATCHES_REGEX | &quot;NOT_MATCHES_REGEX&quot; |
| MATCHES_JSON_PATH | &quot;MATCHES_JSON_PATH&quot; |
| NOT_MATCHES_JSON_PATH | &quot;NOT_MATCHES_JSON_PATH&quot; |



