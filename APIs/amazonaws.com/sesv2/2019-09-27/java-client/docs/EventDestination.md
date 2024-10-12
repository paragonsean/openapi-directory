

# EventDestination

In the Amazon SES API v2, <i>events</i> include message sends, deliveries, opens, clicks, bounces, complaints and delivery delays. <i>Event destinations</i> are places that you can send information about these events to. For example, you can send event data to Amazon SNS to receive notifications when you receive bounces or complaints, or you can use Amazon Kinesis Data Firehose to stream data to Amazon S3 for long-term storage.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | [**String**](String.md) |  |  |
|**enabled** | [**Boolean**](Boolean.md) |  |  [optional] |
|**matchingEventTypes** | [**List**](List.md) |  |  |
|**kinesisFirehoseDestination** | [**CreateConfigurationSetEventDestinationRequestEventDestinationKinesisFirehoseDestination**](CreateConfigurationSetEventDestinationRequestEventDestinationKinesisFirehoseDestination.md) |  |  [optional] |
|**cloudWatchDestination** | [**CreateConfigurationSetEventDestinationRequestEventDestinationCloudWatchDestination**](CreateConfigurationSetEventDestinationRequestEventDestinationCloudWatchDestination.md) |  |  [optional] |
|**snsDestination** | [**CreateConfigurationSetEventDestinationRequestEventDestinationSnsDestination**](CreateConfigurationSetEventDestinationRequestEventDestinationSnsDestination.md) |  |  [optional] |
|**pinpointDestination** | [**CreateConfigurationSetEventDestinationRequestEventDestinationPinpointDestination**](CreateConfigurationSetEventDestinationRequestEventDestinationPinpointDestination.md) |  |  [optional] |



