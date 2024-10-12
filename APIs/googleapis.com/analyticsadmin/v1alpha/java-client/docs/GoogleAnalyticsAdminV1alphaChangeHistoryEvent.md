

# GoogleAnalyticsAdminV1alphaChangeHistoryEvent

A set of changes within a Google Analytics account or its child properties that resulted from the same cause. Common causes would be updates made in the Google Analytics UI, changes from customer support, or automatic Google Analytics system changes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actorType** | [**ActorTypeEnum**](#ActorTypeEnum) | The type of actor that made this change. |  [optional] |
|**changeTime** | **String** | Time when change was made. |  [optional] |
|**changes** | [**List&lt;GoogleAnalyticsAdminV1alphaChangeHistoryChange&gt;**](GoogleAnalyticsAdminV1alphaChangeHistoryChange.md) | A list of changes made in this change history event that fit the filters specified in SearchChangeHistoryEventsRequest. |  [optional] |
|**changesFiltered** | **Boolean** | If true, then the list of changes returned was filtered, and does not represent all changes that occurred in this event. |  [optional] |
|**id** | **String** | ID of this change history event. This ID is unique across Google Analytics. |  [optional] |
|**userActorEmail** | **String** | Email address of the Google account that made the change. This will be a valid email address if the actor field is set to USER, and empty otherwise. Google accounts that have been deleted will cause an error. |  [optional] |



## Enum: ActorTypeEnum

| Name | Value |
|---- | -----|
| ACTOR_TYPE_UNSPECIFIED | &quot;ACTOR_TYPE_UNSPECIFIED&quot; |
| USER | &quot;USER&quot; |
| SYSTEM | &quot;SYSTEM&quot; |
| SUPPORT | &quot;SUPPORT&quot; |



