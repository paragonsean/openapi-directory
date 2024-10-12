

# GetPaymentsForPayoutResponseV3Summary


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**confirmedPayments** | **Integer** | The count of payments within the payout which have been confirmed. |  [optional] |
|**failedPayments** | **Integer** | The count of payments within the payout which have failed or been returned. |  [optional] |
|**incompletePayments** | **Integer** | The count of payments within the payout which are incomplete. |  [optional] |
|**instructedDateTime** | **OffsetDateTime** | The date/time at which the payout was instructed. |  [optional] |
|**payoutMemo** | **String** | The memo attached to the payout. |  [optional] |
|**payoutStatus** | **String** | The current status of the payout. One of the following values: ACCEPTED, REJECTED, SUBMITTED, QUOTED, INSTRUCTED, COMPLETED, INCOMPLETE, CONFIRMED, WITHDRAWN |  [optional] |
|**releasedPayments** | **Integer** | The count of payments within the payout which have been released. |  [optional] |
|**submittedDateTime** | **OffsetDateTime** | The date/time at which the payout was submitted. |  [optional] |
|**totalPayments** | **Integer** | The count of payments within the payout. |  [optional] |
|**withdrawnDateTime** | **OffsetDateTime** | The date/time at which the payout was withdrawn. |  [optional] |



