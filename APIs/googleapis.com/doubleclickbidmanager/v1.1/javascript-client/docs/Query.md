# DoubleClickBidManagerApi.Query

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;doubleclickbidmanager#query\&quot;. | [optional] 
**metadata** | [**QueryMetadata**](QueryMetadata.md) |  | [optional] 
**params** | [**Parameters**](Parameters.md) |  | [optional] 
**queryId** | **String** | Query ID. | [optional] 
**reportDataEndTimeMs** | **String** | The ending time for the data that is shown in the report. Note, reportDataEndTimeMs is required if metadata.dataRange is CUSTOM_DATES and ignored otherwise. | [optional] 
**reportDataStartTimeMs** | **String** | The starting time for the data that is shown in the report. Note, reportDataStartTimeMs is required if metadata.dataRange is CUSTOM_DATES and ignored otherwise. | [optional] 
**schedule** | [**QuerySchedule**](QuerySchedule.md) |  | [optional] 
**timezoneCode** | **String** | Canonical timezone code for report data time. Defaults to America/New_York. | [optional] 


