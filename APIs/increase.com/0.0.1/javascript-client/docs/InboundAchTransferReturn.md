# IncreaseApi.InboundAchTransferReturn

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | The ID of the Inbound ACH Transfer Return. | 
**inboundAchTransferTransactionId** | **String** | The ID for the Transaction that is being returned. | 
**reason** | **String** | The reason why this transfer will be returned. This is sent to the initiating bank. | 
**status** | **String** | The lifecycle status of the transfer. | 
**submission** | [**InboundACHTransferReturnSubmission**](InboundACHTransferReturnSubmission.md) |  | 
**transactionId** | **String** | The ID for the transaction refunding the transfer. | 
**type** | **String** | A constant representing the object&#39;s type. For this resource it will always be &#x60;inbound_ach_transfer_return&#x60;. | 



## Enum: ReasonEnum


* `authorization_revoked_by_customer` (value: `"authorization_revoked_by_customer"`)

* `payment_stopped` (value: `"payment_stopped"`)

* `customer_advised_unauthorized_improper_ineligible_or_incomplete` (value: `"customer_advised_unauthorized_improper_ineligible_or_incomplete"`)

* `representative_payee_deceased_or_unable_to_continue_in_that_capacity` (value: `"representative_payee_deceased_or_unable_to_continue_in_that_capacity"`)

* `beneficiary_or_account_holder_deceased` (value: `"beneficiary_or_account_holder_deceased"`)

* `credit_entry_refused_by_receiver` (value: `"credit_entry_refused_by_receiver"`)

* `duplicate_entry` (value: `"duplicate_entry"`)

* `corporate_customer_advised_not_authorized` (value: `"corporate_customer_advised_not_authorized"`)





## Enum: StatusEnum


* `pending_submitting` (value: `"pending_submitting"`)

* `submitted` (value: `"submitted"`)





## Enum: TypeEnum


* `inbound_ach_transfer_return` (value: `"inbound_ach_transfer_return"`)




