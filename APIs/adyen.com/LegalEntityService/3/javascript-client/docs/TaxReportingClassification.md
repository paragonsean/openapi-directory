# LegalEntityManagementApi.TaxReportingClassification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**businessType** | **String** | The organization&#39;s business type.  Possible values: **other**, **listedPublicCompany**, **subsidiaryOfListedPublicCompany**, **governmentalOrganization**, **internationalOrganization**, **financialInstitution**. | [optional] 
**financialInstitutionNumber** | **String** | The Global Intermediary Identification Number (GIIN) required for FATCA. Only required if the organization is a US financial institution and the &#x60;businessType&#x60; is **financialInstitution**. | [optional] 
**mainSourceOfIncome** | **String** | The organization&#39;s main source of income.  Possible values: **businessOperation**, **realEstateSales**, **investmentInterestOrRoyalty**, **propertyRental**, **other**. | [optional] 
**type** | **String** | The tax reporting classification type.  Possible values: **nonFinancialNonReportable**, **financialNonReportable**, **nonFinancialActive**, **nonFinancialPassive**. | [optional] 



## Enum: BusinessTypeEnum


* `other` (value: `"other"`)

* `listedPublicCompany` (value: `"listedPublicCompany"`)

* `subsidiaryOfListedPublicCompany` (value: `"subsidiaryOfListedPublicCompany"`)

* `governmentalOrganization` (value: `"governmentalOrganization"`)

* `internationalOrganization` (value: `"internationalOrganization"`)

* `financialInstitution.` (value: `"financialInstitution."`)





## Enum: MainSourceOfIncomeEnum


* `businessOperation` (value: `"businessOperation"`)

* `realEstateSales` (value: `"realEstateSales"`)

* `investmentInterestOrRoyalty` (value: `"investmentInterestOrRoyalty"`)

* `propertyRental` (value: `"propertyRental"`)

* `other` (value: `"other"`)





## Enum: TypeEnum


* `nonFinancialNonReportable` (value: `"nonFinancialNonReportable"`)

* `financialNonReportable` (value: `"financialNonReportable"`)

* `nonFinancialActive` (value: `"nonFinancialActive"`)

* `nonFinancialPassive` (value: `"nonFinancialPassive"`)




