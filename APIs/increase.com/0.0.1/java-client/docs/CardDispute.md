

# CardDispute

If unauthorized activity occurs on a card, you can create a Card Dispute and we'll return the funds if appropriate.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**acceptance** | [**CardDisputeAcceptance**](CardDisputeAcceptance.md) |  |  |
|**createdAt** | **OffsetDateTime** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which the Card Dispute was created. |  |
|**disputedTransactionId** | **String** | The identifier of the Transaction that was disputed. |  |
|**explanation** | **String** | Why you disputed the Transaction in question. |  |
|**id** | **String** | The Card Dispute identifier. |  |
|**rejection** | [**CardDisputeRejection**](CardDisputeRejection.md) |  |  |
|**status** | [**StatusEnum**](#StatusEnum) | The results of the Dispute investigation. |  |
|**type** | [**TypeEnum**](#TypeEnum) | A constant representing the object&#39;s type. For this resource it will always be &#x60;card_dispute&#x60;. |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING_REVIEWING | &quot;pending_reviewing&quot; |
| ACCEPTED | &quot;accepted&quot; |
| REJECTED | &quot;rejected&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CARD_DISPUTE | &quot;card_dispute&quot; |



