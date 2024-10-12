

# TextToColumnsRequest

Splits a column of text into multiple columns, based on a delimiter in each cell.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**delimiter** | **String** | The delimiter to use. Used only if delimiterType is CUSTOM. |  [optional] |
|**delimiterType** | [**DelimiterTypeEnum**](#DelimiterTypeEnum) | The delimiter type to use. |  [optional] |
|**source** | [**GridRange**](GridRange.md) |  |  [optional] |



## Enum: DelimiterTypeEnum

| Name | Value |
|---- | -----|
| DELIMITER_TYPE_UNSPECIFIED | &quot;DELIMITER_TYPE_UNSPECIFIED&quot; |
| COMMA | &quot;COMMA&quot; |
| SEMICOLON | &quot;SEMICOLON&quot; |
| PERIOD | &quot;PERIOD&quot; |
| SPACE | &quot;SPACE&quot; |
| CUSTOM | &quot;CUSTOM&quot; |
| AUTODETECT | &quot;AUTODETECT&quot; |



