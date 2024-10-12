# CloudDatastoreApi.RunAggregationQueryResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch** | [**AggregationResultBatch**](AggregationResultBatch.md) |  | [optional] 
**query** | [**AggregationQuery**](AggregationQuery.md) |  | [optional] 
**transaction** | **Blob** | The identifier of the transaction that was started as part of this RunAggregationQuery request. Set only when ReadOptions.new_transaction was set in RunAggregationQueryRequest.read_options. | [optional] 


