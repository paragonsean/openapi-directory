

# ChangeOrderStatusApiModel


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **Integer** | Order Id |  [optional] |
|**reason** | **String** | Reason for status change |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | New status of the order |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING_PAYMENT | &quot;PendingPayment&quot; |
| PROCESSING | &quot;Processing&quot; |
| SHIPPED | &quot;Shipped&quot; |
| COMPLETED | &quot;Completed&quot; |
| ON_HOLD | &quot;OnHold&quot; |
| CANCELLED | &quot;Cancelled&quot; |
| REFUNDED | &quot;Refunded&quot; |
| FAILED | &quot;Failed&quot; |



