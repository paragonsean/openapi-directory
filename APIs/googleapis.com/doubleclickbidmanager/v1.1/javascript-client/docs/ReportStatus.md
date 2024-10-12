# DoubleClickBidManagerApi.ReportStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failure** | [**ReportFailure**](ReportFailure.md) |  | [optional] 
**finishTimeMs** | **String** | The time when this report either completed successfully or failed. | [optional] 
**format** | **String** | The file type of the report. | [optional] 
**state** | **String** | The state of the report. | [optional] 



## Enum: FormatEnum


* `CSV` (value: `"CSV"`)

* `EXCEL_CSV` (value: `"EXCEL_CSV"`)

* `XLSX` (value: `"XLSX"`)





## Enum: StateEnum


* `RUNNING` (value: `"RUNNING"`)

* `DONE` (value: `"DONE"`)

* `FAILED` (value: `"FAILED"`)




