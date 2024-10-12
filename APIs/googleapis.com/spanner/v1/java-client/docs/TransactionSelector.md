

# TransactionSelector

This message is used to select the transaction in which a Read or ExecuteSql call runs. See TransactionOptions for more information about transactions.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**begin** | [**TransactionOptions**](TransactionOptions.md) |  |  [optional] |
|**id** | **byte[]** | Execute the read or SQL query in a previously-started transaction. |  [optional] |
|**singleUse** | [**TransactionOptions**](TransactionOptions.md) |  |  [optional] |



