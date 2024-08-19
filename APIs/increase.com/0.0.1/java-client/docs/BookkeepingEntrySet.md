

# BookkeepingEntrySet

Entry Sets are accounting entries that are transactionally applied.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**date** | **OffsetDateTime** | The timestamp of the entry set. |  |
|**entries** | [**List&lt;EntriesElement&gt;**](EntriesElement.md) | The entries |  |
|**id** | **String** | The entry set identifier. |  |
|**transactionId** | **String** | The transaction identifier, if any. |  |
|**type** | [**TypeEnum**](#TypeEnum) | A constant representing the object&#39;s type. For this resource it will always be &#x60;bookkeeping_entry_set&#x60;. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| BOOKKEEPING_ENTRY_SET | &quot;bookkeeping_entry_set&quot; |



