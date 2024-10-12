# Vimeo.Video

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | [**[Category]**](Category.md) | The categories to which this video belongs. | 
**contentRating** | **[String]** | The content ratings of this video. | 
**context** | [**VideoContext**](VideoContext.md) |  | 
**createdTime** | **String** | The time in ISO 8601 format when the video was created. | 
**description** | **String** | A brief explanation of the video&#39;s content. | 
**duration** | **Number** | The video&#39;s duration in seconds. | 
**embed** | [**EmbedSettings**](EmbedSettings.md) | Information about embedding this video. | 
**height** | **Number** | The video&#39;s height in pixels. | 
**language** | **String** | The video&#39;s primary language. | 
**lastUserActionEventDate** | **String** | The time in ISO 8601 format when the user last modified the video. | [optional] 
**license** | **String** | The [Creative Commons](http://creativecommons.org/licenses/) license used for the video:  Option descriptions:  * &#x60;by&#x60; - Attribution  * &#x60;by-nc&#x60; - Attribution Non-Commercial  * &#x60;by-nc-nd&#x60; - Attribution Non-Commercial No Derivatives  * &#x60;by-nc-sa&#x60; - Attribution Non-Commercial Share Alike  * &#x60;by-nd&#x60; - Attribution No Derivatives  * &#x60;by-sa&#x60; - Attribution Share Alike  * &#x60;cc0&#x60; - Public Domain Dedication  | 
**link** | **String** | The link to the video. | 
**metadata** | [**VideoMetadata**](VideoMetadata.md) |  | 
**modifiedTime** | **String** | The time in ISO 8601 format when the video metadata was last modified. | 
**name** | **String** | The video&#39;s title. | 
**parentFolder** | [**Project**](Project.md) | Information about the folder that contains this video. | [optional] 
**password** | **String** | The privacy-enabled password to watch this video. Only users can see their own video passwords. This data requires a bearer token with the &#x60;private&#x60; scope. | [optional] 
**pictures** | [**Picture**](Picture.md) | The active picture for this video. | 
**privacy** | [**VideoPrivacy**](VideoPrivacy.md) |  | 
**releaseTime** | **String** | The time in ISO 8601 format when the video was released. | 
**resourceKey** | **String** | The resource key string of the video. | 
**spatial** | [**VideoSpatial**](VideoSpatial.md) |  | 
**stats** | [**VideoStats**](VideoStats.md) |  | 
**status** | **String** | The status code for the availability of the video. This field is deprecated in favor of &#x60;upload&#x60; and &#x60;transcode&#x60;.  Option descriptions:  * &#x60;available&#x60; - The video is available.  * &#x60;quota_exceeded&#x60; - The user&#39;s quota is exceeded with this video.  * &#x60;total_cap_exceeded&#x60; - The user has exceeded their total cap with this video.  * &#x60;transcode_starting&#x60; - Transcoding is beginning for the video.  * &#x60;transcoding&#x60; - Transcoding is underway for the video.  * &#x60;transcoding_error&#x60; - There was an error in transcoding the video.  * &#x60;unavailable&#x60; - The video is unavailable.  * &#x60;uploading&#x60; - The video is being uploaded.  * &#x60;uploading_error&#x60; - There was an error in uploading the video.  | 
**tags** | [**[Tag]**](Tag.md) | An array of all tags assigned to this video. | 
**transcode** | [**VideoTranscode**](VideoTranscode.md) |  | 
**upload** | [**VideoUpload**](VideoUpload.md) |  | 
**uri** | **String** | The video&#39;s canonical relative URI. | 
**user** | [**User**](User.md) | The video owner. | 
**width** | **Number** | The video&#39;s width in pixels. | 



## Enum: LicenseEnum


* `by` (value: `"by"`)

* `by-nc` (value: `"by-nc"`)

* `by-nc-nd` (value: `"by-nc-nd"`)

* `by-nc-sa` (value: `"by-nc-sa"`)

* `by-nd` (value: `"by-nd"`)

* `by-sa` (value: `"by-sa"`)

* `cc0` (value: `"cc0"`)





## Enum: StatusEnum


* `available` (value: `"available"`)

* `quota_exceeded` (value: `"quota_exceeded"`)

* `total_cap_exceeded` (value: `"total_cap_exceeded"`)

* `transcode_starting` (value: `"transcode_starting"`)

* `transcoding` (value: `"transcoding"`)

* `transcoding_error` (value: `"transcoding_error"`)

* `unavailable` (value: `"unavailable"`)

* `uploading` (value: `"uploading"`)

* `uploading_error` (value: `"uploading_error"`)




