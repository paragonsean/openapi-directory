# RebillyRestApi.TransactionTimeline

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


* `amount-adjusted` (value: `"amount-adjusted"`)

* `blocklist-matched` (value: `"blocklist-matched"`)

* `bump-offer-accepted` (value: `"bump-offer-accepted"`)

* `bump-offer-presented` (value: `"bump-offer-presented"`)

* `bump-offer-rejected` (value: `"bump-offer-rejected"`)

* `customer-redirected-offsite` (value: `"customer-redirected-offsite"`)

* `customer-returned` (value: `"customer-returned"`)

* `dcc-offer-accepted` (value: `"dcc-offer-accepted"`)

* `dcc-offer-forced` (value: `"dcc-offer-forced"`)

* `dcc-offer-presented` (value: `"dcc-offer-presented"`)

* `dcc-offer-rejected` (value: `"dcc-offer-rejected"`)

* `dispute-changed` (value: `"dispute-changed"`)

* `dispute-created` (value: `"dispute-created"`)

* `dispute-forfeited` (value: `"dispute-forfeited"`)

* `dispute-lost` (value: `"dispute-lost"`)

* `dispute-responded` (value: `"dispute-responded"`)

* `dispute-won` (value: `"dispute-won"`)

* `gateway-connection-failed` (value: `"gateway-connection-failed"`)

* `gateway-connection-timed-out` (value: `"gateway-connection-timed-out"`)

* `gateway-response-received` (value: `"gateway-response-received"`)

* `risk-score-changed` (value: `"risk-score-changed"`)

* `timeline-comment-created` (value: `"timeline-comment-created"`)

* `transaction-abandoned` (value: `"transaction-abandoned"`)

* `transaction-amount-discrepancy-found` (value: `"transaction-amount-discrepancy-found"`)

* `transaction-approved` (value: `"transaction-approved"`)

* `transaction-canceled` (value: `"transaction-canceled"`)

* `transaction-capture-delayed` (value: `"transaction-capture-delayed"`)

* `transaction-captured` (value: `"transaction-captured"`)

* `transaction-declined` (value: `"transaction-declined"`)

* `transaction-discrepancy-found` (value: `"transaction-discrepancy-found"`)

* `transaction-initiated` (value: `"transaction-initiated"`)

* `transaction-reconciled` (value: `"transaction-reconciled"`)

* `transaction-refunded` (value: `"transaction-refunded"`)

* `transaction-retried` (value: `"transaction-retried"`)

* `transaction-rules-processed` (value: `"transaction-rules-processed"`)

* `transaction-scheduled-time-changed` (value: `"transaction-scheduled-time-changed"`)

* `transaction-timeout-resolved` (value: `"transaction-timeout-resolved"`)

* `transaction-voided` (value: `"transaction-voided"`)

* `transaction-waiting-gateway` (value: `"transaction-waiting-gateway"`)

* `transaction-queried` (value: `"transaction-queried"`)

* `transaction-updated` (value: `"transaction-updated"`)




