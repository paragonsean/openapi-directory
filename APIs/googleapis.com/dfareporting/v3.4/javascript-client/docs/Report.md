# CampaignManager360Api.Report

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | The account ID to which this report belongs. | [optional] 
**criteria** | [**ReportCriteria**](ReportCriteria.md) |  | [optional] 
**crossDimensionReachCriteria** | [**ReportCrossDimensionReachCriteria**](ReportCrossDimensionReachCriteria.md) |  | [optional] 
**delivery** | [**ReportDelivery**](ReportDelivery.md) |  | [optional] 
**etag** | **String** | The eTag of this response for caching purposes. | [optional] 
**fileName** | **String** | The filename used when generating report files for this report. | [optional] 
**floodlightCriteria** | [**ReportFloodlightCriteria**](ReportFloodlightCriteria.md) |  | [optional] 
**format** | **String** | The output format of the report. If not specified, default format is \&quot;CSV\&quot;. Note that the actual format in the completed report file might differ if for instance the report&#39;s size exceeds the format&#39;s capabilities. \&quot;CSV\&quot; will then be the fallback format. | [optional] 
**id** | **String** | The unique ID identifying this report resource. | [optional] 
**kind** | **String** | The kind of resource this is, in this case dfareporting#report. | [optional] 
**lastModifiedTime** | **String** | The timestamp (in milliseconds since epoch) of when this report was last modified. | [optional] 
**name** | **String** | The name of the report. | [optional] 
**ownerProfileId** | **String** | The user profile id of the owner of this report. | [optional] 
**pathAttributionCriteria** | [**ReportPathAttributionCriteria**](ReportPathAttributionCriteria.md) |  | [optional] 
**pathCriteria** | [**ReportPathCriteria**](ReportPathCriteria.md) |  | [optional] 
**pathToConversionCriteria** | [**ReportPathToConversionCriteria**](ReportPathToConversionCriteria.md) |  | [optional] 
**reachCriteria** | [**ReportReachCriteria**](ReportReachCriteria.md) |  | [optional] 
**schedule** | [**ReportSchedule**](ReportSchedule.md) |  | [optional] 
**subAccountId** | **String** | The subaccount ID to which this report belongs if applicable. | [optional] 
**type** | **String** | The type of the report. | [optional] 



## Enum: FormatEnum


* `CSV` (value: `"CSV"`)

* `EXCEL` (value: `"EXCEL"`)





## Enum: TypeEnum


* `STANDARD` (value: `"STANDARD"`)

* `REACH` (value: `"REACH"`)

* `PATH_TO_CONVERSION` (value: `"PATH_TO_CONVERSION"`)

* `CROSS_DIMENSION_REACH` (value: `"CROSS_DIMENSION_REACH"`)

* `FLOODLIGHT` (value: `"FLOODLIGHT"`)

* `PATH` (value: `"PATH"`)

* `PATH_ATTRIBUTION` (value: `"PATH_ATTRIBUTION"`)




