

# Report

Report represents a point-in-time rendering of the ReportConfig results.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. Creation timestamp. |  [optional] [readonly] |
|**description** | **String** | Free-text description. |  [optional] |
|**displayName** | **String** | User-friendly display name. Maximum length is 63 characters. |  [optional] |
|**name** | **String** | Output only. Name of resource. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Report creation state. |  [optional] |
|**summary** | [**ReportSummary**](ReportSummary.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Report type. |  [optional] |
|**updateTime** | **String** | Output only. Last update timestamp. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| PENDING | &quot;PENDING&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| FAILED | &quot;FAILED&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| TOTAL_COST_OF_OWNERSHIP | &quot;TOTAL_COST_OF_OWNERSHIP&quot; |



