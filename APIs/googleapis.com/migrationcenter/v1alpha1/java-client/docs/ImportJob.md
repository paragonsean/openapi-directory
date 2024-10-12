

# ImportJob

A resource that represents the background job that imports asset frames.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assetSource** | **String** | Required. Reference to a source. |  [optional] |
|**completeTime** | **String** | Output only. The timestamp when the import job was completed. |  [optional] [readonly] |
|**createTime** | **String** | Output only. The timestamp when the import job was created. |  [optional] [readonly] |
|**displayName** | **String** | User-friendly display name. Maximum length is 63 characters. |  [optional] |
|**executionReport** | [**ExecutionReport**](ExecutionReport.md) |  |  [optional] |
|**gcsPayload** | [**GCSPayloadInfo**](GCSPayloadInfo.md) |  |  [optional] |
|**inlinePayload** | [**InlinePayloadInfo**](InlinePayloadInfo.md) |  |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Labels as key value pairs. |  [optional] |
|**name** | **String** | Output only. The full name of the import job. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The state of the import job. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. The timestamp when the import job was last updated. |  [optional] [readonly] |
|**validationReport** | [**ValidationReport**](ValidationReport.md) |  |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;IMPORT_JOB_STATE_UNSPECIFIED&quot; |
| PENDING | &quot;IMPORT_JOB_STATE_PENDING&quot; |
| RUNNING | &quot;IMPORT_JOB_STATE_RUNNING&quot; |
| COMPLETED | &quot;IMPORT_JOB_STATE_COMPLETED&quot; |
| FAILED | &quot;IMPORT_JOB_STATE_FAILED&quot; |
| VALIDATING | &quot;IMPORT_JOB_STATE_VALIDATING&quot; |
| FAILED_VALIDATION | &quot;IMPORT_JOB_STATE_FAILED_VALIDATION&quot; |
| READY | &quot;IMPORT_JOB_STATE_READY&quot; |



