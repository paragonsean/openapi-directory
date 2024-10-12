

# V3SiriProductionTimetableSubscriptionRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**consumerAddress** | **String** | Siri Consumer Address - Baseline and Updates will be sent to this address |  |
|**endTime** | **OffsetDateTime** | Siri End Time of the Validity Period |  |
|**initialTerminationTime** | **OffsetDateTime** | Siri Initial Termination Time - Expiry of the subscription |  |
|**siriFormat** | [**SiriFormatEnum**](#SiriFormatEnum) | Siri Message Format &#39;xml&#39; or &#39;json&#39; |  |
|**siriVersion** | **String** | Siri Message Version &#39;1.3&#39; or &#39;2.0&#39; |  |
|**startTime** | **OffsetDateTime** | Siri Start Time of the Validity Period |  |
|**subscriberRef** | **String** | Siri Subscriber Ref |  |
|**subscriptionRef** | **String** | Siri Subscription Ref - Unique to a Subscriber Ref |  |
|**topics** | [**List&lt;V3SiriSubscriptionTopic&gt;**](V3SiriSubscriptionTopic.md) |  |  |



## Enum: SiriFormatEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |



