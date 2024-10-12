# Vimeo.UserPreferencesVideosPrivacy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add** | **Boolean** | Whether other users can add the user&#39;s videos. | [optional] 
**comments** | **String** | The user&#39;s privacy preference for comments:  Option descriptions:  * &#x60;anybody&#x60; - Anyone can comment on the user&#39;s videos.  * &#x60;contacts&#x60; - Only contacts can comment on the user&#39;s videos.  * &#x60;nobody&#x60; - No one can comment on the user&#39;s videos.  | [optional] 
**download** | **Boolean** | Whether other users can download the user&#39;s videos. | [optional] 
**embed** | **String** | The user&#39;s privacy preference for embeds:  Option descriptions:  * &#x60;private&#x60; - Only the user can embed their own videos.  * &#x60;public&#x60; - Anyone can embed the user&#39;s videos.  * &#x60;whitelist&#x60; - Only those on the whitelist can embed the user&#39;s videos.  | [optional] 
**view** | **String** | The user&#39;s privacy preference for views:  Option descriptions:  * &#x60;anybody&#x60; - Anyone can view the user&#39;s videos.  * &#x60;contacts&#x60; - Only contacts can view the user&#39;s videos.  * &#x60;disable&#x60; - Views are disabled for the user&#39;s videos.  * &#x60;nobody&#x60; - No one except the user can view the user&#39;s videos.  * &#x60;password&#x60; - Only those with the password can view the user&#39;s videos.  * &#x60;unlisted&#x60; - Anybody can view the user&#39;s videos if they have a link.  * &#x60;users&#x60; - Only other Vimeo members can view the user&#39;s videos.  | [optional] 



## Enum: CommentsEnum


* `anybody` (value: `"anybody"`)

* `contacts` (value: `"contacts"`)

* `nobody` (value: `"nobody"`)





## Enum: EmbedEnum


* `private` (value: `"private"`)

* `public` (value: `"public"`)

* `whitelist` (value: `"whitelist"`)





## Enum: ViewEnum


* `anybody` (value: `"anybody"`)

* `contacts` (value: `"contacts"`)

* `disable` (value: `"disable"`)

* `nobody` (value: `"nobody"`)

* `password` (value: `"password"`)

* `unlisted` (value: `"unlisted"`)

* `users` (value: `"users"`)




