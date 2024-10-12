# GoogleAnalyticsAdminApi.GoogleAnalyticsAdminV1betaChangeHistoryEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actorType** | **String** | The type of actor that made this change. | [optional] 
**changeTime** | **String** | Time when change was made. | [optional] 
**changes** | [**[GoogleAnalyticsAdminV1betaChangeHistoryChange]**](GoogleAnalyticsAdminV1betaChangeHistoryChange.md) | A list of changes made in this change history event that fit the filters specified in SearchChangeHistoryEventsRequest. | [optional] 
**changesFiltered** | **Boolean** | If true, then the list of changes returned was filtered, and does not represent all changes that occurred in this event. | [optional] 
**id** | **String** | ID of this change history event. This ID is unique across Google Analytics. | [optional] 
**userActorEmail** | **String** | Email address of the Google account that made the change. This will be a valid email address if the actor field is set to USER, and empty otherwise. Google accounts that have been deleted will cause an error. | [optional] 



## Enum: ActorTypeEnum


* `ACTOR_TYPE_UNSPECIFIED` (value: `"ACTOR_TYPE_UNSPECIFIED"`)

* `USER` (value: `"USER"`)

* `SYSTEM` (value: `"SYSTEM"`)

* `SUPPORT` (value: `"SUPPORT"`)




