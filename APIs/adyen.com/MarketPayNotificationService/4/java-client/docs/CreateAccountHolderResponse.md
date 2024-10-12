

# CreateAccountHolderResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountCode** | **String** | The code of a new account created for the account holder. |  [optional] |
|**accountHolderCode** | **String** | The code of the new account holder. |  [optional] |
|**accountHolderDetails** | [**AccountHolderDetails**](AccountHolderDetails.md) | Details of the new account holder. |  [optional] |
|**accountHolderStatus** | [**AccountHolderStatus**](AccountHolderStatus.md) | The status of the new account holder. |  [optional] |
|**description** | **String** | The description of the new account holder. |  [optional] |
|**invalidFields** | [**List&lt;ErrorFieldTypeWrapper&gt;**](ErrorFieldTypeWrapper.md) | A list of fields that caused the &#x60;/createAccountHolder&#x60; request to fail. |  [optional] |
|**legalEntity** | [**LegalEntityEnum**](#LegalEntityEnum) | The type of legal entity of the new account holder. |  [optional] |
|**pspReference** | **String** | The reference of a request. Can be used to uniquely identify the request. |  [optional] |
|**resultCode** | **String** | The result code. |  [optional] |
|**submittedAsync** | **Boolean** | Indicates whether the request is processed asynchronously. Depending on the request&#39;s platform settings, the following scenarios may be applied: * **true**: The request is queued and will be executed when the providing service is available in the order in which the requests are received. * **false**: The processing of the request is immediately attempted; it may result in an error if the providing service is unavailable. |  [optional] |
|**verification** | [**KYCVerificationResult**](KYCVerificationResult.md) | The details of KYC Verification of the account holder. |  [optional] |



## Enum: LegalEntityEnum

| Name | Value |
|---- | -----|
| BUSINESS | &quot;Business&quot; |
| INDIVIDUAL | &quot;Individual&quot; |
| NON_PROFIT | &quot;NonProfit&quot; |



