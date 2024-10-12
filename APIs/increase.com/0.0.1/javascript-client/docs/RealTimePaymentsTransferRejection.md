# IncreaseApi.RealTimePaymentsTransferRejection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rejectReasonAdditionalInformation** | **String** | Additional information about the rejection provided by the recipient bank when the &#x60;reject_reason_code&#x60; is &#x60;NARRATIVE&#x60;. | 
**rejectReasonCode** | **String** | The reason the transfer was rejected as provided by the recipient bank or the Real Time Payments network. | 
**rejectedAt** | **Date** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which the transfer was rejected. | 



## Enum: RejectReasonCodeEnum


* `account_closed` (value: `"account_closed"`)

* `account_blocked` (value: `"account_blocked"`)

* `invalid_creditor_account_type` (value: `"invalid_creditor_account_type"`)

* `invalid_creditor_account_number` (value: `"invalid_creditor_account_number"`)

* `invalid_creditor_financial_institution_identifier` (value: `"invalid_creditor_financial_institution_identifier"`)

* `end_customer_deceased` (value: `"end_customer_deceased"`)

* `narrative` (value: `"narrative"`)

* `transaction_forbidden` (value: `"transaction_forbidden"`)

* `transaction_type_not_supported` (value: `"transaction_type_not_supported"`)

* `unexpected_amount` (value: `"unexpected_amount"`)

* `amount_exceeds_bank_limits` (value: `"amount_exceeds_bank_limits"`)

* `invalid_creditor_address` (value: `"invalid_creditor_address"`)

* `unknown_end_customer` (value: `"unknown_end_customer"`)

* `invalid_debtor_address` (value: `"invalid_debtor_address"`)

* `timeout` (value: `"timeout"`)

* `unsupported_message_for_recipient` (value: `"unsupported_message_for_recipient"`)

* `recipient_connection_not_available` (value: `"recipient_connection_not_available"`)

* `real_time_payments_suspended` (value: `"real_time_payments_suspended"`)

* `instructed_agent_signed_off` (value: `"instructed_agent_signed_off"`)

* `processing_error` (value: `"processing_error"`)

* `other` (value: `"other"`)




