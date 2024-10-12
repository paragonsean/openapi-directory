

# InvoiceTimeline


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | [**List&lt;SelfLink&gt;**](SelfLink.md) | The links related to resource. |  [optional] [readonly] |
|**extraData** | [**TimelineExtraData**](TimelineExtraData.md) |  |  [optional] |
|**id** | **String** | The Timeline message identifier string. |  [optional] [readonly] |
|**message** | **String** | The message that describes the message details. |  [optional] |
|**occurredTime** | **OffsetDateTime** | Timeline message time. |  [optional] [readonly] |
|**triggeredBy** | [**TriggeredByEnum**](#TriggeredByEnum) | Shows who or what triggered the Timeline event. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | Timeline message type. |  [optional] [readonly] |



## Enum: TriggeredByEnum

| Name | Value |
|---- | -----|
| REBILLY | &quot;rebilly&quot; |
| APP | &quot;app&quot; |
| DIRECT_API | &quot;direct-api&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TIMELINE_COMMENT_CREATED | &quot;timeline-comment-created&quot; |
| INVOICE_CREATED | &quot;invoice-created&quot; |
| INVOICE_ISSUED | &quot;invoice-issued&quot; |
| INVOICE_ABANDONED | &quot;invoice-abandoned&quot; |
| INVOICE_VOIDED | &quot;invoice-voided&quot; |
| INVOICE_PAST_DUE | &quot;invoice-past-due&quot; |
| INVOICE_PAID | &quot;invoice-paid&quot; |
| INVOICE_PARTIALLY_PAID | &quot;invoice-partially-paid&quot; |
| INVOICE_DISPUTED | &quot;invoice-disputed&quot; |
| INVOICE_REFUNDED | &quot;invoice-refunded&quot; |
| INVOICE_PARTIALLY_REFUNDED | &quot;invoice-partially-refunded&quot; |
| INVOICE_RENEWAL_PAYMENT_DECLINED | &quot;invoice-renewal-payment-declined&quot; |
| EMAIL_MESSAGE_SENT | &quot;email-message-sent&quot; |
| COUPON_APPLIED | &quot;coupon-applied&quot; |
| TRANSACTION_APPROVED | &quot;transaction-approved&quot; |
| TRANSACTION_ABANDONED | &quot;transaction-abandoned&quot; |
| TRANSACTION_CANCELED | &quot;transaction-canceled&quot; |
| TRANSACTION_DECLINED | &quot;transaction-declined&quot; |
| TRANSACTION_INITIATED | &quot;transaction-initiated&quot; |
| TRANSACTION_REFUNDED | &quot;transaction-refunded&quot; |
| TRANSACTION_VOIDED | &quot;transaction-voided&quot; |



