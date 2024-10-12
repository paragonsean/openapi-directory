# DoubleClickBidManagerApi.Parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**[FilterPair]**](FilterPair.md) | Filters used to match traffic data in your report. | [optional] 
**groupBys** | **[String]** | Data is grouped by the filters listed in this field. | [optional] 
**metrics** | **[String]** | Metrics to include as columns in your report. | [optional] 
**options** | [**Options**](Options.md) |  | [optional] 
**type** | **String** | The type of the report. The type of the report will dictate what dimesions, filters, and metrics can be used. | [optional] 



## Enum: TypeEnum


* `REPORT_TYPE_UNSPECIFIED` (value: `"REPORT_TYPE_UNSPECIFIED"`)

* `STANDARD` (value: `"STANDARD"`)

* `INVENTORY_AVAILABILITY` (value: `"INVENTORY_AVAILABILITY"`)

* `AUDIENCE_COMPOSITION` (value: `"AUDIENCE_COMPOSITION"`)

* `FLOODLIGHT` (value: `"FLOODLIGHT"`)

* `YOUTUBE` (value: `"YOUTUBE"`)

* `GRP` (value: `"GRP"`)

* `YOUTUBE_PROGRAMMATIC_GUARANTEED` (value: `"YOUTUBE_PROGRAMMATIC_GUARANTEED"`)

* `REACH` (value: `"REACH"`)

* `UNIQUE_REACH_AUDIENCE` (value: `"UNIQUE_REACH_AUDIENCE"`)

* `FULL_PATH` (value: `"FULL_PATH"`)

* `PATH_ATTRIBUTION` (value: `"PATH_ATTRIBUTION"`)




