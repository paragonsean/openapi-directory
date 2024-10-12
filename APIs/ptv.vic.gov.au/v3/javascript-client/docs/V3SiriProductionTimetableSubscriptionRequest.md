# PtvTimetableApiVersion3.V3SiriProductionTimetableSubscriptionRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumerAddress** | **String** | Siri Consumer Address - Baseline and Updates will be sent to this address | 
**endTime** | **Date** | Siri End Time of the Validity Period | 
**initialTerminationTime** | **Date** | Siri Initial Termination Time - Expiry of the subscription | 
**siriFormat** | **Number** | Siri Message Format &#39;xml&#39; or &#39;json&#39; | 
**siriVersion** | **String** | Siri Message Version &#39;1.3&#39; or &#39;2.0&#39; | 
**startTime** | **Date** | Siri Start Time of the Validity Period | 
**subscriberRef** | **String** | Siri Subscriber Ref | 
**subscriptionRef** | **String** | Siri Subscription Ref - Unique to a Subscriber Ref | 
**topics** | [**[V3SiriSubscriptionTopic]**](V3SiriSubscriptionTopic.md) |  | 



## Enum: SiriFormatEnum


* `0` (value: `0`)

* `1` (value: `1`)




