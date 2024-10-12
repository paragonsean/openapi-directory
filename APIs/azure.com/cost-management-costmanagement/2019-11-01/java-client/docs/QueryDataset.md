

# QueryDataset

The definition of data present in the query.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aggregation** | [**Map&lt;String, QueryAggregation&gt;**](QueryAggregation.md) | Dictionary of aggregation expression to use in the query. The key of each item in the dictionary is the alias for the aggregated column. Query can have up to 2 aggregation clauses. |  [optional] |
|**_configuration** | [**QueryDatasetConfiguration**](QueryDatasetConfiguration.md) |  |  [optional] |
|**filter** | [**QueryFilter**](QueryFilter.md) |  |  [optional] |
|**granularity** | [**GranularityEnum**](#GranularityEnum) | The granularity of rows in the query. |  [optional] |
|**grouping** | [**List&lt;QueryGrouping&gt;**](QueryGrouping.md) | Array of group by expression to use in the query. Query can have up to 2 group by clauses. |  [optional] |



## Enum: GranularityEnum

| Name | Value |
|---- | -----|
| DAILY | &quot;Daily&quot; |



