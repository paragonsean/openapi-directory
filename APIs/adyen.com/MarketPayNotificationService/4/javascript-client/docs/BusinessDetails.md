# ClassicPlatformsNotifications.BusinessDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**doingBusinessAs** | **String** | The registered name of the company (if it differs from the legal name of the company). | [optional] 
**legalBusinessName** | **String** | The legal name of the company. | [optional] 
**listedUltimateParentCompany** | [**[UltimateParentCompanyWrapper]**](UltimateParentCompanyWrapper.md) | Information about the parent public company. Required if the account holder is 100% owned by a publicly listed company. | [optional] 
**registrationNumber** | **String** | The registration number of the company. | [optional] 
**shareholders** | [**[ShareholderContactWrapper]**](ShareholderContactWrapper.md) | Array containing information about individuals associated with the account holder either through ownership or control. For details about how you can identify them, refer to [our verification guide](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-process#identify-ubos). | [optional] 
**signatories** | [**[SignatoryContactWrapper]**](SignatoryContactWrapper.md) | Signatories associated with the company. Each array entry should represent one signatory. | [optional] 
**taxId** | **String** | The tax ID of the company. | [optional] 


