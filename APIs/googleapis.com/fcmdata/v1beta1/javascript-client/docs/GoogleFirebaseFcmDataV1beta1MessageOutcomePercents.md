# FirebaseCloudMessagingDataApi.GoogleFirebaseFcmDataV1beta1MessageOutcomePercents

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivered** | **Number** | The percentage of all accepted messages that were successfully delivered to the device. | [optional] 
**droppedAppForceStopped** | **Number** | The percentage of accepted messages that were dropped because the application was force stopped on the device at the time of delivery and retries were unsuccessful. | [optional] 
**droppedDeviceInactive** | **Number** | The percentage of accepted messages that were dropped because the target device is inactive. FCM will drop messages if the target device is deemed inactive by our servers. If a device does reconnect, we call [OnDeletedMessages()](https://firebase.google.com/docs/cloud-messaging/android/receive#override-ondeletedmessages) in our SDK instead of delivering the messages. | [optional] 
**droppedTooManyPendingMessages** | **Number** | The percentage of accepted messages that were dropped due to [too many undelivered non-collapsible messages](https://firebase.google.com/docs/cloud-messaging/concept-options#collapsible_and_non-collapsible_messages). Specifically, each app instance can only have 100 pending messages stored on our servers for a device which is disconnected. When that device reconnects, those messages are delivered. When there are more than the maximum pending messages, we call [OnDeletedMessages()](https://firebase.google.com/docs/cloud-messaging/android/receive#override-ondeletedmessages) in our SDK instead of delivering the messages. | [optional] 
**pending** | **Number** | The percentage of messages accepted on this day that were not dropped and not delivered, due to the device being disconnected (as of the end of the America/Los_Angeles day when the message was sent to FCM). A portion of these messages will be delivered the next day when the device connects but others may be destined to devices that ultimately never reconnect. | [optional] 


