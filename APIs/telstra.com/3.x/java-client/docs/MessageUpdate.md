

# MessageUpdate


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deliveryNotification** | **Boolean** | If set to **true**, you will receive a notification to the statusCallbackUrl when your message is delivered (paid feature). |  [optional] |
|**from** | **String** | This will be either \&quot;privateNumber\&quot;, one of your Virtual Numbers or your senderName. |  [optional] |
|**messageContent** | **String** | The content of the message. |  [optional] |
|**messageId** | **UUID** | Use this UUID with our other endpoints to fetch, update or delete the message. |  [optional] |
|**multimedia** | [**List&lt;MultimediaGet&gt;**](MultimediaGet.md) | The multimedia content of the message (MMS only). It will include:  |  [optional] |
|**queuePriority** | **Integer** | The priority assigned to the message. |  [optional] |
|**retryTimeout** | **Integer** | How many minutes you asked the server to keep trying to send the message. |  [optional] |
|**scheduleSend** | **OffsetDateTime** | The time the message is scheduled to send. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status will be either queued, sent, delivered, expired or undeliverable. |  [optional] |
|**statusCallbackUrl** | **String** | The URL the API will call when the status of the message changes. |  [optional] |
|**tags** | **List&lt;String&gt;** | Any customisable tags assigned to the message. |  [optional] |
|**to** | **String** | The recipient&#39;s mobile number. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| QUEUED | &quot;queued&quot; |
| SENT | &quot;sent&quot; |
| DELIVERED | &quot;delivered&quot; |
| EXPIRED | &quot;expired&quot; |
| UNDELIVERABLE | &quot;undeliverable&quot; |



