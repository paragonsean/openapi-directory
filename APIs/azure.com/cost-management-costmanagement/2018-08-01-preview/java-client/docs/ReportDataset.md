

# ReportDataset

The definition of data present in the report.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aggregation** | [**Map&lt;String, ReportAggregation&gt;**](ReportAggregation.md) | Dictionary of aggregation expression to use in the report. The key of each item in the dictionary is the alias for the aggregated column. Report can have up to 2 aggregation clauses. |  [optional] |
|**_configuration** | [**ReportDatasetConfiguration**](ReportDatasetConfiguration.md) |  |  [optional] |
|**filter** | [**ReportFilter**](ReportFilter.md) |  |  [optional] |
|**granularity** | [**GranularityEnum**](#GranularityEnum) | The granularity of rows in the report. |  [optional] |
|**grouping** | [**List&lt;ReportGrouping&gt;**](ReportGrouping.md) | Array of group by expression to use in the report. Report can have up to 2 group by clauses. |  [optional] |



## Enum: GranularityEnum

| Name | Value |
|---- | -----|
| DAILY | &quot;Daily&quot; |
| HOURLY | &quot;Hourly&quot; |



