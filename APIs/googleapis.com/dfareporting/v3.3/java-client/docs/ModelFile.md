

# ModelFile

Represents a File resource. A file contains the metadata for a report run. It shows the status of the run and holds the URLs to the generated report data if the run is finished and the status is \"REPORT_AVAILABLE\".

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dateRange** | [**DateRange**](DateRange.md) |  |  [optional] |
|**etag** | **String** | Etag of this resource. |  [optional] |
|**fileName** | **String** | The filename of the file. |  [optional] |
|**format** | [**FormatEnum**](#FormatEnum) | The output format of the report. Only available once the file is available. |  [optional] |
|**id** | **String** | The unique ID of this report file. |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;dfareporting#file\&quot;. |  [optional] |
|**lastModifiedTime** | **String** | The timestamp in milliseconds since epoch when this file was last modified. |  [optional] |
|**reportId** | **String** | The ID of the report this file was generated from. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the report file. |  [optional] |
|**urls** | [**FileUrls**](FileUrls.md) |  |  [optional] |



## Enum: FormatEnum

| Name | Value |
|---- | -----|
| CSV | &quot;CSV&quot; |
| EXCEL | &quot;EXCEL&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PROCESSING | &quot;PROCESSING&quot; |
| REPORT_AVAILABLE | &quot;REPORT_AVAILABLE&quot; |
| FAILED | &quot;FAILED&quot; |
| CANCELLED | &quot;CANCELLED&quot; |



