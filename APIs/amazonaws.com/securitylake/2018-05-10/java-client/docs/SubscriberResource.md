

# SubscriberResource

Provides details about the Amazon Security Lake account subscription. Subscribers are notified of new objects for a source as the data is written to your Amazon S3 bucket for Security Lake.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessTypes** | [**List**](List.md) |  |  [optional] |
|**createdAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**resourceShareArn** | [**String**](String.md) |  |  [optional] |
|**resourceShareName** | [**String**](String.md) |  |  [optional] |
|**roleArn** | [**String**](String.md) |  |  [optional] |
|**s3BucketArn** | [**String**](String.md) |  |  [optional] |
|**sources** | [**List**](List.md) |  |  |
|**subscriberArn** | [**String**](String.md) |  |  |
|**subscriberDescription** | [**String**](String.md) |  |  [optional] |
|**subscriberEndpoint** | [**String**](String.md) |  |  [optional] |
|**subscriberId** | [**String**](String.md) |  |  |
|**subscriberIdentity** | [**CreateSubscriberRequestSubscriberIdentity**](CreateSubscriberRequestSubscriberIdentity.md) |  |  |
|**subscriberName** | [**String**](String.md) |  |  |
|**subscriberStatus** | [**SubscriberStatus**](SubscriberStatus.md) |  |  [optional] |
|**updatedAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |



