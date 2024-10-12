# AccountApi.GetAccountHolderResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountHolderCode** | **String** | The code of the account holder. | [optional] 
**accountHolderDetails** | [**AccountHolderDetails**](AccountHolderDetails.md) | Details of the account holder. | [optional] 
**accountHolderStatus** | [**AccountHolderStatus**](AccountHolderStatus.md) | The status of the account holder. | [optional] 
**accounts** | [**[Account]**](Account.md) | A list of the accounts under the account holder. | [optional] 
**description** | **String** | The description of the account holder. | [optional] 
**invalidFields** | [**[ErrorFieldType]**](ErrorFieldType.md) | Contains field validation errors that would prevent requests from being processed. | [optional] 
**legalEntity** | **String** | The legal entity of the account holder. | [optional] 
**migrationData** | [**MigrationData**](MigrationData.md) | Details of the account holder migrated to the balance platform. | [optional] 
**primaryCurrency** | **String** | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes), with which the prospective account holder primarily deals. | [optional] 
**pspReference** | **String** | The reference of a request. Can be used to uniquely identify the request. | [optional] 
**resultCode** | **String** | The result code. | [optional] 
**systemUpToDateTime** | **Date** | The time that shows how up to date is the information in the response. | [optional] 
**verification** | [**KYCVerificationResult**](KYCVerificationResult.md) | The details of KYC Verification of the account holder. | [optional] 
**verificationProfile** | **String** | The identifier of the profile that applies to this entity. | [optional] 



## Enum: LegalEntityEnum


* `Business` (value: `"Business"`)

* `Individual` (value: `"Individual"`)

* `NonProfit` (value: `"NonProfit"`)

* `Partnership` (value: `"Partnership"`)

* `PublicCompany` (value: `"PublicCompany"`)




