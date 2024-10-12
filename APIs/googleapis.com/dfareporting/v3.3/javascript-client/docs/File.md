# CampaignManager360Api.File

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dateRange** | [**DateRange**](DateRange.md) |  | [optional] 
**etag** | **String** | Etag of this resource. | [optional] 
**fileName** | **String** | The filename of the file. | [optional] 
**format** | **String** | The output format of the report. Only available once the file is available. | [optional] 
**id** | **String** | The unique ID of this report file. | [optional] 
**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;dfareporting#file\&quot;. | [optional] 
**lastModifiedTime** | **String** | The timestamp in milliseconds since epoch when this file was last modified. | [optional] 
**reportId** | **String** | The ID of the report this file was generated from. | [optional] 
**status** | **String** | The status of the report file. | [optional] 
**urls** | [**FileUrls**](FileUrls.md) |  | [optional] 



## Enum: FormatEnum


* `CSV` (value: `"CSV"`)

* `EXCEL` (value: `"EXCEL"`)





## Enum: StatusEnum


* `PROCESSING` (value: `"PROCESSING"`)

* `REPORT_AVAILABLE` (value: `"REPORT_AVAILABLE"`)

* `FAILED` (value: `"FAILED"`)

* `CANCELLED` (value: `"CANCELLED"`)




