

# ReportStatus

Report status.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**failure** | [**ReportFailure**](ReportFailure.md) |  |  [optional] |
|**finishTimeMs** | **String** | The time when this report either completed successfully or failed. |  [optional] |
|**format** | [**FormatEnum**](#FormatEnum) | The file type of the report. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The state of the report. |  [optional] |



## Enum: FormatEnum

| Name | Value |
|---- | -----|
| CSV | &quot;CSV&quot; |
| EXCEL_CSV | &quot;EXCEL_CSV&quot; |
| XLSX | &quot;XLSX&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| RUNNING | &quot;RUNNING&quot; |
| DONE | &quot;DONE&quot; |
| FAILED | &quot;FAILED&quot; |



