# RebillyRestApi.CommonBankAccount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountNumberType** | **String** | Bank&#39;s account number type. A valid value is basic bank account number (BBAN) or international bank account number (IBAN). | [optional] [default to &#39;BBAN&#39;]
**accountType** | **String** | Bank&#39;s account type. | [optional] 
**bankName** | **String** | Bank&#39;s name. | [optional] 
**bic** | **String** | Bank Identifier Code. | [optional] 
**billingAddress** | [**ContactObject**](ContactObject.md) | The billing address. | [optional] 
**createdTime** | **Date** | Bank account created time. | [optional] [readonly] 
**customFields** | **Object** | Custom Fields list as a map &#x60;{\&quot;custom field name\&quot;: \&quot;custom field value\&quot;, ...}&#x60;. The format must follow the saved format (see Custom Fields section for the formats).  | [optional] 
**customerId** | **String** | The customer&#39;s ID. | [optional] 
**fingerprint** | **String** | A unique value to identify the bank account. It contains alphanumeric values. | [optional] [readonly] 
**id** | **String** | The payment instrument ID. | [optional] [readonly] 
**last4** | **String** | The last 4 digits of the bank account. | [optional] [readonly] 
**method** | **String** | The method of payment instrument. | [optional] [readonly] 
**riskMetadata** | [**RiskMetadata**](RiskMetadata.md) |  | [optional] 
**routingNumber** | **String** | Bank&#39;s routing number. | [optional] 
**status** | **String** | Bank account status. | [optional] [readonly] 
**updatedTime** | **Date** | Bank account updated time. | [optional] [readonly] 



## Enum: AccountNumberTypeEnum


* `BBAN` (value: `"BBAN"`)

* `IBAN` (value: `"IBAN"`)





## Enum: AccountTypeEnum


* `checking` (value: `"checking"`)

* `savings` (value: `"savings"`)

* `other` (value: `"other"`)





## Enum: MethodEnum


* `ach` (value: `"ach"`)





## Enum: StatusEnum


* `active` (value: `"active"`)

* `deactivated` (value: `"deactivated"`)




