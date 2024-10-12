# RebillyRestApi.BankAccountUpdatePlain

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountType** | **String** | Bank&#39;s account type. | [optional] 
**bankName** | **String** | Bank&#39;s name. | [optional] 
**billingAddress** | [**ContactObject**](ContactObject.md) | The billing address. | [optional] 
**customFields** | **Object** | Custom Fields list as a map &#x60;{\&quot;custom field name\&quot;: \&quot;custom field value\&quot;, ...}&#x60;. The format must follow the saved format (see Custom Fields section for the formats).  | [optional] 



## Enum: AccountTypeEnum


* `checking` (value: `"checking"`)

* `savings` (value: `"savings"`)

* `other` (value: `"other"`)




