# CloudDatastoreApi.RunQueryResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch** | [**QueryResultBatch**](QueryResultBatch.md) |  | [optional] 
**query** | [**Query**](Query.md) |  | [optional] 
**transaction** | **Blob** | The identifier of the transaction that was started as part of this RunQuery request. Set only when ReadOptions.new_transaction was set in RunQueryRequest.read_options. | [optional] 


