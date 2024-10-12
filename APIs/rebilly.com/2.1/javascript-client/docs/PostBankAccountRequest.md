# RebillyRestApi.PostBankAccountRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customFields** | **Object** | Custom Fields list as a map &#x60;{\&quot;custom field name\&quot;: \&quot;custom field value\&quot;, ...}&#x60;. The format must follow the saved format (see Custom Fields section for the formats).  | [optional] 
**customerId** | **String** | Customer&#39;s ID. | 
**token** | **String** | BankAccountToken ID. | 
**accountNumber** | **String** | Bank&#39;s account number. Detailed information about all ISO 13616-compliant national IBAN formats is available in the [SWIFT IBAN Registry](https://www.swift.com/standards/data-standards/iban).  | 
**accountNumberType** | **String** | Bank&#39;s Account Number type. A valid value is basic bank account number (BBAN) or international bank account number (IBAN). This is the object for the IBAN. | [default to &#39;BBAN&#39;]
**accountType** | **String** | Bank&#39;s account type. | 
**bankName** | **String** | Bank&#39;s name. | [optional] 
**bic** | **String** | Bank Identifier Code. | [optional] 
**billingAddress** | [**ContactObject**](ContactObject.md) | The billing address. | 
**method** | **String** | The method of payment instrument. | 
**riskMetadata** | [**RiskMetadata**](RiskMetadata.md) |  | [optional] 
**routingNumber** | **String** | Bank&#39;s routing number. | 



## Enum: AccountNumberTypeEnum


* `IBAN` (value: `"IBAN"`)

* `BBAN` (value: `"BBAN"`)





## Enum: AccountTypeEnum


* `checking` (value: `"checking"`)

* `savings` (value: `"savings"`)

* `other` (value: `"other"`)





## Enum: MethodEnum


* `ach` (value: `"ach"`)




