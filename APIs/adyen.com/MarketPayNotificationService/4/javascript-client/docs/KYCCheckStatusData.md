# ClassicPlatformsNotifications.KYCCheckStatusData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requiredFields** | **[String]** | A list of the fields required for execution of the check. | [optional] 
**status** | **String** | The status of the check.  Possible values: **AWAITING_DATA** , **DATA_PROVIDED**, **FAILED**, **INVALID_DATA**, **PASSED**, **PENDING**, **RETRY_LIMIT_REACHED**. | 
**summary** | [**KYCCheckSummary**](KYCCheckSummary.md) | A summary of the execution of the check. | [optional] 
**type** | **String** | The type of check.  Possible values:   * **BANK_ACCOUNT_VERIFICATION**: Used in v5 and earlier. Replaced by **PAYOUT_METHOD_VERIFICATION** in v6 and later.   * **COMPANY_VERIFICATION**    * **CARD_VERIFICATION**  * **IDENTITY_VERIFICATION**  * **LEGAL_ARRANGEMENT_VERIFICATION**  * **NONPROFIT_VERIFICATION**   * **PASSPORT_VERIFICATION**  * **PAYOUT_METHOD_VERIFICATION**: Used in v6 and later.  * **PCI_VERIFICATION** | 



## Enum: StatusEnum


* `AWAITING_DATA` (value: `"AWAITING_DATA"`)

* `DATA_PROVIDED` (value: `"DATA_PROVIDED"`)

* `FAILED` (value: `"FAILED"`)

* `INVALID_DATA` (value: `"INVALID_DATA"`)

* `PASSED` (value: `"PASSED"`)

* `PENDING` (value: `"PENDING"`)

* `PENDING_REVIEW` (value: `"PENDING_REVIEW"`)

* `RETRY_LIMIT_REACHED` (value: `"RETRY_LIMIT_REACHED"`)

* `UNCHECKED` (value: `"UNCHECKED"`)





## Enum: TypeEnum


* `BANK_ACCOUNT_VERIFICATION` (value: `"BANK_ACCOUNT_VERIFICATION"`)

* `CARD_VERIFICATION` (value: `"CARD_VERIFICATION"`)

* `COMPANY_VERIFICATION` (value: `"COMPANY_VERIFICATION"`)

* `IDENTITY_VERIFICATION` (value: `"IDENTITY_VERIFICATION"`)

* `LEGAL_ARRANGEMENT_VERIFICATION` (value: `"LEGAL_ARRANGEMENT_VERIFICATION"`)

* `NONPROFIT_VERIFICATION` (value: `"NONPROFIT_VERIFICATION"`)

* `PASSPORT_VERIFICATION` (value: `"PASSPORT_VERIFICATION"`)

* `PAYOUT_METHOD_VERIFICATION` (value: `"PAYOUT_METHOD_VERIFICATION"`)

* `PCI_VERIFICATION` (value: `"PCI_VERIFICATION"`)




