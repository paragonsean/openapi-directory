# IncreaseApi.Visa

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**electronicCommerceIndicator** | **String** | For electronic commerce transactions, this identifies the level of security used in obtaining the customer&#39;s payment credential. For mail or telephone order transactions, identifies the type of mail or telephone order. | 
**pointOfServiceEntryMode** | **String** | The method used to enter the cardholder&#39;s primary account number and card expiration date | 



## Enum: ElectronicCommerceIndicatorEnum


* `mail_phone_order` (value: `"mail_phone_order"`)

* `recurring` (value: `"recurring"`)

* `installment` (value: `"installment"`)

* `unknown_mail_phone_order` (value: `"unknown_mail_phone_order"`)

* `secure_electronic_commerce` (value: `"secure_electronic_commerce"`)

* `non_authenticated_security_transaction_at_3ds_capable_merchant` (value: `"non_authenticated_security_transaction_at_3ds_capable_merchant"`)

* `non_authenticated_security_transaction` (value: `"non_authenticated_security_transaction"`)

* `non_secure_transaction` (value: `"non_secure_transaction"`)





## Enum: PointOfServiceEntryModeEnum


* `manual` (value: `"manual"`)

* `magnetic_stripe_no_cvv` (value: `"magnetic_stripe_no_cvv"`)

* `optical_code` (value: `"optical_code"`)

* `integrated_circuit_card` (value: `"integrated_circuit_card"`)

* `contactless` (value: `"contactless"`)

* `credential_on_file` (value: `"credential_on_file"`)

* `magnetic_stripe` (value: `"magnetic_stripe"`)

* `contactless_magnetic_stripe` (value: `"contactless_magnetic_stripe"`)

* `integrated_circuit_card_no_cvv` (value: `"integrated_circuit_card_no_cvv"`)




