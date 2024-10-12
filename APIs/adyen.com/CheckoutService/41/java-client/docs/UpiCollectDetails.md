

# UpiCollectDetails


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billingSequenceNumber** | **String** | The sequence number for the debit. For example, send **2** if this is the second debit for the subscription. The sequence number is included in the notification sent to the shopper. |  |
|**recurringDetailReference** | **String** | This is the &#x60;recurringDetailReference&#x60; returned in the response when you created the token. |  [optional] |
|**shopperNotificationReference** | **String** | The &#x60;shopperNotificationReference&#x60; returned in the response when you requested to notify the shopper. Used for recurring payment only. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | **upi_collect** |  |
|**virtualPaymentAddress** | **String** | The virtual payment address for UPI. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| UPI_COLLECT | &quot;upi_collect&quot; |



