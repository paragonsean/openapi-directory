# ClassicPlatformsNotifications.AccountHolderCreateNotification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**CreateAccountHolderResponse**](CreateAccountHolderResponse.md) | The details of the account holder creation. | [optional] 
**error** | [**NotificationErrorContainer**](NotificationErrorContainer.md) | Error information of failed request. No value provided here if no error occurred on processing. | [optional] 
**eventDate** | **Date** | The date and time when an event has been completed. | 
**eventType** | **String** | The event type of the notification. | 
**executingUserKey** | **String** | The user or process that has triggered the notification. | 
**live** | **Boolean** | Indicates whether the notification originated from the live environment or the test environment. If true, the notification originated from the live environment. If false, the notification originated from the test environment. | 
**pspReference** | **String** | The PSP reference of the request from which the notification originates. | 


