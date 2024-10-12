# MastodonApiSpecificationHttpsGithubComMastodonMastodon.Notification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**Account**](Account.md) |  | 
**createdAt** | **Date** | The timestamp of the notification. ISO 8601 Datetime. | 
**id** | **String** | The id of the notification in the database. Cast from an integer, but not guaranteed to be a number. | 
**status** | [**Status**](Status.md) |  | [optional] 
**type** | **String** | The type of event that resulted in the notification. | 



## Enum: TypeEnum


* `follow` (value: `"follow"`)

* `follow_request` (value: `"follow_request"`)

* `mention` (value: `"mention"`)

* `reblog` (value: `"reblog"`)

* `favourite` (value: `"favourite"`)

* `poll` (value: `"poll"`)

* `status` (value: `"status"`)




