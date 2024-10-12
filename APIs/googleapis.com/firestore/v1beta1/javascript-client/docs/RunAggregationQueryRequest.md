# CloudFirestoreApi.RunAggregationQueryRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**newTransaction** | [**TransactionOptions**](TransactionOptions.md) |  | [optional] 
**readTime** | **String** | Executes the query at the given timestamp. This must be a microsecond precision timestamp within the past one hour, or if Point-in-Time Recovery is enabled, can additionally be a whole minute timestamp within the past 7 days. | [optional] 
**structuredAggregationQuery** | [**StructuredAggregationQuery**](StructuredAggregationQuery.md) |  | [optional] 
**transaction** | **Blob** | Run the aggregation within an already active transaction. The value here is the opaque transaction ID to execute the query in. | [optional] 


