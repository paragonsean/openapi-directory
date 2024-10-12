

# CommonPayPalAccount


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billingAddress** | [**ContactObject**](ContactObject.md) | The billing address. |  |
|**createdTime** | **OffsetDateTime** | PayPal account created time. |  [optional] [readonly] |
|**customFields** | **Object** | Custom Fields list as a map &#x60;{\&quot;custom field name\&quot;: \&quot;custom field value\&quot;, ...}&#x60;. The format must follow the saved format (see Custom Fields section for the formats).  |  [optional] |
|**customerId** | **String** | The customer&#39;s ID. |  |
|**id** | **String** | The payment instrument ID. |  [optional] [readonly] |
|**method** | [**MethodEnum**](#MethodEnum) | The method of payment instrument. |  |
|**riskMetadata** | [**RiskMetadata**](RiskMetadata.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | PayPal account status. |  [optional] [readonly] |
|**updatedTime** | **OffsetDateTime** | PayPal account updated time. |  [optional] [readonly] |
|**username** | **String** | PayPal username. |  [optional] [readonly] |



## Enum: MethodEnum

| Name | Value |
|---- | -----|
| PAYPAL | &quot;paypal&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| INACTIVE | &quot;inactive&quot; |
| ACTIVE | &quot;active&quot; |
| DEACTIVATED | &quot;deactivated&quot; |



