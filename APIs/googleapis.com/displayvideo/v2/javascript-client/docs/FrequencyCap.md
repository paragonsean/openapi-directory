# DisplayVideo360Api.FrequencyCap

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maxImpressions** | **Number** | The maximum number of times a user may be shown the same ad during this period. Must be greater than 0. Required when unlimited is &#x60;false&#x60; and max_views is not set. | [optional] 
**maxViews** | **Number** | Optional. The maximum number of times a user may click-through or fully view an ad during this period until it is no longer served to them. Must be greater than 0. Only applicable to YouTube and Partners resources. Required when unlimited is &#x60;false&#x60; and max_impressions is not set. | [optional] 
**timeUnit** | **String** | The time unit in which the frequency cap will be applied. Required when unlimited is &#x60;false&#x60;. | [optional] 
**timeUnitCount** | **Number** | The number of time_unit the frequency cap will last. Required when unlimited is &#x60;false&#x60;. The following restrictions apply based on the value of time_unit: * &#x60;TIME_UNIT_LIFETIME&#x60; - this field is output only and will default to 1 * &#x60;TIME_UNIT_MONTHS&#x60; - must be between 1 and 2 * &#x60;TIME_UNIT_WEEKS&#x60; - must be between 1 and 4 * &#x60;TIME_UNIT_DAYS&#x60; - must be between 1 and 6 * &#x60;TIME_UNIT_HOURS&#x60; - must be between 1 and 23 * &#x60;TIME_UNIT_MINUTES&#x60; - must be between 1 and 59 | [optional] 
**unlimited** | **Boolean** | Whether unlimited frequency capping is applied. When this field is set to &#x60;true&#x60;, the remaining frequency cap fields are not applicable. | [optional] 



## Enum: TimeUnitEnum


* `UNSPECIFIED` (value: `"TIME_UNIT_UNSPECIFIED"`)

* `LIFETIME` (value: `"TIME_UNIT_LIFETIME"`)

* `MONTHS` (value: `"TIME_UNIT_MONTHS"`)

* `WEEKS` (value: `"TIME_UNIT_WEEKS"`)

* `DAYS` (value: `"TIME_UNIT_DAYS"`)

* `HOURS` (value: `"TIME_UNIT_HOURS"`)

* `MINUTES` (value: `"TIME_UNIT_MINUTES"`)




