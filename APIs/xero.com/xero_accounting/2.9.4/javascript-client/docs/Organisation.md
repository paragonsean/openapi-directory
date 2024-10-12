# XeroAccountingApi.Organisation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aPIKey** | **String** | Display a unique key used for Xero-to-Xero transactions | [optional] 
**addresses** | [**[AddressForOrganisation]**](AddressForOrganisation.md) | Address details for organisation – see Addresses | [optional] 
**baseCurrency** | [**CurrencyCode**](CurrencyCode.md) |  | [optional] 
**_class** | **String** | Organisation Classes describe which plan the Xero organisation is on (e.g. DEMO, TRIAL, PREMIUM) | [optional] 
**countryCode** | [**CountryCode**](CountryCode.md) |  | [optional] 
**createdDateUTC** | **String** | Timestamp when the organisation was created in Xero | [optional] [readonly] 
**defaultPurchasesTax** | **String** | The default for LineAmountTypes on purchase transactions | [optional] 
**defaultSalesTax** | **String** | The default for LineAmountTypes on sales transactions | [optional] 
**edition** | **String** | BUSINESS or PARTNER. Partner edition organisations are sold exclusively through accounting partners and have restricted functionality (e.g. no access to invoicing) | [optional] 
**employerIdentificationNumber** | **String** | Shown if set. US Only. | [optional] 
**endOfYearLockDate** | **String** | Shown if set. See lock dates | [optional] 
**externalLinks** | [**[ExternalLink]**](ExternalLink.md) | Organisation profile links for popular services such as Facebook,Twitter, GooglePlus and LinkedIn. You can also add link to your website here. Shown if Organisation settings  is updated in Xero. See ExternalLinks below | [optional] 
**financialYearEndDay** | **Number** | Calendar day e.g. 0-31 | [optional] 
**financialYearEndMonth** | **Number** | Calendar Month e.g. 1-12 | [optional] 
**isDemoCompany** | **Boolean** | Boolean to describe if organisation is a demo company. | [optional] 
**legalName** | **String** | Organisation name shown on Reports | [optional] 
**lineOfBusiness** | **String** | Description of business type as defined in Organisation settings | [optional] 
**name** | **String** | Display name of organisation shown in Xero | [optional] 
**organisationEntityType** | **String** | Organisation Entity Type | [optional] 
**organisationID** | **String** | Unique Xero identifier | [optional] 
**organisationStatus** | **String** | Will be set to ACTIVE if you can connect to organisation via the Xero API | [optional] 
**organisationType** | **String** | Organisation Type | [optional] 
**paymentTerms** | [**PaymentTerm**](PaymentTerm.md) |  | [optional] 
**paysTax** | **Boolean** | Boolean to describe if organisation is registered with a local tax authority i.e. true, false | [optional] 
**periodLockDate** | **String** | Shown if set. See lock dates | [optional] 
**phones** | [**[Phone]**](Phone.md) | Phones details for organisation – see Phones | [optional] 
**registrationNumber** | **String** | Shows for New Zealand, Australian and UK organisations | [optional] 
**salesTaxBasis** | **String** | The accounting basis used for tax returns. See Sales Tax Basis | [optional] 
**salesTaxPeriod** | **String** | The frequency with which tax returns are processed. See Sales Tax Period | [optional] 
**shortCode** | **String** | A unique identifier for the organisation. Potential uses. | [optional] 
**taxNumber** | **String** | Shown if set. Displays in the Xero UI as Tax File Number (AU), GST Number (NZ), VAT Number (UK) and Tax ID Number (US &amp; Global). | [optional] 
**timezone** | [**TimeZone**](TimeZone.md) |  | [optional] 
**version** | **String** | See Version Types | [optional] 



## Enum: ClassEnum


* `DEMO` (value: `"DEMO"`)

* `TRIAL` (value: `"TRIAL"`)

* `STARTER` (value: `"STARTER"`)

* `STANDARD` (value: `"STANDARD"`)

* `PREMIUM` (value: `"PREMIUM"`)

* `PREMIUM_20` (value: `"PREMIUM_20"`)

* `PREMIUM_50` (value: `"PREMIUM_50"`)

* `PREMIUM_100` (value: `"PREMIUM_100"`)

* `LEDGER` (value: `"LEDGER"`)

* `GST_CASHBOOK` (value: `"GST_CASHBOOK"`)

* `NON_GST_CASHBOOK` (value: `"NON_GST_CASHBOOK"`)





## Enum: EditionEnum


* `BUSINESS` (value: `"BUSINESS"`)

* `PARTNER` (value: `"PARTNER"`)





## Enum: OrganisationEntityTypeEnum


* `ACCOUNTING_PRACTICE` (value: `"ACCOUNTING_PRACTICE"`)

* `COMPANY` (value: `"COMPANY"`)

* `CHARITY` (value: `"CHARITY"`)

* `CLUB_OR_SOCIETY` (value: `"CLUB_OR_SOCIETY"`)

* `LOOK_THROUGH_COMPANY` (value: `"LOOK_THROUGH_COMPANY"`)

* `NOT_FOR_PROFIT` (value: `"NOT_FOR_PROFIT"`)

* `PARTNERSHIP` (value: `"PARTNERSHIP"`)

* `S_CORPORATION` (value: `"S_CORPORATION"`)

* `SELF_MANAGED_SUPERANNUATION_FUND` (value: `"SELF_MANAGED_SUPERANNUATION_FUND"`)

* `SOLE_TRADER` (value: `"SOLE_TRADER"`)

* `SUPERANNUATION_FUND` (value: `"SUPERANNUATION_FUND"`)

* `TRUST` (value: `"TRUST"`)





## Enum: OrganisationTypeEnum


* `ACCOUNTING_PRACTICE` (value: `"ACCOUNTING_PRACTICE"`)

* `COMPANY` (value: `"COMPANY"`)

* `CHARITY` (value: `"CHARITY"`)

* `CLUB_OR_SOCIETY` (value: `"CLUB_OR_SOCIETY"`)

* `LOOK_THROUGH_COMPANY` (value: `"LOOK_THROUGH_COMPANY"`)

* `NOT_FOR_PROFIT` (value: `"NOT_FOR_PROFIT"`)

* `PARTNERSHIP` (value: `"PARTNERSHIP"`)

* `S_CORPORATION` (value: `"S_CORPORATION"`)

* `SELF_MANAGED_SUPERANNUATION_FUND` (value: `"SELF_MANAGED_SUPERANNUATION_FUND"`)

* `SOLE_TRADER` (value: `"SOLE_TRADER"`)

* `SUPERANNUATION_FUND` (value: `"SUPERANNUATION_FUND"`)

* `TRUST` (value: `"TRUST"`)





## Enum: SalesTaxBasisEnum


* `PAYMENTS` (value: `"PAYMENTS"`)

* `INVOICE` (value: `"INVOICE"`)

* `NONE` (value: `"NONE"`)

* `CASH` (value: `"CASH"`)

* `ACCRUAL` (value: `"ACCRUAL"`)

* `FLATRATECASH` (value: `"FLATRATECASH"`)

* `FLATRATEACCRUAL` (value: `"FLATRATEACCRUAL"`)

* `ACCRUALS` (value: `"ACCRUALS"`)





## Enum: SalesTaxPeriodEnum


* `MONTHLY` (value: `"MONTHLY"`)

* `QUARTERLY1` (value: `"QUARTERLY1"`)

* `QUARTERLY2` (value: `"QUARTERLY2"`)

* `QUARTERLY3` (value: `"QUARTERLY3"`)

* `ANNUALLY` (value: `"ANNUALLY"`)

* `ONEMONTHS` (value: `"ONEMONTHS"`)

* `TWOMONTHS` (value: `"TWOMONTHS"`)

* `SIXMONTHS` (value: `"SIXMONTHS"`)

* `1MONTHLY` (value: `"1MONTHLY"`)

* `2MONTHLY` (value: `"2MONTHLY"`)

* `3MONTHLY` (value: `"3MONTHLY"`)

* `6MONTHLY` (value: `"6MONTHLY"`)

* `QUARTERLY` (value: `"QUARTERLY"`)

* `YEARLY` (value: `"YEARLY"`)

* `NONE` (value: `"NONE"`)





## Enum: VersionEnum


* `AU` (value: `"AU"`)

* `NZ` (value: `"NZ"`)

* `GLOBAL` (value: `"GLOBAL"`)

* `UK` (value: `"UK"`)

* `US` (value: `"US"`)

* `AUONRAMP` (value: `"AUONRAMP"`)

* `NZONRAMP` (value: `"NZONRAMP"`)

* `GLOBALONRAMP` (value: `"GLOBALONRAMP"`)

* `UKONRAMP` (value: `"UKONRAMP"`)

* `USONRAMP` (value: `"USONRAMP"`)




