

# OrderTimeline


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | [**List&lt;SelfLink&gt;**](SelfLink.md) | The links related to resource. |  [optional] [readonly] |
|**extraData** | [**TimelineExtraData**](TimelineExtraData.md) |  |  [optional] |
|**id** | **String** | The Timeline message identifier string. |  [optional] [readonly] |
|**message** | **String** | The message that describes the message details. |  [optional] |
|**occurredTime** | **OffsetDateTime** | Timeline message time. |  [optional] [readonly] |
|**triggeredBy** | [**TriggeredByEnum**](#TriggeredByEnum) | Shows who or what triggered the Timeline message. |  [optional] [readonly] |
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
| ORDER_RENEWED | &quot;order-renewed&quot; |
| ORDER_ACTIVATED | &quot;order-activated&quot; |
| ORDER_COMPLETED | &quot;order-completed&quot; |
| ORDER_REACTIVATED | &quot;order-reactivated&quot; |
| ORDER_CANCELED | &quot;order-canceled&quot; |
| ORDER_UPGRADED | &quot;order-upgraded&quot; |
| ORDER_DOWNGRADED | &quot;order-downgraded&quot; |
| ORDER_BILLING_ADDRESS_CHANGED | &quot;order-billing-address-changed&quot; |
| ORDER_DELIVERY_ADDRESS_CHANGED | &quot;order-delivery-address-changed&quot; |
| ORDER_RENEWAL_TIME_CHANGED | &quot;order-renewal-time-changed&quot; |
| ORDER_CHURNED | &quot;order-churned&quot; |
| ORDER_CUSTOM_FIELDS_CHANGED | &quot;order-custom-fields-changed&quot; |
| ORDER_ITEMS_CHANGED | &quot;order-items-changed&quot; |
| ORDER_BILLING_ANCHOR_CHANGED | &quot;order-billing-anchor-changed&quot; |
| ORDER_RECURRING_INTERVAL_CHANGED | &quot;order-recurring-interval-changed&quot; |
| ORDER_RISK_METADATA_CHANGED | &quot;order-risk-metadata-changed&quot; |
| ORDER_PAID_EARLY | &quot;order-paid-early&quot; |
| ORDER_QUANTITY_CHANGED | &quot;order-quantity-changed&quot; |
| EMAIL_MESSAGE_SENT | &quot;email-message-sent&quot; |
| COUPON_APPLIED | &quot;coupon-applied&quot; |
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



