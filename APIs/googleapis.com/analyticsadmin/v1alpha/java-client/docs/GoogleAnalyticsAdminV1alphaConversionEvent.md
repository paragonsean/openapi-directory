

# GoogleAnalyticsAdminV1alphaConversionEvent

A conversion event in a Google Analytics property.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**countingMethod** | [**CountingMethodEnum**](#CountingMethodEnum) | Optional. The method by which conversions will be counted across multiple events within a session. If this value is not provided, it will be set to &#x60;ONCE_PER_EVENT&#x60;. |  [optional] |
|**createTime** | **String** | Output only. Time when this conversion event was created in the property. |  [optional] [readonly] |
|**custom** | **Boolean** | Output only. If set to true, this conversion event refers to a custom event. If set to false, this conversion event refers to a default event in GA. Default events typically have special meaning in GA. Default events are usually created for you by the GA system, but in some cases can be created by property admins. Custom events count towards the maximum number of custom conversion events that may be created per property. |  [optional] [readonly] |
|**defaultConversionValue** | [**GoogleAnalyticsAdminV1alphaConversionEventDefaultConversionValue**](GoogleAnalyticsAdminV1alphaConversionEventDefaultConversionValue.md) |  |  [optional] |
|**deletable** | **Boolean** | Output only. If set, this event can currently be deleted with DeleteConversionEvent. |  [optional] [readonly] |
|**eventName** | **String** | Immutable. The event name for this conversion event. Examples: &#39;click&#39;, &#39;purchase&#39; |  [optional] |
|**name** | **String** | Output only. Resource name of this conversion event. Format: properties/{property}/conversionEvents/{conversion_event} |  [optional] [readonly] |



## Enum: CountingMethodEnum

| Name | Value |
|---- | -----|
| CONVERSION_COUNTING_METHOD_UNSPECIFIED | &quot;CONVERSION_COUNTING_METHOD_UNSPECIFIED&quot; |
| ONCE_PER_EVENT | &quot;ONCE_PER_EVENT&quot; |
| ONCE_PER_SESSION | &quot;ONCE_PER_SESSION&quot; |



