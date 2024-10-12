

# ReportConfigDataset

The definition of data present in the report.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aggregation** | [**Map&lt;String, ReportConfigAggregation&gt;**](ReportConfigAggregation.md) | Dictionary of aggregation expression to use in the report. The key of each item in the dictionary is the alias for the aggregated column. Report can have up to 2 aggregation clauses. |  [optional] |
|**_configuration** | [**ReportConfigDatasetConfiguration**](ReportConfigDatasetConfiguration.md) |  |  [optional] |
|**filter** | [**ReportConfigFilter**](ReportConfigFilter.md) |  |  [optional] |
|**granularity** | [**GranularityEnum**](#GranularityEnum) | The granularity of rows in the report. |  [optional] |
|**grouping** | [**List&lt;ReportConfigGrouping&gt;**](ReportConfigGrouping.md) | Array of group by expression to use in the report. Report can have up to 2 group by clauses. |  [optional] |
|**sorting** | [**List&lt;ReportConfigSorting&gt;**](ReportConfigSorting.md) | Array of order by expression to use in the report. |  [optional] |



## Enum: GranularityEnum

| Name | Value |
|---- | -----|
| DAILY | &quot;Daily&quot; |



