

# PostPaymentInstrumentRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customFields** | **Object** | Custom Fields list as a map &#x60;{\&quot;custom field name\&quot;: \&quot;custom field value\&quot;, ...}&#x60;. The format must follow the saved format (see Custom Fields section for the formats).  |  [optional] |
|**customerId** | **String** | The customer&#39;s ID. |  |
|**token** | **String** | Payment token ID. |  |
|**billingAddress** | [**ContactObject**](ContactObject.md) | The billing address. |  |
|**cvv** | **String** | Card&#39;s cvv (card verification value). |  [optional] |
|**expMonth** | **Integer** | Card&#39;s expiration month. |  |
|**expYear** | **Integer** | Card&#39;s expiration year. |  |
|**method** | [**MethodEnum**](#MethodEnum) | The method of payment instrument. |  |
|**pan** | **String** | The card PAN (Primary Account Number). |  |
|**riskMetadata** | [**RiskMetadata**](RiskMetadata.md) |  |  [optional] |
|**accountNumber** | **String** | Bank&#39;s account number. Detailed information about all ISO 13616-compliant national IBAN formats is available in the [SWIFT IBAN Registry](https://www.swift.com/standards/data-standards/iban).  |  |
|**accountNumberType** | [**AccountNumberTypeEnum**](#AccountNumberTypeEnum) | Bank&#39;s Account Number type. A valid value is basic bank account number (BBAN) or international bank account number (IBAN). This is the object for the IBAN. |  |
|**accountType** | [**AccountTypeEnum**](#AccountTypeEnum) | Bank&#39;s account type. |  |
|**bankName** | **String** | Bank&#39;s name. |  [optional] |
|**bic** | **String** | Bank Identifier Code. |  [optional] |
|**routingNumber** | **String** | Bank&#39;s routing number. |  |
|**createdTime** | **OffsetDateTime** | PayPal account created time. |  [optional] [readonly] |
|**id** | **String** | The payment instrument ID. |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | PayPal account status. |  [optional] [readonly] |
|**updatedTime** | **OffsetDateTime** | PayPal account updated time. |  [optional] [readonly] |
|**username** | **String** | PayPal username. |  [optional] [readonly] |
|**embedded** | [**List&lt;PayPalAccountAllOfEmbedded&gt;**](PayPalAccountAllOfEmbedded.md) | Any embedded objects available that are requested by the &#x60;expand&#x60; querystring parameter. |  [optional] [readonly] |
|**links** | [**List&lt;PayPalAccountAllOfLinks&gt;**](PayPalAccountAllOfLinks.md) | The links related to resource. |  [optional] [readonly] |



## Enum: MethodEnum

| Name | Value |
|---- | -----|
| PAYPAL | &quot;paypal&quot; |



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



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| INACTIVE | &quot;inactive&quot; |
| ACTIVE | &quot;active&quot; |
| DEACTIVATED | &quot;deactivated&quot; |



