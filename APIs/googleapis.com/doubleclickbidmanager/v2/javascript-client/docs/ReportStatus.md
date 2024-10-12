# DoubleClickBidManagerApi.ReportStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**finishTime** | **String** | Output only. The time when this report either completed successfully or failed. | [optional] [readonly] 
**format** | **String** | The file type of the report. | [optional] 
**state** | **String** | Output only. The state of the report. | [optional] [readonly] 



## Enum: FormatEnum


* `FORMAT_UNSPECIFIED` (value: `"FORMAT_UNSPECIFIED"`)

* `CSV` (value: `"CSV"`)

* `XLSX` (value: `"XLSX"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `QUEUED` (value: `"QUEUED"`)

* `RUNNING` (value: `"RUNNING"`)

* `DONE` (value: `"DONE"`)

* `FAILED` (value: `"FAILED"`)




