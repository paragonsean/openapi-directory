# Vimeo.EditVideoRequestPrivacy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add** | **Boolean** | Whether a user can add the video to an album, channel, or group. | [optional] 
**comments** | **String** | The privacy level required to comment on the video. | [optional] 
**download** | **Boolean** | Whether a user can download the video. Not available to users with a Basic membership. | [optional] 
**embed** | **String** | The video&#39;s new embed settings. The &#x60;whitelist&#x60; value enables you to define all valid embed domains. See our [documentation](https://developer.vimeo.com/api/endpoints/videos#/{video_id}/privacy/domains) for details on adding and removing domains. | [optional] 
**view** | **String** | The video&#39;s new privacy setting. When privacy is &#x60;users&#x60;, &#x60;application/json&#x60; is the only valid content type. Basic users can&#39;t set privacy to &#x60;unlisted&#x60;. | [optional] 



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




