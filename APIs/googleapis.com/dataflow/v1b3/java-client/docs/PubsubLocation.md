

# PubsubLocation

Identifies a pubsub location to use for transferring data into or out of a streaming Dataflow job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dropLateData** | **Boolean** | Indicates whether the pipeline allows late-arriving data. |  [optional] |
|**dynamicDestinations** | **Boolean** | If true, then this location represents dynamic topics. |  [optional] |
|**idLabel** | **String** | If set, contains a pubsub label from which to extract record ids. If left empty, record deduplication will be strictly best effort. |  [optional] |
|**subscription** | **String** | A pubsub subscription, in the form of \&quot;pubsub.googleapis.com/subscriptions//\&quot; |  [optional] |
|**timestampLabel** | **String** | If set, contains a pubsub label from which to extract record timestamps. If left empty, record timestamps will be generated upon arrival. |  [optional] |
|**topic** | **String** | A pubsub topic, in the form of \&quot;pubsub.googleapis.com/topics//\&quot; |  [optional] |
|**trackingSubscription** | **String** | If set, specifies the pubsub subscription that will be used for tracking custom time timestamps for watermark estimation. |  [optional] |
|**withAttributes** | **Boolean** | If true, then the client has requested to get pubsub attributes. |  [optional] |



