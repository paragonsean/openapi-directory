

# NotificationConfigurationDetails


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**active** | **Boolean** | Indicates whether the notification subscription is active. |  [optional] |
|**apiVersion** | **Integer** | The version of the notification to which you are subscribing. To make sure that your integration can properly process the notification, subscribe to the same version as the API that you&#39;re using. |  [optional] |
|**description** | **String** | A description of the notification subscription configuration. |  [optional] |
|**eventConfigs** | [**List&lt;NotificationEventConfigurationWrapper&gt;**](NotificationEventConfigurationWrapper.md) | Contains objects that define event types and their subscription settings. |  [optional] |
|**messageFormat** | [**MessageFormatEnum**](#MessageFormatEnum) | The data format of the notification to be sent. &gt;Permitted values: &#x60;JSON&#x60;, &#x60;SOAP&#x60;. |  [optional] |
|**notificationId** | **Long** | Adyen-generated ID for the entry, returned in the response when you create a notification configuration. Required when updating an existing configuration using [&#x60;/updateNotificationConfiguration&#x60;](https://docs.adyen.com/api-explorer/#/NotificationConfigurationService/latest/post/updateNotificationConfiguration). |  [optional] |
|**notifyPassword** | **String** | The password to use when accessing the notifyURL with the specified username. |  [optional] |
|**notifyURL** | **String** | The URL to which the notifications are to be sent. |  [optional] |
|**notifyUsername** | **String** | The username to use when accessing the notifyURL. |  [optional] |
|**sendActionHeader** | **Boolean** | Indicates whether an action header should be included. &gt;Only applies to SOAP messages (as specified in messageFormat). |  [optional] |
|**sslProtocol** | [**SslProtocolEnum**](#SslProtocolEnum) | The SSL protocol employed by the endpoint. &gt;Permitted values: &#x60;TLSv12&#x60;, &#x60;TLSv13&#x60;. |  [optional] |



## Enum: MessageFormatEnum

| Name | Value |
|---- | -----|
| JSON | &quot;JSON&quot; |
| SOAP | &quot;SOAP&quot; |



## Enum: SslProtocolEnum

| Name | Value |
|---- | -----|
| TLSV12 | &quot;TLSv12&quot; |
| TLSV13 | &quot;TLSv13&quot; |



