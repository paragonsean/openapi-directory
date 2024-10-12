# DisplayVideo360Api.ContentOutstreamPositionAssignedTargetingOptionDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adType** | **String** | Output only. The ad type to target. Only applicable to insertion order targeting and new line items supporting the specified ad type will inherit this targeting option by default. Possible values are: * &#x60;AD_TYPE_DISPLAY&#x60;, the setting will be inherited by new line item when line_item_type is &#x60;LINE_ITEM_TYPE_DISPLAY_DEFAULT&#x60;. * &#x60;AD_TYPE_VIDEO&#x60;, the setting will be inherited by new line item when line_item_type is &#x60;LINE_ITEM_TYPE_VIDEO_DEFAULT&#x60;. | [optional] [readonly] 
**contentOutstreamPosition** | **String** | Required. The content outstream position. | [optional] 



## Enum: AdTypeEnum


* `UNSPECIFIED` (value: `"AD_TYPE_UNSPECIFIED"`)

* `DISPLAY` (value: `"AD_TYPE_DISPLAY"`)

* `VIDEO` (value: `"AD_TYPE_VIDEO"`)

* `AUDIO` (value: `"AD_TYPE_AUDIO"`)





## Enum: ContentOutstreamPositionEnum


* `UNSPECIFIED` (value: `"CONTENT_OUTSTREAM_POSITION_UNSPECIFIED"`)

* `UNKNOWN` (value: `"CONTENT_OUTSTREAM_POSITION_UNKNOWN"`)

* `IN_ARTICLE` (value: `"CONTENT_OUTSTREAM_POSITION_IN_ARTICLE"`)

* `IN_BANNER` (value: `"CONTENT_OUTSTREAM_POSITION_IN_BANNER"`)

* `IN_FEED` (value: `"CONTENT_OUTSTREAM_POSITION_IN_FEED"`)

* `INTERSTITIAL` (value: `"CONTENT_OUTSTREAM_POSITION_INTERSTITIAL"`)




