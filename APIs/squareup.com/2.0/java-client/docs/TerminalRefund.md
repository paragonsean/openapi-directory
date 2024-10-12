

# TerminalRefund



## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amountMoney** | [**Money**](Money.md) |  |  |
|**appId** | **String** | The ID of the application that created the refund. |  [optional] |
|**cancelReason** | **String** | Present if the status is &#x60;CANCELED&#x60;. |  [optional] |
|**createdAt** | **String** | The time when the &#x60;TerminalRefund&#x60; was created, as an RFC 3339 timestamp. |  [optional] |
|**deadlineDuration** | **String** | The RFC 3339 duration, after which the refund is automatically canceled. A &#x60;TerminalRefund&#x60; that is &#x60;PENDING&#x60; is automatically &#x60;CANCELED&#x60; and has a cancellation reason of &#x60;TIMED_OUT&#x60;.  Default: 5 minutes from creation.  Maximum: 5 minutes |  [optional] |
|**deviceId** | **String** | The unique ID of the device intended for this &#x60;TerminalRefund&#x60;. The Id can be retrieved from /v2/devices api. |  [optional] |
|**id** | **String** | A unique ID for this &#x60;TerminalRefund&#x60;. |  [optional] |
|**locationId** | **String** | The location of the device where the &#x60;TerminalRefund&#x60; was directed. |  [optional] |
|**orderId** | **String** | The reference to the Square order ID for the payment identified by the &#x60;payment_id&#x60;. |  [optional] |
|**paymentId** | **String** | The unique ID of the payment being refunded. |  |
|**reason** | **String** | A description of the reason for the refund. Note: maximum 192 characters |  [optional] |
|**refundId** | **String** | The reference to the payment refund created by completing this &#x60;TerminalRefund&#x60;. |  [optional] |
|**status** | **String** | The status of the &#x60;TerminalRefund&#x60;. Options: &#x60;PENDING&#x60;, &#x60;IN_PROGRESS&#x60;, &#x60;CANCELED&#x60;, or &#x60;COMPLETED&#x60;. |  [optional] |
|**updatedAt** | **String** | The time when the &#x60;TerminalRefund&#x60; was last updated, as an RFC 3339 timestamp. |  [optional] |



