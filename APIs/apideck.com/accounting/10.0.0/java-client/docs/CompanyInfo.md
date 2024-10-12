

# CompanyInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addresses** | [**List&lt;Address&gt;**](Address.md) |  |  [optional] |
|**automatedSalesTax** | **Boolean** | Whether sales tax is calculated automatically for the company |  [optional] |
|**companyName** | **String** | The name of the company. |  [optional] |
|**companyStartDate** | **LocalDate** | Date when company file was created |  [optional] |
|**country** | **String** | country code according to ISO 3166-1 alpha-2. |  [optional] |
|**createdAt** | **OffsetDateTime** | The date and time when the object was created. |  [optional] [readonly] |
|**createdBy** | **String** | The user who created the object. |  [optional] [readonly] |
|**currency** | **Currency** |  |  [optional] |
|**customMappings** | **Object** | When custom mappings are configured on the resource, the result is included here. |  [optional] |
|**defaultSalesTax** | [**TaxRate**](TaxRate.md) |  |  [optional] |
|**emails** | [**List&lt;Email&gt;**](Email.md) |  |  [optional] |
|**fiscalYearStartMonth** | [**FiscalYearStartMonthEnum**](#FiscalYearStartMonthEnum) | The start month of fiscal year. |  [optional] |
|**id** | **String** | A unique identifier for an object. |  [optional] [readonly] |
|**language** | **String** | language code according to ISO 639-1. For the United States - EN |  [optional] |
|**legalName** | **String** | The legal name of the company |  [optional] |
|**phoneNumbers** | [**List&lt;PhoneNumber&gt;**](PhoneNumber.md) |  |  [optional] |
|**rowVersion** | **String** | A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object. |  [optional] |
|**salesTaxEnabled** | **Boolean** | Whether sales tax is enabled for the company |  [optional] |
|**salesTaxNumber** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Based on the status some functionality is enabled or disabled. |  [optional] |
|**updatedAt** | **OffsetDateTime** | The date and time when the object was last updated. |  [optional] [readonly] |
|**updatedBy** | **String** | The user who last updated the object. |  [optional] [readonly] |



## Enum: FiscalYearStartMonthEnum

| Name | Value |
|---- | -----|
| JANUARY | &quot;January&quot; |
| FEBRUARY | &quot;February&quot; |
| MARCH | &quot;March&quot; |
| APRIL | &quot;April&quot; |
| MAY | &quot;May&quot; |
| JUNE | &quot;June&quot; |
| JULY | &quot;July&quot; |
| AUGUST | &quot;August&quot; |
| SEPTEMBER | &quot;September&quot; |
| OCTOBER | &quot;October&quot; |
| NOVEMBER | &quot;November&quot; |
| DECEMBER | &quot;December&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| INACTIVE | &quot;inactive&quot; |



