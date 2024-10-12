

# JMS

JMS message denotes the source of the event

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Optional. Name of the JMS source. i.e. queueName or topicName |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Optional. Type of the JMS Source. i.e. Queue or Topic |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| QUEUE | &quot;QUEUE&quot; |
| TOPIC | &quot;TOPIC&quot; |



