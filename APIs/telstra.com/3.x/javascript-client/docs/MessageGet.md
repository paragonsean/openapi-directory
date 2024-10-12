# MessagingApiV3X.MessageGet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTimestamp** | **Date** | The time you submitted the message to the queue for sending. | [optional] 
**deliveryNotification** | **Boolean** | If set to **true**, you will receive a notification to the statusCallbackUrl when your message is delivered (paid feature). | [optional] [default to false]
**direction** | **String** | * **outgoing** – messages sent from your account. * **incoming** – messages sent to your account.  | [optional] 
**from** | **String** | This will be either \&quot;privateNumber\&quot;, one of your Virtual Numbers or your senderName. | [optional] 
**messageContent** | **String** | The content of the message. | [optional] 
**messageId** | **String** | Use this UUID with our other endpoints to fetch, update or delete the message. | [optional] 
**multimedia** | [**[MultimediaGet]**](MultimediaGet.md) | The multimedia content of the message (MMS only). It will include:  | [optional] 
**queuePriority** | **Number** | The priority assigned to the message. | [optional] [default to 2]
**receivedTimestamp** | **Date** | The time the message was received by the recipient&#39;s device. | [optional] 
**retryTimeout** | **Number** | How many minutes you asked the server to keep trying to send the message. | [optional] [default to 10]
**scheduleSend** | **Date** | The time the message is scheduled to send. | [optional] 
**sentTimestamp** | **Date** | The time the message was sent from the server. | [optional] 
**status** | **String** | The status will be either queued, sent, delivered, expired or undeliverable. | [optional] 
**statusCallbackUrl** | **String** | The URL the API will call when the status of the message changes. | [optional] 
**tags** | **[String]** | Any customisable tags assigned to the message. | [optional] 
**to** | **String** | The recipient&#39;s mobile number. | [optional] 



## Enum: DirectionEnum


* `outgoing` (value: `"outgoing"`)

* `incoming` (value: `"incoming"`)





## Enum: StatusEnum


* `queued` (value: `"queued"`)

* `sent` (value: `"sent"`)

* `delivered` (value: `"delivered"`)

* `expired` (value: `"expired"`)

* `undeliverable` (value: `"undeliverable"`)




