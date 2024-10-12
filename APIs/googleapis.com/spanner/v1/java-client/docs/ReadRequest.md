

# ReadRequest

The request for Read and StreamingRead.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**columns** | **List&lt;String&gt;** | Required. The columns of table to be returned for each row matching this request. |  [optional] |
|**dataBoostEnabled** | **Boolean** | If this is for a partitioned read and this field is set to &#x60;true&#x60;, the request is executed with Spanner Data Boost independent compute resources. If the field is set to &#x60;true&#x60; but the request does not set &#x60;partition_token&#x60;, the API returns an &#x60;INVALID_ARGUMENT&#x60; error. |  [optional] |
|**directedReadOptions** | [**DirectedReadOptions**](DirectedReadOptions.md) |  |  [optional] |
|**index** | **String** | If non-empty, the name of an index on table. This index is used instead of the table primary key when interpreting key_set and sorting result rows. See key_set for further information. |  [optional] |
|**keySet** | [**KeySet**](KeySet.md) |  |  [optional] |
|**limit** | **String** | If greater than zero, only the first &#x60;limit&#x60; rows are yielded. If &#x60;limit&#x60; is zero, the default is no limit. A limit cannot be specified if &#x60;partition_token&#x60; is set. |  [optional] |
|**partitionToken** | **byte[]** | If present, results will be restricted to the specified partition previously created using PartitionRead(). There must be an exact match for the values of fields common to this message and the PartitionReadRequest message used to create this partition_token. |  [optional] |
|**requestOptions** | [**RequestOptions**](RequestOptions.md) |  |  [optional] |
|**resumeToken** | **byte[]** | If this request is resuming a previously interrupted read, &#x60;resume_token&#x60; should be copied from the last PartialResultSet yielded before the interruption. Doing this enables the new read to resume where the last read left off. The rest of the request parameters must exactly match the request that yielded this token. |  [optional] |
|**table** | **String** | Required. The name of the table in the database to be read. |  [optional] |
|**transaction** | [**TransactionSelector**](TransactionSelector.md) |  |  [optional] |



