

# AggregationResult

The result of a single bucket from a Firestore aggregation query. The keys of `aggregate_fields` are the same for all results in an aggregation query, unlike document queries which can have different fields present for each result.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aggregateFields** | [**Map&lt;String, Value&gt;**](Value.md) | The result of the aggregation functions, ex: &#x60;COUNT(*) AS total_docs&#x60;. The key is the alias assigned to the aggregation function on input and the size of this map equals the number of aggregation functions in the query. |  [optional] |



