# NotificationConfigurationApi.NotificationConfigurationDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **Boolean** | Indicates whether the notification subscription is active. | [optional] 
**apiVersion** | **Number** | The version of the notification to which you are subscribing. To make sure that your integration can properly process the notification, subscribe to the same version as the API that you&#39;re using. | [optional] 
**description** | **String** | A description of the notification subscription configuration. | [optional] 
**eventConfigs** | [**[NotificationEventConfiguration]**](NotificationEventConfiguration.md) | Contains objects that define event types and their subscription settings. | [optional] 
**hmacSignatureKey** | **String** | A string with which to salt the notification(s) before hashing. If this field is provided, a hash value will be included under the notification header &#x60;HmacSignature&#x60; and the hash protocol will be included under the notification header &#x60;Protocol&#x60;. A notification body along with its &#x60;hmacSignatureKey&#x60; and &#x60;Protocol&#x60; can be used to calculate a hash value; matching this hash value with the &#x60;HmacSignature&#x60; will ensure that the notification body has not been tampered with or corrupted.  &gt;Must be a 32-byte hex-encoded string (i.e. a string containing 64 hexadecimal characters; e.g. \&quot;b0ea55c2fe60d4d1d605e9c385e0e7f7e6cafbb939ce07010f31a327a0871f27\&quot;).  The omission of this field will preclude the provision of the &#x60;HmacSignature&#x60; and &#x60;Protocol&#x60; headers in notification(s). | [optional] 
**notificationId** | **Number** | Adyen-generated ID for the entry, returned in the response when you create a notification configuration. Required when updating an existing configuration using [&#x60;/updateNotificationConfiguration&#x60;](https://docs.adyen.com/api-explorer/#/NotificationConfigurationService/latest/post/updateNotificationConfiguration). | [optional] 
**notifyPassword** | **String** | The password to use when accessing the notifyURL with the specified username. | [optional] 
**notifyURL** | **String** | The URL to which the notifications are to be sent. | [optional] 
**notifyUsername** | **String** | The username to use when accessing the notifyURL. | [optional] 
**sslProtocol** | **String** | The SSL protocol employed by the endpoint. &gt;Permitted values: &#x60;TLSv12&#x60;, &#x60;TLSv13&#x60;. | [optional] 



## Enum: SslProtocolEnum


* `TLSv12` (value: `"TLSv12"`)

* `TLSv13` (value: `"TLSv13"`)




