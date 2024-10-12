

# StringMatcher

Specifies the way to match a string. [#next-free-field: 8]

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contains** | **String** | The input string must have the substring specified here. Note: empty contains match is not allowed, please use regex instead. Examples: * &#x60;&#x60;abc&#x60;&#x60; matches the value &#x60;&#x60;xyz.abc.def&#x60;&#x60; |  [optional] |
|**exact** | **String** | The input string must match exactly the string specified here. Examples: * &#x60;&#x60;abc&#x60;&#x60; only matches the value &#x60;&#x60;abc&#x60;&#x60;. |  [optional] |
|**ignoreCase** | **Boolean** | If true, indicates the exact/prefix/suffix/contains matching should be case insensitive. This has no effect for the safe_regex match. For example, the matcher &#x60;&#x60;data&#x60;&#x60; will match both input string &#x60;&#x60;Data&#x60;&#x60; and &#x60;&#x60;data&#x60;&#x60; if set to true. |  [optional] |
|**prefix** | **String** | The input string must have the prefix specified here. Note: empty prefix is not allowed, please use regex instead. Examples: * &#x60;&#x60;abc&#x60;&#x60; matches the value &#x60;&#x60;abc.xyz&#x60;&#x60; |  [optional] |
|**safeRegex** | [**RegexMatcher**](RegexMatcher.md) |  |  [optional] |
|**suffix** | **String** | The input string must have the suffix specified here. Note: empty prefix is not allowed, please use regex instead. Examples: * &#x60;&#x60;abc&#x60;&#x60; matches the value &#x60;&#x60;xyz.abc&#x60;&#x60; |  [optional] |



