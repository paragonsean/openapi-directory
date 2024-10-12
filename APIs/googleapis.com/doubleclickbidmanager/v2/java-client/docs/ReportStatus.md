

# ReportStatus

Report status.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**finishTime** | **String** | Output only. The time when this report either completed successfully or failed. |  [optional] [readonly] |
|**format** | [**FormatEnum**](#FormatEnum) | The file type of the report. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The state of the report. |  [optional] [readonly] |



## Enum: FormatEnum

| Name | Value |
|---- | -----|
| FORMAT_UNSPECIFIED | &quot;FORMAT_UNSPECIFIED&quot; |
| CSV | &quot;CSV&quot; |
| XLSX | &quot;XLSX&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| QUEUED | &quot;QUEUED&quot; |
| RUNNING | &quot;RUNNING&quot; |
| DONE | &quot;DONE&quot; |
| FAILED | &quot;FAILED&quot; |



