# CostManagementClient.ReportDataset

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregation** | [**{String: ReportAggregation}**](ReportAggregation.md) | Dictionary of aggregation expression to use in the report. The key of each item in the dictionary is the alias for the aggregated column. Report can have up to 2 aggregation clauses. | [optional] 
**configuration** | [**ReportDatasetConfiguration**](ReportDatasetConfiguration.md) |  | [optional] 
**filter** | [**ReportFilter**](ReportFilter.md) |  | [optional] 
**granularity** | **String** | The granularity of rows in the report. | [optional] 
**grouping** | [**[ReportGrouping]**](ReportGrouping.md) | Array of group by expression to use in the report. Report can have up to 2 group by clauses. | [optional] 



## Enum: GranularityEnum


* `Daily` (value: `"Daily"`)

* `Hourly` (value: `"Hourly"`)




