# NotificationConfigurationApi.NotificationConfigurationDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **Boolean** | Indicates whether the notification subscription is active. | [optional] 
**apiVersion** | **Number** | The version of the notification to which you are subscribing. To make sure that your integration can properly process the notification, subscribe to the same version as the API that you&#39;re using. | [optional] 
**description** | **String** | A description of the notification subscription configuration. | [optional] 
**eventConfigs** | [**[NotificationEventConfigurationWrapper]**](NotificationEventConfigurationWrapper.md) | Contains objects that define event types and their subscription settings. | [optional] 
**messageFormat** | **String** | The data format of the notification to be sent. &gt;Permitted values: &#x60;JSON&#x60;, &#x60;SOAP&#x60;. | [optional] 
**notificationId** | **Number** | Adyen-generated ID for the entry, returned in the response when you create a notification configuration. Required when updating an existing configuration using [&#x60;/updateNotificationConfiguration&#x60;](https://docs.adyen.com/api-explorer/#/NotificationConfigurationService/latest/post/updateNotificationConfiguration). | [optional] 
**notifyPassword** | **String** | The password to use when accessing the notifyURL with the specified username. | [optional] 
**notifyURL** | **String** | The URL to which the notifications are to be sent. | [optional] 
**notifyUsername** | **String** | The username to use when accessing the notifyURL. | [optional] 
**sendActionHeader** | **Boolean** | Indicates whether an action header should be included. &gt;Only applies to SOAP messages (as specified in messageFormat). | [optional] 
**sslProtocol** | **String** | The SSL protocol employed by the endpoint. &gt;Permitted values: &#x60;TLSv12&#x60;, &#x60;TLSv13&#x60;. | [optional] 



## Enum: MessageFormatEnum


* `JSON` (value: `"JSON"`)

* `SOAP` (value: `"SOAP"`)





## Enum: SslProtocolEnum


* `TLSv12` (value: `"TLSv12"`)

* `TLSv13` (value: `"TLSv13"`)




