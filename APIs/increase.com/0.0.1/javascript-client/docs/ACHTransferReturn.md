# IncreaseApi.ACHTransferReturn

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **Date** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which the transfer was created. | 
**returnReasonCode** | **String** | Why the ACH Transfer was returned. | 
**transactionId** | **String** | The identifier of the Tranasaction associated with this return. | 
**transferId** | **String** | The identifier of the ACH Transfer associated with this return. | 



## Enum: ReturnReasonCodeEnum


* `insufficient_fund` (value: `"insufficient_fund"`)

* `no_account` (value: `"no_account"`)

* `account_closed` (value: `"account_closed"`)

* `invalid_account_number_structure` (value: `"invalid_account_number_structure"`)

* `account_frozen_entry_returned_per_ofac_instruction` (value: `"account_frozen_entry_returned_per_ofac_instruction"`)

* `credit_entry_refused_by_receiver` (value: `"credit_entry_refused_by_receiver"`)

* `unauthorized_debit_to_consumer_account_using_corporate_sec_code` (value: `"unauthorized_debit_to_consumer_account_using_corporate_sec_code"`)

* `corporate_customer_advised_not_authorized` (value: `"corporate_customer_advised_not_authorized"`)

* `payment_stopped` (value: `"payment_stopped"`)

* `non_transaction_account` (value: `"non_transaction_account"`)

* `uncollected_funds` (value: `"uncollected_funds"`)

* `routing_number_check_digit_error` (value: `"routing_number_check_digit_error"`)

* `customer_advised_unauthorized_improper_ineligible_or_incomplete` (value: `"customer_advised_unauthorized_improper_ineligible_or_incomplete"`)

* `amount_field_error` (value: `"amount_field_error"`)

* `authorization_revoked_by_customer` (value: `"authorization_revoked_by_customer"`)

* `invalid_ach_routing_number` (value: `"invalid_ach_routing_number"`)

* `file_record_edit_criteria` (value: `"file_record_edit_criteria"`)

* `enr_invalid_individual_name` (value: `"enr_invalid_individual_name"`)

* `returned_per_odfi_request` (value: `"returned_per_odfi_request"`)

* `addenda_error` (value: `"addenda_error"`)

* `limited_participation_dfi` (value: `"limited_participation_dfi"`)

* `incorrectly_coded_outbound_international_payment` (value: `"incorrectly_coded_outbound_international_payment"`)

* `other` (value: `"other"`)




