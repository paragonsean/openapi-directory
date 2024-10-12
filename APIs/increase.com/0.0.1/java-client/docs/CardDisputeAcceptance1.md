

# CardDisputeAcceptance1

A Card Dispute Acceptance object. This field will be present in the JSON response if and only if `category` is equal to `card_dispute_acceptance`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**acceptedAt** | **OffsetDateTime** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which the Card Dispute was accepted. |  |
|**cardDisputeId** | **String** | The identifier of the Card Dispute that was accepted. |  |
|**transactionId** | **String** | The identifier of the Transaction that was created to return the disputed funds to your account. |  |



