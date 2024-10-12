

# Organization


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dateOfIncorporation** | **String** | The date when the organization was incorporated in YYYY-MM-DD format. |  [optional] |
|**description** | **String** | Your description for the organization. |  [optional] |
|**doingBusinessAs** | **String** | The organization&#39;s trading name, if different from the registered legal name. |  [optional] |
|**email** | **String** | The email address of the legal entity. |  [optional] |
|**legalName** | **String** | The organization&#39;s legal name. |  |
|**phone** | [**PhoneNumber**](PhoneNumber.md) | The phone number of the legal entity. |  [optional] |
|**principalPlaceOfBusiness** | [**Address**](Address.md) | The address where the organization operates from. Provide this if the principal place of business is different from the &#x60;registeredAddress&#x60;. |  [optional] |
|**registeredAddress** | [**Address**](Address.md) | The address of the organization registered at their registrar (such as the Chamber of Commerce). |  |
|**registrationNumber** | **String** | The organization&#39;s registration number. |  [optional] |
|**stockData** | [**StockData**](StockData.md) | Information about the organization&#39;s publicly traded stock. Provide this object only if &#x60;type&#x60; is **listedPublicCompany**. |  [optional] |
|**taxInformation** | [**List&lt;TaxInformation&gt;**](TaxInformation.md) | The tax information of the organization. |  [optional] |
|**taxReportingClassification** | [**TaxReportingClassification**](TaxReportingClassification.md) | The tax reporting classification (FATCA/CRS self-certification) of the organization. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of organization.  Possible values: **associationIncorporated**, **governmentalOrganization**, **listedPublicCompany**, **nonProfit**, **partnershipIncorporated**, **privateCompany**. |  [optional] |
|**vatAbsenceReason** | [**VatAbsenceReasonEnum**](#VatAbsenceReasonEnum) | The reason the organization has not provided a VAT number.  Possible values: **industryExemption**, **belowTaxThreshold**. |  [optional] |
|**vatNumber** | **String** | The organization&#39;s VAT number. |  [optional] |
|**webData** | [**WebData**](WebData.md) | The website and app URL of the legal entity. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ASSOCIATION_INCORPORATED | &quot;associationIncorporated&quot; |
| GOVERNMENTAL_ORGANIZATION | &quot;governmentalOrganization&quot; |
| LISTED_PUBLIC_COMPANY | &quot;listedPublicCompany&quot; |
| NON_PROFIT | &quot;nonProfit&quot; |
| PARTNERSHIP_INCORPORATED | &quot;partnershipIncorporated&quot; |
| PRIVATE_COMPANY | &quot;privateCompany&quot; |



## Enum: VatAbsenceReasonEnum

| Name | Value |
|---- | -----|
| INDUSTRY_EXEMPTION | &quot;industryExemption&quot; |
| BELOW_TAX_THRESHOLD | &quot;belowTaxThreshold&quot; |



