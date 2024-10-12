

# ApiWarning

An Admin API warning message.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | [**CodeEnum**](#CodeEnum) | Code to uniquely identify the warning type. |  [optional] |
|**message** | **String** | The warning message. |  [optional] |
|**region** | **String** | The region name for REGION_UNREACHABLE warning. |  [optional] |



## Enum: CodeEnum

| Name | Value |
|---- | -----|
| SQL_API_WARNING_CODE_UNSPECIFIED | &quot;SQL_API_WARNING_CODE_UNSPECIFIED&quot; |
| REGION_UNREACHABLE | &quot;REGION_UNREACHABLE&quot; |
| MAX_RESULTS_EXCEEDS_LIMIT | &quot;MAX_RESULTS_EXCEEDS_LIMIT&quot; |
| COMPROMISED_CREDENTIALS | &quot;COMPROMISED_CREDENTIALS&quot; |
| INTERNAL_STATE_FAILURE | &quot;INTERNAL_STATE_FAILURE&quot; |



