# LegalEntityManagementApi.Organization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | Your description for the organization. | [optional] 
**doingBusinessAs** | **String** | The organization&#39;s trading name, if different from the registered legal name. | [optional] 
**email** | **String** | The email address of the legal entity. | [optional] 
**legalName** | **String** | The organization&#39;s legal name. | 
**phone** | [**PhoneNumber**](PhoneNumber.md) | The phone number of the legal entity. | [optional] 
**principalPlaceOfBusiness** | [**Address**](Address.md) | The address where the organization operates from. Provide this if the principal place of business is different from the &#x60;registeredAddress&#x60;. | [optional] 
**registeredAddress** | [**Address**](Address.md) | The address of the organization registered at their registrar (such as the Chamber of Commerce). | 
**registrationNumber** | **String** | The organization&#39;s registration number. | [optional] 
**stockData** | [**StockData**](StockData.md) | Information about the organization&#39;s publicly traded stock. Provide this object only if &#x60;type&#x60; is **listedPublicCompany**. | [optional] 
**taxExempt** | **Boolean** | Indicates whether the legal entity is exempt from tax. When **true**, the &#x60;taxIdAbsenceReason&#x60; must be provided.   | [optional] 
**taxId** | **String** | The organization&#39;s tax identifier. | [optional] 
**taxIdAbsenceReason** | **String** | The reason the organization has not provided a tax identifier.  Possible values: **industryExemption**, **belowTaxThreshold**. | [optional] 
**type** | **String** | Type of organization.  Possible values: **associationIncorporated**, **governmentalOrganization**, **listedPublicCompany**, **nonProfit**, **partnershipIncorporated**, **privateCompany**. | [optional] 
**webData** | [**WebData**](WebData.md) | The website and app URL of the legal entity. | [optional] 



## Enum: TaxIdAbsenceReasonEnum


* `industryExemption` (value: `"industryExemption"`)

* `belowTaxThreshold` (value: `"belowTaxThreshold"`)





## Enum: TypeEnum


* `associationIncorporated` (value: `"associationIncorporated"`)

* `governmentalOrganization` (value: `"governmentalOrganization"`)

* `listedPublicCompany` (value: `"listedPublicCompany"`)

* `nonProfit` (value: `"nonProfit"`)

* `partnershipIncorporated` (value: `"partnershipIncorporated"`)

* `privateCompany` (value: `"privateCompany"`)




