

# GooglePrivacyDlpV2CharsToIgnore

Characters to skip when doing deidentification of a value. These will be left alone and skipped.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**charactersToSkip** | **String** | Characters to not transform when masking. |  [optional] |
|**commonCharactersToIgnore** | [**CommonCharactersToIgnoreEnum**](#CommonCharactersToIgnoreEnum) | Common characters to not transform when masking. Useful to avoid removing punctuation. |  [optional] |



## Enum: CommonCharactersToIgnoreEnum

| Name | Value |
|---- | -----|
| COMMON_CHARS_TO_IGNORE_UNSPECIFIED | &quot;COMMON_CHARS_TO_IGNORE_UNSPECIFIED&quot; |
| NUMERIC | &quot;NUMERIC&quot; |
| ALPHA_UPPER_CASE | &quot;ALPHA_UPPER_CASE&quot; |
| ALPHA_LOWER_CASE | &quot;ALPHA_LOWER_CASE&quot; |
| PUNCTUATION | &quot;PUNCTUATION&quot; |
| WHITESPACE | &quot;WHITESPACE&quot; |



