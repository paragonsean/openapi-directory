

# ACHTransferReturn

If your transfer is returned, this will contain details of the return.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which the transfer was created. |  |
|**returnReasonCode** | [**ReturnReasonCodeEnum**](#ReturnReasonCodeEnum) | Why the ACH Transfer was returned. |  |
|**transactionId** | **String** | The identifier of the Tranasaction associated with this return. |  |
|**transferId** | **String** | The identifier of the ACH Transfer associated with this return. |  |



## Enum: ReturnReasonCodeEnum

| Name | Value |
|---- | -----|
| INSUFFICIENT_FUND | &quot;insufficient_fund&quot; |
| NO_ACCOUNT | &quot;no_account&quot; |
| ACCOUNT_CLOSED | &quot;account_closed&quot; |
| INVALID_ACCOUNT_NUMBER_STRUCTURE | &quot;invalid_account_number_structure&quot; |
| ACCOUNT_FROZEN_ENTRY_RETURNED_PER_OFAC_INSTRUCTION | &quot;account_frozen_entry_returned_per_ofac_instruction&quot; |
| CREDIT_ENTRY_REFUSED_BY_RECEIVER | &quot;credit_entry_refused_by_receiver&quot; |
| UNAUTHORIZED_DEBIT_TO_CONSUMER_ACCOUNT_USING_CORPORATE_SEC_CODE | &quot;unauthorized_debit_to_consumer_account_using_corporate_sec_code&quot; |
| CORPORATE_CUSTOMER_ADVISED_NOT_AUTHORIZED | &quot;corporate_customer_advised_not_authorized&quot; |
| PAYMENT_STOPPED | &quot;payment_stopped&quot; |
| NON_TRANSACTION_ACCOUNT | &quot;non_transaction_account&quot; |
| UNCOLLECTED_FUNDS | &quot;uncollected_funds&quot; |
| ROUTING_NUMBER_CHECK_DIGIT_ERROR | &quot;routing_number_check_digit_error&quot; |
| CUSTOMER_ADVISED_UNAUTHORIZED_IMPROPER_INELIGIBLE_OR_INCOMPLETE | &quot;customer_advised_unauthorized_improper_ineligible_or_incomplete&quot; |
| AMOUNT_FIELD_ERROR | &quot;amount_field_error&quot; |
| AUTHORIZATION_REVOKED_BY_CUSTOMER | &quot;authorization_revoked_by_customer&quot; |
| INVALID_ACH_ROUTING_NUMBER | &quot;invalid_ach_routing_number&quot; |
| FILE_RECORD_EDIT_CRITERIA | &quot;file_record_edit_criteria&quot; |
| ENR_INVALID_INDIVIDUAL_NAME | &quot;enr_invalid_individual_name&quot; |
| RETURNED_PER_ODFI_REQUEST | &quot;returned_per_odfi_request&quot; |
| ADDENDA_ERROR | &quot;addenda_error&quot; |
| LIMITED_PARTICIPATION_DFI | &quot;limited_participation_dfi&quot; |
| INCORRECTLY_CODED_OUTBOUND_INTERNATIONAL_PAYMENT | &quot;incorrectly_coded_outbound_international_payment&quot; |
| OTHER | &quot;other&quot; |



