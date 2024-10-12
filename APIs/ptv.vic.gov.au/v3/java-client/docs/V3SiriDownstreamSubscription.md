

# V3SiriDownstreamSubscription


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**consumerAddress** | **String** |  |  [optional] |
|**initialTerminationTime** | **OffsetDateTime** |  |  [optional] |
|**messageType** | [**MessageTypeEnum**](#MessageTypeEnum) |  |  [optional] |
|**previewInterval** | **String** |  |  [optional] |
|**siriFormat** | [**SiriFormatEnum**](#SiriFormatEnum) |  |  [optional] |
|**siriVersion** | **String** |  |  [optional] |
|**subscriberRef** | **String** |  |  [optional] |
|**subscriptionRef** | **String** |  |  [optional] |
|**topics** | [**List&lt;V3SiriDownstreamSubscriptionTopic&gt;**](V3SiriDownstreamSubscriptionTopic.md) |  |  [optional] |
|**validityPeriodEnd** | **OffsetDateTime** |  |  [optional] |
|**validityPeriodStart** | **OffsetDateTime** |  |  [optional] |



## Enum: MessageTypeEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |



## Enum: SiriFormatEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |



