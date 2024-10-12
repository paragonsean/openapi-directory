

# AggregationResult

The result of a single bucket from a Datastore aggregation query. The keys of `aggregate_properties` are the same for all results in an aggregation query, unlike entity queries which can have different fields present for each result.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aggregateProperties** | [**Map&lt;String, Value&gt;**](Value.md) | The result of the aggregation functions, ex: &#x60;COUNT(*) AS total_entities&#x60;. The key is the alias assigned to the aggregation function on input and the size of this map equals the number of aggregation functions in the query. |  [optional] |



