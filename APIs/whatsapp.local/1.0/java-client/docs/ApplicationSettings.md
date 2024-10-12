

# ApplicationSettings


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**callbackBackoffDelayMs** | **String** | Backoff delay for a failed callback in milliseconds This setting is used to configure the amount of time the backoff delays before retrying a failed callback. The backoff delay increases linearly by this value each time a callback fails to get a HTTPS 200 OK response. The backoff delay is capped by the max_callback_backoff_delay_ms setting. |  [optional] |
|**callbackPersist** | **Boolean** | Stores callbacks on disk until they are successfully acknowledged by the Webhook or not. Restart required. |  [optional] |
|**heartbeatInterval** | **Integer** | Multiconnect: Interval of the Master node monitoring of Coreapp nodes in seconds |  [optional] |
|**maxCallbackBackoffDelayMs** | **String** | Maximum delay for a failed callback in milliseconds |  [optional] |
|**media** | [**Media**](Media.md) |  |  [optional] |
|**onCallPager** | **String** | Set to valid WhatsApp Group with users who wish to see alerts for critical errors and messages. |  [optional] |
|**passThrough** | **Boolean** | When true, removes messages from the local database after they are delivered to or read by the recipient. When false, saves all messages on local storage until they are explicitly deleted. When messages are sent, they are stored in a local database. This database is used as the application&#39;s history. Since the business keeps its own history, you can specify whether you want message pass_through or not. Restart required. |  [optional] |
|**sentStatus** | **Boolean** | Receive a notification that a message is sent to server. When true, you will receive a message indicating that a message has been sent. If false (default), you will not receive notification. |  [optional] |
|**unhealthyInterval** | **Integer** | Multiconnect: Maximum amount of seconds a Master node waits for a Coreapp node to respond to a heartbeat before considering it unhealthy and starting the failover process. |  [optional] |
|**webhooks** | [**Webhooks**](Webhooks.md) |  |  [optional] |



