

# RunAggregationQueryResponse

The response for Datastore.RunAggregationQuery.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**batch** | [**AggregationResultBatch**](AggregationResultBatch.md) |  |  [optional] |
|**query** | [**AggregationQuery**](AggregationQuery.md) |  |  [optional] |
|**transaction** | **byte[]** | The identifier of the transaction that was started as part of this RunAggregationQuery request. Set only when ReadOptions.new_transaction was set in RunAggregationQueryRequest.read_options. |  [optional] |



