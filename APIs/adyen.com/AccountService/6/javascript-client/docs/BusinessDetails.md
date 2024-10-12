# AccountApi.BusinessDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**doingBusinessAs** | **String** | The registered name of the company (if it differs from the legal name of the company). | [optional] 
**legalBusinessName** | **String** | The legal name of the company. | [optional] 
**listedUltimateParentCompany** | [**[UltimateParentCompany]**](UltimateParentCompany.md) | Information about the parent public company. Required if the account holder is 100% owned by a publicly listed company. | [optional] 
**registrationNumber** | **String** | The registration number of the company. | [optional] 
**shareholders** | [**[ShareholderContact]**](ShareholderContact.md) | Array containing information about individuals associated with the account holder either through ownership or control. For details about how you can identify them, refer to [our verification guide](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-process#identify-ubos). | [optional] 
**signatories** | [**[SignatoryContact]**](SignatoryContact.md) | Signatories associated with the company. Each array entry should represent one signatory. | [optional] 
**stockExchange** | **String** | Market Identifier Code (MIC). | [optional] 
**stockNumber** | **String** | International Securities Identification Number (ISIN). | [optional] 
**stockTicker** | **String** | Stock Ticker symbol. | [optional] 
**taxId** | **String** | The tax ID of the company. | [optional] 


