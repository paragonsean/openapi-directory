

# ReadWrite

Message type to initiate a read-write transaction. Currently this transaction type has no options.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**readLockMode** | [**ReadLockModeEnum**](#ReadLockModeEnum) | Read lock mode for the transaction. |  [optional] |



## Enum: ReadLockModeEnum

| Name | Value |
|---- | -----|
| READ_LOCK_MODE_UNSPECIFIED | &quot;READ_LOCK_MODE_UNSPECIFIED&quot; |
| PESSIMISTIC | &quot;PESSIMISTIC&quot; |
| OPTIMISTIC | &quot;OPTIMISTIC&quot; |



