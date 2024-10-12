# YouTubeDataApiV3.VideoContentDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caption** | **String** | The value of captions indicates whether the video has captions or not. | [optional] 
**contentRating** | [**ContentRating**](ContentRating.md) |  | [optional] 
**countryRestriction** | [**AccessPolicy**](AccessPolicy.md) |  | [optional] 
**definition** | **String** | The value of definition indicates whether the video is available in high definition or only in standard definition. | [optional] 
**dimension** | **String** | The value of dimension indicates whether the video is available in 3D or in 2D. | [optional] 
**duration** | **String** | The length of the video. The tag value is an ISO 8601 duration in the format PT#M#S, in which the letters PT indicate that the value specifies a period of time, and the letters M and S refer to length in minutes and seconds, respectively. The # characters preceding the M and S letters are both integers that specify the number of minutes (or seconds) of the video. For example, a value of PT15M51S indicates that the video is 15 minutes and 51 seconds long. | [optional] 
**hasCustomThumbnail** | **Boolean** | Indicates whether the video uploader has provided a custom thumbnail image for the video. This property is only visible to the video uploader. | [optional] 
**licensedContent** | **Boolean** | The value of is_license_content indicates whether the video is licensed content. | [optional] 
**projection** | **String** | Specifies the projection format of the video. | [optional] 
**regionRestriction** | [**VideoContentDetailsRegionRestriction**](VideoContentDetailsRegionRestriction.md) |  | [optional] 



## Enum: CaptionEnum


* `true` (value: `"true"`)

* `false` (value: `"false"`)





## Enum: DefinitionEnum


* `sd` (value: `"sd"`)

* `hd` (value: `"hd"`)





## Enum: ProjectionEnum


* `rectangular` (value: `"rectangular"`)

* `360` (value: `"360"`)




