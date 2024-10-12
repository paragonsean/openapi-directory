# AccountingApi.CompanyInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | [**[Address]**](Address.md) |  | [optional] 
**automatedSalesTax** | **Boolean** | Whether sales tax is calculated automatically for the company | [optional] 
**companyName** | **String** | The name of the company. | [optional] 
**companyStartDate** | **Date** | Date when company file was created | [optional] 
**country** | **String** | country code according to ISO 3166-1 alpha-2. | [optional] 
**createdAt** | **Date** | The date and time when the object was created. | [optional] [readonly] 
**createdBy** | **String** | The user who created the object. | [optional] [readonly] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**customMappings** | **Object** | When custom mappings are configured on the resource, the result is included here. | [optional] 
**defaultSalesTax** | [**TaxRate**](TaxRate.md) |  | [optional] 
**emails** | [**[Email]**](Email.md) |  | [optional] 
**fiscalYearStartMonth** | **String** | The start month of fiscal year. | [optional] 
**id** | **String** | A unique identifier for an object. | [optional] [readonly] 
**language** | **String** | language code according to ISO 639-1. For the United States - EN | [optional] 
**legalName** | **String** | The legal name of the company | [optional] 
**phoneNumbers** | [**[PhoneNumber]**](PhoneNumber.md) |  | [optional] 
**rowVersion** | **String** | A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object. | [optional] 
**salesTaxEnabled** | **Boolean** | Whether sales tax is enabled for the company | [optional] 
**salesTaxNumber** | **String** |  | [optional] 
**status** | **String** | Based on the status some functionality is enabled or disabled. | [optional] 
**updatedAt** | **Date** | The date and time when the object was last updated. | [optional] [readonly] 
**updatedBy** | **String** | The user who last updated the object. | [optional] [readonly] 



## Enum: FiscalYearStartMonthEnum


* `January` (value: `"January"`)

* `February` (value: `"February"`)

* `March` (value: `"March"`)

* `April` (value: `"April"`)

* `May` (value: `"May"`)

* `June` (value: `"June"`)

* `July` (value: `"July"`)

* `August` (value: `"August"`)

* `September` (value: `"September"`)

* `October` (value: `"October"`)

* `November` (value: `"November"`)

* `December` (value: `"December"`)





## Enum: StatusEnum


* `active` (value: `"active"`)

* `inactive` (value: `"inactive"`)




