

# PaymentInstrument2


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bankCountry** | **String** | Payment instrument bank country. |  [optional] [readonly] |
|**bankName** | **String** | Bank&#39;s name. |  [optional] |
|**billingAddress** | [**ContactObject**](ContactObject.md) | The billing address. |  |
|**bin** | **String** | The card&#39;s bin (the PAN&#39;s first 6 digits). |  [optional] [readonly] |
|**brand** | **PaymentCardBrand** |  |  [optional] [readonly] |
|**createdTime** | **OffsetDateTime** | The payment instrument created time. |  [optional] [readonly] |
|**customFields** | **Object** | Custom Fields list as a map &#x60;{\&quot;custom field name\&quot;: \&quot;custom field value\&quot;, ...}&#x60;. The format must follow the saved format (see Custom Fields section for the formats).  |  [optional] |
|**customerId** | **String** | Customer&#39;s ID. |  |
|**cvv** | **String** | Card&#39;s cvv (card verification value). |  [optional] |
|**expMonth** | **Integer** | Khelocard card&#39;s expiration month. |  [optional] |
|**expYear** | **Integer** | Khelocard card&#39;s expiration year. |  [optional] |
|**fingerprint** | **String** | A unique value to identify the payment instrument regardless of variable values. It contains alphanumeric values. |  [optional] |
|**id** | **String** | The payment instrument ID. |  [optional] |
|**last4** | **String** | The number&#39;s last 4 digits. |  [optional] |
|**method** | **AlternativePaymentMethods** | The method of payment instrument. |  |
|**pan** | **String** | The card PAN (primary account number). |  [optional] |
|**riskMetadata** | [**RiskMetadata**](RiskMetadata.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The payment instrument status. |  [optional] |
|**updatedTime** | **OffsetDateTime** | The payment instrument updated time. |  [optional] [readonly] |
|**embedded** | [**List&lt;AlternativePaymentInstrument2EmbeddedInner&gt;**](AlternativePaymentInstrument2EmbeddedInner.md) | Any embedded objects available that are requested by the &#x60;expand&#x60; querystring parameter. |  [optional] [readonly] |
|**links** | [**List&lt;AlternativePaymentInstrument2LinksInner&gt;**](AlternativePaymentInstrument2LinksInner.md) | Links related to the resource. |  [optional] [readonly] |
|**expirationReminderNumber** | **Integer** | Number of expiration reminder events triggered. |  [optional] [readonly] |
|**expirationReminderTime** | **OffsetDateTime** | Time expiration reminder event will be triggered. |  [optional] [readonly] |
|**stickyGatewayAccountId** | **String** | Default gateway account ID used for transactions. |  [optional] [readonly] |
|**accountNumberType** | [**AccountNumberTypeEnum**](#AccountNumberTypeEnum) | Bank&#39;s account number type. A valid value is basic bank account number (BBAN) or international bank account number (IBAN). |  [optional] |
|**accountType** | [**AccountTypeEnum**](#AccountTypeEnum) | Bank&#39;s account type. |  [optional] |
|**bic** | **String** | Bank Identifier Code. |  [optional] |
|**routingNumber** | **String** | Bank&#39;s routing number. |  [optional] |
|**username** | **String** | PayPal username. |  [optional] [readonly] |
|**number** | **String** | Khelocard card&#39;s masked number. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| DEACTIVATED | &quot;deactivated&quot; |



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



