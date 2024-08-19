

# RealTimePaymentsTransferRejection

If the transfer is rejected by Real Time Payments or the destination financial institution, this will contain supplemental details.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**rejectReasonAdditionalInformation** | **String** | Additional information about the rejection provided by the recipient bank when the &#x60;reject_reason_code&#x60; is &#x60;NARRATIVE&#x60;. |  |
|**rejectReasonCode** | [**RejectReasonCodeEnum**](#RejectReasonCodeEnum) | The reason the transfer was rejected as provided by the recipient bank or the Real Time Payments network. |  |
|**rejectedAt** | **OffsetDateTime** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which the transfer was rejected. |  |



## Enum: RejectReasonCodeEnum

| Name | Value |
|---- | -----|
| ACCOUNT_CLOSED | &quot;account_closed&quot; |
| ACCOUNT_BLOCKED | &quot;account_blocked&quot; |
| INVALID_CREDITOR_ACCOUNT_TYPE | &quot;invalid_creditor_account_type&quot; |
| INVALID_CREDITOR_ACCOUNT_NUMBER | &quot;invalid_creditor_account_number&quot; |
| INVALID_CREDITOR_FINANCIAL_INSTITUTION_IDENTIFIER | &quot;invalid_creditor_financial_institution_identifier&quot; |
| END_CUSTOMER_DECEASED | &quot;end_customer_deceased&quot; |
| NARRATIVE | &quot;narrative&quot; |
| TRANSACTION_FORBIDDEN | &quot;transaction_forbidden&quot; |
| TRANSACTION_TYPE_NOT_SUPPORTED | &quot;transaction_type_not_supported&quot; |
| UNEXPECTED_AMOUNT | &quot;unexpected_amount&quot; |
| AMOUNT_EXCEEDS_BANK_LIMITS | &quot;amount_exceeds_bank_limits&quot; |
| INVALID_CREDITOR_ADDRESS | &quot;invalid_creditor_address&quot; |
| UNKNOWN_END_CUSTOMER | &quot;unknown_end_customer&quot; |
| INVALID_DEBTOR_ADDRESS | &quot;invalid_debtor_address&quot; |
| TIMEOUT | &quot;timeout&quot; |
| UNSUPPORTED_MESSAGE_FOR_RECIPIENT | &quot;unsupported_message_for_recipient&quot; |
| RECIPIENT_CONNECTION_NOT_AVAILABLE | &quot;recipient_connection_not_available&quot; |
| REAL_TIME_PAYMENTS_SUSPENDED | &quot;real_time_payments_suspended&quot; |
| INSTRUCTED_AGENT_SIGNED_OFF | &quot;instructed_agent_signed_off&quot; |
| PROCESSING_ERROR | &quot;processing_error&quot; |
| OTHER | &quot;other&quot; |



