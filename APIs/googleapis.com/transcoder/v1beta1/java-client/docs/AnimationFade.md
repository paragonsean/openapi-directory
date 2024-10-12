

# AnimationFade

Display overlay object with fade animation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTimeOffset** | **String** | The time to end the fade animation, in seconds. Default: &#x60;start_time_offset&#x60; + 1s |  [optional] |
|**fadeType** | [**FadeTypeEnum**](#FadeTypeEnum) | Required. Type of fade animation: &#x60;FADE_IN&#x60; or &#x60;FADE_OUT&#x60;. |  [optional] |
|**startTimeOffset** | **String** | The time to start the fade animation, in seconds. Default: 0 |  [optional] |
|**xy** | [**NormalizedCoordinate**](NormalizedCoordinate.md) |  |  [optional] |



## Enum: FadeTypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;FADE_TYPE_UNSPECIFIED&quot; |
| IN | &quot;FADE_IN&quot; |
| OUT | &quot;FADE_OUT&quot; |



