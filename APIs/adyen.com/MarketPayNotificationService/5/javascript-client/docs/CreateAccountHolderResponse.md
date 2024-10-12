# ClassicPlatformsNotifications.CreateAccountHolderResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountCode** | **String** | The code of a new account created for the account holder. | [optional] 
**accountHolderCode** | **String** | The code of the new account holder. | [optional] 
**accountHolderDetails** | [**AccountHolderDetails**](AccountHolderDetails.md) | Details of the new account holder. | [optional] 
**accountHolderStatus** | [**AccountHolderStatus**](AccountHolderStatus.md) | The status of the new account holder. | [optional] 
**description** | **String** | The description of the new account holder. | [optional] 
**invalidFields** | [**[ErrorFieldType]**](ErrorFieldType.md) | A list of fields that caused the &#x60;/createAccountHolder&#x60; request to fail. | [optional] 
**legalEntity** | **String** | The type of legal entity of the new account holder. | [optional] 
**primaryCurrency** | **String** | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes), with which the prospective account holder primarily deals. | [optional] 
**pspReference** | **String** | The reference of a request. Can be used to uniquely identify the request. | [optional] 
**resultCode** | **String** | The result code. | [optional] 
**verification** | [**KYCVerificationResult**](KYCVerificationResult.md) | The details of KYC Verification of the account holder. | [optional] 



## Enum: LegalEntityEnum


* `Business` (value: `"Business"`)

* `Individual` (value: `"Individual"`)

* `NonProfit` (value: `"NonProfit"`)




