

# HttpRouteHeaderMatch

Specifies how to select a route rule based on HTTP request headers.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**exactMatch** | **String** | The value of the header should match exactly the content of exact_match. |  [optional] |
|**header** | **String** | The name of the HTTP header to match against. |  [optional] |
|**invertMatch** | **Boolean** | If specified, the match result will be inverted before checking. Default value is set to false. |  [optional] |
|**prefixMatch** | **String** | The value of the header must start with the contents of prefix_match. |  [optional] |
|**presentMatch** | **Boolean** | A header with header_name must exist. The match takes place whether or not the header has a value. |  [optional] |
|**rangeMatch** | [**HttpRouteHeaderMatchIntegerRange**](HttpRouteHeaderMatchIntegerRange.md) |  |  [optional] |
|**regexMatch** | **String** | The value of the header must match the regular expression specified in regex_match. For regular expression grammar, please see: https://github.com/google/re2/wiki/Syntax |  [optional] |
|**suffixMatch** | **String** | The value of the header must end with the contents of suffix_match. |  [optional] |



