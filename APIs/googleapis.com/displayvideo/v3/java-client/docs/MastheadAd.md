

# MastheadAd

Details for a Masthead Ad.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoplayVideoDuration** | **String** | The duration of time the video will autoplay. |  [optional] |
|**autoplayVideoStartMillisecond** | **String** | The amount of time in milliseconds after which the video will start to play. |  [optional] |
|**callToActionButtonLabel** | **String** | The text on the call-to-action button. |  [optional] |
|**callToActionFinalUrl** | **String** | The destination URL for the call-to-action button. |  [optional] |
|**callToActionTrackingUrl** | **String** | The tracking URL for the call-to-action button. |  [optional] |
|**companionYoutubeVideos** | [**List&lt;YoutubeVideoDetails&gt;**](YoutubeVideoDetails.md) | The videos that appear next to the Masthead Ad on desktop. Can be no more than two. |  [optional] |
|**description** | **String** | The description of the ad. |  [optional] |
|**headline** | **String** | The headline of the ad. |  [optional] |
|**showChannelArt** | **Boolean** | Whether to show a background or banner that appears at the top of a YouTube page. |  [optional] |
|**video** | [**YoutubeVideoDetails**](YoutubeVideoDetails.md) |  |  [optional] |
|**videoAspectRatio** | [**VideoAspectRatioEnum**](#VideoAspectRatioEnum) | The aspect ratio of the autoplaying YouTube video on the Masthead. |  [optional] |



## Enum: VideoAspectRatioEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;VIDEO_ASPECT_RATIO_UNSPECIFIED&quot; |
| WIDESCREEN | &quot;VIDEO_ASPECT_RATIO_WIDESCREEN&quot; |
| FIXED_16_9 | &quot;VIDEO_ASPECT_RATIO_FIXED_16_9&quot; |



