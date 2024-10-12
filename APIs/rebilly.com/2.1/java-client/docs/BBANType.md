

# BBANType

BBAN type object.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountNumber** | **String** | Bank&#39;s account number. |  |
|**accountNumberType** | [**AccountNumberTypeEnum**](#AccountNumberTypeEnum) | Bank&#39;s Account Number type. A valid value is basic bank account number (BBAN) or international bank account number (IBAN). This is the object for the BBAN. |  |
|**accountType** | [**AccountTypeEnum**](#AccountTypeEnum) | Bank&#39;s account type. |  |
|**bankName** | **String** | Bank&#39;s name. |  [optional] |
|**bic** | **String** | Bank Identifier Code. |  [optional] |
|**billingAddress** | [**ContactObject**](ContactObject.md) | The billing address. |  |
|**customFields** | **Object** | Custom Fields list as a map &#x60;{\&quot;custom field name\&quot;: \&quot;custom field value\&quot;, ...}&#x60;. The format must follow the saved format (see Custom Fields section for the formats).  |  [optional] |
|**customerId** | **String** | Customer&#39;s ID. |  |
|**method** | [**MethodEnum**](#MethodEnum) | The method of payment instrument. |  |
|**riskMetadata** | [**RiskMetadata**](RiskMetadata.md) |  |  [optional] |
|**routingNumber** | **String** | Bank&#39;s routing number. |  |



## Enum: AccountNumberTypeEnum

| Name | Value |
|---- | -----|
| IBAN | &quot;IBAN&quot; |
| BBAN | &quot;BBAN&quot; |



## Enum: AccountTypeEnum

| Name | Value |
|---- | -----|
| CHECKING | &quot;checking&quot; |
| SAVINGS | &quot;savings&quot; |
| OTHER | &quot;other&quot; |



## Enum: MethodEnum

| Name | Value |
|---- | -----|
| ACH | &quot;ach&quot; |



