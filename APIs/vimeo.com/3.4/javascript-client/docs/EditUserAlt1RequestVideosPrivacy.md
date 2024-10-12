# Vimeo.EditUserAlt1RequestVideosPrivacy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add** | **Boolean** | Whether a user can add the video to an album, channel, or group. This value becomes the default add setting for all future videos uploaded by the user. | [optional] 
**comments** | **String** | Who can comment on the video. This value becomes the default comment setting for all future videos that this user uploads. | [optional] 
**download** | **Boolean** | Whether a user can download the video. This value becomes the default download setting for all future videos that this user uploads. | [optional] 
**embed** | **String** | The privacy for embed videos. The &#x60;whitelist&#x60; value enables you to define all valid embed domains. See our [documentation](https://developer.vimeo.com/api/endpoints/videos#/{video_id}/privacy/domains) for adding and removing domains. | [optional] 
**view** | **String** | Who can view the video. This value becomes the default view setting for all future videos that this user uploads. | [optional] 



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




