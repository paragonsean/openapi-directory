# DisplayVideo360Api.TargetingExpansionConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**excludeFirstPartyAudience** | **Boolean** | Whether to exclude first-party audiences from use in targeting expansion. This field was deprecated with the launch of [optimized targeting](//support.google.com/displayvideo/answer/12060859). This field will be set to &#x60;false&#x60;. If this field is set to &#x60;true&#x60; when deprecated, all positive first-party audience targeting assigned to this line item will be replaced with negative targeting of the same first-party audiences to ensure the continued exclusion of those audiences. | [optional] 
**targetingExpansionLevel** | **String** | Required. Whether optimized targeting is turned on. This field supports the following values: * &#x60;NO_EXPANSION&#x60;: optimized targeting is turned off * &#x60;LEAST_EXPANSION&#x60;: optimized targeting is turned on If this field is set to any other value, it will automatically be set to &#x60;LEAST_EXPANSION&#x60;. &#x60;NO_EXPANSION&#x60; will be the default value for the field and will be automatically assigned if you do not set the field. | [optional] 



## Enum: TargetingExpansionLevelEnum


* `TARGETING_EXPANSION_LEVEL_UNSPECIFIED` (value: `"TARGETING_EXPANSION_LEVEL_UNSPECIFIED"`)

* `NO_EXPANSION` (value: `"NO_EXPANSION"`)

* `LEAST_EXPANSION` (value: `"LEAST_EXPANSION"`)

* `SOME_EXPANSION` (value: `"SOME_EXPANSION"`)

* `BALANCED_EXPANSION` (value: `"BALANCED_EXPANSION"`)

* `MORE_EXPANSION` (value: `"MORE_EXPANSION"`)

* `MOST_EXPANSION` (value: `"MOST_EXPANSION"`)




