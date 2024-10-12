

# EditUserAlt1RequestVideosPrivacy


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**add** | **Boolean** | Whether a user can add the video to an album, channel, or group. This value becomes the default add setting for all future videos uploaded by the user. |  [optional] |
|**comments** | [**CommentsEnum**](#CommentsEnum) | Who can comment on the video. This value becomes the default comment setting for all future videos that this user uploads. |  [optional] |
|**download** | **Boolean** | Whether a user can download the video. This value becomes the default download setting for all future videos that this user uploads. |  [optional] |
|**embed** | [**EmbedEnum**](#EmbedEnum) | The privacy for embed videos. The &#x60;whitelist&#x60; value enables you to define all valid embed domains. See our [documentation](https://developer.vimeo.com/api/endpoints/videos#/{video_id}/privacy/domains) for adding and removing domains. |  [optional] |
|**view** | [**ViewEnum**](#ViewEnum) | Who can view the video. This value becomes the default view setting for all future videos that this user uploads. |  [optional] |



## Enum: CommentsEnum

| Name | Value |
|---- | -----|
| ANYBODY | &quot;anybody&quot; |
| CONTACTS | &quot;contacts&quot; |
| NOBODY | &quot;nobody&quot; |



## Enum: EmbedEnum

| Name | Value |
|---- | -----|
| PRIVATE | &quot;private&quot; |
| PUBLIC | &quot;public&quot; |
| WHITELIST | &quot;whitelist&quot; |



## Enum: ViewEnum

| Name | Value |
|---- | -----|
| ANYBODY | &quot;anybody&quot; |
| CONTACTS | &quot;contacts&quot; |
| DISABLE | &quot;disable&quot; |
| NOBODY | &quot;nobody&quot; |
| PASSWORD | &quot;password&quot; |
| UNLISTED | &quot;unlisted&quot; |
| USERS | &quot;users&quot; |



