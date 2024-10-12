

# StartTransactionRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**transactionType** | [**TransactionTypeEnum**](#TransactionTypeEnum) | Indicates whether this transaction should be read only or read and write. Writes made using a read-only transaction ID will be rejected. Read-only transactions do not need to be committed.  |  [optional] |



## Enum: TransactionTypeEnum

| Name | Value |
|---- | -----|
| AND_WRITE | &quot;READ_AND_WRITE&quot; |
| ONLY | &quot;READ_ONLY&quot; |



