# Vimeo.VideoPrivacy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add** | **Boolean** | Whether the video can be added to collections. | 
**comments** | **String** | Who can comment on the video:  Option descriptions:  * &#x60;anybody&#x60; - Anyone can comment on the video.  * &#x60;contacts&#x60; - Only contacts can comment on the video.  * &#x60;nobody&#x60; - No one can comment on the video.  | 
**download** | **Boolean** | The video&#39;s download permission setting. | 
**embed** | **String** | The video&#39;s embed permission setting:  Option descriptions:  * &#x60;private&#x60; - The video is private.  * &#x60;public&#x60; - Anyone can embed the video.  | 
**view** | **String** | The general privacy setting for the video:  Option descriptions:  * &#x60;anybody&#x60; - Anyone can view the video.  * &#x60;contacts&#x60; - Only contacts can view the video.  * &#x60;disable&#x60; - Hide from vimeo  * &#x60;nobody&#x60; - No one besides the owner can view the video.  * &#x60;password&#x60; - Anyone with the video&#39;s password can view the video.  * &#x60;unlisted&#x60; - Not searchable from vimeo.com  * &#x60;users&#x60; - Only people with a Vimeo account can view the video.  | 



## Enum: CommentsEnum


* `anybody` (value: `"anybody"`)

* `contacts` (value: `"contacts"`)

* `nobody` (value: `"nobody"`)





## Enum: EmbedEnum


* `private` (value: `"private"`)

* `public` (value: `"public"`)





## Enum: ViewEnum


* `anybody` (value: `"anybody"`)

* `contacts` (value: `"contacts"`)

* `disable` (value: `"disable"`)

* `nobody` (value: `"nobody"`)

* `password` (value: `"password"`)

* `unlisted` (value: `"unlisted"`)

* `users` (value: `"users"`)




