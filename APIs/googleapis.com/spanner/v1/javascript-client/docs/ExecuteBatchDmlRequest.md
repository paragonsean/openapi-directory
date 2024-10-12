# CloudSpannerApi.ExecuteBatchDmlRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requestOptions** | [**RequestOptions**](RequestOptions.md) |  | [optional] 
**seqno** | **String** | Required. A per-transaction sequence number used to identify this request. This field makes each request idempotent such that if the request is received multiple times, at most one will succeed. The sequence number must be monotonically increasing within the transaction. If a request arrives for the first time with an out-of-order sequence number, the transaction may be aborted. Replays of previously handled requests will yield the same response as the first execution. | [optional] 
**statements** | [**[Statement]**](Statement.md) | Required. The list of statements to execute in this batch. Statements are executed serially, such that the effects of statement &#x60;i&#x60; are visible to statement &#x60;i+1&#x60;. Each statement must be a DML statement. Execution stops at the first failed statement; the remaining statements are not executed. Callers must provide at least one statement. | [optional] 
**transaction** | [**TransactionSelector**](TransactionSelector.md) |  | [optional] 


