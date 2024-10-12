# AwsLakeFormation.StartTransactionRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transactionType** | **String** | Indicates whether this transaction should be read only or read and write. Writes made using a read-only transaction ID will be rejected. Read-only transactions do not need to be committed.  | [optional] 



## Enum: TransactionTypeEnum


* `AND_WRITE` (value: `"READ_AND_WRITE"`)

* `ONLY` (value: `"READ_ONLY"`)




