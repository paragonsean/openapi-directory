

# Parameters

Parameters of a query or report.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**filters** | [**List&lt;FilterPair&gt;**](FilterPair.md) | Filters used to match traffic data in your report. |  [optional] |
|**groupBys** | **List&lt;String&gt;** | Data is grouped by the filters listed in this field. |  [optional] |
|**metrics** | **List&lt;String&gt;** | Metrics to include as columns in your report. |  [optional] |
|**options** | [**Options**](Options.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the report. The type of the report will dictate what dimesions, filters, and metrics can be used. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| REPORT_TYPE_UNSPECIFIED | &quot;REPORT_TYPE_UNSPECIFIED&quot; |
| STANDARD | &quot;STANDARD&quot; |
| INVENTORY_AVAILABILITY | &quot;INVENTORY_AVAILABILITY&quot; |
| AUDIENCE_COMPOSITION | &quot;AUDIENCE_COMPOSITION&quot; |
| FLOODLIGHT | &quot;FLOODLIGHT&quot; |
| YOUTUBE | &quot;YOUTUBE&quot; |
| GRP | &quot;GRP&quot; |
| YOUTUBE_PROGRAMMATIC_GUARANTEED | &quot;YOUTUBE_PROGRAMMATIC_GUARANTEED&quot; |
| REACH | &quot;REACH&quot; |
| UNIQUE_REACH_AUDIENCE | &quot;UNIQUE_REACH_AUDIENCE&quot; |
| FULL_PATH | &quot;FULL_PATH&quot; |
| PATH_ATTRIBUTION | &quot;PATH_ATTRIBUTION&quot; |



