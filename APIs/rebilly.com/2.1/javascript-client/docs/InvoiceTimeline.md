# RebillyRestApi.InvoiceTimeline

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**[SelfLink]**](SelfLink.md) | The links related to resource. | [optional] [readonly] 
**extraData** | [**TimelineExtraData**](TimelineExtraData.md) |  | [optional] 
**id** | **String** | The Timeline message identifier string. | [optional] [readonly] 
**message** | **String** | The message that describes the message details. | [optional] 
**occurredTime** | **Date** | Timeline message time. | [optional] [readonly] 
**triggeredBy** | **String** | Shows who or what triggered the Timeline event. | [optional] [readonly] 
**type** | **String** | Timeline message type. | [optional] [readonly] 



## Enum: TriggeredByEnum


* `rebilly` (value: `"rebilly"`)

* `app` (value: `"app"`)

* `direct-api` (value: `"direct-api"`)





## Enum: TypeEnum


* `timeline-comment-created` (value: `"timeline-comment-created"`)

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

* `email-message-sent` (value: `"email-message-sent"`)

* `coupon-applied` (value: `"coupon-applied"`)

* `transaction-approved` (value: `"transaction-approved"`)

* `transaction-abandoned` (value: `"transaction-abandoned"`)

* `transaction-canceled` (value: `"transaction-canceled"`)

* `transaction-declined` (value: `"transaction-declined"`)

* `transaction-initiated` (value: `"transaction-initiated"`)

* `transaction-refunded` (value: `"transaction-refunded"`)

* `transaction-voided` (value: `"transaction-voided"`)




