

# GetPaymentsForPayoutResponseV4Summary


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**confirmedPayments** | **Integer** | The count of payments within the payout which have been confirmed. |  [optional] |
|**incompletePayments** | **Integer** | The count of payments within the payout which are incomplete. |  [optional] |
|**instructed** | [**PayoutPrincipal**](PayoutPrincipal.md) |  |  [optional] |
|**instructedDateTime** | **OffsetDateTime** | The date/time at which the payout was instructed. |  [optional] |
|**payoutFrom** | [**PayoutPayor**](PayoutPayor.md) |  |  [optional] |
|**payoutMemo** | **String** | The memo attached to the payout. |  [optional] |
|**payoutStatus** | **String** | Current status of the Payout. One of the following values: ACCEPTED, REJECTED, SUBMITTED, QUOTED, INSTRUCTED, COMPLETED, INCOMPLETE, CONFIRMED, WITHDRAWN |  [optional] |
|**payoutTo** | [**PayoutPayor**](PayoutPayor.md) |  |  [optional] |
|**payoutType** | **String** | The type of payout. One of the following values: STANDARD, AS, ON_BEHALF_OF |  [optional] |
|**quoted** | [**PayoutPrincipal**](PayoutPrincipal.md) |  |  [optional] |
|**quotedDateTime** | **OffsetDateTime** | The date/time at which the payout was quoted. |  [optional] |
|**releasedPayments** | **Integer** | The count of payments within the payout which have been released. |  [optional] |
|**returnedPayments** | **Integer** | The count of payments within the payout which have been returned. |  [optional] |
|**schedule** | [**PayoutSchedule**](PayoutSchedule.md) |  |  [optional] |
|**submittedDateTime** | **OffsetDateTime** | The date/time at which the payout was submitted. |  [optional] |
|**submitting** | [**PayoutPayor**](PayoutPayor.md) |  |  [optional] |
|**totalPayments** | **Integer** | The count of payments within the payout. |  [optional] |
|**withdrawn** | [**PayoutPrincipal**](PayoutPrincipal.md) |  |  [optional] |
|**withdrawnDateTime** | **OffsetDateTime** |  |  [optional] |
|**withdrawnPayments** | **Integer** | The count of payments within the payout which have been withdrawn. |  [optional] |



