

# ServiceBusQueueMessage


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**queueName** | **String** | Gets or sets the queue name. |  [optional] |
|**authentication** | [**ServiceBusAuthentication**](ServiceBusAuthentication.md) |  |  [optional] |
|**brokeredMessageProperties** | [**ServiceBusBrokeredMessageProperties**](ServiceBusBrokeredMessageProperties.md) |  |  [optional] |
|**customMessageProperties** | **Map&lt;String, String&gt;** | Gets or sets the custom message properties. |  [optional] |
|**message** | **String** | Gets or sets the message. |  [optional] |
|**namespace** | **String** | Gets or sets the namespace. |  [optional] |
|**transportType** | [**TransportTypeEnum**](#TransportTypeEnum) | Gets or sets the transport type. |  [optional] |



## Enum: TransportTypeEnum

| Name | Value |
|---- | -----|
| NOT_SPECIFIED | &quot;NotSpecified&quot; |
| NET_MESSAGING | &quot;NetMessaging&quot; |
| AMQP | &quot;AMQP&quot; |



