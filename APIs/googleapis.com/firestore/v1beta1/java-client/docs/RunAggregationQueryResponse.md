

# RunAggregationQueryResponse

The response for Firestore.RunAggregationQuery.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**readTime** | **String** | The time at which the aggregate result was computed. This is always monotonically increasing; in this case, the previous AggregationResult in the result stream are guaranteed not to have changed between their &#x60;read_time&#x60; and this one. If the query returns no results, a response with &#x60;read_time&#x60; and no &#x60;result&#x60; will be sent, and this represents the time at which the query was run. |  [optional] |
|**result** | [**AggregationResult**](AggregationResult.md) |  |  [optional] |
|**transaction** | **byte[]** | The transaction that was started as part of this request. Only present on the first response when the request requested to start a new transaction. |  [optional] |



