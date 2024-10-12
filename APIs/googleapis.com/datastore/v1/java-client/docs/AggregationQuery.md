

# AggregationQuery

Datastore query for running an aggregation over a Query.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aggregations** | [**List&lt;Aggregation&gt;**](Aggregation.md) | Optional. Series of aggregations to apply over the results of the &#x60;nested_query&#x60;. Requires: * A minimum of one and maximum of five aggregations per query. |  [optional] |
|**nestedQuery** | [**Query**](Query.md) |  |  [optional] |



