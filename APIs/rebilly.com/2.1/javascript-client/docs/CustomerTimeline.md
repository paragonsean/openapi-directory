# RebillyRestApi.CustomerTimeline

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**[SelfLink]**](SelfLink.md) | The links related to resource. | [optional] [readonly] 
**customData** | **Object** | Timeline custom event data. Used with &#x60;custom-event&#x60; type. Will be transformed to &#x60;extraData&#x60; two-column table in response. | [optional] 
**customEventType** | **String** | Timeline custom event type. Used with &#x60;custom-event&#x60; type. Must be defined using [Customer Timeline custom event API](#operation/PostCustomerTimelineCustomEventType). | [optional] 
**extraData** | [**TimelineExtraData**](TimelineExtraData.md) |  | [optional] 
**id** | **String** | The Timeline message identifier string. | [optional] [readonly] 
**message** | **String** | The message that describes the message details. | [optional] 
**occurredTime** | **Date** | Timeline message time. | [optional] [readonly] 
**triggeredBy** | **String** | Shows who or what triggered the Timeline message. | [optional] [readonly] 
**type** | **String** | Timeline message type. | [optional] 



## Enum: TriggeredByEnum


* `rebilly` (value: `"rebilly"`)

* `app` (value: `"app"`)

* `direct-api` (value: `"direct-api"`)





## Enum: TypeEnum


* `customer-comment-created` (value: `"customer-comment-created"`)

* `customer-created` (value: `"customer-created"`)

* `primary-address-changed` (value: `"primary-address-changed"`)

* `default-payment-instrument-changed` (value: `"default-payment-instrument-changed"`)

* `lead-source-changed` (value: `"lead-source-changed"`)

* `custom-fields-changed` (value: `"custom-fields-changed"`)

* `coupon-applied` (value: `"coupon-applied"`)

* `coupon-redeemed` (value: `"coupon-redeemed"`)

* `coupon-redemption-canceled` (value: `"coupon-redemption-canceled"`)

* `kyc-document-created` (value: `"kyc-document-created"`)

* `kyc-document-accepted` (value: `"kyc-document-accepted"`)

* `kyc-document-manually-accepted` (value: `"kyc-document-manually-accepted"`)

* `kyc-document-rejected` (value: `"kyc-document-rejected"`)

* `kyc-document-manually-rejected` (value: `"kyc-document-manually-rejected"`)

* `kyc-document-modified` (value: `"kyc-document-modified"`)

* `payment-card-expired` (value: `"payment-card-expired"`)

* `payment-instrument-created` (value: `"payment-instrument-created"`)

* `payment-instrument-deactivated` (value: `"payment-instrument-deactivated"`)

* `customer-bank-account-blocked` (value: `"customer-bank-account-blocked"`)

* `customer-blocked` (value: `"customer-blocked"`)

* `customer-payment-card-blocked` (value: `"customer-payment-card-blocked"`)

* `invoice-created` (value: `"invoice-created"`)

* `invoice-issued` (value: `"invoice-issued"`)

* `invoice-abandoned` (value: `"invoice-abandoned"`)

* `invoice-voided` (value: `"invoice-voided"`)

* `invoice-past-due` (value: `"invoice-past-due"`)

* `invoice-paid` (value: `"invoice-paid"`)

* `invoice-partially-paid` (value: `"invoice-partially-paid"`)

* `invoice-disputed` (value: `"invoice-disputed"`)

* `invoice-refunded` (value: `"invoice-refunded"`)

* `invoice-partially-refunded` (value: `"invoice-partially-refunded"`)

* `order-created` (value: `"order-created"`)

* `order-renewed` (value: `"order-renewed"`)

* `order-activated` (value: `"order-activated"`)

* `order-completed` (value: `"order-completed"`)

* `order-reactivated` (value: `"order-reactivated"`)

* `order-canceled` (value: `"order-canceled"`)

* `order-upgraded` (value: `"order-upgraded"`)

* `order-downgraded` (value: `"order-downgraded"`)

* `order-churned` (value: `"order-churned"`)

* `order-paid-early` (value: `"order-paid-early"`)

* `transaction-approved` (value: `"transaction-approved"`)

* `transaction-canceled` (value: `"transaction-canceled"`)

* `transaction-declined` (value: `"transaction-declined"`)

* `transaction-abandoned` (value: `"transaction-abandoned"`)

* `transaction-refunded` (value: `"transaction-refunded"`)

* `transaction-voided` (value: `"transaction-voided"`)

* `transaction-discrepancy-found` (value: `"transaction-discrepancy-found"`)

* `transaction-amount-discrepancy-found` (value: `"transaction-amount-discrepancy-found"`)

* `email-message-sent` (value: `"email-message-sent"`)

* `custom-event-processed` (value: `"custom-event-processed"`)

* `custom-event` (value: `"custom-event"`)

* `transaction-waiting-gateway` (value: `"transaction-waiting-gateway"`)

* `aml-list-was-possibly-matched` (value: `"aml-list-was-possibly-matched"`)

* `experian-check-performed` (value: `"experian-check-performed"`)




