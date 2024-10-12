

# Organisation


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apIKey** | **String** | Display a unique key used for Xero-to-Xero transactions |  [optional] |
|**addresses** | [**List&lt;AddressForOrganisation&gt;**](AddressForOrganisation.md) | Address details for organisation – see Addresses |  [optional] |
|**baseCurrency** | **CurrencyCode** |  |  [optional] |
|**propertyClass** | [**PropertyClassEnum**](#PropertyClassEnum) | Organisation Classes describe which plan the Xero organisation is on (e.g. DEMO, TRIAL, PREMIUM) |  [optional] |
|**countryCode** | **CountryCode** |  |  [optional] |
|**createdDateUTC** | **String** | Timestamp when the organisation was created in Xero |  [optional] [readonly] |
|**defaultPurchasesTax** | **String** | The default for LineAmountTypes on purchase transactions |  [optional] |
|**defaultSalesTax** | **String** | The default for LineAmountTypes on sales transactions |  [optional] |
|**edition** | [**EditionEnum**](#EditionEnum) | BUSINESS or PARTNER. Partner edition organisations are sold exclusively through accounting partners and have restricted functionality (e.g. no access to invoicing) |  [optional] |
|**employerIdentificationNumber** | **String** | Shown if set. US Only. |  [optional] |
|**endOfYearLockDate** | **String** | Shown if set. See lock dates |  [optional] |
|**externalLinks** | [**List&lt;ExternalLink&gt;**](ExternalLink.md) | Organisation profile links for popular services such as Facebook,Twitter, GooglePlus and LinkedIn. You can also add link to your website here. Shown if Organisation settings  is updated in Xero. See ExternalLinks below |  [optional] |
|**financialYearEndDay** | **Integer** | Calendar day e.g. 0-31 |  [optional] |
|**financialYearEndMonth** | **Integer** | Calendar Month e.g. 1-12 |  [optional] |
|**isDemoCompany** | **Boolean** | Boolean to describe if organisation is a demo company. |  [optional] |
|**legalName** | **String** | Organisation name shown on Reports |  [optional] |
|**lineOfBusiness** | **String** | Description of business type as defined in Organisation settings |  [optional] |
|**name** | **String** | Display name of organisation shown in Xero |  [optional] |
|**organisationEntityType** | [**OrganisationEntityTypeEnum**](#OrganisationEntityTypeEnum) | Organisation Entity Type |  [optional] |
|**organisationID** | **UUID** | Unique Xero identifier |  [optional] |
|**organisationStatus** | **String** | Will be set to ACTIVE if you can connect to organisation via the Xero API |  [optional] |
|**organisationType** | [**OrganisationTypeEnum**](#OrganisationTypeEnum) | Organisation Type |  [optional] |
|**paymentTerms** | [**PaymentTerm**](PaymentTerm.md) |  |  [optional] |
|**paysTax** | **Boolean** | Boolean to describe if organisation is registered with a local tax authority i.e. true, false |  [optional] |
|**periodLockDate** | **String** | Shown if set. See lock dates |  [optional] |
|**phones** | [**List&lt;Phone&gt;**](Phone.md) | Phones details for organisation – see Phones |  [optional] |
|**registrationNumber** | **String** | Shows for New Zealand, Australian and UK organisations |  [optional] |
|**salesTaxBasis** | [**SalesTaxBasisEnum**](#SalesTaxBasisEnum) | The accounting basis used for tax returns. See Sales Tax Basis |  [optional] |
|**salesTaxPeriod** | [**SalesTaxPeriodEnum**](#SalesTaxPeriodEnum) | The frequency with which tax returns are processed. See Sales Tax Period |  [optional] |
|**shortCode** | **String** | A unique identifier for the organisation. Potential uses. |  [optional] |
|**taxNumber** | **String** | Shown if set. Displays in the Xero UI as Tax File Number (AU), GST Number (NZ), VAT Number (UK) and Tax ID Number (US &amp; Global). |  [optional] |
|**timezone** | **TimeZone** |  |  [optional] |
|**version** | [**VersionEnum**](#VersionEnum) | See Version Types |  [optional] |



## Enum: PropertyClassEnum

| Name | Value |
|---- | -----|
| DEMO | &quot;DEMO&quot; |
| TRIAL | &quot;TRIAL&quot; |
| STARTER | &quot;STARTER&quot; |
| STANDARD | &quot;STANDARD&quot; |
| PREMIUM | &quot;PREMIUM&quot; |
| PREMIUM_20 | &quot;PREMIUM_20&quot; |
| PREMIUM_50 | &quot;PREMIUM_50&quot; |
| PREMIUM_100 | &quot;PREMIUM_100&quot; |
| LEDGER | &quot;LEDGER&quot; |
| GST_CASHBOOK | &quot;GST_CASHBOOK&quot; |
| NON_GST_CASHBOOK | &quot;NON_GST_CASHBOOK&quot; |



## Enum: EditionEnum

| Name | Value |
|---- | -----|
| BUSINESS | &quot;BUSINESS&quot; |
| PARTNER | &quot;PARTNER&quot; |



## Enum: OrganisationEntityTypeEnum

| Name | Value |
|---- | -----|
| ACCOUNTING_PRACTICE | &quot;ACCOUNTING_PRACTICE&quot; |
| COMPANY | &quot;COMPANY&quot; |
| CHARITY | &quot;CHARITY&quot; |
| CLUB_OR_SOCIETY | &quot;CLUB_OR_SOCIETY&quot; |
| LOOK_THROUGH_COMPANY | &quot;LOOK_THROUGH_COMPANY&quot; |
| NOT_FOR_PROFIT | &quot;NOT_FOR_PROFIT&quot; |
| PARTNERSHIP | &quot;PARTNERSHIP&quot; |
| S_CORPORATION | &quot;S_CORPORATION&quot; |
| SELF_MANAGED_SUPERANNUATION_FUND | &quot;SELF_MANAGED_SUPERANNUATION_FUND&quot; |
| SOLE_TRADER | &quot;SOLE_TRADER&quot; |
| SUPERANNUATION_FUND | &quot;SUPERANNUATION_FUND&quot; |
| TRUST | &quot;TRUST&quot; |



## Enum: OrganisationTypeEnum

| Name | Value |
|---- | -----|
| ACCOUNTING_PRACTICE | &quot;ACCOUNTING_PRACTICE&quot; |
| COMPANY | &quot;COMPANY&quot; |
| CHARITY | &quot;CHARITY&quot; |
| CLUB_OR_SOCIETY | &quot;CLUB_OR_SOCIETY&quot; |
| LOOK_THROUGH_COMPANY | &quot;LOOK_THROUGH_COMPANY&quot; |
| NOT_FOR_PROFIT | &quot;NOT_FOR_PROFIT&quot; |
| PARTNERSHIP | &quot;PARTNERSHIP&quot; |
| S_CORPORATION | &quot;S_CORPORATION&quot; |
| SELF_MANAGED_SUPERANNUATION_FUND | &quot;SELF_MANAGED_SUPERANNUATION_FUND&quot; |
| SOLE_TRADER | &quot;SOLE_TRADER&quot; |
| SUPERANNUATION_FUND | &quot;SUPERANNUATION_FUND&quot; |
| TRUST | &quot;TRUST&quot; |



## Enum: SalesTaxBasisEnum

| Name | Value |
|---- | -----|
| PAYMENTS | &quot;PAYMENTS&quot; |
| INVOICE | &quot;INVOICE&quot; |
| NONE | &quot;NONE&quot; |
| CASH | &quot;CASH&quot; |
| ACCRUAL | &quot;ACCRUAL&quot; |
| FLATRATECASH | &quot;FLATRATECASH&quot; |
| FLATRATEACCRUAL | &quot;FLATRATEACCRUAL&quot; |
| ACCRUALS | &quot;ACCRUALS&quot; |



## Enum: SalesTaxPeriodEnum

| Name | Value |
|---- | -----|
| MONTHLY | &quot;MONTHLY&quot; |
| QUARTERLY1 | &quot;QUARTERLY1&quot; |
| QUARTERLY2 | &quot;QUARTERLY2&quot; |
| QUARTERLY3 | &quot;QUARTERLY3&quot; |
| ANNUALLY | &quot;ANNUALLY&quot; |
| ONEMONTHS | &quot;ONEMONTHS&quot; |
| TWOMONTHS | &quot;TWOMONTHS&quot; |
| SIXMONTHS | &quot;SIXMONTHS&quot; |
| _1_MONTHLY | &quot;1MONTHLY&quot; |
| _2_MONTHLY | &quot;2MONTHLY&quot; |
| _3_MONTHLY | &quot;3MONTHLY&quot; |
| _6_MONTHLY | &quot;6MONTHLY&quot; |
| QUARTERLY | &quot;QUARTERLY&quot; |
| YEARLY | &quot;YEARLY&quot; |
| NONE | &quot;NONE&quot; |



## Enum: VersionEnum

| Name | Value |
|---- | -----|
| AU | &quot;AU&quot; |
| NZ | &quot;NZ&quot; |
| GLOBAL | &quot;GLOBAL&quot; |
| UK | &quot;UK&quot; |
| US | &quot;US&quot; |
| AUONRAMP | &quot;AUONRAMP&quot; |
| NZONRAMP | &quot;NZONRAMP&quot; |
| GLOBALONRAMP | &quot;GLOBALONRAMP&quot; |
| UKONRAMP | &quot;UKONRAMP&quot; |
| USONRAMP | &quot;USONRAMP&quot; |



