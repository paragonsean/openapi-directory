# ClassicPlatformsNotifications.AccountHolderVerificationNotificationContent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountHolderCode** | **String** | The code of the account holder. | [optional] 
**bankAccountUUID** | **String** | The unique ID of the bank account that has been verified. | [optional] 
**shareholderCode** | **String** | The code of the shareholder that has been verified. | [optional] 
**signatoryCode** | **String** | The code of the signatory that has been verified. | [optional] 
**statusSummary** | [**KYCCheckSummary**](KYCCheckSummary.md) | A summary of the verification status. | [optional] 
**verificationStatus** | **String** | The status of verification. | [optional] 
**verificationType** | **String** | The type of validation performed. | [optional] 



## Enum: VerificationStatusEnum


* `AWAITING_DATA` (value: `"AWAITING_DATA"`)

* `DATA_PROVIDED` (value: `"DATA_PROVIDED"`)

* `FAILED` (value: `"FAILED"`)

* `INVALID_DATA` (value: `"INVALID_DATA"`)

* `PASSED` (value: `"PASSED"`)

* `PENDING` (value: `"PENDING"`)

* `PENDING_REVIEW` (value: `"PENDING_REVIEW"`)

* `RETRY_LIMIT_REACHED` (value: `"RETRY_LIMIT_REACHED"`)

* `UNCHECKED` (value: `"UNCHECKED"`)





## Enum: VerificationTypeEnum


* `BANK_ACCOUNT_VERIFICATION` (value: `"BANK_ACCOUNT_VERIFICATION"`)

* `CARD_VERIFICATION` (value: `"CARD_VERIFICATION"`)

* `COMPANY_VERIFICATION` (value: `"COMPANY_VERIFICATION"`)

* `IDENTITY_VERIFICATION` (value: `"IDENTITY_VERIFICATION"`)

* `LEGAL_ARRANGEMENT_VERIFICATION` (value: `"LEGAL_ARRANGEMENT_VERIFICATION"`)

* `NONPROFIT_VERIFICATION` (value: `"NONPROFIT_VERIFICATION"`)

* `PASSPORT_VERIFICATION` (value: `"PASSPORT_VERIFICATION"`)

* `PAYOUT_METHOD_VERIFICATION` (value: `"PAYOUT_METHOD_VERIFICATION"`)

* `PCI_VERIFICATION` (value: `"PCI_VERIFICATION"`)




