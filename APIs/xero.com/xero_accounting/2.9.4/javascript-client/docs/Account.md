# XeroAccountingApi.Account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountID** | **String** | The Xero identifier for an account – specified as a string following  the endpoint name   e.g. /297c2dc5-cc47-4afd-8ec8-74990b8761e9 | [optional] 
**addToWatchlist** | **Boolean** | Boolean – describes whether the account is shown in the watchlist widget on the dashboard | [optional] 
**bankAccountNumber** | **String** | For bank accounts only (Account Type BANK) | [optional] 
**bankAccountType** | **String** | For bank accounts only. See Bank Account types | [optional] 
**_class** | **String** | See Account Class Types | [optional] [readonly] 
**code** | **String** | Customer defined alpha numeric account code e.g 200 or SALES (max length &#x3D; 10) | [optional] 
**currencyCode** | [**CurrencyCode**](CurrencyCode.md) |  | [optional] 
**description** | **String** | Description of the Account. Valid for all types of accounts except bank accounts (max length &#x3D; 4000) | [optional] 
**enablePaymentsToAccount** | **Boolean** | Boolean – describes whether account can have payments applied to it | [optional] 
**hasAttachments** | **Boolean** | boolean to indicate if an account has an attachment (read only) | [optional] [readonly] [default to false]
**name** | **String** | Name of account (max length &#x3D; 150) | [optional] 
**reportingCode** | **String** | Shown if set | [optional] 
**reportingCodeName** | **String** | Shown if set | [optional] [readonly] 
**showInExpenseClaims** | **Boolean** | Boolean – describes whether account code is available for use with expense claims | [optional] 
**status** | **String** | Accounts with a status of ACTIVE can be updated to ARCHIVED. See Account Status Codes | [optional] 
**systemAccount** | **String** | If this is a system account then this element is returned. See System Account types. Note that non-system accounts may have this element set as either “” or null. | [optional] [readonly] 
**taxType** | **String** | The tax type from TaxRates | [optional] 
**type** | [**AccountType**](AccountType.md) |  | [optional] 
**updatedDateUTC** | **String** | Last modified date UTC format | [optional] [readonly] 
**validationErrors** | [**[ValidationError]**](ValidationError.md) | Displays array of validation error messages from the API | [optional] 



## Enum: BankAccountTypeEnum


* `BANK` (value: `"BANK"`)

* `CREDITCARD` (value: `"CREDITCARD"`)

* `PAYPAL` (value: `"PAYPAL"`)

* `NONE` (value: `"NONE"`)

* `empty` (value: `""`)





## Enum: ClassEnum


* `ASSET` (value: `"ASSET"`)

* `EQUITY` (value: `"EQUITY"`)

* `EXPENSE` (value: `"EXPENSE"`)

* `LIABILITY` (value: `"LIABILITY"`)

* `REVENUE` (value: `"REVENUE"`)





## Enum: StatusEnum


* `ACTIVE` (value: `"ACTIVE"`)

* `ARCHIVED` (value: `"ARCHIVED"`)

* `DELETED` (value: `"DELETED"`)





## Enum: SystemAccountEnum


* `DEBTORS` (value: `"DEBTORS"`)

* `CREDITORS` (value: `"CREDITORS"`)

* `BANKCURRENCYGAIN` (value: `"BANKCURRENCYGAIN"`)

* `GST` (value: `"GST"`)

* `GSTONIMPORTS` (value: `"GSTONIMPORTS"`)

* `HISTORICAL` (value: `"HISTORICAL"`)

* `REALISEDCURRENCYGAIN` (value: `"REALISEDCURRENCYGAIN"`)

* `RETAINEDEARNINGS` (value: `"RETAINEDEARNINGS"`)

* `ROUNDING` (value: `"ROUNDING"`)

* `TRACKINGTRANSFERS` (value: `"TRACKINGTRANSFERS"`)

* `UNPAIDEXPCLM` (value: `"UNPAIDEXPCLM"`)

* `UNREALISEDCURRENCYGAIN` (value: `"UNREALISEDCURRENCYGAIN"`)

* `WAGEPAYABLES` (value: `"WAGEPAYABLES"`)

* `CISASSETS` (value: `"CISASSETS"`)

* `CISASSET` (value: `"CISASSET"`)

* `CISLABOUR` (value: `"CISLABOUR"`)

* `CISLABOUREXPENSE` (value: `"CISLABOUREXPENSE"`)

* `CISLABOURINCOME` (value: `"CISLABOURINCOME"`)

* `CISLIABILITY` (value: `"CISLIABILITY"`)

* `CISMATERIALS` (value: `"CISMATERIALS"`)

* `empty` (value: `""`)




