# RebillyRestApi.OrderTimeline

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**[SelfLink]**](SelfLink.md) | The links related to resource. | [optional] [readonly] 
**extraData** | [**TimelineExtraData**](TimelineExtraData.md) |  | [optional] 
**id** | **String** | The Timeline message identifier string. | [optional] [readonly] 
**message** | **String** | The message that describes the message details. | [optional] 
**occurredTime** | **Date** | Timeline message time. | [optional] [readonly] 
**triggeredBy** | **String** | Shows who or what triggered the Timeline message. | [optional] [readonly] 
**type** | **String** | Timeline message type. | [optional] [readonly] 



## Enum: TriggeredByEnum


* `rebilly` (value: `"rebilly"`)

* `app` (value: `"app"`)

* `direct-api` (value: `"direct-api"`)





## Enum: TypeEnum


* `timeline-comment-created` (value: `"timeline-comment-created"`)

* `order-renewed` (value: `"order-renewed"`)

* `order-activated` (value: `"order-activated"`)

* `order-completed` (value: `"order-completed"`)

* `order-reactivated` (value: `"order-reactivated"`)

* `order-canceled` (value: `"order-canceled"`)

* `order-upgraded` (value: `"order-upgraded"`)

* `order-downgraded` (value: `"order-downgraded"`)

* `order-billing-address-changed` (value: `"order-billing-address-changed"`)

* `order-delivery-address-changed` (value: `"order-delivery-address-changed"`)

* `order-renewal-time-changed` (value: `"order-renewal-time-changed"`)

* `order-churned` (value: `"order-churned"`)

* `order-custom-fields-changed` (value: `"order-custom-fields-changed"`)

* `order-items-changed` (value: `"order-items-changed"`)

* `order-billing-anchor-changed` (value: `"order-billing-anchor-changed"`)

* `order-recurring-interval-changed` (value: `"order-recurring-interval-changed"`)

* `order-risk-metadata-changed` (value: `"order-risk-metadata-changed"`)

* `order-paid-early` (value: `"order-paid-early"`)

* `order-quantity-changed` (value: `"order-quantity-changed"`)

* `email-message-sent` (value: `"email-message-sent"`)

* `coupon-applied` (value: `"coupon-applied"`)

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

* `invoice-renewal-payment-declined` (value: `"invoice-renewal-payment-declined"`)




