

# VideoPrivacy

The video's privacy setting.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**add** | **Boolean** | Whether the video can be added to collections. |  |
|**comments** | [**CommentsEnum**](#CommentsEnum) | Who can comment on the video:  Option descriptions:  * &#x60;anybody&#x60; - Anyone can comment on the video.  * &#x60;contacts&#x60; - Only contacts can comment on the video.  * &#x60;nobody&#x60; - No one can comment on the video.  |  |
|**download** | **Boolean** | The video&#39;s download permission setting. |  |
|**embed** | [**EmbedEnum**](#EmbedEnum) | The video&#39;s embed permission setting:  Option descriptions:  * &#x60;private&#x60; - The video is private.  * &#x60;public&#x60; - Anyone can embed the video.  |  |
|**view** | [**ViewEnum**](#ViewEnum) | The general privacy setting for the video:  Option descriptions:  * &#x60;anybody&#x60; - Anyone can view the video.  * &#x60;contacts&#x60; - Only contacts can view the video.  * &#x60;disable&#x60; - Hide from vimeo  * &#x60;nobody&#x60; - No one besides the owner can view the video.  * &#x60;password&#x60; - Anyone with the video&#39;s password can view the video.  * &#x60;unlisted&#x60; - Not searchable from vimeo.com  * &#x60;users&#x60; - Only people with a Vimeo account can view the video.  |  |



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



