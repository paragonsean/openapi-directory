# CostManagementClient.QueryDataset

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregation** | [**{String: QueryAggregation}**](QueryAggregation.md) | Dictionary of aggregation expression to use in the query. The key of each item in the dictionary is the alias for the aggregated column. Query can have up to 2 aggregation clauses. | [optional] 
**configuration** | [**QueryDatasetConfiguration**](QueryDatasetConfiguration.md) |  | [optional] 
**filter** | [**QueryFilter**](QueryFilter.md) |  | [optional] 
**granularity** | **String** | The granularity of rows in the query. | [optional] 
**grouping** | [**[QueryGrouping]**](QueryGrouping.md) | Array of group by expression to use in the query. Query can have up to 2 group by clauses. | [optional] 



## Enum: GranularityEnum


* `Daily` (value: `"Daily"`)




