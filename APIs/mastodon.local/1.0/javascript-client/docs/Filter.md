# MastodonApiSpecificationHttpsGithubComMastodonMastodon.Filter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **[String]** | The contexts in which the filter should be applied. | [optional] 
**expiresAt** | **String** | When the filter should no longer be applied. ISO 8601 Datetime, or null if the filter does not expire | [optional] 
**id** | **String** | The ID of the filter in the database. Cast from an integer, but not guaranteed to be a number. | [optional] 
**irreversible** | **Boolean** | Should matching entities in home and notifications be dropped by the server? | [optional] 
**phrase** | **String** | The text to be filtered. | [optional] 
**wholeWord** | **Boolean** | Should the filter consider word boundaries? | [optional] 



## Enum: [ContextEnum]


* `home` (value: `"home"`)

* `notifications` (value: `"notifications"`)

* `public` (value: `"public"`)

* `thread` (value: `"thread"`)




