

# CustomerTimeline


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | [**List&lt;SelfLink&gt;**](SelfLink.md) | The links related to resource. |  [optional] [readonly] |
|**customData** | **Object** | Timeline custom event data. Used with &#x60;custom-event&#x60; type. Will be transformed to &#x60;extraData&#x60; two-column table in response. |  [optional] |
|**customEventType** | **String** | Timeline custom event type. Used with &#x60;custom-event&#x60; type. Must be defined using [Customer Timeline custom event API](#operation/PostCustomerTimelineCustomEventType). |  [optional] |
|**extraData** | [**TimelineExtraData**](TimelineExtraData.md) |  |  [optional] |
|**id** | **String** | The Timeline message identifier string. |  [optional] [readonly] |
|**message** | **String** | The message that describes the message details. |  [optional] |
|**occurredTime** | **OffsetDateTime** | Timeline message time. |  [optional] [readonly] |
|**triggeredBy** | [**TriggeredByEnum**](#TriggeredByEnum) | Shows who or what triggered the Timeline message. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | Timeline message type. |  [optional] |



## Enum: TriggeredByEnum

| Name | Value |
|---- | -----|
| REBILLY | &quot;rebilly&quot; |
| APP | &quot;app&quot; |
| DIRECT_API | &quot;direct-api&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CUSTOMER_COMMENT_CREATED | &quot;customer-comment-created&quot; |
| CUSTOMER_CREATED | &quot;customer-created&quot; |
| PRIMARY_ADDRESS_CHANGED | &quot;primary-address-changed&quot; |
| DEFAULT_PAYMENT_INSTRUMENT_CHANGED | &quot;default-payment-instrument-changed&quot; |
| LEAD_SOURCE_CHANGED | &quot;lead-source-changed&quot; |
| CUSTOM_FIELDS_CHANGED | &quot;custom-fields-changed&quot; |
| COUPON_APPLIED | &quot;coupon-applied&quot; |
| COUPON_REDEEMED | &quot;coupon-redeemed&quot; |
| COUPON_REDEMPTION_CANCELED | &quot;coupon-redemption-canceled&quot; |
| KYC_DOCUMENT_CREATED | &quot;kyc-document-created&quot; |
| KYC_DOCUMENT_ACCEPTED | &quot;kyc-document-accepted&quot; |
| KYC_DOCUMENT_MANUALLY_ACCEPTED | &quot;kyc-document-manually-accepted&quot; |
| KYC_DOCUMENT_REJECTED | &quot;kyc-document-rejected&quot; |
| KYC_DOCUMENT_MANUALLY_REJECTED | &quot;kyc-document-manually-rejected&quot; |
| KYC_DOCUMENT_MODIFIED | &quot;kyc-document-modified&quot; |
| PAYMENT_CARD_EXPIRED | &quot;payment-card-expired&quot; |
| PAYMENT_INSTRUMENT_CREATED | &quot;payment-instrument-created&quot; |
| PAYMENT_INSTRUMENT_DEACTIVATED | &quot;payment-instrument-deactivated&quot; |
| CUSTOMER_BANK_ACCOUNT_BLOCKED | &quot;customer-bank-account-blocked&quot; |
| CUSTOMER_BLOCKED | &quot;customer-blocked&quot; |
| CUSTOMER_PAYMENT_CARD_BLOCKED | &quot;customer-payment-card-blocked&quot; |
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
| ORDER_CREATED | &quot;order-created&quot; |
| ORDER_RENEWED | &quot;order-renewed&quot; |
| ORDER_ACTIVATED | &quot;order-activated&quot; |
| ORDER_COMPLETED | &quot;order-completed&quot; |
| ORDER_REACTIVATED | &quot;order-reactivated&quot; |
| ORDER_CANCELED | &quot;order-canceled&quot; |
| ORDER_UPGRADED | &quot;order-upgraded&quot; |
| ORDER_DOWNGRADED | &quot;order-downgraded&quot; |
| ORDER_CHURNED | &quot;order-churned&quot; |
| ORDER_PAID_EARLY | &quot;order-paid-early&quot; |
| TRANSACTION_APPROVED | &quot;transaction-approved&quot; |
| TRANSACTION_CANCELED | &quot;transaction-canceled&quot; |
| TRANSACTION_DECLINED | &quot;transaction-declined&quot; |
| TRANSACTION_ABANDONED | &quot;transaction-abandoned&quot; |
| TRANSACTION_REFUNDED | &quot;transaction-refunded&quot; |
| TRANSACTION_VOIDED | &quot;transaction-voided&quot; |
| TRANSACTION_DISCREPANCY_FOUND | &quot;transaction-discrepancy-found&quot; |
| TRANSACTION_AMOUNT_DISCREPANCY_FOUND | &quot;transaction-amount-discrepancy-found&quot; |
| EMAIL_MESSAGE_SENT | &quot;email-message-sent&quot; |
| CUSTOM_EVENT_PROCESSED | &quot;custom-event-processed&quot; |
| CUSTOM_EVENT | &quot;custom-event&quot; |
| TRANSACTION_WAITING_GATEWAY | &quot;transaction-waiting-gateway&quot; |
| AML_LIST_WAS_POSSIBLY_MATCHED | &quot;aml-list-was-possibly-matched&quot; |
| EXPERIAN_CHECK_PERFORMED | &quot;experian-check-performed&quot; |



