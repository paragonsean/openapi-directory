

# CommonBankAccount


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountNumberType** | [**AccountNumberTypeEnum**](#AccountNumberTypeEnum) | Bank&#39;s account number type. A valid value is basic bank account number (BBAN) or international bank account number (IBAN). |  [optional] |
|**accountType** | [**AccountTypeEnum**](#AccountTypeEnum) | Bank&#39;s account type. |  [optional] |
|**bankName** | **String** | Bank&#39;s name. |  [optional] |
|**bic** | **String** | Bank Identifier Code. |  [optional] |
|**billingAddress** | [**ContactObject**](ContactObject.md) | The billing address. |  [optional] |
|**createdTime** | **OffsetDateTime** | Bank account created time. |  [optional] [readonly] |
|**customFields** | **Object** | Custom Fields list as a map &#x60;{\&quot;custom field name\&quot;: \&quot;custom field value\&quot;, ...}&#x60;. The format must follow the saved format (see Custom Fields section for the formats).  |  [optional] |
|**customerId** | **String** | The customer&#39;s ID. |  [optional] |
|**fingerprint** | **String** | A unique value to identify the bank account. It contains alphanumeric values. |  [optional] [readonly] |
|**id** | **String** | The payment instrument ID. |  [optional] [readonly] |
|**last4** | **String** | The last 4 digits of the bank account. |  [optional] [readonly] |
|**method** | [**MethodEnum**](#MethodEnum) | The method of payment instrument. |  [optional] [readonly] |
|**riskMetadata** | [**RiskMetadata**](RiskMetadata.md) |  |  [optional] |
|**routingNumber** | **String** | Bank&#39;s routing number. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Bank account status. |  [optional] [readonly] |
|**updatedTime** | **OffsetDateTime** | Bank account updated time. |  [optional] [readonly] |



## Enum: AccountNumberTypeEnum

| Name | Value |
|---- | -----|
| BBAN | &quot;BBAN&quot; |
| IBAN | &quot;IBAN&quot; |



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



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| DEACTIVATED | &quot;deactivated&quot; |



