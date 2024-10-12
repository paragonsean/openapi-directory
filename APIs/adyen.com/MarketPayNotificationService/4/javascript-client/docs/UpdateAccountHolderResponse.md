# ClassicPlatformsNotifications.UpdateAccountHolderResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountHolderCode** | **String** | The code of the account holder. | [optional] 
**accountHolderDetails** | [**AccountHolderDetails**](AccountHolderDetails.md) | Details of the account holder. | [optional] 
**accountHolderStatus** | [**AccountHolderStatus**](AccountHolderStatus.md) | The new status of the account holder. | [optional] 
**description** | **String** | The description of the account holder. | [optional] 
**invalidFields** | [**[ErrorFieldTypeWrapper]**](ErrorFieldTypeWrapper.md) | in case the account holder has not been updated, contains account holder fields, that did not pass the validation. | [optional] 
**legalEntity** | **String** | The legal entity of the account holder. | [optional] 
**pspReference** | **String** | The reference of a request. Can be used to uniquely identify the request. | [optional] 
**resultCode** | **String** | The result code. | [optional] 
**submittedAsync** | **Boolean** | Indicates whether the request is processed asynchronously. Depending on the request&#39;s platform settings, the following scenarios may be applied: * **true**: The request is queued and will be executed when the providing service is available in the order in which the requests are received. * **false**: The processing of the request is immediately attempted; it may result in an error if the providing service is unavailable. | [optional] 
**updatedFields** | [**[FieldTypeWrapper]**](FieldTypeWrapper.md) | A list of the fields updated through the request. | [optional] 
**verification** | [**KYCVerificationResult**](KYCVerificationResult.md) | The details of KYC Verification of the account holder. | [optional] 



## Enum: LegalEntityEnum


* `Business` (value: `"Business"`)

* `Individual` (value: `"Individual"`)

* `NonProfit` (value: `"NonProfit"`)




