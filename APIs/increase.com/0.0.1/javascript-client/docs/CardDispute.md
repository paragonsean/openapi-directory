# IncreaseApi.CardDispute

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acceptance** | [**CardDisputeAcceptance**](CardDisputeAcceptance.md) |  | 
**createdAt** | **Date** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which the Card Dispute was created. | 
**disputedTransactionId** | **String** | The identifier of the Transaction that was disputed. | 
**explanation** | **String** | Why you disputed the Transaction in question. | 
**id** | **String** | The Card Dispute identifier. | 
**rejection** | [**CardDisputeRejection**](CardDisputeRejection.md) |  | 
**status** | **String** | The results of the Dispute investigation. | 
**type** | **String** | A constant representing the object&#39;s type. For this resource it will always be &#x60;card_dispute&#x60;. | 



## Enum: StatusEnum


* `pending_reviewing` (value: `"pending_reviewing"`)

* `accepted` (value: `"accepted"`)

* `rejected` (value: `"rejected"`)





## Enum: TypeEnum


* `card_dispute` (value: `"card_dispute"`)




