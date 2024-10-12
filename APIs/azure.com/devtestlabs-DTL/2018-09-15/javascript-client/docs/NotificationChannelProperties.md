# DevTestLabsClient.NotificationChannelProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdDate** | **Date** | The creation date of the notification channel. | [optional] [readonly] 
**description** | **String** | Description of notification. | [optional] 
**emailRecipient** | **String** | The email recipient to send notifications to (can be a list of semi-colon separated email addresses). | [optional] 
**events** | [**[Event]**](Event.md) | The list of event for which this notification is enabled. | [optional] 
**notificationLocale** | **String** | The locale to use when sending a notification (fallback for unsupported languages is EN). | [optional] 
**provisioningState** | **String** | The provisioning status of the resource. | [optional] [readonly] 
**uniqueIdentifier** | **String** | The unique immutable identifier of a resource (Guid). | [optional] [readonly] 
**webHookUrl** | **String** | The webhook URL to send notifications to. | [optional] 


