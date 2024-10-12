# GoogleChatApi.User

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayName** | **String** | Output only. The user&#39;s display name. | [optional] [readonly] 
**domainId** | **String** | Unique identifier of the user&#39;s Google Workspace domain. | [optional] 
**isAnonymous** | **Boolean** | Output only. When &#x60;true&#x60;, the user is deleted or their profile is not visible. | [optional] [readonly] 
**name** | **String** | Resource name for a Google Chat user. Format: &#x60;users/{user}&#x60;. &#x60;users/app&#x60; can be used as an alias for the calling app bot user. For human users, &#x60;{user}&#x60; is the same user identifier as: - the &#x60;id&#x60; for the [Person](https://developers.google.com/people/api/rest/v1/people) in the People API. For example, &#x60;users/123456789&#x60; in Chat API represents the same person as the &#x60;123456789&#x60; Person profile ID in People API. - the &#x60;id&#x60; for a [user](https://developers.google.com/admin-sdk/directory/reference/rest/v1/users) in the Admin SDK Directory API. - the user&#39;s email address can be used as an alias for &#x60;{user}&#x60; in API requests. For example, if the People API Person profile ID for &#x60;user@example.com&#x60; is &#x60;123456789&#x60;, you can use &#x60;users/user@example.com&#x60; as an alias to reference &#x60;users/123456789&#x60;. Only the canonical resource name (for example &#x60;users/123456789&#x60;) will be returned from the API. | [optional] 
**type** | **String** | User type. | [optional] 



## Enum: TypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `HUMAN` (value: `"HUMAN"`)

* `BOT` (value: `"BOT"`)




