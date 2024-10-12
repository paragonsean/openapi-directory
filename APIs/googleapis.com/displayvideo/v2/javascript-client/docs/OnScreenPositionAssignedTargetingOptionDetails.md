# DisplayVideo360Api.OnScreenPositionAssignedTargetingOptionDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adType** | **String** | Output only. The ad type to target. Only applicable to insertion order targeting and new line items supporting the specified ad type will inherit this targeting option by default. Possible values are: * &#x60;AD_TYPE_DISPLAY&#x60;, the setting will be inherited by new line item when line_item_type is &#x60;LINE_ITEM_TYPE_DISPLAY_DEFAULT&#x60;. * &#x60;AD_TYPE_VIDEO&#x60;, the setting will be inherited by new line item when line_item_type is &#x60;LINE_ITEM_TYPE_VIDEO_DEFAULT&#x60;. | [optional] [readonly] 
**onScreenPosition** | **String** | Output only. The on screen position. | [optional] [readonly] 
**targetingOptionId** | **String** | Required. The targeting_option_id field when targeting_type is &#x60;TARGETING_TYPE_ON_SCREEN_POSITION&#x60;. | [optional] 



## Enum: AdTypeEnum


* `UNSPECIFIED` (value: `"AD_TYPE_UNSPECIFIED"`)

* `DISPLAY` (value: `"AD_TYPE_DISPLAY"`)

* `VIDEO` (value: `"AD_TYPE_VIDEO"`)

* `AUDIO` (value: `"AD_TYPE_AUDIO"`)





## Enum: OnScreenPositionEnum


* `UNSPECIFIED` (value: `"ON_SCREEN_POSITION_UNSPECIFIED"`)

* `UNKNOWN` (value: `"ON_SCREEN_POSITION_UNKNOWN"`)

* `ABOVE_THE_FOLD` (value: `"ON_SCREEN_POSITION_ABOVE_THE_FOLD"`)

* `BELOW_THE_FOLD` (value: `"ON_SCREEN_POSITION_BELOW_THE_FOLD"`)




