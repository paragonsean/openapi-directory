

# AlternativePaymentInstrument2


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**embedded** | [**List&lt;AlternativePaymentInstrument2EmbeddedInner&gt;**](AlternativePaymentInstrument2EmbeddedInner.md) | Any embedded objects available that are requested by the &#x60;expand&#x60; querystring parameter. |  [optional] [readonly] |
|**links** | [**List&lt;AlternativePaymentInstrument2LinksInner&gt;**](AlternativePaymentInstrument2LinksInner.md) | Links related to the resource. |  [optional] [readonly] |
|**billingAddress** | [**ContactObject**](ContactObject.md) | The billing address. |  [optional] |
|**createdTime** | **OffsetDateTime** | The payment instrument created time. |  [optional] [readonly] |
|**customFields** | **Object** | Custom Fields list as a map &#x60;{\&quot;custom field name\&quot;: \&quot;custom field value\&quot;, ...}&#x60;. The format must follow the saved format (see Custom Fields section for the formats).  |  [optional] |
|**customerId** | **String** | Customer&#39;s ID. |  [optional] |
|**id** | **String** | The payment instrument ID. |  [optional] |
|**method** | **AlternativePaymentMethods** | The method of payment instrument. |  [optional] |
|**riskMetadata** | [**RiskMetadata**](RiskMetadata.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The payment instrument status. |  [optional] |
|**updatedTime** | **OffsetDateTime** | The payment instrument updated time. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| DEACTIVATED | &quot;deactivated&quot; |



