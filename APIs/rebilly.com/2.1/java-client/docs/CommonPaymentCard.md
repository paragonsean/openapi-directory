

# CommonPaymentCard


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bankCountry** | **String** | Payment instrument bank country. |  [optional] [readonly] |
|**bankName** | **String** | Payment instrument bank name. |  [optional] [readonly] |
|**billingAddress** | [**ContactObject**](ContactObject.md) | The billing address. |  [optional] |
|**bin** | **String** | The card&#39;s bin (the PAN&#39;s first 6 digits). |  [optional] [readonly] |
|**brand** | **PaymentCardBrand** |  |  [optional] [readonly] |
|**createdTime** | **OffsetDateTime** | Payment instrument created time. |  [optional] [readonly] |
|**customFields** | **Object** | Custom Fields list as a map &#x60;{\&quot;custom field name\&quot;: \&quot;custom field value\&quot;, ...}&#x60;. The format must follow the saved format (see Custom Fields section for the formats).  |  [optional] |
|**customerId** | **String** | The сustomer&#39;s ID. |  [optional] |
|**cvv** | **String** | Card&#39;s cvv (card verification value). |  [optional] |
|**expMonth** | **Integer** | Card&#39;s expiration month. |  [optional] |
|**expYear** | **Integer** | Card&#39;s expiration year. |  [optional] |
|**fingerprint** | **String** | A unique value to identify the payment instrument regardless of variable values. It contains alphanumeric values. |  [optional] [readonly] |
|**id** | **String** | The payment instrument ID. |  [optional] [readonly] |
|**last4** | **String** | The PAN&#39;s last 4 digits. |  [optional] [readonly] |
|**method** | [**MethodEnum**](#MethodEnum) | The method of payment instrument. |  [optional] [readonly] |
|**pan** | **String** | The card PAN (primary account number). |  [optional] |
|**riskMetadata** | [**RiskMetadata**](RiskMetadata.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Payment instrument status. When an instrument is &#x60;active&#x60; it means it has been used at least once for an approved transaction. To remove an instrument from being in use, set it as &#x60;deactivated&#x60; (see the deactivation endpoint).  |  [optional] |
|**updatedTime** | **OffsetDateTime** | Payment instrument updated time. |  [optional] [readonly] |



## Enum: MethodEnum

| Name | Value |
|---- | -----|
| PAYMENT_CARD | &quot;payment-card&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| INACTIVE | &quot;inactive&quot; |
| EXPIRED | &quot;expired&quot; |
| DEACTIVATED | &quot;deactivated&quot; |
| VERIFICATION_NEEDED | &quot;verification-needed&quot; |



