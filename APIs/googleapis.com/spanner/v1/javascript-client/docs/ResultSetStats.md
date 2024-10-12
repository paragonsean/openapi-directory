# CloudSpannerApi.ResultSetStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**queryPlan** | [**QueryPlan**](QueryPlan.md) |  | [optional] 
**queryStats** | **{String: Object}** | Aggregated statistics from the execution of the query. Only present when the query is profiled. For example, a query could return the statistics as follows: { \&quot;rows_returned\&quot;: \&quot;3\&quot;, \&quot;elapsed_time\&quot;: \&quot;1.22 secs\&quot;, \&quot;cpu_time\&quot;: \&quot;1.19 secs\&quot; } | [optional] 
**rowCountExact** | **String** | Standard DML returns an exact count of rows that were modified. | [optional] 
**rowCountLowerBound** | **String** | Partitioned DML does not offer exactly-once semantics, so it returns a lower bound of the rows modified. | [optional] 


