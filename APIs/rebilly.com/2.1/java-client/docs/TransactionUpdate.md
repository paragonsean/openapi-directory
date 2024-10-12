

# TransactionUpdate

Update a Transaction manually to completed status with given result with optional currency and amount.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **Double** | The transaction amount. |  [optional] |
|**currency** | **String** | The transaction currency. |  [optional] |
|**result** | [**ResultEnum**](#ResultEnum) | Transaction result. |  |



## Enum: ResultEnum

| Name | Value |
|---- | -----|
| ABANDONED | &quot;abandoned&quot; |
| APPROVED | &quot;approved&quot; |
| CANCELED | &quot;canceled&quot; |
| DECLINED | &quot;declined&quot; |



