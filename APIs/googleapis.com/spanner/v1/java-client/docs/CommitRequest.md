

# CommitRequest

The request for Commit.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**maxCommitDelay** | **String** | Optional. The amount of latency this request is willing to incur in order to improve throughput. If this field is not set, Spanner assumes requests are relatively latency sensitive and automatically determines an appropriate delay time. You can specify a batching delay value between 0 and 500 ms. |  [optional] |
|**mutations** | [**List&lt;Mutation&gt;**](Mutation.md) | The mutations to be executed when this transaction commits. All mutations are applied atomically, in the order they appear in this list. |  [optional] |
|**requestOptions** | [**RequestOptions**](RequestOptions.md) |  |  [optional] |
|**returnCommitStats** | **Boolean** | If &#x60;true&#x60;, then statistics related to the transaction will be included in the CommitResponse. Default value is &#x60;false&#x60;. |  [optional] |
|**singleUseTransaction** | [**TransactionOptions**](TransactionOptions.md) |  |  [optional] |
|**transactionId** | **byte[]** | Commit a previously-started transaction. |  [optional] |



