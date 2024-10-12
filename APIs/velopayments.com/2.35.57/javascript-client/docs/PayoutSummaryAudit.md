# VeloPaymentsApis.PayoutSummaryAudit

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dateTime** | **Date** |  | [optional] 
**fxSummaries** | [**[FxSummary]**](FxSummary.md) |  | [optional] 
**instructedDateTime** | **String** |  | [optional] 
**payorId** | **String** |  | [optional] 
**payorName** | **String** |  | 
**payoutId** | **String** |  | [optional] 
**payoutMemo** | **String** |  | [optional] 
**payoutType** | **String** | The type of payout. One of the following values: STANDARD, AS, ON_BEHALF_OF | 
**schedule** | [**PayoutSchedule**](PayoutSchedule.md) |  | [optional] 
**sourceAccountSummary** | [**[SourceAccountSummary]**](SourceAccountSummary.md) |  | [optional] 
**status** | **String** | Current status of the Payout. One of the following values: ACCEPTED, REJECTED, SUBMITTED, QUOTED, INSTRUCTED, COMPLETED, INCOMPLETE, CONFIRMED, WITHDRAWN | 
**submittedDateTime** | **String** |  | 
**totalIncompletePayments** | **Number** |  | [optional] 
**totalPayments** | **Number** |  | [optional] 
**totalReturnedPayments** | **Number** |  | [optional] 
**totalWithdrawnPayments** | **Number** |  | [optional] 
**withdrawnDateTime** | **Date** |  | [optional] 


