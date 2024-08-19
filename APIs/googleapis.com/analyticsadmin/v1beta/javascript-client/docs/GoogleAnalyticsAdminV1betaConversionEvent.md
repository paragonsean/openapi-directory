# GoogleAnalyticsAdminApi.GoogleAnalyticsAdminV1betaConversionEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**countingMethod** | **String** | Optional. The method by which conversions will be counted across multiple events within a session. If this value is not provided, it will be set to &#x60;ONCE_PER_EVENT&#x60;. | [optional] 
**createTime** | **String** | Output only. Time when this conversion event was created in the property. | [optional] [readonly] 
**custom** | **Boolean** | Output only. If set to true, this conversion event refers to a custom event. If set to false, this conversion event refers to a default event in GA. Default events typically have special meaning in GA. Default events are usually created for you by the GA system, but in some cases can be created by property admins. Custom events count towards the maximum number of custom conversion events that may be created per property. | [optional] [readonly] 
**defaultConversionValue** | [**GoogleAnalyticsAdminV1betaConversionEventDefaultConversionValue**](GoogleAnalyticsAdminV1betaConversionEventDefaultConversionValue.md) |  | [optional] 
**deletable** | **Boolean** | Output only. If set, this event can currently be deleted with DeleteConversionEvent. | [optional] [readonly] 
**eventName** | **String** | Immutable. The event name for this conversion event. Examples: &#39;click&#39;, &#39;purchase&#39; | [optional] 
**name** | **String** | Output only. Resource name of this conversion event. Format: properties/{property}/conversionEvents/{conversion_event} | [optional] [readonly] 



## Enum: CountingMethodEnum


* `CONVERSION_COUNTING_METHOD_UNSPECIFIED` (value: `"CONVERSION_COUNTING_METHOD_UNSPECIFIED"`)

* `ONCE_PER_EVENT` (value: `"ONCE_PER_EVENT"`)

* `ONCE_PER_SESSION` (value: `"ONCE_PER_SESSION"`)




