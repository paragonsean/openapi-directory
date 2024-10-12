

# KhelocardCard


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**embedded** | [**List&lt;BankAccountAllOfEmbedded&gt;**](BankAccountAllOfEmbedded.md) | Any embedded objects available that are requested by the &#x60;expand&#x60; querystring parameter. |  [optional] [readonly] |
|**links** | [**List&lt;BankAccountAllOfLinks&gt;**](BankAccountAllOfLinks.md) | Links related to the resource. |  [optional] [readonly] |
|**billingAddress** | [**ContactObject**](ContactObject.md) | The billing address. |  [optional] |
|**createdTime** | **OffsetDateTime** | The payment instrument created time. |  [optional] [readonly] |
|**customFields** | **Object** | Custom Fields list as a map &#x60;{\&quot;custom field name\&quot;: \&quot;custom field value\&quot;, ...}&#x60;. The format must follow the saved format (see Custom Fields section for the formats).  |  [optional] |
|**customerId** | **String** | Customer&#39;s ID. |  [optional] |
|**expMonth** | **Integer** | Khelocard card&#39;s expiration month. |  [optional] |
|**expYear** | **Integer** | Khelocard card&#39;s expiration year. |  [optional] |
|**fingerprint** | **String** | A unique value to identify the payment instrument regardless of variable values. It contains alphanumeric values. |  [optional] |
|**id** | **String** | The payment instrument ID. |  [optional] |
|**last4** | **String** | The number&#39;s last 4 digits. |  [optional] |
|**method** | [**MethodEnum**](#MethodEnum) | The method of payment instrument. |  [optional] |
|**number** | **String** | Khelocard card&#39;s masked number. |  [optional] |
|**riskMetadata** | [**RiskMetadata**](RiskMetadata.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The payment instrument status. |  [optional] |
|**updatedTime** | **OffsetDateTime** | The payment instrument updated time. |  [optional] [readonly] |



## Enum: MethodEnum

| Name | Value |
|---- | -----|
| KHELOCARD | &quot;Khelocard&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| DEACTIVATED | &quot;deactivated&quot; |



