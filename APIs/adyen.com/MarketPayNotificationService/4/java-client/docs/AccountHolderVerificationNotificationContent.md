

# AccountHolderVerificationNotificationContent


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountHolderCode** | **String** | The code of the account holder. |  [optional] |
|**bankAccountUUID** | **String** | The unique ID of the bank account that has been verified. |  [optional] |
|**shareholderCode** | **String** | The code of the shareholder that has been verified. |  [optional] |
|**signatoryCode** | **String** | The code of the signatory that has been verified. |  [optional] |
|**statusSummary** | [**KYCCheckSummary**](KYCCheckSummary.md) | A summary of the verification status. |  [optional] |
|**verificationStatus** | [**VerificationStatusEnum**](#VerificationStatusEnum) | The status of verification. |  [optional] |
|**verificationType** | [**VerificationTypeEnum**](#VerificationTypeEnum) | The type of validation performed. |  [optional] |



## Enum: VerificationStatusEnum

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



## Enum: VerificationTypeEnum

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



