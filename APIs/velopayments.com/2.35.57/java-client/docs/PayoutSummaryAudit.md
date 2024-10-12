

# PayoutSummaryAudit


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dateTime** | **OffsetDateTime** |  |  [optional] |
|**fxSummaries** | [**List&lt;FxSummary&gt;**](FxSummary.md) |  |  [optional] |
|**instructedDateTime** | **String** |  |  [optional] |
|**payorId** | **UUID** |  |  [optional] |
|**payorName** | **String** |  |  |
|**payoutId** | **UUID** |  |  [optional] |
|**payoutMemo** | **String** |  |  [optional] |
|**payoutType** | **String** | The type of payout. One of the following values: STANDARD, AS, ON_BEHALF_OF |  |
|**schedule** | [**PayoutSchedule**](PayoutSchedule.md) |  |  [optional] |
|**sourceAccountSummary** | [**List&lt;SourceAccountSummary&gt;**](SourceAccountSummary.md) |  |  [optional] |
|**status** | **String** | Current status of the Payout. One of the following values: ACCEPTED, REJECTED, SUBMITTED, QUOTED, INSTRUCTED, COMPLETED, INCOMPLETE, CONFIRMED, WITHDRAWN |  |
|**submittedDateTime** | **String** |  |  |
|**totalIncompletePayments** | **Integer** |  |  [optional] |
|**totalPayments** | **Integer** |  |  [optional] |
|**totalReturnedPayments** | **Integer** |  |  [optional] |
|**totalWithdrawnPayments** | **Integer** |  |  [optional] |
|**withdrawnDateTime** | **OffsetDateTime** |  |  [optional] |



