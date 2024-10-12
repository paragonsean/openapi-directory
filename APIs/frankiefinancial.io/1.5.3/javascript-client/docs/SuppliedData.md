# FrankieFinancialApi.SuppliedData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abn** | **String** | Australian Business Number - MUST be 11 digits. Can be supplied in lieu of the ACN  | 
**acn** | **String** | Australian Company Number on file - MUST be zero left-padded to 9 digits  | 
**companyType** | **String** | The type of company on file. Use the ABR&#39;s company types, as given here:  https://abr.business.gov.au/Documentation/ReferenceData (entity types)  | 
**customerReference** | **String** | Your reference number for this company | 
**name** | **String** | The name of the company to be verified  | 



## Enum: CompanyTypeEnum


* `PRV` (value: `"PRV"`)

* `PUB` (value: `"PUB"`)




