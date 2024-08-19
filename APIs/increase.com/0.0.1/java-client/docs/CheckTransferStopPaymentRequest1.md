

# CheckTransferStopPaymentRequest1

A Check Transfer Stop Payment Request object. This field will be present in the JSON response if and only if `category` is equal to `check_transfer_stop_payment_request`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**requestedAt** | **OffsetDateTime** | The time the stop-payment was requested. |  |
|**transactionId** | **String** | The transaction ID of the corresponding credit transaction. |  |
|**transferId** | **String** | The ID of the check transfer that was stopped. |  |
|**type** | [**TypeEnum**](#TypeEnum) | A constant representing the object&#39;s type. For this resource it will always be &#x60;check_transfer_stop_payment_request&#x60;. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CHECK_TRANSFER_STOP_PAYMENT_REQUEST | &quot;check_transfer_stop_payment_request&quot; |



