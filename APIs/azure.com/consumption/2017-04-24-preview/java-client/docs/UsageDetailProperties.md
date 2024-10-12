

# UsageDetailProperties

The properties of the usage detail.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalProperties** | **Map&lt;String, String&gt;** | The list of key/value pairs for the additional properties, in the format &#39;key&#39;:&#39;value&#39; where key &#x3D; the field name, and value &#x3D; the field value. By default this is not populated, unless it&#39;s specified in $expand. |  [optional] [readonly] |
|**billableQuantity** | **BigDecimal** | The billable usage quantity. |  [optional] [readonly] |
|**billingPeriodId** | **String** | The id of the billing period resource that the usage belongs to. |  [optional] [readonly] |
|**currency** | **String** | The ISO currency in which the meter is charged, for example, USD. |  [optional] [readonly] |
|**instanceId** | **String** | The uri of the resource instance that the usage is about. |  [optional] [readonly] |
|**instanceLocation** | **String** | The location of the resource instance that the usage is about. |  [optional] [readonly] |
|**instanceName** | **String** | The name of the resource instance that the usage is about. |  [optional] [readonly] |
|**invoiceId** | **String** | The id of the invoice resource that the usage belongs to. |  [optional] [readonly] |
|**isEstimated** | **Boolean** | The estimated usage is subject to change. |  [optional] [readonly] |
|**meterDetails** | [**MeterDetails**](MeterDetails.md) |  |  [optional] |
|**meterId** | **String** | The meter id. |  [optional] [readonly] |
|**pretaxCost** | **BigDecimal** | The amount of cost before tax. |  [optional] [readonly] |
|**usageEnd** | **OffsetDateTime** | The end of the date time range covered by the usage detail. |  [optional] [readonly] |
|**usageQuantity** | **BigDecimal** | The quantity of usage. |  [optional] [readonly] |
|**usageStart** | **OffsetDateTime** | The start of the date time range covered by the usage detail. |  [optional] [readonly] |



