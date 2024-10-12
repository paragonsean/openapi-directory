# WebSiteManagementClient.Recommendation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actionName** | **String** | Name of action recommended by this object. | [optional] 
**channels** | **String** | List of channels that this recommendation can apply. | 
**creationTime** | **Date** | Timestamp when this instance was created. | [optional] 
**displayName** | **String** | UI friendly name of the rule (may not be unique) | [optional] 
**enabled** | **Number** | On/off flag indicating the rule is currently enabled or disabled. | [optional] 
**endTime** | **Date** | The end time of a range that the recommendation refers to. | [optional] 
**level** | **String** | Level indicating how critical this recommendation can impact. | 
**message** | **String** | Localized text of recommendation, good for UI. | [optional] 
**nextNotificationTime** | **Date** | When to notify this recommendation next. Null means that this will never be notified anymore. | [optional] 
**notificationExpirationTime** | **Date** | Date and time when this notification expires. | [optional] 
**notifiedTime** | **Date** | Last timestamp this instance was actually notified. Null means that this recommendation hasn&#39;t been notified yet. | [optional] 
**recommendationId** | **String** | A GUID value that each recommendation object is associated with. | [optional] 
**resourceId** | **String** | Full ARM resource ID string that this recommendation object is associated with. | [optional] 
**resourceScope** | **String** | Name of a resource type this recommendation applies, e.g. Subscription, ServerFarm, Site. | [optional] 
**ruleName** | **String** | Unique name of the rule | [optional] 
**score** | **Number** | A metric value measured by the rule. | [optional] 
**startTime** | **Date** | The beginning time of a range that the recommendation refers to. | [optional] 
**tags** | **[String]** | The list of category tags that this recommendation belongs to. | [optional] 



## Enum: ChannelsEnum


* `Notification` (value: `"Notification"`)

* `Api` (value: `"Api"`)

* `Email` (value: `"Email"`)

* `All` (value: `"All"`)





## Enum: LevelEnum


* `Critical` (value: `"Critical"`)

* `Warning` (value: `"Warning"`)

* `Information` (value: `"Information"`)

* `NonUrgentSuggestion` (value: `"NonUrgentSuggestion"`)




