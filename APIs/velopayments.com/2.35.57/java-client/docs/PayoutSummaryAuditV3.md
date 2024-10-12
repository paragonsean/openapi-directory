

# PayoutSummaryAuditV3


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fxSummaries** | [**List&lt;FxSummaryV3&gt;**](FxSummaryV3.md) |  |  [optional] |
|**instructedDateTime** | **String** |  |  [optional] |
|**payorId** | **UUID** |  |  [optional] |
|**payoutId** | **UUID** |  |  |
|**payoutMemo** | **String** |  |  [optional] |
|**sourceAccountSummary** | [**List&lt;SourceAccountSummaryV3&gt;**](SourceAccountSummaryV3.md) |  |  [optional] |
|**status** | **String** | Current status of the payout. One of the following values: ACCEPTED, REJECTED, SUBMITTED, QUOTED, INSTRUCTED, COMPLETED, INCOMPLETE, CONFIRMED, WITHDRAWN |  |
|**submittedDateTime** | **String** |  |  |
|**totalFailedPayments** | **Integer** |  |  [optional] |
|**totalIncompletePayments** | **Integer** |  |  [optional] |
|**totalPayments** | **Integer** |  |  [optional] |
|**withdrawnDateTime** | **String** |  |  [optional] |



