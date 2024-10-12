

# PayoutSummaryResponseV3


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**acceptedPayments** | [**List&lt;AcceptedPaymentV3&gt;**](AcceptedPaymentV3.md) |  |  |
|**accounts** | [**List&lt;SourceAccountV3&gt;**](SourceAccountV3.md) |  |  |
|**fxSummaries** | [**List&lt;QuoteFxSummaryV3&gt;**](QuoteFxSummaryV3.md) |  |  |
|**paymentsAccepted** | **Integer** | The number of payments that were accepted in the payout |  [optional] |
|**paymentsRejected** | **Integer** | The number of payments that were rejected in the payout |  [optional] |
|**paymentsSubmitted** | **Integer** | The number of payments that were submitted in the payout |  [optional] |
|**paymentsWithdrawn** | **Integer** | The number of payments that were withdrawn in the payout |  |
|**payoutId** | **UUID** | The id of the payout |  [optional] |
|**rejectedPayments** | [**List&lt;RejectedPaymentV3&gt;**](RejectedPaymentV3.md) |  |  |
|**schedule** | [**PayoutScheduleV3**](PayoutScheduleV3.md) |  |  [optional] |
|**status** | **String** | The status of the payout (one of SUBMITTED, ACCEPTED, REJECTED, QUOTED, INSTRUCTED, COMPLETED, INCOMPLETE, WITHDRAWN) |  [optional] |



