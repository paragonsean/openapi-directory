

# PartitionReadRequest

The request for PartitionRead

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**columns** | **List&lt;String&gt;** | The columns of table to be returned for each row matching this request. |  [optional] |
|**index** | **String** | If non-empty, the name of an index on table. This index is used instead of the table primary key when interpreting key_set and sorting result rows. See key_set for further information. |  [optional] |
|**keySet** | [**KeySet**](KeySet.md) |  |  [optional] |
|**partitionOptions** | [**PartitionOptions**](PartitionOptions.md) |  |  [optional] |
|**table** | **String** | Required. The name of the table in the database to be read. |  [optional] |
|**transaction** | [**TransactionSelector**](TransactionSelector.md) |  |  [optional] |



