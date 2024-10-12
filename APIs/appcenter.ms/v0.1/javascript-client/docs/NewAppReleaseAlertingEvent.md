# AppCenterClient.NewAppReleaseAlertingEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eventId** | **String** | A unique identifier for this event instance. Useful for deduplication | 
**eventTimestamp** | **String** | ISO 8601 date time when event was generated | 
**properties** | **Object** | Obsolete. Use emailProperties. | [optional] 
**appReleaseProperties** | [**NewAppReleaseAlertingEventAllOfAppReleaseProperties**](NewAppReleaseAlertingEventAllOfAppReleaseProperties.md) |  | [optional] 
**disableWebhook** | **Boolean** | indicate whether notify via webhook or not | [optional] 
**userIds** | **[String]** | List of users who need to receive an email notification. If this is not null, then only sending emails will be triggered even if the event requires calling webhooks or doing other actions. | [optional] 


