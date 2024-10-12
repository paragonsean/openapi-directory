# VeloPaymentsApis.GetPaymentsForPayoutResponseV4Summary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confirmedPayments** | **Number** | The count of payments within the payout which have been confirmed. | [optional] 
**incompletePayments** | **Number** | The count of payments within the payout which are incomplete. | [optional] 
**instructed** | [**PayoutPrincipal**](PayoutPrincipal.md) |  | [optional] 
**instructedDateTime** | **Date** | The date/time at which the payout was instructed. | [optional] 
**payoutFrom** | [**PayoutPayor**](PayoutPayor.md) |  | [optional] 
**payoutMemo** | **String** | The memo attached to the payout. | [optional] 
**payoutStatus** | **String** | Current status of the Payout. One of the following values: ACCEPTED, REJECTED, SUBMITTED, QUOTED, INSTRUCTED, COMPLETED, INCOMPLETE, CONFIRMED, WITHDRAWN | [optional] 
**payoutTo** | [**PayoutPayor**](PayoutPayor.md) |  | [optional] 
**payoutType** | **String** | The type of payout. One of the following values: STANDARD, AS, ON_BEHALF_OF | [optional] 
**quoted** | [**PayoutPrincipal**](PayoutPrincipal.md) |  | [optional] 
**quotedDateTime** | **Date** | The date/time at which the payout was quoted. | [optional] 
**releasedPayments** | **Number** | The count of payments within the payout which have been released. | [optional] 
**returnedPayments** | **Number** | The count of payments within the payout which have been returned. | [optional] 
**schedule** | [**PayoutSchedule**](PayoutSchedule.md) |  | [optional] 
**submittedDateTime** | **Date** | The date/time at which the payout was submitted. | [optional] 
**submitting** | [**PayoutPayor**](PayoutPayor.md) |  | [optional] 
**totalPayments** | **Number** | The count of payments within the payout. | [optional] 
**withdrawn** | [**PayoutPrincipal**](PayoutPrincipal.md) |  | [optional] 
**withdrawnDateTime** | **Date** |  | [optional] 
**withdrawnPayments** | **Number** | The count of payments within the payout which have been withdrawn. | [optional] 


