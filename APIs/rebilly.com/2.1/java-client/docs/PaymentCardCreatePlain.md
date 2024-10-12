

# PaymentCardCreatePlain


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billingAddress** | [**ContactObject**](ContactObject.md) | The billing address. |  |
|**customFields** | **Object** | Custom Fields list as a map &#x60;{\&quot;custom field name\&quot;: \&quot;custom field value\&quot;, ...}&#x60;. The format must follow the saved format (see Custom Fields section for the formats).  |  [optional] |
|**customerId** | **String** | The Customer&#39;s ID. |  |
|**cvv** | **String** | Card&#39;s cvv (card verification value). |  [optional] |
|**expMonth** | **Integer** | Card&#39;s expiration month. |  |
|**expYear** | **Integer** | Card&#39;s expiration year. |  |
|**method** | [**MethodEnum**](#MethodEnum) | The method of payment instrument. |  |
|**pan** | **String** | The card PAN (Primary Account Number). |  |
|**riskMetadata** | [**RiskMetadata**](RiskMetadata.md) |  |  [optional] |



## Enum: MethodEnum

| Name | Value |
|---- | -----|
| PAYMENT_CARD | &quot;payment-card&quot; |



