# IncreaseApi.CreateAnAchReturnParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **String** | The reason why this transfer will be returned. The most usual return codes are &#x60;payment_stopped&#x60; for debits and &#x60;credit_entry_refused_by_receiver&#x60; for credits. | 
**transactionId** | **String** | The transaction identifier of the Inbound ACH Transfer to return to the originating financial institution. | 



## Enum: ReasonEnum


* `authorization_revoked_by_customer` (value: `"authorization_revoked_by_customer"`)

* `payment_stopped` (value: `"payment_stopped"`)

* `customer_advised_unauthorized_improper_ineligible_or_incomplete` (value: `"customer_advised_unauthorized_improper_ineligible_or_incomplete"`)

* `representative_payee_deceased_or_unable_to_continue_in_that_capacity` (value: `"representative_payee_deceased_or_unable_to_continue_in_that_capacity"`)

* `beneficiary_or_account_holder_deceased` (value: `"beneficiary_or_account_holder_deceased"`)

* `credit_entry_refused_by_receiver` (value: `"credit_entry_refused_by_receiver"`)

* `duplicate_entry` (value: `"duplicate_entry"`)

* `corporate_customer_advised_not_authorized` (value: `"corporate_customer_advised_not_authorized"`)




