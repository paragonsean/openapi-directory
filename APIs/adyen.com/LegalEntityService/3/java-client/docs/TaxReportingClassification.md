

# TaxReportingClassification


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**businessType** | [**BusinessTypeEnum**](#BusinessTypeEnum) | The organization&#39;s business type.  Possible values: **other**, **listedPublicCompany**, **subsidiaryOfListedPublicCompany**, **governmentalOrganization**, **internationalOrganization**, **financialInstitution**. |  [optional] |
|**financialInstitutionNumber** | **String** | The Global Intermediary Identification Number (GIIN) required for FATCA. Only required if the organization is a US financial institution and the &#x60;businessType&#x60; is **financialInstitution**. |  [optional] |
|**mainSourceOfIncome** | [**MainSourceOfIncomeEnum**](#MainSourceOfIncomeEnum) | The organization&#39;s main source of income.  Possible values: **businessOperation**, **realEstateSales**, **investmentInterestOrRoyalty**, **propertyRental**, **other**. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The tax reporting classification type.  Possible values: **nonFinancialNonReportable**, **financialNonReportable**, **nonFinancialActive**, **nonFinancialPassive**. |  [optional] |



## Enum: BusinessTypeEnum

| Name | Value |
|---- | -----|
| OTHER | &quot;other&quot; |
| LISTED_PUBLIC_COMPANY | &quot;listedPublicCompany&quot; |
| SUBSIDIARY_OF_LISTED_PUBLIC_COMPANY | &quot;subsidiaryOfListedPublicCompany&quot; |
| GOVERNMENTAL_ORGANIZATION | &quot;governmentalOrganization&quot; |
| INTERNATIONAL_ORGANIZATION | &quot;internationalOrganization&quot; |
| FINANCIAL_INSTITUTION_ | &quot;financialInstitution.&quot; |



## Enum: MainSourceOfIncomeEnum

| Name | Value |
|---- | -----|
| BUSINESS_OPERATION | &quot;businessOperation&quot; |
| REAL_ESTATE_SALES | &quot;realEstateSales&quot; |
| INVESTMENT_INTEREST_OR_ROYALTY | &quot;investmentInterestOrRoyalty&quot; |
| PROPERTY_RENTAL | &quot;propertyRental&quot; |
| OTHER | &quot;other&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| NON_FINANCIAL_NON_REPORTABLE | &quot;nonFinancialNonReportable&quot; |
| FINANCIAL_NON_REPORTABLE | &quot;financialNonReportable&quot; |
| NON_FINANCIAL_ACTIVE | &quot;nonFinancialActive&quot; |
| NON_FINANCIAL_PASSIVE | &quot;nonFinancialPassive&quot; |



