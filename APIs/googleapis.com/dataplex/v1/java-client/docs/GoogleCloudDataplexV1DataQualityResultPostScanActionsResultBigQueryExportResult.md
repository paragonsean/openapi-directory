

# GoogleCloudDataplexV1DataQualityResultPostScanActionsResultBigQueryExportResult

The result of BigQuery export post scan action.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**message** | **String** | Output only. Additional information about the BigQuery exporting. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. Execution state for the BigQuery exporting. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| FAILED | &quot;FAILED&quot; |
| SKIPPED | &quot;SKIPPED&quot; |



