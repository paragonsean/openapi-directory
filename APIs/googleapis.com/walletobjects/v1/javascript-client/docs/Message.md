# GoogleWalletApi.Message

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **String** | The message body. | [optional] 
**displayInterval** | [**TimeInterval**](TimeInterval.md) |  | [optional] 
**header** | **String** | The message header. | [optional] 
**id** | **String** | The ID associated with a message. This field is here to enable ease of management of messages. Notice ID values could possibly duplicate across multiple messages in the same class/instance, and care must be taken to select a reasonable ID for each message. | [optional] 
**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string &#x60;\&quot;walletobjects#walletObjectMessage\&quot;&#x60;. | [optional] 
**localizedBody** | [**LocalizedString**](LocalizedString.md) |  | [optional] 
**localizedHeader** | [**LocalizedString**](LocalizedString.md) |  | [optional] 
**messageType** | **String** | The message type. | [optional] 



## Enum: MessageTypeEnum


* `MESSAGE_TYPE_UNSPECIFIED` (value: `"MESSAGE_TYPE_UNSPECIFIED"`)

* `TEXT` (value: `"TEXT"`)

* `text` (value: `"text"`)

* `EXPIRATION_NOTIFICATION` (value: `"EXPIRATION_NOTIFICATION"`)

* `expirationNotification` (value: `"expirationNotification"`)




