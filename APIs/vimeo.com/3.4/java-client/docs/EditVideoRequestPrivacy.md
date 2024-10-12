

# EditVideoRequestPrivacy


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**add** | **Boolean** | Whether a user can add the video to an album, channel, or group. |  [optional] |
|**comments** | [**CommentsEnum**](#CommentsEnum) | The privacy level required to comment on the video. |  [optional] |
|**download** | **Boolean** | Whether a user can download the video. Not available to users with a Basic membership. |  [optional] |
|**embed** | [**EmbedEnum**](#EmbedEnum) | The video&#39;s new embed settings. The &#x60;whitelist&#x60; value enables you to define all valid embed domains. See our [documentation](https://developer.vimeo.com/api/endpoints/videos#/{video_id}/privacy/domains) for details on adding and removing domains. |  [optional] |
|**view** | [**ViewEnum**](#ViewEnum) | The video&#39;s new privacy setting. When privacy is &#x60;users&#x60;, &#x60;application/json&#x60; is the only valid content type. Basic users can&#39;t set privacy to &#x60;unlisted&#x60;. |  [optional] |



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



