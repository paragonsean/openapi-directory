# CostManagementClient.ReportConfigDataset

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregation** | [**{String: ReportConfigAggregation}**](ReportConfigAggregation.md) | Dictionary of aggregation expression to use in the report. The key of each item in the dictionary is the alias for the aggregated column. Report can have up to 2 aggregation clauses. | [optional] 
**configuration** | [**ReportConfigDatasetConfiguration**](ReportConfigDatasetConfiguration.md) |  | [optional] 
**filter** | [**ReportConfigFilter**](ReportConfigFilter.md) |  | [optional] 
**granularity** | **String** | The granularity of rows in the report. | [optional] 
**grouping** | [**[ReportConfigGrouping]**](ReportConfigGrouping.md) | Array of group by expression to use in the report. Report can have up to 2 group by clauses. | [optional] 
**sorting** | [**[ReportConfigSorting]**](ReportConfigSorting.md) | Array of order by expression to use in the report. | [optional] 



## Enum: GranularityEnum


* `Daily` (value: `"Daily"`)

* `Monthly` (value: `"Monthly"`)




