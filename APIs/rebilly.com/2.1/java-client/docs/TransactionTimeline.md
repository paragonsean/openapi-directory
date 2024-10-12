

# TransactionTimeline


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
| AMOUNT_ADJUSTED | &quot;amount-adjusted&quot; |
| BLOCKLIST_MATCHED | &quot;blocklist-matched&quot; |
| BUMP_OFFER_ACCEPTED | &quot;bump-offer-accepted&quot; |
| BUMP_OFFER_PRESENTED | &quot;bump-offer-presented&quot; |
| BUMP_OFFER_REJECTED | &quot;bump-offer-rejected&quot; |
| CUSTOMER_REDIRECTED_OFFSITE | &quot;customer-redirected-offsite&quot; |
| CUSTOMER_RETURNED | &quot;customer-returned&quot; |
| DCC_OFFER_ACCEPTED | &quot;dcc-offer-accepted&quot; |
| DCC_OFFER_FORCED | &quot;dcc-offer-forced&quot; |
| DCC_OFFER_PRESENTED | &quot;dcc-offer-presented&quot; |
| DCC_OFFER_REJECTED | &quot;dcc-offer-rejected&quot; |
| DISPUTE_CHANGED | &quot;dispute-changed&quot; |
| DISPUTE_CREATED | &quot;dispute-created&quot; |
| DISPUTE_FORFEITED | &quot;dispute-forfeited&quot; |
| DISPUTE_LOST | &quot;dispute-lost&quot; |
| DISPUTE_RESPONDED | &quot;dispute-responded&quot; |
| DISPUTE_WON | &quot;dispute-won&quot; |
| GATEWAY_CONNECTION_FAILED | &quot;gateway-connection-failed&quot; |
| GATEWAY_CONNECTION_TIMED_OUT | &quot;gateway-connection-timed-out&quot; |
| GATEWAY_RESPONSE_RECEIVED | &quot;gateway-response-received&quot; |
| RISK_SCORE_CHANGED | &quot;risk-score-changed&quot; |
| TIMELINE_COMMENT_CREATED | &quot;timeline-comment-created&quot; |
| TRANSACTION_ABANDONED | &quot;transaction-abandoned&quot; |
| TRANSACTION_AMOUNT_DISCREPANCY_FOUND | &quot;transaction-amount-discrepancy-found&quot; |
| TRANSACTION_APPROVED | &quot;transaction-approved&quot; |
| TRANSACTION_CANCELED | &quot;transaction-canceled&quot; |
| TRANSACTION_CAPTURE_DELAYED | &quot;transaction-capture-delayed&quot; |
| TRANSACTION_CAPTURED | &quot;transaction-captured&quot; |
| TRANSACTION_DECLINED | &quot;transaction-declined&quot; |
| TRANSACTION_DISCREPANCY_FOUND | &quot;transaction-discrepancy-found&quot; |
| TRANSACTION_INITIATED | &quot;transaction-initiated&quot; |
| TRANSACTION_RECONCILED | &quot;transaction-reconciled&quot; |
| TRANSACTION_REFUNDED | &quot;transaction-refunded&quot; |
| TRANSACTION_RETRIED | &quot;transaction-retried&quot; |
| TRANSACTION_RULES_PROCESSED | &quot;transaction-rules-processed&quot; |
| TRANSACTION_SCHEDULED_TIME_CHANGED | &quot;transaction-scheduled-time-changed&quot; |
| TRANSACTION_TIMEOUT_RESOLVED | &quot;transaction-timeout-resolved&quot; |
| TRANSACTION_VOIDED | &quot;transaction-voided&quot; |
| TRANSACTION_WAITING_GATEWAY | &quot;transaction-waiting-gateway&quot; |
| TRANSACTION_QUERIED | &quot;transaction-queried&quot; |
| TRANSACTION_UPDATED | &quot;transaction-updated&quot; |



