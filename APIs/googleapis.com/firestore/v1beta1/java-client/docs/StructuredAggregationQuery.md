

# StructuredAggregationQuery

Firestore query for running an aggregation over a StructuredQuery.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aggregations** | [**List&lt;Aggregation&gt;**](Aggregation.md) | Optional. Series of aggregations to apply over the results of the &#x60;structured_query&#x60;. Requires: * A minimum of one and maximum of five aggregations per query. |  [optional] |
|**structuredQuery** | [**StructuredQuery**](StructuredQuery.md) |  |  [optional] |



