

# KYCCheckStatusData


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**requiredFields** | **List&lt;String&gt;** | A list of the fields required for execution of the check. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the check.  Possible values: **AWAITING_DATA** , **DATA_PROVIDED**, **FAILED**, **INVALID_DATA**, **PASSED**, **PENDING**, **RETRY_LIMIT_REACHED**. |  |
|**summary** | [**KYCCheckSummary**](KYCCheckSummary.md) | A summary of the execution of the check. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of check.  Possible values:   * **BANK_ACCOUNT_VERIFICATION**: Used in v5 and earlier. Replaced by **PAYOUT_METHOD_VERIFICATION** in v6 and later.   * **COMPANY_VERIFICATION**    * **CARD_VERIFICATION**  * **IDENTITY_VERIFICATION**  * **LEGAL_ARRANGEMENT_VERIFICATION**  * **NONPROFIT_VERIFICATION**   * **PASSPORT_VERIFICATION**  * **PAYOUT_METHOD_VERIFICATION**: Used in v6 and later.  * **PCI_VERIFICATION** |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| AWAITING_DATA | &quot;AWAITING_DATA&quot; |
| DATA_PROVIDED | &quot;DATA_PROVIDED&quot; |
| FAILED | &quot;FAILED&quot; |
| INVALID_DATA | &quot;INVALID_DATA&quot; |
| PASSED | &quot;PASSED&quot; |
| PENDING | &quot;PENDING&quot; |
| PENDING_REVIEW | &quot;PENDING_REVIEW&quot; |
| RETRY_LIMIT_REACHED | &quot;RETRY_LIMIT_REACHED&quot; |
| UNCHECKED | &quot;UNCHECKED&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| BANK_ACCOUNT_VERIFICATION | &quot;BANK_ACCOUNT_VERIFICATION&quot; |
| CARD_VERIFICATION | &quot;CARD_VERIFICATION&quot; |
| COMPANY_VERIFICATION | &quot;COMPANY_VERIFICATION&quot; |
| IDENTITY_VERIFICATION | &quot;IDENTITY_VERIFICATION&quot; |
| LEGAL_ARRANGEMENT_VERIFICATION | &quot;LEGAL_ARRANGEMENT_VERIFICATION&quot; |
| NONPROFIT_VERIFICATION | &quot;NONPROFIT_VERIFICATION&quot; |
| PASSPORT_VERIFICATION | &quot;PASSPORT_VERIFICATION&quot; |
| PAYOUT_METHOD_VERIFICATION | &quot;PAYOUT_METHOD_VERIFICATION&quot; |
| PCI_VERIFICATION | &quot;PCI_VERIFICATION&quot; |



