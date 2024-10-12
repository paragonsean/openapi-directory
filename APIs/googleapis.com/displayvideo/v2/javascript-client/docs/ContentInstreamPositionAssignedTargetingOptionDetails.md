# DisplayVideo360Api.ContentInstreamPositionAssignedTargetingOptionDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adType** | **String** | Output only. The ad type to target. Only applicable to insertion order targeting and new line items supporting the specified ad type will inherit this targeting option by default. Possible values are: * &#x60;AD_TYPE_VIDEO&#x60;, the setting will be inherited by new line item when line_item_type is &#x60;LINE_ITEM_TYPE_VIDEO_DEFAULT&#x60;. * &#x60;AD_TYPE_AUDIO&#x60;, the setting will be inherited by new line item when line_item_type is &#x60;LINE_ITEM_TYPE_AUDIO_DEFAULT&#x60;. | [optional] [readonly] 
**contentInstreamPosition** | **String** | Required. The content instream position for video or audio ads. | [optional] 



## Enum: AdTypeEnum


* `UNSPECIFIED` (value: `"AD_TYPE_UNSPECIFIED"`)

* `DISPLAY` (value: `"AD_TYPE_DISPLAY"`)

* `VIDEO` (value: `"AD_TYPE_VIDEO"`)

* `AUDIO` (value: `"AD_TYPE_AUDIO"`)





## Enum: ContentInstreamPositionEnum


* `UNSPECIFIED` (value: `"CONTENT_INSTREAM_POSITION_UNSPECIFIED"`)

* `PRE_ROLL` (value: `"CONTENT_INSTREAM_POSITION_PRE_ROLL"`)

* `MID_ROLL` (value: `"CONTENT_INSTREAM_POSITION_MID_ROLL"`)

* `POST_ROLL` (value: `"CONTENT_INSTREAM_POSITION_POST_ROLL"`)

* `UNKNOWN` (value: `"CONTENT_INSTREAM_POSITION_UNKNOWN"`)




