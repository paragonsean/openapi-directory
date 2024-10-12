

# StringMatcher

Specifies the way to match a string. [#next-free-field: 7]

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**exact** | **String** | The input string must match exactly the string specified here. Examples: * *abc* only matches the value *abc*. |  [optional] |
|**ignoreCase** | **Boolean** | If true, indicates the exact/prefix/suffix matching should be case insensitive. This has no effect for the safe_regex match. For example, the matcher *data* will match both input string *Data* and *data* if set to true. |  [optional] |
|**prefix** | **String** | The input string must have the prefix specified here. Note: empty prefix is not allowed, please use regex instead. Examples: * *abc* matches the value *abc.xyz* |  [optional] |
|**regex** | **String** | The input string must match the regular expression specified here. The regex grammar is defined &#x60;here &#x60;_. Examples: * The regex &#x60;&#x60;\\d{3}&#x60;&#x60; matches the value *123* * The regex &#x60;&#x60;\\d{3}&#x60;&#x60; does not match the value *1234* * The regex &#x60;&#x60;\\d{3}&#x60;&#x60; does not match the value *123.456* .. attention:: This field has been deprecated in favor of &#x60;safe_regex&#x60; as it is not safe for use with untrusted input in all cases. |  [optional] |
|**safeRegex** | [**RegexMatcher**](RegexMatcher.md) |  |  [optional] |
|**suffix** | **String** | The input string must have the suffix specified here. Note: empty prefix is not allowed, please use regex instead. Examples: * *abc* matches the value *xyz.abc* |  [optional] |



