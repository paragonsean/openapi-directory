

# Media

The `Media` object contains a reference for most any media associated with a team or event on TBA.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**details** | **Object** | If required, a JSON dict of additional media information. |  [optional] |
|**directUrl** | **String** | Direct URL to the media. |  [optional] |
|**foreignKey** | **String** | The key used to identify this media on the media site. |  |
|**preferred** | **Boolean** | True if the media is of high quality. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | String type of the media element. |  |
|**viewUrl** | **String** | The URL that leads to the full web page for the media, if one exists. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| YOUTUBE | &quot;youtube&quot; |
| CDPHOTOTHREAD | &quot;cdphotothread&quot; |
| IMGUR | &quot;imgur&quot; |
| FACEBOOK_PROFILE | &quot;facebook-profile&quot; |
| YOUTUBE_CHANNEL | &quot;youtube-channel&quot; |
| TWITTER_PROFILE | &quot;twitter-profile&quot; |
| GITHUB_PROFILE | &quot;github-profile&quot; |
| INSTAGRAM_PROFILE | &quot;instagram-profile&quot; |
| PERISCOPE_PROFILE | &quot;periscope-profile&quot; |
| GRABCAD | &quot;grabcad&quot; |
| INSTAGRAM_IMAGE | &quot;instagram-image&quot; |
| EXTERNAL_LINK | &quot;external-link&quot; |
| AVATAR | &quot;avatar&quot; |



