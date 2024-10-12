

# UpdateAccountHolderResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountHolderCode** | **String** | The code of the account holder. |  [optional] |
|**accountHolderDetails** | [**AccountHolderDetails**](AccountHolderDetails.md) | Details of the account holder. |  [optional] |
|**accountHolderStatus** | [**AccountHolderStatus**](AccountHolderStatus.md) | The new status of the account holder. |  [optional] |
|**description** | **String** | The description of the account holder. |  [optional] |
|**invalidFields** | [**List&lt;ErrorFieldType&gt;**](ErrorFieldType.md) | in case the account holder has not been updated, contains account holder fields, that did not pass the validation. |  [optional] |
|**legalEntity** | [**LegalEntityEnum**](#LegalEntityEnum) | The legal entity of the account holder. |  [optional] |
|**primaryCurrency** | **String** | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes), with which the prospective account holder primarily deals. |  [optional] |
|**pspReference** | **String** | The reference of a request. Can be used to uniquely identify the request. |  [optional] |
|**resultCode** | **String** | The result code. |  [optional] |
|**verification** | [**KYCVerificationResult**](KYCVerificationResult.md) | The details of KYC Verification of the account holder. |  [optional] |



## Enum: LegalEntityEnum

| Name | Value |
|---- | -----|
| BUSINESS | &quot;Business&quot; |
| INDIVIDUAL | &quot;Individual&quot; |
| NON_PROFIT | &quot;NonProfit&quot; |



