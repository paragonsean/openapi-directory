

# BiEngineReason

Reason why BI Engine didn't accelerate the query (or sub-query).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | [**CodeEnum**](#CodeEnum) | Output only. High-level BI Engine reason for partial or disabled acceleration |  [optional] [readonly] |
|**message** | **String** | Output only. Free form human-readable reason for partial or disabled acceleration. |  [optional] [readonly] |



## Enum: CodeEnum

| Name | Value |
|---- | -----|
| CODE_UNSPECIFIED | &quot;CODE_UNSPECIFIED&quot; |
| NO_RESERVATION | &quot;NO_RESERVATION&quot; |
| INSUFFICIENT_RESERVATION | &quot;INSUFFICIENT_RESERVATION&quot; |
| UNSUPPORTED_SQL_TEXT | &quot;UNSUPPORTED_SQL_TEXT&quot; |
| INPUT_TOO_LARGE | &quot;INPUT_TOO_LARGE&quot; |
| OTHER_REASON | &quot;OTHER_REASON&quot; |
| TABLE_EXCLUDED | &quot;TABLE_EXCLUDED&quot; |



