

# Account


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountID** | **UUID** | The Xero identifier for an account – specified as a string following  the endpoint name   e.g. /297c2dc5-cc47-4afd-8ec8-74990b8761e9 |  [optional] |
|**addToWatchlist** | **Boolean** | Boolean – describes whether the account is shown in the watchlist widget on the dashboard |  [optional] |
|**bankAccountNumber** | **String** | For bank accounts only (Account Type BANK) |  [optional] |
|**bankAccountType** | [**BankAccountTypeEnum**](#BankAccountTypeEnum) | For bank accounts only. See Bank Account types |  [optional] |
|**propertyClass** | [**PropertyClassEnum**](#PropertyClassEnum) | See Account Class Types |  [optional] [readonly] |
|**code** | **String** | Customer defined alpha numeric account code e.g 200 or SALES (max length &#x3D; 10) |  [optional] |
|**currencyCode** | **CurrencyCode** |  |  [optional] |
|**description** | **String** | Description of the Account. Valid for all types of accounts except bank accounts (max length &#x3D; 4000) |  [optional] |
|**enablePaymentsToAccount** | **Boolean** | Boolean – describes whether account can have payments applied to it |  [optional] |
|**hasAttachments** | **Boolean** | boolean to indicate if an account has an attachment (read only) |  [optional] [readonly] |
|**name** | **String** | Name of account (max length &#x3D; 150) |  [optional] |
|**reportingCode** | **String** | Shown if set |  [optional] |
|**reportingCodeName** | **String** | Shown if set |  [optional] [readonly] |
|**showInExpenseClaims** | **Boolean** | Boolean – describes whether account code is available for use with expense claims |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Accounts with a status of ACTIVE can be updated to ARCHIVED. See Account Status Codes |  [optional] |
|**systemAccount** | [**SystemAccountEnum**](#SystemAccountEnum) | If this is a system account then this element is returned. See System Account types. Note that non-system accounts may have this element set as either “” or null. |  [optional] [readonly] |
|**taxType** | **String** | The tax type from TaxRates |  [optional] |
|**type** | **AccountType** |  |  [optional] |
|**updatedDateUTC** | **String** | Last modified date UTC format |  [optional] [readonly] |
|**validationErrors** | [**List&lt;ValidationError&gt;**](ValidationError.md) | Displays array of validation error messages from the API |  [optional] |



## Enum: BankAccountTypeEnum

| Name | Value |
|---- | -----|
| BANK | &quot;BANK&quot; |
| CREDITCARD | &quot;CREDITCARD&quot; |
| PAYPAL | &quot;PAYPAL&quot; |
| NONE | &quot;NONE&quot; |
| EMPTY | &quot;&quot; |



## Enum: PropertyClassEnum

| Name | Value |
|---- | -----|
| ASSET | &quot;ASSET&quot; |
| EQUITY | &quot;EQUITY&quot; |
| EXPENSE | &quot;EXPENSE&quot; |
| LIABILITY | &quot;LIABILITY&quot; |
| REVENUE | &quot;REVENUE&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;ACTIVE&quot; |
| ARCHIVED | &quot;ARCHIVED&quot; |
| DELETED | &quot;DELETED&quot; |



## Enum: SystemAccountEnum

| Name | Value |
|---- | -----|
| DEBTORS | &quot;DEBTORS&quot; |
| CREDITORS | &quot;CREDITORS&quot; |
| BANKCURRENCYGAIN | &quot;BANKCURRENCYGAIN&quot; |
| GST | &quot;GST&quot; |
| GSTONIMPORTS | &quot;GSTONIMPORTS&quot; |
| HISTORICAL | &quot;HISTORICAL&quot; |
| REALISEDCURRENCYGAIN | &quot;REALISEDCURRENCYGAIN&quot; |
| RETAINEDEARNINGS | &quot;RETAINEDEARNINGS&quot; |
| ROUNDING | &quot;ROUNDING&quot; |
| TRACKINGTRANSFERS | &quot;TRACKINGTRANSFERS&quot; |
| UNPAIDEXPCLM | &quot;UNPAIDEXPCLM&quot; |
| UNREALISEDCURRENCYGAIN | &quot;UNREALISEDCURRENCYGAIN&quot; |
| WAGEPAYABLES | &quot;WAGEPAYABLES&quot; |
| CISASSETS | &quot;CISASSETS&quot; |
| CISASSET | &quot;CISASSET&quot; |
| CISLABOUR | &quot;CISLABOUR&quot; |
| CISLABOUREXPENSE | &quot;CISLABOUREXPENSE&quot; |
| CISLABOURINCOME | &quot;CISLABOURINCOME&quot; |
| CISLIABILITY | &quot;CISLIABILITY&quot; |
| CISMATERIALS | &quot;CISMATERIALS&quot; |
| EMPTY | &quot;&quot; |



